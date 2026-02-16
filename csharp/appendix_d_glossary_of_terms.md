# Appendix D: Glossary of Terms

This glossary provides definitions for key terms and concepts used throughout the book. Terms are listed alphabetically for quick reference.

---

### A

**abstract class**  
A class that cannot be instantiated and is intended to be a base for other classes. It may contain abstract methods (without implementation) that derived classes must override. (Chapter 9)

**abstraction**  
The concept of hiding complex implementation details and exposing only the essential features of an object or system. Achieved through abstract classes and interfaces. (Chapter 6)

**access modifier**  
A keyword that specifies the accessibility of a type or member (e.g., `public`, `private`, `protected`, `internal`). Controls encapsulation. (Chapter 6, 11)

**aggregate (DDD)**  
A cluster of domain objects that can be treated as a single unit, with an aggregate root enforcing invariants. (Chapter 27)

**anonymous type**  
A compiler‑generated type that holds a set of read‑only properties. Created using `new { Property = value }` syntax, often in LINQ queries. (Chapter 15)

**API (Application Programming Interface)**  
A set of rules and protocols that allow one software application to interact with another. In web development, often refers to HTTP‑based services (REST APIs). (Chapter 22)

**array**  
A fixed‑size, zero‑based indexed collection of elements of the same type. (Chapter 4)

**ASP.NET Core**  
A cross‑platform, high‑performance framework for building modern web applications and APIs. (Chapter 22)

**assembly**  
A compiled .NET code unit (`.dll` or `.exe`) that contains metadata, IL code, and resources. The fundamental unit of deployment. (Chapter 1)

**async/await**  
Keywords that enable asynchronous programming, allowing methods to run without blocking the calling thread. (Chapter 16)

**attribute**  
A declarative tag used to add metadata to code elements (classes, methods, properties). Can be queried at runtime via reflection. (Chapter 20)

**authentication**  
The process of verifying the identity of a user or system. (Chapter 28)

**authorization**  
The process of determining whether an authenticated user has permission to access a resource. (Chapter 28)

---

### B

**base class**  
A class that is inherited by another class (derived class). Also called a parent class. (Chapter 9)

**benchmark**  
A measurement of performance, often using tools like BenchmarkDotNet to compare different implementations. (Chapter 25)

**binding (model binding)**  
The process in ASP.NET Core that maps HTTP request data (form, query string, route) to action method parameters. (Chapter 22)

**boxing/unboxing**  
Boxing converts a value type to a reference type (e.g., `int` to `object`); unboxing extracts the value type back. Both have performance costs. (Chapter 2)

**built‑in types**  
Primitive types provided by the language, such as `int`, `string`, `bool`, `double`. Aliases for .NET types (`System.Int32`, etc.). (Chapter 2)

---

### C

**cancellation token**  
A mechanism to cooperatively cancel an asynchronous operation. (Chapter 16)

**class**  
A blueprint for creating objects. Defines fields, properties, methods, and events. (Chapter 6)

**client**  
A consumer of a service or API, such as a browser, mobile app, or another server. (Chapter 22)

**CLI (Common Language Infrastructure)**  
An international standard that describes the foundation of the .NET runtime. Often used interchangeably with the .NET runtime. (Chapter 1)

**CLR (Common Language Runtime)**  
The virtual machine component of .NET that manages execution, memory, garbage collection, and security. (Chapter 1)

**closure**  
A lambda expression that captures variables from its surrounding scope, extending their lifetime. (Chapter 12)

**cohesion**  
A measure of how closely related the members of a class are. High cohesion is desirable. (Chapter 11)

**collection**  
A data structure that holds multiple elements, such as `List<T>`, `Dictionary<TKey, TValue>`, or arrays. (Chapter 4)

**command (design pattern)**  
A behavioral pattern that encapsulates a request as an object, allowing parameterization and queuing of operations. (Chapter 26)

**comment**  
Text in code that is ignored by the compiler, used for documentation and explanation. (`//` single‑line, `/* */` multi‑line).

**compiler**  
A program that translates source code into executable code. The C# compiler (Roslyn) converts C# into Intermediate Language (IL). (Chapter 1)

**concurrent collection**  
Thread‑safe collections from `System.Collections.Concurrent`, designed for multi‑threaded scenarios. (Chapter 24)

**const**  
A keyword that declares a compile‑time constant. Must be initialized at declaration and cannot be changed. (Chapter 2, 11)

**constructor**  
A special method called when an object is instantiated. Used to initialize the object's state. (Chapter 8)

**container (DI)**  
A library that automatically constructs object graphs and manages dependencies based on registrations. (Chapter 21)

**controller (MVC)**  
A class that handles HTTP requests in ASP.NET Core MVC, containing action methods. (Chapter 22)

**coupling**  
A measure of dependency between classes. Low coupling (loose coupling) is desirable. (Chapter 11)

**covariance/contravariance**  
Covariance allows using a more derived type than originally specified (`out` keyword). Contravariance allows using a less derived type (`in` keyword). Applies to delegates and interfaces. (Chapter 13)

---

### D

**DDD (Domain‑Driven Design)**  
An approach to software development that focuses on modeling a complex business domain, using patterns like entities, value objects, aggregates, and repositories. (Chapter 27)

**deadlock**  
A situation where two or more threads are blocked forever, each waiting for the other to release a resource. (Chapter 24)

**delegate**  
A type that represents references to methods with a specific signature. Used for callbacks and events. (Chapter 12)

**dependency injection**  
A technique where objects receive their dependencies from an external source rather than creating them internally. Promotes loose coupling and testability. (Chapter 21)

**derived class**  
A class that inherits from a base class. (Chapter 9)

**design pattern**  
A reusable solution to a common problem in software design. (Chapter 26)

**DTO (Data Transfer Object)**  
A simple object that carries data between processes, often used to transfer data between layers or over the network. (Chapter 22)

---

### E

**EF Core (Entity Framework Core)**  
A lightweight, extensible ORM (Object‑Relational Mapper) for .NET. (Chapter 22)

**encapsulation**  
The bundling of data and methods that operate on that data within a class, hiding internal details from outside. (Chapter 11)

**entity**  
An object with a distinct identity that persists over time, central to Domain‑Driven Design. (Chapter 27)

**enum**  
A value type defined by a set of named constants. (Chapter 2)

**event**  
A member that enables an object to notify subscribers when something happens. Built on delegates. (Chapter 12)

**exception**  
An object that represents an error condition. Thrown when an unexpected situation occurs. (Chapter 14)

**expression‑bodied member**  
A concise syntax for defining methods, properties, etc., using `=>` (e.g., `int Add(int a, int b) => a + b;`). (Chapter 5)

---

### F

**factory pattern**  
A creational pattern that provides an interface for creating objects without specifying their concrete classes. (Chapter 26)

**field**  
A variable declared directly in a class or struct, holding data. Usually private. (Chapter 6)

**finalizer**  
A method called by the garbage collector before reclaiming an object's memory. Used to release unmanaged resources. (Chapter 18)

**foreach**  
A loop statement that iterates over a collection, accessing each element. (Chapter 4)

**framework**  
A collection of libraries and tools that provide common functionality for developing applications. .NET is a framework.

---

### G

**garbage collection (GC)**  
Automatic memory management where the runtime reclaims memory occupied by objects no longer in use. (Chapter 18)

**generics**  
A feature that allows classes, methods, and interfaces to work with any data type while preserving type safety. (Chapter 13)

**getter/setter**  
Accessor methods of a property. The `get` accessor returns the property value; the `set` accessor assigns a new value. (Chapter 7)

---

### H

**heap/stack**  
Memory regions in .NET. Value types are typically stored on the stack (or inline in objects), reference types on the heap. (Chapter 2, 18)

**HTTP**  
Hypertext Transfer Protocol, the foundation of data communication on the web.

**HTTPS**  
HTTP over TLS/SSL, providing encrypted communication. (Chapter 28)

---

### I

**identity**  
The unique identifier of an entity in DDD, distinguishing it from other objects. (Chapter 27)

**IDisposable**  
An interface that defines a `Dispose()` method for releasing unmanaged resources. (Chapter 18)

**immutability**  
The property of an object whose state cannot be changed after creation. Records and `readonly` fields promote immutability. (Chapter 7, 11)

**indexer**  
A member that allows an object to be indexed like an array (e.g., `collection[i]`). (Chapter 7)

**inheritance**  
A mechanism where a class derives from another class, reusing and extending its functionality. (Chapter 9)

**initialization**  
The process of assigning initial values to variables or setting up an object's state. (Chapter 2, 8)

**instance**  
An object created from a class. Each instance has its own copy of instance fields. (Chapter 6)

**interface**  
A contract that defines a set of members (methods, properties, events) that implementing classes must provide. (Chapter 10)

**internal**  
An access modifier that limits visibility to within the same assembly. (Chapter 11)

**invariant**  
A condition that must always hold true for an object. Enforced by the aggregate root in DDD. (Chapter 27)

**IoC (Inversion of Control)**  
A principle where the control of object creation and flow is inverted from the application to a container or framework. Dependency injection is a form of IoC. (Chapter 21)

**IEnumerable<T>**  
An interface that represents a forward‑only cursor over a sequence of elements. The basis of `foreach` and LINQ. (Chapter 4)

**IQueryable<T>**  
An interface that represents a query that can be translated to another language (e.g., SQL) and executed remotely. Used by EF Core. (Chapter 15)

---

### J

**JIT (Just‑In‑Time) compiler**  
The compiler that translates Intermediate Language (IL) to native machine code at runtime. (Chapter 1)

**JSON**  
JavaScript Object Notation, a lightweight data interchange format. (Chapter 19)

**JWT (JSON Web Token)**  
A compact, URL‑safe token format used for authentication and information exchange. (Chapter 28)

---

### K

**key**  
In a dictionary, the unique identifier used to look up a value. (Chapter 4)

---

### L

**lambda**  
An anonymous function defined using the `=>` syntax. Widely used in LINQ and event handling. (Chapter 12)

**LINQ (Language Integrated Query)**  
A set of features that allows querying data from various sources using a SQL‑like syntax or method chains. (Chapter 15)

**list**  
An ordered, dynamically resizable collection. Usually refers to `List<T>`. (Chapter 4)

**lock**  
A statement that acquires a mutual‑exclusion lock, ensuring that only one thread can execute a block of code at a time. (Chapter 24)

**loop**  
A control structure that repeats a block of code (e.g., `for`, `foreach`, `while`, `do`). (Chapter 3)

---

### M

**method**  
A block of code that performs an action and optionally returns a value. Encapsulates behavior. (Chapter 5)

**middleware**  
Components in ASP.NET Core that form the request pipeline, handling requests and responses. (Chapter 22)

**mocking**  
Creating fake objects that simulate the behavior of real dependencies for unit testing. (Chapter 23)

**model**  
In MVC, the part that represents the data and business logic. In web APIs, often a DTO or entity. (Chapter 22)

**model binding**  
The process of mapping HTTP request data to action method parameters in ASP.NET Core. (Chapter 22)

**module**  
A logical unit of code that can contain types; historically, a compiled unit smaller than an assembly.

**MSIL (Microsoft Intermediate Language)**  
The low‑level language that C# compiles to; now commonly called IL (Intermediate Language). (Chapter 1)

**MVC (Model‑View‑Controller)**  
A pattern that separates an application into three interconnected components: Model (data), View (UI), Controller (logic). (Chapter 22)

---

### N

**namespace**  
A container for organizing types (classes, interfaces, etc.) and avoiding naming conflicts. (Chapter 1)

**nullable types**  
Value types that can also hold `null`. Denoted by `?` (e.g., `int?`). (Chapter 2)

**NuGet**  
The package manager for .NET, used to distribute and consume libraries. (Appendix C)

---

### O

**object**  
An instance of a class; a concrete entity that encapsulates state and behavior. (Chapter 6)

**object initializer**  
Syntax that sets properties or fields of an object at creation time without calling a constructor. (Chapter 8)

**OOP (Object‑Oriented Programming)**  
A programming paradigm based on objects containing data and methods. Key concepts: encapsulation, inheritance, polymorphism. (Chapters 6‑11)

**operator**  
A symbol that defines an operation (e.g., `+`, `-`, `&&`). (Chapter 3)

**ORM (Object‑Relational Mapper)**  
A library that maps database tables to objects in code, e.g., Entity Framework Core. (Chapter 22)

**out parameter**  
A parameter passed by reference that does not need to be initialized before the call and must be assigned in the method. (Chapter 5)

**override**  
A keyword used to provide a new implementation of a virtual or abstract method inherited from a base class. (Chapter 9)

---

### P

**package**  
A NuGet package containing compiled code and metadata for reuse.

**parallel**  
Executing multiple tasks simultaneously on multiple cores. (Chapter 24)

**parameter**  
A variable in a method definition that receives a value when the method is called. (Chapter 5)

**pattern matching**  
A feature that tests an expression against a set of patterns, enabling concise conditional logic. (Chapter 17)

**performance profiling**  
Analyzing an application to identify performance bottlenecks (CPU, memory, I/O). (Chapter 25)

**PLINQ (Parallel LINQ)**  
A parallel implementation of LINQ that executes queries concurrently. (Chapter 24)

**polymorphism**  
The ability of objects of different types to respond to the same method call, each in its own way. Achieved via virtual methods and interfaces. (Chapter 9)

**primitive types**  
Basic data types built into the language, such as `int`, `bool`, `double`. (Chapter 2)

**primary constructor**  
A constructor defined directly in the class declaration, with parameters available throughout the class (C# 12). (Chapter 8, 29)

**property**  
A member that provides access to a field with optional logic (validation, computation). Encapsulates state. (Chapter 6, 7)

**public/private/protected**  
Access modifiers controlling visibility. (Chapter 6, 11)

---

### R

**race condition**  
A situation where the outcome of a program depends on the unpredictable timing of threads. (Chapter 24)

**Razor**  
A view engine for generating HTML in ASP.NET MVC. (Chapter 22)

**readonly**  
A keyword that marks a field as assignable only at declaration or in the constructor. Also used in `readonly struct`. (Chapter 11)

**record**  
A reference type with built‑in value semantics, immutability, and a concise syntax. Introduced in C# 9. (Chapter 7, 29)

**ref**  
A keyword that passes an argument by reference, allowing the method to modify the original variable. (Chapter 5, 25)

**reference type**  
A type whose variable holds a reference to the actual data (e.g., `class`, `string`, `array`). (Chapter 2)

**reflection**  
The ability of code to inspect and interact with types, members, and attributes at runtime. (Chapter 20)

**repository**  
A pattern that mediates between the domain and data mapping layers, providing collection‑like access to aggregates. (Chapter 27)

**request/response**  
The fundamental message exchange pattern in HTTP: a client sends a request, a server returns a response. (Chapter 22)

**resource (managed/unmanaged)**  
Managed resources are handled by the GC; unmanaged resources (file handles, etc.) must be released explicitly via `IDisposable`. (Chapter 18)

**REST**  
Representational State Transfer, an architectural style for designing networked applications, often using HTTP. (Chapter 22)

**route**  
A URL pattern that maps to a controller action or endpoint. (Chapter 22)

---

### S

**SDK (Software Development Kit)**  
A set of tools, libraries, and documentation for developing software. The .NET SDK includes the CLI, compilers, and runtime.

**sealed**  
A keyword that prevents a class from being inherited or a method from being overridden. (Chapter 9)

**serialization**  
The process of converting an object into a format that can be stored or transmitted (e.g., JSON, XML, binary). (Chapter 19)

**server**  
A computer or program that provides services to clients.

**service**  
A class that encapsulates business logic, often used in dependency injection. (Chapter 21)

**signature**  
The combination of a method's name, parameter types, and number of parameters (return type not included for overloading). (Chapter 5)

**singleton**  
A design pattern ensuring a class has only one instance and providing global access. (Chapter 26)

**SOLID principles**  
Five design principles for maintainable object‑oriented software: Single Responsibility, Open‑Closed, Liskov Substitution, Interface Segregation, Dependency Inversion. (Chapter 11)

**source generator**  
A component that runs at compile time and can generate additional C# source code based on existing code. (Chapter 20)

**stack trace**  
A report of the active stack frames at a particular point in time, often used for debugging exceptions. (Chapter 14)

**static**  
A keyword that declares a member belonging to the type itself, not to an instance. (Chapter 6)

**stream**  
A sequence of bytes used for reading/writing data, often from/to files, network, or memory. (Chapter 19)

**string interpolation**  
A syntax for embedding expressions in strings using `$"{expression}"`. (Chapter 1)

**struct**  
A value type that can contain data and methods, typically used for small, immutable objects. (Chapter 2)

**switch expression**  
A concise form of switch statement that returns a value, introduced in C# 8. (Chapter 3, 17)

---

### T

**task**  
A unit of asynchronous work, represented by `Task` and `Task<T>` classes. (Chapter 16)

**thread**  
A lightweight unit of execution within a process. (Chapter 24)

**top‑level statement**  
A feature that allows writing the entry point code without explicit namespace, class, or `Main` method. (Chapter 1, 29)

**tuple**  
A lightweight data structure with multiple fields, often used to return multiple values from a method. (Chapter 5, 17)

**type**  
A classification of data (e.g., `int`, `string`, `Person`) that defines the possible values and operations. (Chapter 2)

---

### U

**ubiquitous language**  
A common language shared by developers and domain experts in DDD, used in code, discussions, and documentation. (Chapter 27)

**unit test**  
An automated test that verifies a small unit of code (typically a method) in isolation. (Chapter 23)

**using statement**  
A statement that ensures `Dispose` is called on an `IDisposable` object when it goes out of scope. (Chapter 18)

---

### V

**validation**  
The process of ensuring data meets certain rules before further processing. (Chapter 22, 28)

**value object**  
An immutable object defined by its attributes, with no identity. Key building block in DDD. (Chapter 27)

**value type**  
A type whose variable directly contains its data (e.g., `struct`, `enum`). Stored on the stack when local. (Chapter 2)

**variable**  
A named storage location that holds a value.

**var**  
A keyword for implicitly typed local variables. The compiler infers the type. (Chapter 2)

**view**  
In MVC, the component responsible for rendering the user interface (HTML). (Chapter 22)

**virtual**  
A keyword that allows a method or property to be overridden in a derived class. (Chapter 9)

**void**  
A keyword indicating that a method does not return a value. (Chapter 5)

---

### W

**web API**  
An API designed to be accessed over HTTP, typically returning JSON or XML. (Chapter 22)

---

### X

**XML**  
eXtensible Markup Language, a markup format for structured data. (Chapter 19)

---

### Y

**yield**  
A keyword used in iterator blocks to return elements one at a time (`yield return`) or end iteration (`yield break`). (Chapter 24)