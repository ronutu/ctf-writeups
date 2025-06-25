# Detective

## Description

This challenge runs remotely at **141.85.224.104:31337**. You can use **netcat** to connect to it.

Investigate the **detective** binary. See what it does and work to get the flag.

You can start from the [exploit_template.py](./exploit_template.py) solution template script.

There is a bonus to this challenge and you will be able to find another flag. See that below.

**Bonus: Get the Second Flag**

You can actually exploit the remote detective executable and get the second flag. Look thoroughly through the executable and craft your payload to exploit the remote service.

You need to keep the connection going. Use the construction: `cat /path/to/file - | nc`

## Intuition

We try running `strings` and then check for a possible buffer overflow.

## Solution

```bash
$ strings ./detective
...
/bin/sh
Well done, here's your flag: 
/bin/cat /home/ctf/flag
There is another flag. Can you get it?
gimme gimme
...
```

There is this strange `gimme gimme` so we try to input it and we get the first flag.

For the second we flag we open the binary in pwndbg and dissasemble it. We see there is an `fgets` so we try to check for a buffer overflow.

To do this we create a `cylcic 100` and then check where we got SIGSEV with `cyclic -l 0x616161616161616a`. The offset is at 72. 

The binary is not PIE and we can use functions such as `system`, but for the sake of this challenge we only need to call the `nononono` function with [main.py](./main.py) to get the second flag.

## Flag

`SSS{what_is_more_meaningful_than_your_own_strength}`

`SSS{a_pair_of_new_boots_size_9_please}`