# sppb

## Description

Connect to **141.85.224.104:42069** and get the flag.

## Intuition

We open the binary in Ghidra.

## Solution

In the main function we see this conditions:

```c
if (((99 < readValue) && (readValue == (readValue / 13) * 13)) && (readValue < 323)) {
    password_accepted();
  }
```

All we have to do is to find a number between 99 and 323, divisible by 13. One of them could be 130.

## Flag

'SSS_CTF{decompiling_spoils_the_fun}'
