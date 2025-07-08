# Simple

## Description

I gave this task to two of my friends. One of them opened it in IDA and had a sudden heart attack for some reason. The other one didn't even use IDA and he somehow managed to solve it!

## Solution

Decompiling the binary in Ghidra shows an big number of functions, but the program’s high-level flow is simple:

1. Read a password from stdin.

2. Transform each input byte using the function at `0x08048660`.

3. Compare the transformed bytes against another 34 hard coded bytes shown in the program.

4. Print “Well done!” if every byte matches; otherwise print “Wrong!”.

The hard-coded bytes look like this:

```c
local_58 = 197;
local_57 = 0xc5;
local_14 = *(int *)(in_GS_OFFSET + 0x14);
local_56 = 0xc5;
local_55 = 0xed;
local_54 = 0x19;
local_53 = 0x6d;
local_52 = 0xb9;
local_51 = 0x49;
local_50 = 0x79;
local_4f = 0x69;
local_4e = 0xc9;
local_4d = 0xf5;
local_4c = 0x49;
local_4b = 0xb9;
local_4a = 0x49;
local_49 = 0x39;
local_48 = 0x6d;
local_47 = 0xcd;
local_46 = 0x69;
local_45 = 0xcd;
local_44 = 0xf5;
local_43 = 0xdd;
local_42 = 0x69;
local_41 = 0xb9;
local_40 = 0xcd;
local_3f = 0xf5;
local_3e = 0x1d;
local_3d = 0x29;
local_3c = 0x59;
local_3b = 0xf5;
local_3a = 0x19;
local_39 = 0x49;
local_38 = 0x6d;
local_37 = 0x7d;
```

Rather than reversing the combination of functions, we noticed something: applying the same function twice returns the original value. In math terms, the function is an involution. Therefore `f(f(x)) = x`.

To call the function in gdb we did this for every byte:

```bash
pwndbg> set $f = (unsigned char (*)(unsigned int))0x08048660
pwndbg> p/x $f(0xc5)
$7 = 0x53
pwndbg> p/c $7
$8 = 83 'S'
```

Repeating that for all 34 bytes yields the full flag.

## Flag

`SSS{dynamic_analysis_wins_the_day}`
