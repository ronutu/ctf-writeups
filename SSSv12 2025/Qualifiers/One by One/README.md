# One by One

## Description

Look through the binary and get the flag.

## Intuition

We try using different commands to look through the binary (`strings`, `ltrace`, `strace`, `readelf`, `xxd`)

## Solution

Using `strings one_by_one` outputs the following:

```bash
dSoo{}o_lft_pk_chchbSi_laeS_GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609
...
...
...
part20
part0
part24
part18
part3
part27
part11
part13
part23
part12
part14
part21
part9
part26
part17
part25
part15
part6
part7
part22
part2
part8
part5
part19
part4
part16
part1
part10
```

Since there are some brackets in the first line and there are also 3 "S", we could say that there is our flag. By looking further down there are some "parts" which look like permutations for the text above. We create a python script (`main.py`) to reverse the permutations and we find the flag.

## Flag

```
SSS{a_chip_of_the_old_block}
```
