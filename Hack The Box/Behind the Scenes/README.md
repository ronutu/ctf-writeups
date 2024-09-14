# Behind the Scenes

## Description

After struggling to secure our secret strings for a long time, we finally figured out the solution to our problem: Make decompilation harder. It should now be impossible to figure out how our programs work!

## Task files:

### behindthescenes

## Solution

We are provided with a file without any information about what it is so we use **file**.

![behind-the-scenes1](https://github.com/user-attachments/assets/5df564e2-5a84-4e94-b9aa-a65e6fcb55ee)

This indicates that the file is an ELF binary file. Next, we run **strings** to look for anything useful:

![behind-the-scenes2](https://github.com/user-attachments/assets/0c071cd2-4332-4239-949a-d4d5aacfb5d1)
