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

In order to understand what it does, we will examine every line of code.

The ```code *pcVar1;``` is Ghidra's way to define a function pointer when it doesn't know what kind of variables it receives and returns. Looking at the end of the program we see that ```pcVar1``` receives the address of this function ```invalidInstructionException()```.  After that it calls the function. We will come back to this later.

We have another few variables defined. A long, a sigaction, 

It appears that the password is written vertically, so we will try that and see what we get:

```bash
./behindthescenes Itz_0nLy_UD2

> HTB{Itz_0nLy_UD2}
```

## Flag

```
HTB{Itz_0nLy_UD2}
```
