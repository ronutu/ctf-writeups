# Behind the Scenes

## Description

After struggling to secure our secret strings for a long time, we finally figured out the solution to our problem: Make decompilation harder. It should now be impossible to figure out how our programs work!

## Task files:

### behindthescenes

## Solution

We are provided with a file without any information about what it is so we use ```file```.

![behind-the-scenes1](https://github.com/user-attachments/assets/5df564e2-5a84-4e94-b9aa-a65e6fcb55ee)

This indicates that the file is an ELF binary file. Next, we run ```strings``` to look for anything useful:

![behind-the-scenes2](https://github.com/user-attachments/assets/0c071cd2-4332-4239-949a-d4d5aacfb5d1)

The output ```./challenge <password>``` and ```> HTB{%s}``` gives us a small clue. We run the file by using ```./behindthescenes password``` and maybe it returns the flag. Next, we will use Ghidra to take a closer look at the file. While examining the file, we find this:


![behind-the-scenes3](https://github.com/user-attachments/assets/66f1cd5c-7fe5-4f5c-b847-a5dbb1c4adea)

It appears that the password is written vertically, so we will try that and see what we get:

![behind-the-scenes4](https://github.com/user-attachments/assets/aebc7b36-2ff2-41ad-adf0-02e869104930)

## Flag

<strong style="color: orange;">HTB{Itz_0nLy_UD2}</strong>
