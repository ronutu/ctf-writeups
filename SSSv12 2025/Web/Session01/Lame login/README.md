# Lame login

## Description

Get the flag from [lame-login](http://141.85.224.70:8087/lamelogin).

## Intuition

We look at the source code.

## Solution

The source code has a commented hash. We try putting it on CrackStation. We see that we get a partial match for a sha1 hash to admin. We divide the hash in 2 parts. For the first part we get an exact match to admin and then for the second hash we also get an exact match for Password123$.

Entering these credentials on the main page reveals the flag

## Flag

`SSS{come_ooon_dude}`
