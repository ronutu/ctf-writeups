# The Talker

## Description

What's it saying? Use SSH to connect to connect@141.85.224.99:2222 using password c0nn3ct and find out the flag.

## Intuition

Just connect using ssh.

## Solution

Doing `ls` and then `cat flag` shows a wrong flag. Going a bit deeper in `cd x` and then `cat rez.txt` shows the real flag.

## Flag

```
SSS{the_talker_has_spoken}
```
