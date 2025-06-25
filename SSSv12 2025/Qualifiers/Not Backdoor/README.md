# Not Backdoor

## Description

We found this strange file which claims to be a Windows NOT backdoor. Can you figure out what it actually is and what it's doing?

## Intuition

We check the file type:

```bash
file not_backdoor.exe
not_backdoor.exe: POSIX tar archive (GNU)
```

## Solution

Seeing it is a tar archive we unarchive it: `tar -xvf not_backdoor.exe`. This reveals an ELF binary.

Using `strace ./not_backdoor` shows a hint (Psst, try passing an argument!):

```bash
write(42, "P", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "s", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "s", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "t", 1)                       = -1 EBADF (Bad file descriptor)
write(42, ",", 1)                       = -1 EBADF (Bad file descriptor)
write(42, " ", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "t", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "r", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "y", 1)                       = -1 EBADF (Bad file descriptor)
write(42, " ", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "p", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "a", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "s", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "s", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "i", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "n", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "g", 1)                       = -1 EBADF (Bad file descriptor)
write(42, " ", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "a", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "n", 1)                       = -1 EBADF (Bad file descriptor)
write(42, " ", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "a", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "r", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "g", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "u", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "m", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "e", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "n", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "t", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "!", 1)                       = -1 EBADF (Bad file descriptor)
write(42, "\n", 1)                      = -1 EBADF (Bad file descriptor)
```

Passing a few arguments and running the file prints weird symbols and artifacts. We create a script that automates runnning the script with random integer values from 0 to 1000.

The script reveals the flag multiple times:

```bash
~$ cat output.txt | grep "SSS"
You chose flag no. 111; Here: SSS{pr3tty_c0nvoluted_fl4g}
You chose flag no. 367; Here: SSS{pr3tty_c0nvoluted_fl4g}
You chose flag no. 623; Here: SSS{pr3tty_c0nvoluted_fl4g}
You chose flag no. 879; Here: SSS{pr3tty_c0nvoluted_fl4g}
```

## Flag

```
SSS{pr3tty_c0nvoluted_fl4g}
```
