# Appendix A: C# Keywords Quick Reference

C# keywords are reserved words that have special meaning to the compiler. They cannot be used as identifiers (variable names, class names, etc.) unless prefixed with `@`. This appendix provides a quick reference to all C# keywords, organized by category, with brief explanations and usage examples.

---

## A.1 Access Modifiers

| Keyword | Description |
|---------|-------------|
| `public` | Access is not restricted. |
| `private` | Access is limited to the containing type. |
| `protected` | Access is limited to the containing type or types derived from it. |
| `internal` | Access is limited to the current assembly. |
| `protected internal` | Access is limited to the current assembly or types derived from the containing class. |
| `private protected` | Access is limited to the containing type or types derived from it **within the current assembly**. |

**Example:**
```csharp
public class MyClass
{
    private int _field;
    protected void Method() { }
}
```

---

## A.2 Type Keywords

| Keyword | Description |
|---------|-------------|
| `bool` | Boolean value (true/false). |
| `byte` | 8‑bit unsigned integer. |
| `sbyte` | 8‑bit signed integer. |
| `char` | 16‑bit Unicode character. |
| `decimal` | 128‑bit precise decimal (28‑29 significant digits). |
| `double` | 64‑bit double‑precision floating point. |
| `float` | 32‑bit single‑precision floating point. |
| `int` | 32‑bit signed integer. |
| `uint` | 32‑bit unsigned integer. |
| `long` | 64‑bit signed integer. |
| `ulong` | 64‑bit unsigned integer. |
| `short` | 16‑bit signed integer. |
| `ushort` | 16‑bit unsigned integer. |
| `object` | Base type of all types. |
| `string` | Sequence of characters (reference type). |
| `dynamic` | Bypasses compile‑time type checking. |

**Example:**
```csharp
int count = 10;
string name = "Alice";
object obj = count;
dynamic dyn = "hello";
```

---

## A.3 Modifier Keywords

| Keyword | Description |
|---------|-------------|
| `abstract` | Indicates that a class or member is incomplete and must be implemented in a derived class. |
| `async` | Modifies a method, lambda, or anonymous method to be asynchronous. |
| `const` | Declares a constant field or local (value is known at compile time). |
| `event` | Declares an event. |
| `extern` | Indicates that a method is implemented externally. |
| `in` | For generic interface contravariance, or as a parameter modifier (read‑only reference). |
| `out` | For generic interface covariance, or as a parameter modifier (output reference). |
| `override` | Extends or modifies the inherited implementation of a virtual/abstract member. |
| `readonly` | Declares a field that can only be assigned at declaration or in a constructor. Also used in `readonly struct`. |
| `sealed` | Prevents a class from being inherited, or a method/property from being overridden. |
| `static` | Declares a member that belongs to the type itself, not to an instance. |
| `unsafe` | Marks a code block that uses pointers. |
| `virtual` | Declares a method or property that can be overridden in a derived class. |
| `volatile` | Indicates that a field may be modified by multiple threads. |

**Example:**
```csharp
public abstract class Animal
{
    public abstract void MakeSound();
}

public class Dog : Animal
{
    public override void MakeSound() => Console.WriteLine("Woof!");
}
```

---

## A.4 Statement Keywords

| Keyword | Description |
|---------|-------------|
| `if` | Conditional execution. |
| `else` | Alternative branch in an `if` statement. |
| `switch` | Multi‑way branch. |
| `case` | Defines a pattern or constant in a `switch`. |
| `default` | Default case in a `switch`, or default value operator. |
| `while` | Executes a block while a condition is true. |
| `do` | Executes a block at least once, then while a condition is true. |
| `for` | Loop with initialization, condition, and iterator. |
| `foreach` | Iterates over a collection. |
| `in` | Used in `foreach` to specify the collection, also in LINQ queries. |
| `break` | Exits a loop or `switch`. |
| `continue` | Skips the rest of the current loop iteration. |
| `goto` | Jumps to a labeled statement (use sparingly). |
| `return` | Exits a method and optionally returns a value. |
| `yield` | Used in iterators to return elements one at a time. |
| `throw` | Throws an exception. |
| `try` | Begins an exception handling block. |
| `catch` | Catches an exception. |
| `finally` | Block that always executes after `try`/`catch`. |
| `checked` | Enables overflow checking for integer arithmetic. |
| `unchecked` | Disables overflow checking. |
| `lock` | Acquires a mutual‑exclusion lock for a block. |
| `using` | Ensures `Dispose` is called, or imports a namespace. |
| `await` | Awaits a task asynchronously. |

**Example:**
```csharp
foreach (var item in collection)
{
    if (item == null) continue;
    Console.WriteLine(item);
}
```

---

## A.5 Method Parameter Keywords

| Keyword | Description |
|---------|-------------|
| `params` | Allows a variable number of arguments. |
| `ref` | Passes an argument by reference (must be initialized). |
| `out` | Passes an argument by reference (need not be initialized before call). |
| `in` | Passes an argument by reference but guarantees it won't be modified. |

**Example:**
```csharp
void Swap(ref int a, ref int b) { int t = a; a = b; b = t; }
bool TryParse(string s, out int result) => int.TryParse(s, out result);
```

---

## A.6 Namespace Keywords

| Keyword | Description |
|---------|-------------|
| `namespace` | Declares a namespace. |
| `using` | Imports a namespace, creates an alias, or ensures disposal. |
| `extern alias` | References an external assembly alias. |

**Example:**
```csharp
using System;
using Project = MyApp.Core.Project;
```

---

## A.7 Operator Keywords

| Keyword | Description |
|---------|-------------|
| `as` | Safely casts an object to a type (returns null if conversion fails). |
| `is` | Checks if an object is compatible with a type. |
| `new` | Creates an object, hides an inherited member, or constrains a generic type. |
| `sizeof` | Gets the size of a value type in bytes (unsafe context). |
| `typeof` | Gets the `Type` object for a type. |
| `stackalloc` | Allocates a block of memory on the stack. |
| `true` / `false` | Boolean literals and operator overloads. |

**Example:**
```csharp
if (obj is string s) Console.WriteLine(s.Length);
Type t = typeof(int);
int* buffer = stackalloc int[10];
```

---

## A.8 Access Keywords

| Keyword | Description |
|---------|-------------|
| `base` | Accesses members of the base class. |
| `this` | Refers to the current instance. |

**Example:**
```csharp
public class Derived : Base
{
    public Derived() : base() { }
    public void Show() => Console.WriteLine(base.Value);
}
```

---

## A.9 Literal Keywords

| Keyword | Description |
|---------|-------------|
| `null` | Null reference. |
| `true` | Boolean true value. |
| `false` | Boolean false value. |
| `default` | Default value of a type. |

**Example:**
```csharp
string s = null;
bool flag = true;
int i = default; // 0
```

---

## A.10 Contextual Keywords

Contextual keywords are not reserved in all contexts; they have special meaning only in certain places. This allows them to be used as identifiers elsewhere.

| Keyword | Context |
|---------|---------|
| `add` | Custom event accessor. |
| `and` | Conjunctive pattern (C# 9). |
| `alias` | Extern alias. |
| `ascending` | Query syntax ordering. |
| `async` | Method modifier. |
| `await` | Await expression. |
| `by` | Query syntax grouping. |
| `descending` | Query syntax ordering. |
| `dynamic` | Type. |
| `equals` | Query syntax join. |
| `from` | Query syntax. |
| `get` | Property accessor. |
| `global` | Global namespace. |
| `group` | Query syntax. |
| `init` | Init‑only property accessor (C# 9). |
| `into` | Query syntax continuation. |
| `join` | Query syntax. |
| `let` | Query syntax. |
| `nameof` | Returns the string name of a symbol. |
| `not` | Negation pattern (C# 9). |
| `on` | Query syntax join condition. |
| `or` | Disjunctive pattern (C# 9). |
| `orderby` | Query syntax. |
| `partial` | Partial type or method. |
| `record` | Reference type with value semantics (C# 9). |
| `remove` | Custom event accessor. |
| `select` | Query syntax. |
| `set` | Property accessor. |
| `unmanaged` | Type constraint for unmanaged types. |
| `value` | Implicit parameter in property/event accessors. |
| `var` | Implicitly typed local variable. |
| `when` | Filter in `catch` or `switch`. |
| `where` | Generic constraint or query filter. |
| `with` | Non‑destructive mutation for records (C# 9). |
| `yield` | Iterator block. |

**Example:**
```csharp
var query = from p in people
            where p.Age > 18
            select p.Name;
```

---

## A.11 Summary

This appendix provides a quick lookup for C# keywords. For detailed information, refer to the [Microsoft C# documentation](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/).

---

**Next:** Appendix B: Common .NET CLI Commands – a collection of frequently used commands for building, testing, and running .NET applications.