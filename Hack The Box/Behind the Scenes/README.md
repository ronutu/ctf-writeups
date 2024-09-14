# Behind the Scenes

## Description

After struggling to secure our secret strings for a long time, we finally figured out the solution to our problem: Make decompilation harder. It should now be impossible to figure out how our programs work!

## Task files:

### behindthescenes

## Solution

We are provided with a file without any information about what it is so we use ```file```.

```console
file behindthescenes

behindthescenes: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e60ae4c886619b869178148afd12d0a5428bfe18, for GNU/Linux 3.2.0, not stripped
```

![behind-the-scenes1](https://github.com/user-attachments/assets/5df564e2-5a84-4e94-b9aa-a65e6fcb55ee)

This indicates that the file is an ELF binary file. Next, we run ```strings``` to look for anything useful:

![behind-the-scenes2](https://github.com/user-attachments/assets/0c071cd2-4332-4239-949a-d4d5aacfb5d1)

The output ```./challenge <password>``` and ```> HTB{%s}``` gives us a small clue. We run the file by using ```./behindthescenes password``` and maybe it returns the flag. Next, we will use Ghidra to take a closer look at the file. While examining the file, we find this:


![behind-the-scenes3](https://github.com/user-attachments/assets/66f1cd5c-7fe5-4f5c-b847-a5dbb1c4adea)

It appears that the password is written vertically, so we will try that and see what we get:

![behind-the-scenes4](https://github.com/user-attachments/assets/aebc7b36-2ff2-41ad-adf0-02e869104930)

## Flag

```
HTB{Itz_0nLy_UD2}
```
