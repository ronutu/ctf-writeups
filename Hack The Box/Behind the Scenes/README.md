# Behind the Scenes

## Description

After struggling to secure our secret strings for a long time, we finally figured out the solution to our problem: Make decompilation harder. It should now be impossible to figure out how our programs work!

## Task files:

### behindthescenes

## Solution

We are provided with a file without any details, so we start by identifying it using the ```file``` command.

```bash
file behindthescenes

behindthescenes: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e60ae4c886619b869178148afd12d0a5428bfe18, for GNU/Linux 3.2.0, not stripped
```

This reveals that the file is an ELF binary. Next, we use the ```strings``` command to search for any useful information:

```bash
strings behindthescenes

lib64/ld-linux-x86-64.so.2
libc.so.6
strncmp
puts
__stack_chk_fail
printf
strlen
sigemptyset
memset
sigaction
__cxa_finalize
__libc_start_main
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
./challenge <password>
> HTB{%s}
...
```

The output ```./challenge <password>``` and ```> HTB{%s}``` gives us a small clue. We run the file by using ```./behindthescenes password``` hoping it returns the flag.

To further investigate, we open the file in Ghidra to analyze it more deeply. While examining the binary, we find the following code:

```nasm
        0010201b 49              ??         49h    I
        0010201c 74              ??         74h    t
        0010201d 7a              ??         7Ah    z
        0010201e 00              ??         00h
        0010201f 5f              ??         5Fh    _
        00102020 30              ??         30h    0
        00102021 6e              ??         6Eh    n
        00102022 00              ??         00h
        00102023 4c              ??         4Ch    L
        00102024 79              ??         79h    y
        00102025 5f              ??         5Fh    _
        00102026 00              ??         00h
        00102027 55              ??         55h    U
        00102028 44              ??         44h    D
        00102029 32              ??         32h    2
        0010202a 00              ??         00h
        0010202b 3e              ??         3Eh    >
        0010202c 20              ??         20h     
        0010202d 48              ??         48h    H
        0010202e 54              ??         54h    T
        0010202f 42              ??         42h    B
        00102030 7b              ??         7Bh    {
        00102031 25              ??         25h    %
        00102032 73              ??         73h    s
        00102033 7d              ??         7Dh    }
        00102034 0a              ??         0Ah
        00102035 00              ??         00h
```

It appears that the password is written vertically, so we will try that and see what we get:

```bash
./behindthescenes Itz_0nLy_UD2

> HTB{Itz_0nLy_UD2}
```

## Flag

```
HTB{Itz_0nLy_UD2}
```
