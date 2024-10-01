# Behind the Scenes

## Description

After struggling to secure our secret strings for a long time, we finally figured out the solution to our problem: Make decompilation harder. It should now be impossible to figure out how our programs work!

## Task files:

### behindthescenes

## Solution

We are provided with a file without any details, so we start by identifying it using the ```file``` command.

```bash
└─$ file behindthescenes
behindthescenes: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e60ae4c886619b869178148afd12d0a5428bfe18, for GNU/Linux 3.2.0, not stripped
```

This reveals that the file is an ELF binary. Let's try running it and see what happens:

```bash
└─$ ./behindthescenes           
./challenge <password>
```

To further investigate, we open the file in Ghidra to analyze it more deeply. The main function looks like this:

```c
void main(void)

{
  code *pcVar1;
  long in_FS_OFFSET;
  sigaction local_a8;
  undefined8 local_10;
  
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  memset(&local_a8,0,0x98);
  sigemptyset(&local_a8.sa_mask);
  local_a8.__sigaction_handler.sa_handler = segill_sigaction;
  local_a8.sa_flags = 4;
  sigaction(4,&local_a8,(sigaction *)0x0);
                    /* WARNING: Does not return */
  pcVar1 = (code *)invalidInstructionException();
  (*pcVar1)();
}
```

The first thing we notice is a warning from Ghidra on the last two lines stating "Does not return". Let's go through the main function from the beginning to understand what's happening.

The ```code *pcVar1;``` is Ghidra's way to define a function pointer when it doesn't know what kind of variables it receives and returns. Going back at the end of the function we see that ```pcVar1``` receives the address of this function ```invalidInstructionException()```. By selecting the function, Ghidra highlights this assembly instruction: ```UD2```.
> Generates an invalid opcode. This instruction is provided for software testing to explicitly generate an invalid opcode. The opcode for this instruction is reserved for this purpose.<br>
Other than raising the invalid opcode exception, this instruction is the same as the NOP instruction.

Practically, the UD2 instruction raises an exceptio and Ghidra doesn't dissamble further more the code. 

```
        001012e6 0f 0b           UD2
        001012e8 83              ??         83h
        001012e9 bd              ??         BDh
        001012ea 5c              ??         5Ch    \
```

We will replace the UD2 instruction with NOP and manually disassemble the code. The newly revealed main function now looks like this:

```c
undefined8 main(void)

{
  int iVar1;
  undefined8 uVar2;
  size_t sVar3;
  long in_RSI;
  int in_EDI;
  long in_FS_OFFSET;
  sigaction local_a8;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  memset(&local_a8,0,0x98);
  sigemptyset(&local_a8.sa_mask);
  local_a8.__sigaction_handler.sa_handler = segill_sigaction;
  local_a8.sa_flags = 4;
  sigaction(4,&local_a8,(sigaction *)0x0);
  if (in_EDI == 2) {
    sVar3 = strlen(*(char **)(in_RSI + 8));
    if (sVar3 == 0xc) {
      iVar1 = strncmp(*(char **)(in_RSI + 8),"Itz",3);
      if (iVar1 == 0) {
        iVar1 = strncmp((char *)(*(long *)(in_RSI + 8) + 3),"_0n",3);
        if (iVar1 == 0) {
          iVar1 = strncmp((char *)(*(long *)(in_RSI + 8) + 6),"Ly_",3);
          if (iVar1 == 0) {
            iVar1 = strncmp((char *)(*(long *)(in_RSI + 8) + 9),"UD2",3);
            if (iVar1 == 0) {
              printf("> HTB{%s}\n",*(undefined8 *)(in_RSI + 8));
              uVar2 = 0;
            }
            else {
              uVar2 = 0;
            }
          }
          else {
            uVar2 = 0;
          }
        }
        else {
          uVar2 = 0;
        }
      }
      else {
        uVar2 = 0;
      }
    }
    else {
      uVar2 = 0;
    }
  }
  else {
    puts("./challenge <password>");
    uVar2 = 1;
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
```

It seems that the function is sequentially comparing four strings, and the expected output should be ```Itz_0nLy_UD2```. Let's try this password.

```bash
./behindthescenes Itz_0nLy_UD2

> HTB{Itz_0nLy_UD2}
```

## Flag

```
HTB{Itz_0nLy_UD2}
```
