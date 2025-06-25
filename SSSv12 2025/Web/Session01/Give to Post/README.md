# Give to Post

## Description

Get the flag from [give-to-post](http://141.85.224.70:8085/give-to-post/).

## Intuition

We change the request to POST.

## Solution

We also need to add another header `Content-Type: application/x-www-form-urlencoded` and also in the body we need to ask for the flag `ask=flag`.

## Flag

`SSS_CTF{this_is_how_we_roll}`
