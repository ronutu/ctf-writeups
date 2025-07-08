from pwn import ELF

elf = ELF("./encoder")

table040 = elf.read(0x804A040, 128 * 4)
table240 = elf.read(0x804A240, 40 * 4)

t040 = list(
    int.from_bytes(table040[i : i + 4], "little", signed=True)
    for i in range(0, len(table040), 4)
)
t240 = list(
    int.from_bytes(table240[i : i + 4], "little", signed=True)
    for i in range(0, len(table240), 4)
)

flag = []
for i in range(40):
    want = t240[i] - i
    j = t040.index(want)
    flag.append(j)

print("Flag bytes:", flag)
print("Flag:", bytes(flag).decode())
