# BabyEncryption

## Description

You are after an organised crime group which is responsible for the illegal weapon market in your country. As a secret agent, you have infiltrated the group enough to be included in meetings with clients. During the last negotiation, you found one of the confidential messages for the customer. It contains crucial information about the delivery. Do you think you can decrypt it?

## Task files:
### 1. chall.py
```python
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
```

### 2. msg.enc
```
6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921
```

## Solution

We are provided with 2 files: an encryption script ('chall.py') and an encrypted message ('msg.enc'). Running the Python script directly results in the following error due to a missing library:
```
Traceback (most recent call last):
    File "chall.py", line 2, in <module>
        from secret import MSG
ImportError: cannot import name 'MSG' from 'secret'
```
The first thing we notice is that the function iterates through each character of the message and performs arithmetic operations before appending the result to a list. Since you can't directly add an integer to a char (`123 * char + 18`), we think that the message was first converted into its ASCII equivalent.

Afterward, the list is converted to bytes and then into hexadecimal format.

To decrypt the message, we need to reverse the process described in the script, essentially working backward from the encrypted output. Here's the script we came up with to decrypt the message:
```python
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
```

One key takeaway is that iterating over a bytes object produces integers, which is helpful since we don't need an extra step to convert the encrypted data from bytes to integers.

We then iterate over each byte in the encrypted message, comparing it to every possible ASCII value. We apply the same arithmetic operations that were used in the encryption function to find which ASCII value matches the byte. Once we find the matching ASCII value, we convert it back into a character and construct the decrypted message.
```
Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.
HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
```

## Flag
```
HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
```
