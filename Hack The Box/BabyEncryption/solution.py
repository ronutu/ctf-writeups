f = open("msg.enc", "r")
msg = f.read()
byte_msg = bytes.fromhex(msg)
decrypted_msg = ""
for char in byte_msg:
        for i in range(256):
                if char == ((123*i + 18) % 256):
                        decrypted_msg += chr(i)
                        break

print(decrypted_msg)

