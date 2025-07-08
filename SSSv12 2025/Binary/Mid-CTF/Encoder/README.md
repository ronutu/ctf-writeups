# Encoder

## Description

We all use structures when we are writing code, but is it easy to understand them when they are found in a binary?

Look for yourself!

## Solution

We decompile the binary and see there is a function that creates a linked list of 128 nodes, where each node has 12 bytes:

```c
for (i = 0; i < 128; i = i + 1) {
    node = (undefined4 *)malloc(12);
    *(char *)(node + 1) = (char)i;
    *node = *(undefined4 *)(&DAT_0804a040 + i * 4);
    node[2] = DAT_0804a300;
    DAT_0804a300 = node;
}
```

The first 4 bytes hold a value copied from `0x0804a040`. Only the lowest byte of the next 4 byte word stores `i` (the other three bytes are padding), and the last 4 bytes store a pointer to the previous head of the list, chaining the nodes together.

Then there is a second function that walks exactly 40 positions of the input flag. For each position it searches the 128-node list for the node whose `ch` byte equals the current flag character, and checks whether `*(0x804a240 + 4*i)` equals `node->value + i`. If any comparison fails, the flag is rejected.

In order to find the flag we create a Python script ([main.py](./main.py)) that dumps the two static arrays from the ELF, solves `table040[flag[i]] = table240[i] - i` for every `i`, and thus reconstructs the 40-byte flag without touching the heap structures at all.

## Flag

'SSS{REV_is_so_cOOl_when_there_are_Lists}'
