# Colors

## Description

Get the flag from [colors](http://141.85.224.70:8082/colors/index.php?index=1).

## Intuition

We look for an IDOR.

## Solution

There is a kind of IDOR by changing the index name: `http://141.85.224.70:8082/colors/index.php?index=1`. We brute force (`main.sh`) the first few hundred colors to find the flag.

## Flag

`SSS{d1d_y0u_4ctu4lly_cl1ck_3141_t1mes}`
