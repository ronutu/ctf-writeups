# Chef hacky mchack

## Description

Get the flag from [Chef hacky mchack](http://141.85.224.70:8087/).

## Intuition

We modify a cookie.

## Solution

By modyfing the `u=hacky mchack` cookie, there appears a new item in the top navbar called `Manage`. This button leads to `http://141.85.224.70:8087/manage.php` where we find the flag.

## Flag

`SSS{n0_m0r3_c00ki3s_f0r_y0u_m1st3r}`
