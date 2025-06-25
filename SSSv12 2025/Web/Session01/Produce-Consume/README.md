# Produce-Consume

## Description

Get the flag from [produce-consume](http://141.85.224.70:8091/produce-consume/).

See resource files: [https://github.com/open-education-hub/web-security/tree/main/chapters/web-application-security/web-basics/drills/produce-consume/public](https://github.com/open-education-hub/web-security/tree/main/chapters/web-application-security/web-basics/drills/produce-consume/public)

## Intuition

We look at the source code of the .php files and we notice a session variable which we must reuse.

## Solution

`produce.php` saves the current timestamp in a session variable and `consume.php` checks if the current session variable is the actual time and then print the flag.

To solve this we must put the cookie from `produce.php` to 'consume.php' almost at the same time. To do this consecutively:

```bash
curl -c cookies.txt http://141.85.224.70:8091/produce-consume/produce.php; curl -b cookies.txt http://141.85.224.70:8091/produce-consume/consume.php
```

## Flag

`SSS_CTF{seven_years_of_bad_luck}`
