# Cake

## Description

Get the flag from Cake.

We all love **applepie**.

## Intuition

The source code is clean and doesn't help us at all so we open the dev tools to look for anything useful.

## Solution

Looking at Storage -> Cookies we see there is an empty `FLAG` variable. We then try to input `applepie` as a value for that variable and refresh the page. The new value shown in the `FLAG` is `SSS%7Bhansel_gretel%7D`. `%7B` and `%7D` are URL encodings for `{` and `}`.

## Flag

```
SSS{hansel_gretel}
```
