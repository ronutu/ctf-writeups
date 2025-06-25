# My Special Name

## Description

Get the flag from [my-special-name](http://141.85.224.70:8088/my-special-name). Retrieve all the names and you will get the flag. Use the [b]name-id[/b] parameter.

## Intuition

We get hinted to use name-id as paramater so we do that.

## Solution

Running:

```bash
http://141.85.224.70:8088/my-special-name?name-id=1
http://141.85.224.70:8088/my-special-name?name-id=2
...
```

We see that every name-id gives us a different name, but repeats after reaching 100. We create a small bash script to print all 100 names ([main.sh](./main.sh)). One of those names is the flag.

## Flag

`SSS{th3_Intrud3r}`
