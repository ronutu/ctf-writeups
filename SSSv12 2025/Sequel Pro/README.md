# Sequel Pro

## Description

At Sequel Pro there is a vulnerable login page. You can login as ctf with password ctf. Can you find out the secret of admin?

## Intuition

The `index.php` contains a login form that posts data on `login.php`. This could lead to SQL Injection if the user input is not properly sanitized.

## Solution

We try the basic SQL Injection payload: `admin' OR '1'='1` and we find the secret.

## Flag

```
SSS{yummy_and_nutritious}
```
