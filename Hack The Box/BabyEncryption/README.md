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

We discovered two approaches to solve this problem: one involves a brute-force method, where each number from 1 to 255 is tested with the given arithmetic operations to check for a match against the resulted message. The other, more elegant approach, transforms the problem into a linear congruence and uses an algorithm to find the solution.

### Method 1:
We will iterate through each number from 0 to 255 and apply the arithmetic operations `(123 * i + 18) % 256` to them. Then, we will compare the results to each character in the encrypted message until the entire message is successfully decrypted.
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
```
Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.
HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
```

### Method 2:
The nicer way involves looking at this problem like it is a linear congruence. In fact, it is like this: $`123*`$i $`+ 18 \equiv`$ a $`\pmod{256}`$, where a is going to take every value from the encrypted message. 

## Flag
```
HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
```
