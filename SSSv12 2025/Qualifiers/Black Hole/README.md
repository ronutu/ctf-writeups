# Black Hole

## Description

The program is trying to hide something from you.

## Intuition

We try using different commands to look through the binary (`strings`, `ltrace`, `strace`, `readelf`, `xxd`)

## Solution

We use `ltrace ./black_hole` and we get this:

```bash
fwrite("SSS{the_more_you_look_the_less_y"..., 48, 1, 0x3d9e12a0)
```

We don't see yet the full flag, but looking at the `ltrace --help` there is an option for the output size:

```bash
 -s STRSIZE          specify the maximum string size to print.
```

Running `ltrace -s 49 ./black_hole` will print the full flag.

## Flag

```
SSS{the_more_you_look_the_less_you_actually_see}
```
