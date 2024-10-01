# conv

## Description
Time for convolutions.
```python
def conv(array1:bytes, array2:bytes) -> bytes:
    len1, len2 = len(array1), len(array2)
    res = [0]*(len1 + len2 - 1)
    for i in range(len1 + len2 - 1):
        csum = 0
        for j in range(max(0, i - len2 + 1), min(len1, i + 1)):
            csum += array1[j] * array2[i - j]
        res[i] = csum % 256
    return res

key = b'\xab\xec\xe9<\xaaC\x7fr\xeb\x8dgQ\xc0\x94\x01\x1d\xc03\x14\x97\xe2\x91\x97\xcf\x8b\x13?\x1d24w|'
cip = conv(plain1,key)
print(bytes(cip).hex())
```
Output:
```
17c080c00398a06e4661e403b2b571b578221bba83e235a0feece7213ad4d65c1d89c2a3afae5ef91bf7f2181f0c797505b7bd55c62d1edf2614b17f88f85eac674fbd6d7be4e2a617605c68e1baf8603cb9b1d32b2bc1ab60d8c62b20be0bc0fb73a546b5641988a3bf8eeb778731e048970308d941a8bd5f6cb56159069364c93b5429afdb85f9dfb5f5b0ca44d314af68bc9d56b39321fe5cc072c9508978693ee60a9bffff5b52f6aa0ca37f9b421eb402a4886b742570926b7479d2b89528caceb7121a338c233164c33a120b9813bc56b855c914124ecb30df3d4a14c92788faa7c9e32b544e24d9d9fe2a5539a280c28466dc6b276ba4b089fa26f8bace95f43f6c5d491e14e5fa09a853fff2dfd73a8cf8d7b54d3d8d693db7b182789f47e343e9cf56f8663e181a1e98276aface8b1052e3ee9c6630d69ad479bfe1106ec1ab585a030ca130a6d849f9c4bed9d0b16f46890f1efa66c8f21f078088f426ef0e1f9af315ae3b2356123df174bb4095ad2361237bedc3e62c294f8ccc135f9766f0ec2a462087cd2648
```
Plaintext is ascii printable.

## Solution
We are given a function that takes two bytes objects as input and produces a third one as output. While we know the second input (key) and the result (cip), we aim to find first input (plain1).

To begin, we examine the lengths of the bytes. **key** consists of 32 integers, while **cip** contains 397 integers. From ```res = [0]*(len1 + len2 - 1)```, we can determine that **plain1** has a length of 366.

Although not strictly necessary, we will tidy up the code a bit, resulting in the following:
```python
def conv(array1:bytes, array2:bytes) -> bytes:
    res = [0]*397
    for i in range(397):
        csum = 0
        for j in range(max(0, i - 31), min(366, i + 1)):
            csum += array1[j] * array2[i - j]
        res[i] = csum % 256
    return res
```

Now that we a have a clearer idea of how the function works, we can observe that this is a linear congruence system that looks like this:<br>

$` plain1 = \{p_0, p_1, p_2, \ldots, p_{365}\} \quad \text{(366 elements)} `$ 
<br>

$` key = \{171, 236, 233, \ldots, 124\} \quad \text{(32 elements)} `$
<br>

$` cip = \{23, 192, 128, \ldots, 72\} \quad \text{(397 elements)} `$ 
<br>

$`
\begin{cases}
p_1 \cdot 171 \equiv 23 \pmod{256}\\
p_1 \cdot 236 + p_2 \cdot 171 \equiv 192 \pmod{256}\\
p_1 \cdot 233 + p_2 \cdot 236 + p_3 \cdot 171 \equiv 128 \pmod{256}\\
\vdots \\
p_2 \cdot 124 + \ldots + p_{31} \cdot 171 \equiv 92 \pmod{256}\\
\vdots \\
p_{335} \cdot 124 + p_{366} \cdot 171 \equiv 241 \pmod{256}\\
\vdots
\end{cases}
`$

We will solve this by constructing 2 matrices, both with 397 rows:<br>

$$
A =
\begin{pmatrix}
171 & 0 & 0 & \ldots & 0 \\
236 & 171 & 0 & \ldots & 0\\
233 & 236 & 171 & \ldots & 0\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
0 & 0 & 0 & \ldots & 171
\end{pmatrix}, 
b =
\begin{pmatrix}
23\\
192\\
128\\
\vdots \\
72
\end{pmatrix}\\
$$

Thus, we have the system of equations represented as $Ax \equiv b \pmod{256}$.

Now we will compute the matrix in Python:
```python
    A = np.zeros((397, 397))

    len1, len2 = len(array1), len(array2)
    res = [0]*(len1 + len2 - 1)
    for i in range(len1 + len2 - 1):
        csum = 0
        for j in range(max(0, i - len2 + 1), min(len1, i + 1)):
            csum += array1[j] * array2[i - j]
            A[i][j] = array1[j] * array2[i - j]
        res[i] = csum % 256
```
And we will also compute the b matrix:
```python
b = np.zeros((397, 1))
for i in range(397):
    b[i][0] = res[i]
```
Next we are going to use [this algorithm](https://stackoverflow.com/questions/48252234/how-to-solve-a-congruence-system-in-python) to solve the congruence system. The final code will be:
```python
import numpy as np


def conv(array1:bytes, array2:bytes) -> bytes:
    A = np.zeros((397, 397))

    len1, len2 = len(array1), len(array2)
    res = [0]*(len1 + len2 - 1)
    for i in range(len1 + len2 - 1):
        csum = 0
        for j in range(max(0, i - len2 + 1), min(len1, i + 1)):
            csum += array1[j] * array2[i - j]
            A[i][j] = array1[j] * array2[i - j]  # compute matrix A
        res[i] = csum % 256
    return res, A


plain1 = [1]*366
key = b'\xab\xec\xe9<\xaaC\x7fr\xeb\x8dgQ\xc0\x94\x01\x1d\xc03\x14\x97\xe2\x91\x97\xcf\x8b\x13?\x1d24w|'
cip, A = conv(plain1,key)
# convert cip from hex to bytes
res = bytes.fromhex("17c080c00398a06e4661e403b2b571b578221bba83e235a0feece7213ad4d65c1d89c2a3afae5ef91bf7f2181f0c797505b7bd55c62d1edf2614b17f88f85eac674fbd6d7be4e2a617605c68e1baf8603cb9b1d32b2bc1ab60d8c62b20be0bc0fb73a546b5641988a3bf8eeb778731e048970308d941a8bd5f6cb56159069364c93b5429afdb85f9dfb5f5b0ca44d314af68bc9d56b39321fe5cc072c9508978693ee60a9bffff5b52f6aa0ca37f9b421eb402a4886b742570926b7479d2b89528caceb7121a338c233164c33a120b9813bc56b855c914124ecb30df3d4a14c92788faa7c9e32b544e24d9d9fe2a5539a280c28466dc6b276ba4b089fa26f8bace95f43f6c5d491e14e5fa09a853fff2dfd73a8cf8d7b54d3d8d693db7b182789f47e343e9cf56f8663e181a1e98276aface8b1052e3ee9c6630d69ad479bfe1106ec1ab585a030ca130a6d849f9c4bed9d0b16f46890f1efa66c8f21f078088f426ef0e1f9af315ae3b2356123df174bb4095ad2361237bedc3e62c294f8ccc135f9766f0ec2a462087cd2648")

# compute matrix b
b = np.zeros((397, 1))
for i in range(397):
    b[i][0] = res[i]



def linear_congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a %= m

    b %= m
    while a > m:
        a -= m

    return (m * linear_congruence(m, -b, a) + b) // a


x = np.zeros((397, 1))
x[0] = linear_congruence(A[0][0], b[0], 256)
for i in range(1, 397):
    sum = 0
    for j in range(0, i):
        sum += A[i][j] * x[j]
    x[i] = linear_congruence(A[i][i], (b[i] - sum) % 256, 256)


flag = ""
for i in x:
    flag += chr(int(i[0]))
print(flag)
```

```
Elit cybernetica fusce stratagemata enigma penetratio exsertus. CTF{89c5cce663fce1500d22c2ef5112dc2885c491d37d3503118251bdd516b4dcc0} Combinatio complexus networkus quantum facilis vectura obfuscatus. Latitudo cripto diversus et preditus, securitas hexadecimale detectus phantasma scriptum. Insidiae infiltratio breviaria kernel status, protus obscura administratio.
```

## Flag
```
CTF{89c5cce663fce1500d22c2ef5112dc2885c491d37d3503118251bdd516b4dcc0}
```

