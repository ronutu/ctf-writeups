# Santa

## Description

Get the flag from [santa](http://141.85.224.70:8083/santa/).

## Intuition

We look in the source code and we check the js scripts.

## Solution

Looking at the source code we see there is a script called: `assets/js/main.js`. At the end of it there is a Base 64 code. We decrypt it and find the flag.

## Flag

`SSS{chr1stm4s_c4m3_e4rly_h3_he_h3}`
