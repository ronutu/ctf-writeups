# Gimme

## Description

Get the flag from [gimme](http://141.85.224.70:8082/gimme) (now it’s safe! no more cockroaches :D). Try to add a new resource.

## Intuition

Try a different request method.

## Solution

On the first page we see this:

```bash
Method Not Allowed

The method is not allowed for the requested URL.
```

We change the method to POST and now we get this:

```bash
Did you miss something ?
```

Furthermore we add another header `Content-Type: text/html; charset=utf-8` to get this:

```bash
Not great, not terrible ! You should try 35 :)
```

35 refers to the length of the body. Entering 35 chars in the body reveals the flag.

## Flag

`SSS{dont_forget_the_content_length}`
