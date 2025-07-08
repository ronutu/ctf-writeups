# First Blood

## Description

This one's easy: get the flag from **141.85.224.104:6660**.

## Solution

The binary prompts for two inputs—a first name and a last name. The last-name buffer begins at `0x1040c0`, which is `m + 0x80` (128 bytes) relative to the start of the first-name buffer `m`.

```c
read_input("What\'s your first name? ",m,128);
read_input("What\'s your last name? ",0x1040c0,512);
```

To reach the shell, we must satisfy the checks in `check()` that inspect specific offsets inside `m`.

```c
if (m._256_4_ == L'\x97979797') {
    iVar2 = strncmp(m + 0x104,"prince of darkness",0x12);
    if ((iVar2 == 0) && (m._296_8_ == 0x1112131415161718)) {
        puts("You win! Have a shell!");
        system("/bin/sh");
    }
}
```

- Offset 0x100 (256) – must contain the dword `0x97979797`.

- Offset 0x104 (260) – must hold the ASCII string "`prince of darkness`" (18 bytes).

- Offset 0x128 (296) – must contain the qword `0x1112131415161718`.

We craft a payload that places these values at the required offsets and send it with a [script](./main.py). Once all conditions are met, the binary prints “You win! Have a shell!” and executes `/bin/sh`, letting us read the flag.

## Flag

'SSS{pretty_easy_eh_rambo?}'
