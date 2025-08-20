# Domino

## Description

Connect to **141.85.224.104:9669** and get the flag.

## Intuition

We open the binary in Ghidra and see there are a series of ifs we have to match.

## Solution

There is a final if condition we have to get past in order to get the shell.

First condition we have to meet is the highest byte need to be equal to 2:

```c
(ABCD >> 24 == 2)
```

Then the second highest byte has to be 0:

```c
pvVar1 = (void *)(BCD >> 0x10 & 0xff)
(pvVar1 == (void *)0x0)
```

After that the third highest byte has to be 09 or 0a or 0b:

```c
(((uint)param_1 >> 8 & 0xff) - 9 < 3)
```

Finally the last byte must be 1:

```c
((D & 0x3fffffff) == 1
```

The final value looks like this: `0x02000901` which is equal to `33556737` (decimal). Connecting to the host with this password will show the flag.

## Flag

`SSS_CTF{now_you_know_your_abcs}`
