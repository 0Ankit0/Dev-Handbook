# Appendix C: JavaScript Reference

---

## Introduction

JavaScript is the programming language of the web. This appendix provides a comprehensive reference to JavaScript's core features, including operators, statements, built‑in objects, and methods. It is organized to help you quickly find the syntax and usage of language elements you need.

The reference is divided into several sections:

- **Operators Reference** – Arithmetic, assignment, comparison, logical, bitwise, and other operators.
- **Statements Reference** – Declaration, conditional, loop, and control flow statements.
- **Built‑in Objects** – Overview of JavaScript's native objects.
- **Array Methods** – Complete list of array methods with descriptions and examples.
- **String Methods** – Complete list of string methods.
- **Number Methods** – Methods and properties of the `Number` object.
- **Math Methods** – Mathematical functions and constants.
- **Date Methods** – Working with dates and times.
- **Object Methods** – Methods for manipulating objects.

This reference assumes a working knowledge of JavaScript; for in‑depth explanations, refer to the relevant chapters in the main handbook.

---

## Operators Reference

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` → `8` |
| `-` | Subtraction | `5 - 3` → `2` |
| `*` | Multiplication | `5 * 3` → `15` |
| `/` | Division | `15 / 3` → `5` |
| `%` | Modulo (remainder) | `5 % 2` → `1` |
| `**` | Exponentiation | `2 ** 3` → `8` |
| `++` | Increment | `let x = 5; x++;` → `x` becomes `6` |
| `--` | Decrement | `let x = 5; x--;` → `x` becomes `4` |
| `+` (unary) | Unary plus (converts to number) | `+"5"` → `5` |
| `-` (unary) | Unary negation | `-5` → `-5` |

### Assignment Operators

| Operator | Description | Equivalent to |
|----------|-------------|---------------|
| `=` | Assignment | `x = y` |
| `+=` | Addition assignment | `x = x + y` |
| `-=` | Subtraction assignment | `x = x - y` |
| `*=` | Multiplication assignment | `x = x * y` |
| `/=` | Division assignment | `x = x / y` |
| `%=` | Modulo assignment | `x = x % y` |
| `**=` | Exponentiation assignment | `x = x ** y` |
| `<<=` | Left shift assignment | `x = x << y` |
| `>>=` | Right shift assignment | `x = x >> y` |
| `>>>=` | Unsigned right shift assignment | `x = x >>> y` |
| `&=` | Bitwise AND assignment | `x = x & y` |
| `^=` | Bitwise XOR assignment | `x = x ^ y` |
| `|=` | Bitwise OR assignment | `x = x | y` |
| `&&=` | Logical AND assignment | `x &&= y` (ES2021) |
| `||=` | Logical OR assignment | `x ||= y` (ES2021) |
| `??=` | Nullish coalescing assignment | `x ??= y` (ES2021) |

### Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to (with type coercion) | `5 == "5"` → `true` |
| `===` | Strict equal to (no coercion) | `5 === "5"` → `false` |
| `!=` | Not equal to | `5 != "5"` → `false` |
| `!==` | Strict not equal to | `5 !== "5"` → `true` |
| `>` | Greater than | `5 > 3` → `true` |
| `>=` | Greater than or equal to | `5 >= 5` → `true` |
| `<` | Less than | `3 < 5` → `true` |
| `<=` | Less than or equal to | `3 <= 3` → `true` |

### Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&&` | Logical AND | `true && false` → `false` |
| `\|\|` | Logical OR | `true \|\| false` → `true` |
| `!` | Logical NOT | `!true` → `false` |
| `!!` | Double NOT (convert to boolean) | `!!"hello"` → `true` |

### Bitwise Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&` | Bitwise AND | `5 & 1` → `1` (0101 & 0001 = 0001) |
| `\|` | Bitwise OR | `5 \| 1` → `5` (0101 | 0001 = 0101) |
| `^` | Bitwise XOR | `5 ^ 1` → `4` (0101 ^ 0001 = 0100) |
| `~` | Bitwise NOT | `~5` → `-6` (inverts bits) |
| `<<` | Left shift | `5 << 1` → `10` (0101 << 1 = 1010) |
| `>>` | Right shift (sign‑propagating) | `-5 >> 1` → `-3` |
| `>>>` | Right shift (zero‑fill) | `5 >>> 1` → `2` |

### String Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | String concatenation | `"Hello" + " " + "World"` → `"Hello World"` |
| `+=` | Concatenation assignment | `let s = "Hello"; s += " World";` → `s` becomes `"Hello World"` |

### Conditional (Ternary) Operator

| Operator | Description | Example |
|----------|-------------|---------|
| `? :` | Ternary conditional | `condition ? exprIfTrue : exprIfFalse` |

### Comma Operator

| Operator | Description | Example |
|----------|-------------|---------|
| `,` | Evaluates both operands, returns the second | `let x = (1, 2, 3);` → `x` is `3` |

### Unary Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `typeof` | Returns type of operand | `typeof "hello"` → `"string"` |
| `instanceof` | Tests if object is instance of class | `arr instanceof Array` → `true` |
| `delete` | Deletes object property | `delete obj.prop` |
| `void` | Evaluates expression and returns `undefined` | `void 0` → `undefined` |
| `await` | Waits for promise (inside async function) | `let result = await promise;` |

### Relational Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Checks if property exists in object | `"length" in []` → `true` |

### Nullish Coalescing Operator

| Operator | Description | Example |
|----------|-------------|---------|
| `??` | Returns right operand if left is `null` or `undefined` | `null ?? "default"` → `"default"` |

### Optional Chaining Operator

| Operator | Description | Example |
|----------|-------------|---------|
| `?.` | Safely accesses nested properties | `obj?.prop?.nested` (returns `undefined` if any part is missing) |

### Spread and Rest Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `...` | Spread (expand iterable) / Rest (collect arguments) | `[...arr]`, `function(...args) {}` |

---

## Statements Reference

### Declaration Statements

| Statement | Description | Example |
|-----------|-------------|---------|
| `let` | Declares block‑scoped variable | `let x = 5;` |
| `const` | Declares block‑scoped constant | `const PI = 3.14;` |
| `var` | Declares function‑scoped variable | `var y = 10;` (avoid in modern code) |
| `function` | Declares a function | `function add(a, b) { return a + b; }` |
| `class` | Declares a class | `class Person { constructor(name) { this.name = name; } }` |
| `import` | Imports from a module | `import { add } from './math.js';` |
| `export` | Exports from a module | `export const PI = 3.14;` |

### Conditional Statements

| Statement | Description | Example |
|-----------|-------------|---------|
| `if` | Executes block if condition true | `if (x > 0) { console.log("positive"); }` |
| `else` | Executes block if condition false | `if (x > 0) { ... } else { ... }` |
| `else if` | Chains multiple conditions | `if (x > 0) { ... } else if (x < 0) { ... } else { ... }` |
| `switch` | Evaluates expression, matches cases | `switch (day) { case 1: ...; break; default: ...; }` |
| `ternary` | (Operator) Conditional expression | `let result = x > 0 ? "positive" : "non-positive";` |

### Loop Statements

| Statement | Description | Example |
|-----------|-------------|---------|
| `for` | Loops with initialization, condition, increment | `for (let i = 0; i < 5; i++) { ... }` |
| `for...in` | Iterates over enumerable property names | `for (let key in obj) { ... }` |
| `for...of` | Iterates over iterable values | `for (let value of arr) { ... }` |
| `while` | Loops while condition true | `while (i < 5) { i++; }` |
| `do...while` | Executes at least once, then while condition | `do { ... } while (condition);` |
| `for await...of` | Iterates over async iterables | `for await (let item of asyncIterable) { ... }` |

### Control Flow Statements

| Statement | Description | Example |
|-----------|-------------|---------|
| `break` | Exits the current loop or switch | `if (x === 5) break;` |
| `continue` | Skips to next iteration of loop | `if (x % 2 === 0) continue;` |
| `return` | Returns from a function | `return x + y;` |
| `throw` | Throws an exception | `throw new Error("Something went wrong");` |
| `try` / `catch` / `finally` | Handles exceptions | `try { ... } catch (e) { ... } finally { ... }` |
| `debugger` | Invokes debugger | `debugger;` |

### Other Statements

| Statement | Description | Example |
|-----------|-------------|---------|
| `with` | Extends scope chain (deprecated, avoid) | `with (obj) { ... }` |
| `label` | Provides a label for break/continue | `outer: for (...) { ... }` |
| `export` | (See declaration) | – |
| `import` | (See declaration) | – |
| `empty` | (;) Does nothing | `;` |

---

## Built‑in Objects

JavaScript provides several built‑in objects that are available globally. This section lists them with brief descriptions.

| Object | Description |
|--------|-------------|
| `Object` | The base object; all objects inherit from it. |
| `Function` | Base for all functions. |
| `Boolean` | Wrapper for boolean values. |
| `Number` | Wrapper for numbers; provides numeric constants and methods. |
| `BigInt` | For integers larger than 2^53‑1. |
| `String` | Wrapper for strings; provides string manipulation methods. |
| `Symbol` | Creates unique identifiers. |
| `Array` | Used for arrays; provides array methods. |
| `ArrayBuffer` | Represents raw binary data buffer. |
| `SharedArrayBuffer` | Shared raw binary data buffer. |
| `DataView` | Reads/writes multiple number types in an `ArrayBuffer`. |
| `TypedArray` | Views for array‑like buffers (e.g., `Uint8Array`, `Int32Array`). |
| `Map` | Key‑value pairs where keys can be any value. |
| `Set` | Collection of unique values. |
| `WeakMap` | Map with weak references (keys must be objects). |
| `WeakSet` | Set with weak references (values must be objects). |
| `Date` | Represents dates and times. |
| `RegExp` | Regular expressions. |
| `Error` | Base for error objects; also `TypeError`, `RangeError`, etc. |
| `Promise` | Represents eventual completion of an async operation. |
| `Proxy` | Allows custom behavior for fundamental operations. |
| `Reflect` | Provides methods for interceptable operations. |
| `Intl` | Internationalization and localization. |
| `JSON` | JSON parsing and serialization. |
| `Math` | Mathematical constants and functions. |
| `Atomics` | Atomic operations for shared memory. |
| `WebAssembly` | WebAssembly interface. |
| `console` | Provides debugging console (browser/Node). |
| `globalThis` | Global object across environments. |

---

## Array Methods

Arrays inherit from `Array.prototype`. The following are the most commonly used methods.

### Mutator Methods (Change the original array)

| Method | Description | Example |
|--------|-------------|---------|
| `push(...items)` | Adds items to end, returns new length. | `arr.push(4, 5);` |
| `pop()` | Removes last item, returns it. | `let last = arr.pop();` |
| `unshift(...items)` | Adds items to beginning, returns new length. | `arr.unshift(0, 1);` |
| `shift()` | Removes first item, returns it. | `let first = arr.shift();` |
| `splice(start, deleteCount, ...items)` | Removes/replaces items. | `arr.splice(2, 1, 'a', 'b');` |
| `sort(compareFn)` | Sorts array (default as strings). | `arr.sort((a,b) => a - b);` |
| `reverse()` | Reverses array. | `arr.reverse();` |
| `fill(value, start, end)` | Fills with static value. | `arr.fill(0, 2, 4);` |
| `copyWithin(target, start, end)` | Copies part of array to another location. | `arr.copyWithin(0, 3, 5);` |

### Accessor Methods (Do not change original, return new array or value)

| Method | Description | Example |
|--------|-------------|---------|
| `concat(...arrays)` | Returns new concatenated array. | `let newArr = arr.concat([4,5]);` |
| `slice(start, end)` | Returns shallow copy of portion. | `let sub = arr.slice(1, 3);` |
| `join(separator)` | Joins elements into string. | `let str = arr.join(', ');` |
| `indexOf(item, fromIndex)` | First index of item, or -1. | `let idx = arr.indexOf(3);` |
| `lastIndexOf(item, fromIndex)` | Last index of item. | `let idx = arr.lastIndexOf(3);` |
| `includes(item, fromIndex)` | Checks if item exists. | `if (arr.includes(5)) { ... }` |
| `toString()` | Returns comma‑separated string. | `arr.toString()` |
| `toLocaleString()` | Locale‑specific string. | `arr.toLocaleString()` |

### Iteration Methods (Often return new array or value)

| Method | Description | Example |
|--------|-------------|---------|
| `forEach(callback)` | Executes callback on each element. | `arr.forEach(x => console.log(x));` |
| `map(callback)` | Returns new array of callback results. | `let squares = arr.map(x => x * x);` |
| `filter(callback)` | Returns new array of elements passing test. | `let evens = arr.filter(x => x % 2 === 0);` |
| `reduce(callback, initialValue)` | Reduces to single value (left‑to‑right). | `let sum = arr.reduce((acc, x) => acc + x, 0);` |
| `reduceRight(callback, initialValue)` | Right‑to‑left. | – |
| `some(callback)` | True if any element passes test. | `if (arr.some(x => x > 10)) { ... }` |
| `every(callback)` | True if all elements pass test. | `if (arr.every(x => x > 0)) { ... }` |
| `find(callback)` | Returns first element passing test. | `let found = arr.find(x => x > 5);` |
| `findIndex(callback)` | Returns index of first element passing test. | `let idx = arr.findIndex(x => x > 5);` |
| `findLast(callback)` | Returns last element passing test. | – |
| `findLastIndex(callback)` | Returns index of last element passing test. | – |
| `flat(depth)` | Flattens nested arrays. | `let flat = [1,[2,3]].flat(1);` → `[1,2,3]` |
| `flatMap(callback)` | Maps then flattens one level. | `let pairs = arr.flatMap(x => [x, x*2]);` |
| `keys()` | Returns iterator of indices. | `for (let key of arr.keys()) { ... }` |
| `values()` | Returns iterator of values. | `for (let val of arr.values()) { ... }` |
| `entries()` | Returns iterator of [index, value] pairs. | `for (let [i, v] of arr.entries()) { ... }` |
| `groupBy(callback)` | Groups elements by key (proposal). | – |
| `groupByToMap(callback)` | Groups into Map. | – |

### Static Methods

| Method | Description | Example |
|--------|-------------|---------|
| `Array.from(arrayLike, mapFn)` | Creates array from array‑like or iterable. | `Array.from('hello')` → `['h','e','l','l','o']` |
| `Array.of(...elements)` | Creates array from arguments. | `Array.of(1,2,3)` → `[1,2,3]` |
| `Array.isArray(obj)` | Checks if object is array. | `Array.isArray([])` → `true` |

---

## String Methods

Strings are immutable; all methods return a new string.

| Method | Description | Example |
|--------|-------------|---------|
| `charAt(index)` | Returns character at index. | `"hello".charAt(1)` → `"e"` |
| `charCodeAt(index)` | Returns UTF‑16 code unit. | `"A".charCodeAt(0)` → `65` |
| `codePointAt(index)` | Returns Unicode code point. | `"𠮷".codePointAt(0)` → `134071` |
| `concat(...strings)` | Concatenates strings. | `"Hello".concat(" ", "World")` |
| `endsWith(searchString, length)` | Checks if string ends with substring. | `"hello".endsWith("lo")` → `true` |
| `includes(searchString, position)` | Checks if substring exists. | `"hello".includes("ell")` → `true` |
| `indexOf(searchString, position)` | Returns first index of substring. | `"hello".indexOf("l")` → `2` |
| `lastIndexOf(searchString, position)` | Returns last index. | `"hello".lastIndexOf("l")` → `3` |
| `localeCompare(compareString)` | Compares strings according to locale. | `"a".localeCompare("b")` → `-1` |
| `match(regexp)` | Matches string against regexp. | `"hello".match(/l/g)` → `["l","l"]` |
| `matchAll(regexp)` | Returns iterator of all matches. | `for (let m of "hello".matchAll(/l/g)) { ... }` |
| `normalize(form)` | Returns Unicode normalization form. | `"é".normalize("NFD")` |
| `padEnd(targetLength, padString)` | Pads end to target length. | `"5".padEnd(3, "0")` → `"500"` |
| `padStart(targetLength, padString)` | Pads start. | `"5".padStart(3, "0")` → `"005"` |
| `repeat(count)` | Repeats string count times. | `"ha".repeat(3)` → `"hahaha"` |
| `replace(search, replaceValue)` | Replaces first match. | `"hello".replace("l", "x")` → `"hexlo"` |
| `replaceAll(search, replaceValue)` | Replaces all matches. | `"hello".replaceAll("l", "x")` → `"hexxo"` |
| `search(regexp)` | Searches for match, returns index. | `"hello".search(/e/)` → `1` |
| `slice(start, end)` | Extracts substring. | `"hello".slice(1, 4)` → `"ell"` |
| `split(separator, limit)` | Splits into array. | `"a,b,c".split(",")` → `["a","b","c"]` |
| `startsWith(searchString, position)` | Checks if string starts with substring. | `"hello".startsWith("he")` → `true` |
| `substring(start, end)` | Returns substring (like slice, but swaps if start > end). | `"hello".substring(1, 4)` → `"ell"` |
| `toLocaleLowerCase()` | Lowercase according to locale. | – |
| `toLocaleUpperCase()` | Uppercase according to locale. | – |
| `toLowerCase()` | Converts to lowercase. | `"HELLO".toLowerCase()` → `"hello"` |
| `toUpperCase()` | Converts to uppercase. | `"hello".toUpperCase()` → `"HELLO"` |
| `trim()` | Removes whitespace from both ends. | `"  hello  ".trim()` → `"hello"` |
| `trimStart()` / `trimLeft()` | Removes whitespace from start. | `"  hello".trimStart()` → `"hello"` |
| `trimEnd()` / `trimRight()` | Removes whitespace from end. | `"hello  ".trimEnd()` → `"hello"` |
| `valueOf()` | Returns primitive value. | `new String("hi").valueOf()` → `"hi"` |

### Static Methods

| Method | Description | Example |
|--------|-------------|---------|
| `String.fromCharCode(...nums)` | Creates string from UTF‑16 codes. | `String.fromCharCode(65,66)` → `"AB"` |
| `String.fromCodePoint(...nums)` | Creates string from Unicode code points. | `String.fromCodePoint(134071)` → `"𠮷"` |
| `String.raw()` | Template tag for raw strings. | `String.raw` `C:\path` → `"C:\\path"` |

---

## Number Methods

### Properties

| Property | Description | Value |
|----------|-------------|-------|
| `Number.EPSILON` | Smallest difference between two representable numbers. | ≈ `2.22e-16` |
| `Number.MAX_SAFE_INTEGER` | Maximum safe integer. | `2^53 - 1` (≈ 9 quadrillion) |
| `Number.MIN_SAFE_INTEGER` | Minimum safe integer. | `-(2^53 - 1)` |
| `Number.MAX_VALUE` | Largest positive finite number. | ≈ `1.8e308` |
| `Number.MIN_VALUE` | Smallest positive finite number. | ≈ `5e-324` |
| `Number.NaN` | Not‑a‑Number. | – |
| `Number.NEGATIVE_INFINITY` | Negative infinity. | – |
| `Number.POSITIVE_INFINITY` | Positive infinity. | – |

### Methods

| Method | Description | Example |
|--------|-------------|---------|
| `Number.isNaN(value)` | Checks if value is `NaN` (strict). | `Number.isNaN(NaN)` → `true` |
| `Number.isFinite(value)` | Checks if value is finite. | `Number.isFinite(Infinity)` → `false` |
| `Number.isInteger(value)` | Checks if value is integer. | `Number.isInteger(5.0)` → `true` |
| `Number.isSafeInteger(value)` | Checks if value is safe integer. | `Number.isSafeInteger(2**53)` → `false` |
| `Number.parseFloat(string)` | Parses string to float. | `Number.parseFloat("3.14")` → `3.14` |
| `Number.parseInt(string, radix)` | Parses string to integer. | `Number.parseInt("101", 2)` → `5` |
| `Number.prototype.toExponential(fractionDigits)` | Returns exponential notation. | `(12345).toExponential(2)` → `"1.23e+4"` |
| `Number.prototype.toFixed(digits)` | Returns fixed‑point notation. | `(3.14159).toFixed(2)` → `"3.14"` |
| `Number.prototype.toPrecision(precision)` | Returns string with specified precision. | `(123.456).toPrecision(4)` → `"123.5"` |
| `Number.prototype.toString(radix)` | Returns string in specified base. | `(255).toString(16)` → `"ff"` |
| `Number.prototype.valueOf()` | Returns primitive value. | `new Number(5).valueOf()` → `5` |

---

## Math Methods

The `Math` object provides mathematical constants and functions. All are static.

### Constants

| Constant | Description | Value |
|----------|-------------|-------|
| `Math.E` | Euler's number. | ≈ `2.718` |
| `Math.LN2` | Natural logarithm of 2. | ≈ `0.693` |
| `Math.LN10` | Natural logarithm of 10. | ≈ `2.302` |
| `Math.LOG2E` | Base‑2 logarithm of e. | ≈ `1.442` |
| `Math.LOG10E` | Base‑10 logarithm of e. | ≈ `0.434` |
| `Math.PI` | Pi. | ≈ `3.14159` |
| `Math.SQRT1_2` | Square root of 1/2. | ≈ `0.707` |
| `Math.SQRT2` | Square root of 2. | ≈ `1.414` |

### Methods

| Method | Description | Example |
|--------|-------------|---------|
| `Math.abs(x)` | Absolute value. | `Math.abs(-5)` → `5` |
| `Math.acos(x)` | Arccosine (in radians). | `Math.acos(1)` → `0` |
| `Math.acosh(x)` | Hyperbolic arccosine. | – |
| `Math.asin(x)` | Arcsine. | – |
| `Math.asinh(x)` | Hyperbolic arcsine. | – |
| `Math.atan(x)` | Arctangent. | – |
| `Math.atan2(y, x)` | Arctangent of quotient. | – |
| `Math.atanh(x)` | Hyperbolic arctangent. | – |
| `Math.cbrt(x)` | Cube root. | `Math.cbrt(27)` → `3` |
| `Math.ceil(x)` | Rounds up to nearest integer. | `Math.ceil(4.2)` → `5` |
| `Math.clz32(x)` | Count leading zeroes in 32‑bit representation. | – |
| `Math.cos(x)` | Cosine. | – |
| `Math.cosh(x)` | Hyperbolic cosine. | – |
| `Math.exp(x)` | e^x. | – |
| `Math.expm1(x)` | e^x - 1. | – |
| `Math.floor(x)` | Rounds down. | `Math.floor(4.9)` → `4` |
| `Math.fround(x)` | Rounds to 32‑bit float. | – |
| `Math.hypot(...values)` | Square root of sum of squares. | `Math.hypot(3,4)` → `5` |
| `Math.imul(a, b)` | 32‑bit integer multiplication. | – |
| `Math.log(x)` | Natural logarithm (base e). | – |
| `Math.log1p(x)` | Natural logarithm of 1 + x. | – |
| `Math.log10(x)` | Base‑10 logarithm. | – |
| `Math.log2(x)` | Base‑2 logarithm. | – |
| `Math.max(...values)` | Returns largest value. | `Math.max(1,5,2)` → `5` |
| `Math.min(...values)` | Returns smallest value. | `Math.min(1,5,2)` → `1` |
| `Math.pow(base, exponent)` | Base raised to exponent. | `Math.pow(2,3)` → `8` |
| `Math.random()` | Returns random number in [0,1). | `Math.random()` → `0.234...` |
| `Math.round(x)` | Rounds to nearest integer. | `Math.round(4.5)` → `5` (bankers rounding? Actually standard rounding) |
| `Math.sign(x)` | Returns sign of x (-1, 0, 1). | `Math.sign(-5)` → `-1` |
| `Math.sin(x)` | Sine. | – |
| `Math.sinh(x)` | Hyperbolic sine. | – |
| `Math.sqrt(x)` | Square root. | `Math.sqrt(9)` → `3` |
| `Math.tan(x)` | Tangent. | – |
| `Math.tanh(x)` | Hyperbolic tangent. | – |
| `Math.trunc(x)` | Removes fractional part. | `Math.trunc(4.9)` → `4` |

---

## Date Methods

The `Date` object handles dates and times. Dates are stored as milliseconds since January 1, 1970, UTC.

### Constructors

| Constructor | Description | Example |
|-------------|-------------|---------|
| `new Date()` | Current date/time. | `let now = new Date();` |
| `new Date(milliseconds)` | From timestamp. | `new Date(1672531200000)` |
| `new Date(dateString)` | From string (parsed). | `new Date("2024-01-15")` |
| `new Date(year, month, day, hour, minute, second, millisecond)` | From components (month is 0‑based). | `new Date(2024, 0, 15, 12, 0, 0)` |

### Static Methods

| Method | Description | Example |
|--------|-------------|---------|
| `Date.now()` | Returns current timestamp. | `Date.now()` |
| `Date.parse(dateString)` | Parses string, returns timestamp. | `Date.parse("2024-01-15")` |
| `Date.UTC(year, month, ...)` | Returns UTC timestamp. | `Date.UTC(2024, 0, 15)` |

### Instance Methods (Getters)

| Method | Description | Example |
|--------|-------------|---------|
| `getDate()` | Day of month (1‑31). | `date.getDate()` |
| `getDay()` | Day of week (0‑6, Sunday = 0). | `date.getDay()` |
| `getFullYear()` | Year (4 digits). | `date.getFullYear()` |
| `getHours()` | Hours (0‑23). | `date.getHours()` |
| `getMilliseconds()` | Milliseconds (0‑999). | – |
| `getMinutes()` | Minutes (0‑59). | – |
| `getMonth()` | Month (0‑11). | – |
| `getSeconds()` | Seconds (0‑59). | – |
| `getTime()` | Milliseconds since epoch. | `date.getTime()` |
| `getTimezoneOffset()` | Timezone offset in minutes from UTC. | – |
| `getUTCDate()`, `getUTCDay()`, ... | UTC versions of above. | – |

### Instance Methods (Setters)

| Method | Description |
|--------|-------------|
| `setDate(day)` | Sets day of month. |
| `setFullYear(year, month, day)` | Sets year. |
| `setHours(hour, min, sec, ms)` | Sets hour. |
| `setMilliseconds(ms)` | Sets milliseconds. |
| `setMinutes(min, sec, ms)` | Sets minutes. |
| `setMonth(month, day)` | Sets month. |
| `setSeconds(sec, ms)` | Sets seconds. |
| `setTime(milliseconds)` | Sets timestamp. |
| `setUTCDate()`, `setUTCFullYear()`, ... | UTC setters. |

### Conversion Methods

| Method | Description | Example |
|--------|-------------|---------|
| `toDateString()` | Returns date portion as string. | `date.toDateString()` → `"Mon Jan 15 2024"` |
| `toISOString()` | Returns ISO 8601 string. | `date.toISOString()` → `"2024-01-15T12:00:00.000Z"` |
| `toJSON()` | Same as `toISOString()`. | – |
| `toLocaleDateString(locales, options)` | Locale‑specific date. | – |
| `toLocaleString(locales, options)` | Locale‑specific date and time. | – |
| `toLocaleTimeString(locales, options)` | Locale‑specific time. | – |
| `toString()` | Full string representation. | – |
| `toTimeString()` | Time portion as string. | – |
| `toUTCString()` | UTC string (RFC 7231). | – |
| `valueOf()` | Primitive value (timestamp). | – |

---

## Object Methods

The `Object` constructor provides methods for working with objects.

### Static Methods

| Method | Description | Example |
|--------|-------------|---------|
| `Object.assign(target, ...sources)` | Copies properties from sources to target. | `Object.assign(obj, {a:1}, {b:2})` |
| `Object.create(proto, propertiesObject)` | Creates new object with given prototype. | `let child = Object.create(parent);` |
| `Object.defineProperty(obj, prop, descriptor)` | Defines a single property. | – |
| `Object.defineProperties(obj, props)` | Defines multiple properties. | – |
| `Object.entries(obj)` | Returns array of [key, value] pairs. | `Object.entries({a:1,b:2})` → `[['a',1],['b',2]]` |
| `Object.freeze(obj)` | Freezes object (cannot add/delete/change). | – |
| `Object.fromEntries(iterable)` | Creates object from key‑value pairs. | `Object.fromEntries([['a',1],['b',2]])` → `{a:1,b:2}` |
| `Object.getOwnPropertyDescriptor(obj, prop)` | Returns descriptor for property. | – |
| `Object.getOwnPropertyDescriptors(obj)` | Returns all descriptors. | – |
| `Object.getOwnPropertyNames(obj)` | Returns array of own property names. | – |
| `Object.getOwnPropertySymbols(obj)` | Returns array of own symbol properties. | – |
| `Object.getPrototypeOf(obj)` | Returns prototype of object. | – |
| `Object.groupBy(items, callback)` | Groups items (similar to array method). | – |
| `Object.hasOwn(obj, prop)` | Checks if object has own property. | `Object.hasOwn(obj, 'name')` |
| `Object.is(value1, value2)` | Compares values (like === but handles NaN). | `Object.is(NaN, NaN)` → `true` |
| `Object.isExtensible(obj)` | Checks if object is extensible. | – |
| `Object.isFrozen(obj)` | Checks if object is frozen. | – |
| `Object.isSealed(obj)` | Checks if object is sealed. | – |
| `Object.keys(obj)` | Returns array of own enumerable property names. | `Object.keys({a:1,b:2})` → `['a','b']` |
| `Object.preventExtensions(obj)` | Prevents adding new properties. | – |
| `Object.seal(obj)` | Prevents adding/deleting, but allows modifying existing. | – |
| `Object.setPrototypeOf(obj, prototype)` | Sets prototype. | – |
| `Object.values(obj)` | Returns array of own enumerable property values. | `Object.values({a:1,b:2})` → `[1,2]` |

### Instance Methods (on Object.prototype)

| Method | Description | Example |
|--------|-------------|---------|
| `obj.hasOwnProperty(prop)` | Checks if object has own property. | `obj.hasOwnProperty('name')` |
| `obj.isPrototypeOf(otherObj)` | Checks if object is in prototype chain of otherObj. | – |
| `obj.propertyIsEnumerable(prop)` | Checks if property is enumerable. | – |
| `obj.toLocaleString()` | Locale‑specific string. | – |
| `obj.toString()` | Returns string representation. | – |
| `obj.valueOf()` | Returns primitive value. | – |

---

This appendix provides a comprehensive reference to JavaScript's core features. For the most current and detailed information, consult the [MDN Web Docs JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference).