# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: Python Cheat Sheet

A quick reference for the most frequently used Python syntax. Use this alongside the chapters, not as a replacement.

### Variables and Types

```python
# Basic assignment
name = "Alice"          # str
age = 30                # int
height = 1.75           # float
is_admin = True         # bool
nothing = None          # NoneType

# Type hints (Python 3.5+)
def greet(name: str) -> str:
    return f"Hello, {name}"

# Type conversion
num_str = "42"
num = int(num_str)       # "42" → 42
text = str(42)           # 42 → "42"
pi = float("3.14")       # "3.14" → 3.14
```

### String Operations

```python
s = "Hello, World!"

s.upper()                   # "HELLO, WORLD!"
s.lower()                   # "hello, world!"
s.strip()                   # removes whitespace from both ends
s.split(", ")               # ["Hello", "World!"]
", ".join(["a", "b", "c"])  # "a, b, c"
s.replace("World", "Python") # "Hello, Python!"
s.startswith("Hello")       # True
s.endswith("!")             # True
len(s)                      # 13
s[0:5]                      # "Hello"   (slicing)

# f-strings (recommended formatting)
name = "Alice"
age = 30
print(f"{name} is {age} years old")           # Alice is 30 years old
print(f"Pi is approximately {3.14159:.2f}")   # Pi is approximately 3.14
```

### Data Structures

```python
# List — ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("date")           # add to end
fruits.insert(1, "avocado")     # insert at index 1
fruits.remove("banana")         # remove by value
fruits.pop()                    # remove and return last item
fruits[0]                       # "apple" (index access)
fruits[-1]                      # last item
fruits[1:3]                     # slice [index 1 to 2]
len(fruits)                     # number of items

# Tuple — ordered, IMMUTABLE
point = (3, 4)
x, y = point                    # unpacking

# Dictionary — key-value pairs, ordered (Python 3.7+)
person = {"name": "Alice", "age": 30}
person["name"]                  # "Alice"
person.get("email", "N/A")      # "N/A" (safe access with default)
person["city"] = "London"       # add new key
del person["age"]               # delete key
person.keys()                   # dict_keys(["name", "city"])
person.values()                 # dict_values(["Alice", "London"])
person.items()                  # dict_items([("name", "Alice"), ...])

# Set — unordered, unique values
unique = {1, 2, 3, 2, 1}        # {1, 2, 3}
unique.add(4)
unique.discard(1)
{1, 2} & {2, 3}                 # intersection: {2}
{1, 2} | {2, 3}                 # union: {1, 2, 3}
{1, 2} - {2, 3}                 # difference: {1}
```

### Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Dict comprehension
square_map = {x: x**2 for x in range(5)}

# Set comprehension
unique_lengths = {len(word) for word in ["cat", "dog", "elephant"]}

# Generator expression (lazy evaluation — use for large data)
total = sum(x**2 for x in range(1000000))
```

### Control Flow

```python
# if / elif / else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"

# for loop
for item in ["a", "b", "c"]:
    print(item)

for i, item in enumerate(["a", "b", "c"]):
    print(i, item)           # 0 a, 1 b, 2 c

for key, value in person.items():
    print(f"{key}: {value}")

# while loop
count = 0
while count < 5:
    count += 1

# break, continue
for x in range(10):
    if x == 3:
        continue             # skip 3
    if x == 7:
        break                # stop at 7
```

### Functions

```python
# Basic function
def add(a: int, b: int) -> int:
    return a + b

# Default arguments
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# *args — variable positional arguments
def total(*numbers):
    return sum(numbers)
total(1, 2, 3)               # 6

# **kwargs — variable keyword arguments
def display(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
display(name="Alice", age=30)

# Lambda (anonymous function)
square = lambda x: x ** 2
sorted_list = sorted(items, key=lambda x: x["age"])
```

### Classes (OOP)

```python
class Animal:
    species = "Unknown"          # class attribute

    def __init__(self, name: str, sound: str):
        self.name = name         # instance attribute
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r})"

class Dog(Animal):              # inheritance
    def __init__(self, name: str):
        super().__init__(name, "Woof")

    def fetch(self):
        return f"{self.name} fetches the ball!"

dog = Dog("Rex")
print(dog.speak())              # Rex says Woof
print(dog.fetch())              # Rex fetches the ball!
```

### Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or value error: {e}")
else:
    print("No error occurred")   # runs if no exception
finally:
    print("Always runs")         # cleanup code

# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Custom exception
class AppError(Exception):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code
```

### Context Managers

```python
# File I/O with automatic close
with open("file.txt", "r") as f:
    content = f.read()

with open("output.txt", "w") as f:
    f.write("Hello, World!\n")

# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.3f}s")

with timer():
    do_something_slow()
```

### Decorators

```python
import functools

def log_call(func):
    @functools.wraps(func)        # preserves function metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

add(2, 3)
# Calling add
# add returned 5
```

### Async / Await

```python
import asyncio

async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)       # simulates I/O wait
    return f"data from {url}"

async def main():
    # Run two tasks concurrently
    result1, result2 = await asyncio.gather(
        fetch_data("https://api.example.com/users"),
        fetch_data("https://api.example.com/posts"),
    )
    print(result1, result2)

asyncio.run(main())
```

### Common Standard Library Modules

```python
import os                        # OS interaction
import sys                       # Python interpreter
import json                      # JSON serialization
import re                        # Regular expressions
import datetime                  # Date and time
import pathlib                   # File paths (modern)
import collections                # defaultdict, Counter, deque
import itertools                  # chain, groupby, combinations
import functools                  # reduce, lru_cache, partial
import typing                    # type hints
import dataclasses               # @dataclass
import abc                       # Abstract base classes
import logging                   # Application logging
import unittest / pytest         # Testing
```

---

## Appendix B: Glossary of Technical Terms

### Python Runtime

**Interpreter**
The program that reads and executes Python code line by line. CPython (the reference implementation) compiles Python source to bytecode, then executes that bytecode in the Python Virtual Machine. When you run `python3 script.py`, you're invoking the interpreter.

**Bytecode**
An intermediate, lower-level representation of your Python code. When you run a `.py` file, Python first compiles it to `.pyc` bytecode (cached in `__pycache__/`). This is faster to execute than reading raw source but is still interpreted, not native machine code.

**Virtual Environment (venv)**
An isolated Python environment with its own copy of pip and installed packages. This prevents conflicts between projects that require different versions of the same library. Always create a new venv for each project.

**GIL (Global Interpreter Lock)**
A mutex in CPython that allows only one thread to execute Python bytecode at a time. This means CPU-bound multi-threaded Python code doesn't run truly in parallel. The workaround: use `multiprocessing` for CPU-bound tasks, or `asyncio` / threads for I/O-bound tasks. (Note: Python 3.13+ introduces a no-GIL build option.)

**REPL (Read-Eval-Print Loop)**
An interactive Python shell where you type one expression at a time and see the result immediately. Run with `python3` or use Jupyter notebooks (which are a more powerful REPL).

**Package vs Module**
A **module** is a single `.py` file containing Python code (functions, classes, etc.). A **package** is a directory of modules with an `__init__.py` file. A **distribution package** (what you install with `pip`) may contain many packages.

**pip**
Python's standard package installer. Installs packages from PyPI (Python Package Index). `pip install requests` downloads and installs the `requests` library and its dependencies.

**PEP (Python Enhancement Proposal)**
The official process for proposing changes to Python. Important PEPs:
- PEP 8: Style guide for Python code
- PEP 20: The Zen of Python (`import this`)
- PEP 484: Type hints
- PEP 572: Walrus operator (`:=`)

### Architecture Terms

**Dependency Injection (DI)**
A design pattern where a function or class receives its dependencies as parameters instead of creating them internally. Makes code more testable and loosely coupled.

**Idempotency**
An operation is idempotent if calling it multiple times produces the same result as calling it once. `PUT /users/1` (replace user) is idempotent; `POST /users` (create user) is not.

**Observability**
The ability to understand what is happening inside a system by looking at its outputs (logs, metrics, traces). The three pillars of observability are: **Logging** (events), **Metrics** (measurements over time), and **Tracing** (request flow through a distributed system).

### Web Terms

**HTTP (HyperText Transfer Protocol)**
The protocol that web browsers and servers use to communicate. Requests have a **method** (GET, POST, PUT, DELETE), a **URL**, **headers**, and optionally a **body**. Responses have a **status code** (200, 404, 500), **headers**, and a **body**.

**REST (Representational State Transfer)**
An architectural style for web APIs. RESTful APIs use HTTP methods semantically: GET to read, POST to create, PUT/PATCH to update, DELETE to remove. Resources are identified by URLs.

**JSON (JavaScript Object Notation)**
A lightweight data format for sending structured data over HTTP. Python's `json` module converts between JSON text and Python dicts/lists.

**ORM (Object Relational Mapper)**
A library that lets you interact with a relational database using Python objects instead of raw SQL. You define models as Python classes; the ORM generates the SQL automatically.

---

## Appendix C: Recommended Resources

### Official Documentation
- [Python docs](https://docs.python.org/3/) — authoritative reference
- [Python Tutorial](https://docs.python.org/3/tutorial/) — official beginner intro
- [What's New in Python](https://docs.python.org/3/whatsnew/) — version changelogs

### Books (by experience level)
- **Beginner**: *Automate the Boring Stuff with Python* (free online) — Al Sweigart
- **Intermediate**: *Fluent Python* (2nd ed.) — Luciano Ramalho
- **Advanced**: *Python Cookbook* (3rd ed.) — David Beazley & Brian K. Jones

### Practice
- [exercism.org/tracks/python](https://exercism.org/tracks/python) — structured exercises with mentoring
- [leetcode.com](https://leetcode.com) — algorithm challenges (use Python)
- [realpython.com](https://realpython.com) — tutorials and articles

### Community
- [r/learnpython](https://reddit.com/r/learnpython) — friendly beginner community
- [Python Discord](https://pythondiscord.com) — active chat community
- [PyPI](https://pypi.org) — browse all Python packages
