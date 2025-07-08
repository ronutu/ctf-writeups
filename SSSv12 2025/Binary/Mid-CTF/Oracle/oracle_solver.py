#!/usr/bin/env python
from pwn import *

def fib(input_num):
    a = 0
    b = 1
    if input_num == 0:
        return 0
    if input_num == 1:
        return 1
    else:
        for iter in range(2, (input_num + 1)):
            local = a + b
            a = b
            b = local
        return b
    

BIN = "./oracle"
context.binary = BIN
elf = ELF(BIN)


# First part: inject
io = remote("141.85.224.104", 6661)
io.recvline() # prima linie
for i in range(1000):
    num = int(io.recvline())
    print(num)
    io.sendline(str(fib(num)))
io.interactive()
