# Tangled

## Description

It's pretty simple, just don't get lost along the way Get the flag from [ctf-18](http://141.85.224.118:5010/).

## Solution

The main page asks for 2 inputs. They are irrelevant. There are some chain functions in the source code that do nothing. There is an interesting function called `the_last_one()` which is not called directly.

```js
function the_last_one() {
	var elem = document.getElementById('form1');
	elem.action="/hillary";
}
```

This function will add to the action attribute inside the form to go to the /hillary endpoint with a post method. This will reveal the flag.

(Going to the hillary endpoint directly will not show the flag since its a get request, not a post)

## Flag

`SSS{living_1n_am3rica}`
