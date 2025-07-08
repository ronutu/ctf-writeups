# Hibercal

## Description

Mission Briefing:

In hyperspace we encountered a species that wants to join forces with us. However, we fear they are actually trying to fool us. As a token of their "friendliness" it is customary to let friend-species sign their hyperspace hibernation calendar. We need to buy some time to figure out their actual intentions. Figure out how to spawn a shell. Can you do it? We're counting on you. You can access the station at 141.85.224.104:6668.

## Solution

First thing to notice is that PIE is disabled for this binary. This is something that will become useful later.

```c
Arch:     i386
RELRO:      Partial RELRO
Stack:      No canary found
NX:         NX enabled
PIE:        No PIE (0x8048000)
Stripped:   No
```

The program starts a listening socket, forks, and asks the client for three values: a name, a day, and the text to write.

The vulnerability of this binary is that we can access an array out of bounds and write things there.

```c
int local_50 [16];

if (allowed_day == 0) {
    printf("You are allowed to write an entry in the %d-day hibernation calendar. What will it be? M ake it a good one!\n"
            ,0x10);
    puts("Which day?");
    __isoc99_scanf(&DAT_08048d83,&allowed_day);
    puts("What do you want to write?");
    __isoc99_scanf(&DAT_08048d83,&entry);
}
else {
    puts("You already wrote in my calendar");
}
local_50[allowed_day] = entry
```

Looking in the disassembly, we see that EIP is at 0x50 (80) bytes from the beginning of the local_50 array. That means, in addition to those 16 x 4 = 64 bytes of the array, we can rewrite the address of the EIP if we access local_50[20]. This can be done since there is no check for out of bounds values.

At local_50[20] we can write the address of `system()` since PIE is disabled.

When we start the program we will input our name as "/bin/sh". Then there will be called `hibercal(name)` which will push our name on the stack.

Next we will input the day number, which we will input 20 to go out of bounds and overwrite the EIP, and finally we will input the address of system (in decimal form because the scanf takes %d) so we can overwrite the EIP with the address of `system()`. Doing all of this will give us a shell.

## Flag

`SSS_CTF{i_hOPE_yOU-re_rIGht_D@rLing._Go0d_Hun7in}`
