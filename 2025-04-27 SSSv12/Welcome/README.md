# Welcome

## Description

Always be patient.

Get the flag from Welcome.

## Intuition

Looking at the source code we can see that the flag is scattered across the html page, css, js, etc.

## Solution

The first part of the flag is in the css file. The second part of the flag is on the main page, but invisible. The third part of the flag is available at `static/hidden.js`. The last part is found at `static/logo.png`. The flag looks like this: `FFF{rirel_svyr_unf_srryvatf}`. Since this isn't the correct flag and the flags in these challanges start with `SSS{...}`, we can expect that there is some kind of letter substitution. The simplest one is Caesar's cipher. We can look at ROT13 (shifts every letter 13 places to the right). By inserting this in CyberChef with the ROT13 operation we find the actual flag.

## Flag

```
SSS{every_file_has_feelings}
```
