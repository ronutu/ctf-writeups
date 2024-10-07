# Bypass

## Description

The Client is in full control. Bypass the authentication and read the key to get the Flag.

## Task files:

**Bypass.exe**

## Solution

We are provided an executable file. Running the file it prompts us to enter a `username` and `password`. After a few tries, the response is always "Wrong username and/or password".

We start by running `strings` on the executable to search for any clues. The output shows the following:
```
HTBChallange
.NETFramework,Version=v4.5.2
FrameworkDisplayName
.NET Framework 4.5.2
Copyright
  2019
_CorExeMain
mscoree.dll
```

This indicates that the application is built using the .NET framework, likely written in C#. Knowing this, we can decompile it using a .NET decompiler such as `dnSpy`.

Opening the file in dnSpy, we notice several functions and locate the main one:
```csharp
using System;

public class 0
{
	public static void 0()
	{
		bool flag = global::0.1();
		bool flag2 = flag;
		if (flag2)
		{
			global::0.2();
		}
		else
		{
			Console.WriteLine(5.0);
			global::0.0();
		}
	}

	public static bool 1()
	{
		Console.Write(5.1);
		string text = Console.ReadLine();
		Console.Write(5.2);
		string text2 = Console.ReadLine();
		return false;
	}

	public static void 2()
	{
		string <<EMPTY_NAME>> = 5.3;
		Console.Write(5.4);
		string b = Console.ReadLine();
		bool flag = <<EMPTY_NAME>> == b;
		if (flag)
		{
			Console.Write(5.5 + global::0.2 + 5.6);
		}
		else
		{
			Console.WriteLine(5.7);
			global::0.2();
		}
	}

	public static string 0;

	public static string 1;

	public static string 2 = 5.8;
}
```

The function names and variable names are obfuscated, but we can still deduce the logic. Let's add some comments to clarify what is happening:
```csharp
	public static bool 1()
	{
		Console.Write(5.1);                // Prints: "Enter a username:"
		string text = Console.ReadLine();  // User inputs username
		Console.Write(5.2);                // Prints: "Enter a password:"
		string text2 = Console.ReadLine(); // User inputs password
		return false;                      // Always returns false, no matter the inputs
	}
```

```csharp
    public static void 0()
	{
		bool flag = global::0.1();         // Calls function 1
		bool flag2 = flag;                 // flag2 = false
		if (flag2)                         // Always false
		{
			global::0.2();                 // Calls another function
		}
		else
		{
			Console.WriteLine(5.0);        // Prints: "Wrong username and/or password"
			global::0.0();                 // Restarts the main function
		}
	}
```

The main function `public static void 0` calls `public static bool 1` which always returns `false`, causing the message "Wrong username and/or password" to be displayed.

To bypass this, we can edit the Intermediate Language (IL) instructions. At index 6, we have the `brfalse.s` instruction:
> brfalse.s: Branch to target if value is zero (false), short form.

We need to change this to `brtrue.s`:
> brtrue.s: Branch to target if value is non-zero (true), short form.

This modification will force the program to take the "if" branch even if the check fails.

Next, the `public static void 2()` function is executed, which asks for a "secret key." The original code looks like this: 
```csharp
	public static void 2()
	{
		string <<EMPTY_NAME>> = 5.3;
		Console.Write(5.4);                // Prints: "Please enter the secret key:"
		string b = Console.ReadLine();     // User inputs the key
		bool flag = <<EMPTY_NAME>> == b;   // flag = true if the input matches the secret key; false otherwise
		if (flag)
		{
			Console.Write(5.5 + global::0.2 + 5.6);
		}
		else
		{
			Console.WriteLine(5.7);        // Prints: "Wrong Key"
			global::0.2();                 // Restarts the function
		}
	}
```

We can similarly modify the IL instructions here to bypass this check, and the flag will be revealed.
```
Nice here is the Flag:HTB{SuP3rC00lFL4g}
```

Another, simpler approach is to add breakpoints at the "if" statements and manually change the boolean values to `true` using dnSpy's interactive debugger. This bypasses both checks. While testing, this also reveals the required key:"ThisIsAReallyReallySecureKeyButYouCanReadItFromSourceSoItSucks".



## Flag

```
HTB{SuP3rC00lFL4g}
```

