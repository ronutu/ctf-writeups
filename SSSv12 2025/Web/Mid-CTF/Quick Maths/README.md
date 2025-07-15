# Quick Maths

## Description

Get the flag from [ctf-14](http://141.85.224.118:8082/). Look out for multiple hints.

## Solution

The source code has the following js:

```js
const _0x4397 = [
  "includes",
  "calculate",
  "memory-",
  "add",
  "matches",
  "operator",
  "round",
  "action",
  "click",
  "decimal",
  "memory-cr",
  "target",
  "dataset",
  ".calculator",
  "firstValue",
  "number",
  ".calculator__display",
  "sqrt",
  ".calculator__keys",
  "children",
  "modValue",
  "fromCharCode",
  "clear",
  "from",
  "textContent",
  "previousKeyType",
  "divide",
  "multiply",
  "parentNode",
  "classList",
  "button",
  "addEventListener",
  "is-depressed",
  "querySelector",
  "subtract",
  "negative",
];
(function (_0x3c30bb, _0x439710) {
  const _0x15bd9b = function (_0x5a6c87) {
    while (--_0x5a6c87) {
      _0x3c30bb["push"](_0x3c30bb["shift"]());
    }
  };
  _0x15bd9b(++_0x439710);
})(_0x4397, 0x161);
const _0x15bd = function (_0x3c30bb, _0x439710) {
  _0x3c30bb = _0x3c30bb - 0x0;
  let _0x15bd9b = _0x4397[_0x3c30bb];
  return _0x15bd9b;
};
var m = 0x0;
const calculate = (_0x109df3, _0x334944, _0x5c1643) => {
    const _0x18515e = parseFloat(_0x109df3),
      _0x1dfe28 = parseFloat(_0x5c1643);
    if (_0x18515e == 0x45 || _0x1dfe28 == 0x45)
      return String[_0x15bd("0x1c")](
        0x67,
        0x6f,
        0x6f,
        0x67,
        0x6f,
        0x6c,
        0x70,
        0x6c,
        0x65,
        0x78,
        0x2e,
        0x70,
        0x68,
        0x70
      );
    if (_0x334944 === _0x15bd("0xa")) return _0x18515e + _0x1dfe28;
    if (_0x334944 === _0x15bd("0x5")) return _0x18515e - _0x1dfe28;
    if (_0x334944 === "multiply") return _0x18515e * _0x1dfe28;
    if (_0x334944 === _0x15bd("0x21")) return _0x18515e / _0x1dfe28;
  },
  getKeyType = (_0x5a553f) => {
    const { action } = _0x5a553f[_0x15bd("0x13")];
    if (!action) return _0x15bd("0x16");
    if (
      action === _0x15bd("0xa") ||
      action === _0x15bd("0x5") ||
      action === _0x15bd("0x22") ||
      action === _0x15bd("0x21")
    )
      return "operator";
    return action;
  },
  createResultString = (_0x317f0b, _0x3c1236, _0x267e0f) => {
    const _0x146fb3 = _0x317f0b[_0x15bd("0x1f")];
    const _0x2dfbfc = getKeyType(_0x317f0b);
    const { firstValue, operator, modValue, previousKeyType } = _0x267e0f;
    if (_0x2dfbfc === _0x15bd("0x16"))
      return _0x3c1236 === "0" ||
        previousKeyType === _0x15bd("0xc") ||
        previousKeyType === _0x15bd("0x8")
        ? _0x146fb3
        : _0x3c1236 + _0x146fb3;
    if (_0x2dfbfc === _0x15bd("0x10")) {
      if (!_0x3c1236[_0x15bd("0x7")](".")) return _0x3c1236 + ".";
      if (
        previousKeyType === _0x15bd("0xc") ||
        previousKeyType === _0x15bd("0x8")
      )
        return "0.";
      return _0x3c1236;
    }
    if (_0x2dfbfc === _0x15bd("0xc"))
      return firstValue &&
        operator &&
        previousKeyType !== "operator" &&
        previousKeyType !== _0x15bd("0x8")
        ? calculate(firstValue, operator, _0x3c1236)
        : _0x3c1236;
    if (_0x2dfbfc === _0x15bd("0x6")) return -0x1 * _0x3c1236;
    if (_0x2dfbfc === "percent") return _0x3c1236 / 0x64;
    if (_0x2dfbfc === _0x15bd("0x18")) return Math["sqrt"](_0x3c1236);
    if (_0x2dfbfc === _0x15bd("0xd")) return Math[_0x15bd("0xd")](_0x3c1236);
    if (_0x2dfbfc === _0x15bd("0x11")) {
      if ((m = 0x0)) {
      }
    }
    if (_0x2dfbfc === _0x15bd("0x9")) {
    }
    if (_0x2dfbfc === _0x15bd("0x1d")) return 0x0;
    if (_0x2dfbfc === _0x15bd("0x8"))
      return firstValue
        ? previousKeyType === _0x15bd("0x8")
          ? calculate(_0x3c1236, operator, modValue)
          : calculate(firstValue, operator, _0x3c1236)
        : _0x3c1236;
  },
  updateCalculatorState = (_0x4793dc, _0x53b7cb, _0xf0acd, _0x59ddc4) => {
    const _0x53c2f7 = getKeyType(_0x4793dc);
    const { firstValue, operator, modValue, previousKeyType } =
      _0x53b7cb["dataset"];
    _0x53b7cb["dataset"]["previousKeyType"] = _0x53c2f7;
    _0x53c2f7 === "operator" &&
      ((_0x53b7cb[_0x15bd("0x13")][_0x15bd("0xc")] =
        _0x4793dc["dataset"][_0x15bd("0xe")]),
      (_0x53b7cb[_0x15bd("0x13")]["firstValue"] =
        firstValue &&
        operator &&
        previousKeyType !== _0x15bd("0xc") &&
        previousKeyType !== _0x15bd("0x8")
          ? _0xf0acd
          : _0x59ddc4));
    _0x53c2f7 === _0x15bd("0x8") &&
      (_0x53b7cb[_0x15bd("0x13")][_0x15bd("0x1b")] =
        firstValue && previousKeyType === _0x15bd("0x8")
          ? modValue
          : _0x59ddc4);
    _0x53c2f7 === _0x15bd("0x1d") &&
      _0x4793dc[_0x15bd("0x1f")] === "AC" &&
      ((_0x53b7cb[_0x15bd("0x13")][_0x15bd("0x15")] = ""),
      (_0x53b7cb[_0x15bd("0x13")][_0x15bd("0x1b")] = ""),
      (_0x53b7cb[_0x15bd("0x13")]["operator"] = ""),
      (_0x53b7cb[_0x15bd("0x13")][_0x15bd("0x20")] = ""));
  },
  updateVisualState = (_0x4ed682, _0x521695) => {
    const _0x3654a3 = getKeyType(_0x4ed682);
    Array[_0x15bd("0x1e")](_0x4ed682[_0x15bd("0x23")][_0x15bd("0x1a")])[
      "forEach"
    ]((_0x396de2) => _0x396de2["classList"]["remove"](_0x15bd("0x3")));
    if (_0x3654a3 === "operator")
      _0x4ed682[_0x15bd("0x0")][_0x15bd("0xa")](_0x15bd("0x3"));
    if (_0x3654a3 === _0x15bd("0x1d") && _0x4ed682[_0x15bd("0x1f")] !== "AC")
      _0x4ed682[_0x15bd("0x1f")] = "AC";
    if (_0x3654a3 !== _0x15bd("0x1d")) {
      const _0x2fd81e = _0x521695[_0x15bd("0x4")]("[data-action=clear]");
      _0x2fd81e[_0x15bd("0x1f")] = "CE";
    }
  },
  calculator = document[_0x15bd("0x4")](_0x15bd("0x14")),
  display = calculator["querySelector"](_0x15bd("0x17")),
  keys = calculator[_0x15bd("0x4")](_0x15bd("0x19"));
keys[_0x15bd("0x2")](_0x15bd("0xf"), (_0x9948ab) => {
  if (!_0x9948ab[_0x15bd("0x12")][_0x15bd("0xb")](_0x15bd("0x1"))) return;
  const _0x830c2c = _0x9948ab["target"],
    _0x3e9018 = display[_0x15bd("0x1f")],
    _0x3d272b = createResultString(
      _0x830c2c,
      _0x3e9018,
      calculator[_0x15bd("0x13")]
    );
  display[_0x15bd("0x1f")] = _0x3d272b;
  updateCalculatorState(_0x830c2c, calculator, _0x3d272b, _0x3e9018);
  updateVisualState(_0x830c2c, calculator);
});
```

Looking through the code we see this array of hex values. They translate to `googolplex.php`. Going to that page shows us a bit of the php source code:

```php
$secret = 736089 + 2 ** 21;
$secret = ((($secret ?? $secret * 3) * 40 - 1234) * 2 - 100) * 2;

if (isset($_SERVER['HTTP_REFERER']) && $_SERVER['HTTP_REFERER'] == $secret) {
	$flag = 'SSS_CTF{...}';
}
```

Computing the `secret` it will be 453313424.

Then we modify the request to add the "Referer" header witht the specified number and we get the flag.

## Flag

`SSS{0ne_plus_0ne_1s_tw0}`
