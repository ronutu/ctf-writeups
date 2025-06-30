# Mind your own business

## Description

Get the flag from [mind-your-own-business](http://141.85.224.70:8085/).

## Intuition

We check for IDOR.

## Solution

There is an IDOR on the webiste for invoices. The only invoice numbers that show something are fibonacci numbers. We create a script to curl the first few fibonacci numbers and then grep for the flag (`main.sh`).

## Flag

`SSS{1ts_n0t_nic3_t0_sn00p_ar0und}`
