# hyp3rs3rv3r

## Description

Connect to **141.85.224.104:4242** and see how a web server behaves like.

Use the hyp3rs3rv3r binary to exploit it and get the flag.

## Intuition

Find a vulnerable function in the disassembler.

## Solution

We open up the binary in Ghidra and see that it is stripped. We manage to find the main function and we figure out this is a binary for a web server.

There are 2 endpoints possible: "LIST" and "GET". There is also a `strstr` function that checks the input starts with "GET":

```c
strstr(input_buffer,"GET")
```

Going further in the "GET" endpoint we see that it does some XORs to check that in the buffer exists " HTT". We can convinently put this string at the end of our payload.

Then we see a vulnerable buffer through memcpy:

```c
memcpy(local_1a7,local_20 + 2,buffer_size);
```

That is because buffer_size is 512 chars and local_1a7 can only hold 123 chars.

Now we need to find the offset where the buffer overflow happens.

```c
        080495ba 8d 85 5d        LEA        EAX=>local_1a7,[EBP + 0xfffffe5d]
                 fe ff ff
        080495c0 50              PUSH       EAX
        080495c1 e8 aa fa        CALL       <EXTERNAL>::memcpy                               void * memcpy(void * __dest, voi
                 ff ff
```

We can see that local_1a7 is at 419 bytes distance from the base pointer. What we need to do next is add 4 more bytes for the length of the return address and then we call any function we want.

Browsing through the function we see see a function that might print our flag so we write our payload in a python script ([main.py](./main.py)) and call that function to get root and find the flag.

## Flag

'SSS{pRoDucE_a_StRinG_PLz}'
