# Mirror Me

## Description

Reverse the binary to find out the combination of two numbers that returns the flag. Get the flag from 141.85.224.99:31338 using netcat.

## Intuition

Use `strings` to look for anything useful.

## Solution

Using `strings mirror_me` reveals this: `find__the__3digits__numbers__whose__product = maximum__mirrored__number`. Seems like the clue we needed for the 2 numbers. We write a python script for this and find the flag.

Let's connect to `nc 141.85.224.99 31338` and input the values needed. Now we get access to move through the system. Going to `home/ctf/flag` gives us the flag.

## Flag

```
SSS{Mirror_mirror_on_the_wall_who_is_the_fairest_of_them_all}
```
