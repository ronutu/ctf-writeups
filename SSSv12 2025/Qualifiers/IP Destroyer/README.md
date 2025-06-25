# IP Destroyer

## Description

Be careful who you ping!

Get the flag from IP Destroyer.

## Intuition

The website lets us ping an ip address. It probably runs the following command without any sanitization: `ping ip_address`.

## Solution

We try avoiding the ping command by inserting `; ls` in the input box. It lists the files in the directory (assets, images, index.php, index.php). There is no flag so we try going back using `;ls /`. Looking through the files (/home/ctf/flag), we find the flag.

## Flag

```
SSS{hey_man_stop_pinging_around}
```
