# Corporate Network

## Description

Gain access to the coporate network at [ctf-14](http://141.85.224.118:8080/).

## Solution

The main page shows this message:

`You can access this page only from the company's intranet!`

We try to modify headers to be granted access. We found an interesting header to use:

> The HTTP X-Forwarded-For (XFF) request header is a de-facto standard header for identifying the originating IP address of a client connecting to a web server through a proxy server.

After using this header `X-Forwarded-For: 192.168.0.1` we are granted with another message:

`You need the use the default browser installed on your Windows Work Computer (Yandex) to access the intranet!`

So we modify the `User-Agent` header to include `YaBrowser`.

Next we see in the response there are 2 cookies set: `user=aladdin` and `assword=opensesame`.

This hints us to authenticate with those credentials. In order to do that we must add the `Authorization` header with the following syntax:

`Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l`

> For Basic authentication, the credentials are constructed by first combining the username and the password with a colon (e.g., aladdin:opensesame), and then by encoding the resulting string in base64 (e.g., YWxhZGRpbjpvcGVuc2VzYW1l).

## Flag

`SSS{oooo0000hh_deeee3333p_bre3ach}`
