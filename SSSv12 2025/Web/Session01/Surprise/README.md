# Surprise

## Description

Get the flag from [surprise](http://141.85.224.70:8093/surprise). Try to modify an existing resource at this location.

## Intuition

We try changing a request method.

## Solution

The default page shows:

```
Method Not Allowed

The method is not allowed for the requested URL.
```

Changing the method to PUT reveals:

```
I don't understand you :(
```

We also put a header in the request `Content-Type: application/json` and the response changes to:

```
Better ! Give me your 'name' in this format
```

Then we add this `{"name":"name"}` in the body of the request and we get the flag.

## Flag

`SSS{valar_morghulis}`
