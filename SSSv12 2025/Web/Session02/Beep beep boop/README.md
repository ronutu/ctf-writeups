# Beep beep boop

## Description

Get the flag from [beep-boop-boop](http://141.85.224.70:8096/).

## Intuition

The name of this challenge is Beep beep boop so we check the `robots.txt` page.

## Solution

On `robots.txt` there is this text shown:

```
User-agent: *
Disallow: /73656372657420666f72204153494d4f.php
```

We are shown this response: `This is a secure area that can only be accessed by the most advanced humanoid robots.` and we also see there appeared a new cookie named `roboType`.

In order to find out what `roboType` we need to put there, there is a hint from that .php page from earlier. The name of the php page can be translated from hex and it returns: `secret for ASIMO`.

This is a reference to Isaac Asimov who was an American writer. Putting this name as a cookie reveals the flag.

## Flag

`SSS{We_w0rsh1p_1saac_As1m0v}`
