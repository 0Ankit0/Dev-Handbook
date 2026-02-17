
---

### The C# Developer's Handbook: From Fundamentals to Enterprise

---

### Part I: The Foundation - Core Concepts

*This part assumes no prior programming knowledge and builds a solid base in C# syntax and logic.*

**[Chapter 1: Hello, World! - Your First Steps](1.%20the_foundation_core_concepts/1.%20hello_world_your_first_steps.ipynb)**
- Understanding the .NET Compilation Process (IL, JIT)
- The `Main` Method as an Entry Point
- Top-Level Statements (The Modern Approach)
- Basic Console I/O (`Console.WriteLine`, `Console.ReadLine`)

**[Chapter 2: Data Types & Variables](1.%20the_foundation_core_concepts/2.%20data_types_variables.ipynb)**
- Value Types vs. Reference Types (The Fundamental Distinction)
- Predefined Data Types (`int`, `double`, `bool`, `char`, `string`, `decimal`)
- Declaring and Initializing Variables
- `var` Keyword and Implicit Typing
- Nullable Value Types (`int?`)

**[Chapter 3: Control Flow in Action](1.%20the_foundation_core_concepts/3.%20control_flow_in_action.ipynb)**
- Boolean Logic and Comparison Operators
- Conditional Statements: `if`, `else if`, `else`
- The `switch` Statement (Classic and Switch Expressions)
- Loops: `for`, `foreach`, `while`, `do-while`
- Jump Statements: `break`, `continue`, `return`

**[Chapter 4: Working with Data - Collections](1.%20the_foundation_core_concepts/4.%20working_with_data_collections.ipynb)**
- Arrays (Single and Multi-Dimensional, Jagged Arrays)
- Generic Collections: `List<T>`, `Dictionary<TKey, TValue>`
- The `System.Linq` Namespace: Introduction to Querying Collections ( `Where`, `Select`, `FirstOrDefault`)
- `foreach` Iteration Deep Dive (`IEnumerable`)

**[Chapter 5: Methods - The Building Blocks of Logic](1.%20the_foundation_core_concepts/5.%20methods_the_building_blocks_of_logic.ipynb)**
- Method Signatures (Access Modifiers, Return Types, Name, Parameters)
- Parameters: `ref`, `out`, `in`, and Parameter Arrays (`params`)
- Method Overloading
- Local Functions
- Expression-Bodied Members

---

### Part II: Object-Oriented Programming (OOP) - The C# Way

*This part covers the heart of C# development, teaching how to model real-world entities and build robust, maintainable code.*

**[Chapter 6: Classes and Objects](2.%20object_oriented_programming_the_c_way/6.%20classes_and_objects.ipynb)**
- Defining a Class: Fields, Properties, Methods
- Objects and Instances: The `new` Keyword
- The `static` Keyword (Static Classes, Members, and `using static`)
- Access Modifiers: `public`, `private`, `internal`, `protected`

**[Chapter 7: Properties, Indexers, and Records](2.%20object_oriented_programming_the_c_way/7.%20properties_indexers_and_records.ipynb)**
- Auto-Implemented Properties
- Full Property Syntax with Validation Logic
- Computed Properties
- Indexers
- **Records:** Immutable Data Objects (Positional Syntax, `with` Expressions, Value-Based Equality)

**[Chapter 8: Constructors & Object Initialization](2.%20object_oriented_programming_the_c_way/8.%20constructors_object_initialization.ipynb)**
- Default and Parameterized Constructors
- Constructor Chaining (`this()`)
- Object Initializers
- The `required` Modifier

**[Chapter 9: Inheritance & Polymorphism](2.%20object_oriented_programming_the_c_way/9.%20inheritance_polymorphism.ipynb)**
- Base Classes and Derived Classes (`:`)
- Virtual and Override Methods
- Abstract Classes and Methods
- Sealed Classes and Methods
- Polymorphism in Action

**[Chapter 10: Interfaces - Defining Contracts](2.%20object_oriented_programming_the_c_way/10.%20interfaces_defining_contracts.ipynb)**
- Defining and Implementing Interfaces
- Explicit Interface Implementation
- Multiple Interface Inheritance
- Default Interface Methods

**[Chapter 11: Encapsulation & Best Practices](2.%20object_oriented_programming_the_c_way/11.%20encapsulation_best_practices.ipynb)**
- Principles of Hiding Implementation Details
- Using Properties for Controlled Access
- The Power of Readonly and Const

---

### Part III: Advanced Language Features

*This part moves into more sophisticated areas of the language that experienced C# developers use daily.*

**[Chapter 12: Delegates, Events, and Lambda Expressions](3.%20advanced_language_features/12.%20delegates_events_and_lambda_expressions.ipynb)**
- What are Delegates? (`Action<T>`, `Func<T,TResult>`)
- Multicast Delegates
- Events: The Publisher/Subscriber Pattern
- Anonymous Methods and Lambda Expressions (`=>`)

**[Chapter 13: Generics - Code Reusability with Type Safety](3.%20advanced_language_features/13.%20generics_code_reusability_with_type_safety.ipynb)**
- Generic Classes and Methods
- Generic Constraints (`where T : class`, `new()`, `BaseClass`)
- Covariance and Contravariance (`out` and `in` keywords)

**[Chapter 14: Exception Handling - Writing Robust Code](3.%20advanced_language_features/14.%20exception_handling_writing_robust_code.ipynb)**
- The `try`, `catch`, `finally` Blocks
- Common Exception Types
- Throwing Exceptions and Best Practices
- Creating Custom Exceptions
- The Importance of Exception Filters

**[Chapter 15: LINQ (Language Integrated Query) Deep Dive](3.%20advanced_language_features/15.%20linq_deep_dive.ipynb)**
- LINQ Syntax: Query vs. Method Syntax
- Deferred Execution vs. Immediate Execution
- Working with `IEnumerable` and `IQueryable`
- LINQ to Objects (In-Memory Collections)
- Projections and Anonymous Types

**[Chapter 16: Asynchronous Programming with `async`/`await`](3.%20advanced_language_features/16.%20asynchronous_programming_with_asyncawait.ipynb)**
- The Problem of Blocking Calls
- Understanding `Task` and `Task<T>`
- The `async` and `await` Keywords
- Best Practices for Async Code (Avoid `async void`)
- Cancellation Tokens (`CancellationToken`)
- `Task.WhenAll` and `Task.WhenAny`

**[Chapter 17: Pattern Matching in Depth](3.%20advanced_language_features/17.%20pattern_matching_in_depth.ipynb)**
- `is` expression and Declaration Patterns
- `switch` expressions revisited
- Property, Positional, and Tuple Patterns
- List Patterns

---

### Part IV: Modern C# and .NET Ecosystem

*This part focuses on the tools and libraries that make up the modern .NET developer's environment.*

**[Chapter 18: Managing Resources - Garbage Collection & `IDisposable`](4.%20modern_c_and_net_ecosystem/18.%20managing_resources_garbage_collection_idisposable.ipynb)**
- How the .NET Garbage Collector Works (Generations)
- The `IDisposable` Interface and the `using` Statement (`using` declaration)
- Finalizers (Destructors) - When and Why to Use Them

**[Chapter 19: File I/O and Serialization](4.%20modern_c_and_net_ecosystem/19.%20file_io_and_serialization.ipynb)**
- Working with the `System.IO` Namespace (`File`, `Directory`, `Path`)
- Reading and Writing Files (Streams: `StreamReader`, `StreamWriter`)
- JSON Serialization with `System.Text.Json`
- XML Serialization

**[Chapter 20: Attributes and Reflection](4.%20modern_c_and_net_ecosystem/20.%20attributes_and_reflection.ipynb)**
- What are Attributes? Predefined Attributes (`[Obsolete]`, `[Serializable]`)
- Creating Custom Attributes
- Introduction to Reflection: Inspecting Types and Members at Runtime
- Performance Considerations of Reflection

**[Chapter 21: Dependency Injection (DI)](4.%20modern_c_and_net_ecosystem/21.%20dependency_injection.ipynb)**
- The Problem of Tight Coupling
- The Dependency Inversion Principle
- The DI Container (Microsoft's Built-in `IServiceProvider`)
- Registering Services (Transient, Scoped, Singleton)
- Constructor Injection

**[Chapter 22: Building Web Applications with ASP.NET Core](4.%20modern_c_and_net_ecosystem/22.%20building_web_applications_with_aspnet_core.ipynb)**
- MVC Pattern vs. Minimal APIs
- Controllers, Actions, and Routing
- Middleware Pipeline
- Model Binding and Validation
- Entity Framework Core (Code-First Approach, Migrations, Querying Data)

**[Chapter 23: Unit Testing for Quality Code](4.%20modern_c_and_net_ecosystem/23.%20unit_testing_for_quality_code.ipynb)**
- The Importance of Testing
- Unit Testing Frameworks: xUnit / NUnit
- Test Naming and Structure (Arrange-Act-Assert)
- Mocking Dependencies with Moq / NSubstitute
- Code Coverage Concepts

---

### Part V: Advanced Architecture and Industry Practices

*This part prepares the reader for complex, real-world enterprise development.*

**[Chapter 24: Concurrency and Parallelism](5.%20advanced_architecture_and_industry_practices/24.%20concurrency_and_parallelism.ipynb)**
- The Threading Model
- `Parallel` LINQ (PLINQ)
- The `System.Threading.Tasks.Parallel` Class
- Concurrent Collections
- Understanding and Avoiding Deadlocks and Race Conditions

**[Chapter 25: Designing for Performance](5.%20advanced_architecture_and_industry_practices/25.%20designing_for_performance.ipynb)**
- `Span<T>` and `Memory<T>` for Stack Allocations
- `ref struct` and `ref returns`
- Understanding the `StringBuilder`
- Benchmarking with `BenchmarkDotNet`
- Profiling and Identifying Bottlenecks

**[Chapter 26: Key Design Patterns in C#](5.%20advanced_architecture_and_industry_practices/26.%20key_design_patterns_in_c.ipynb)**
- Creational: Singleton, Factory Method, Builder
- Structural: Adapter, Decorator, Facade
- Behavioral: Strategy, Observer (Events), Command

**[Chapter 27: Domain-Driven Design (DDD) Concepts](5.%20advanced_architecture_and_industry_practices/27.%20domain_driven_design_concepts.ipynb)**
- Entities vs. Value Objects (Records are perfect for VOs!)
- Aggregates and Repositories
- Domain Events

**[Chapter 28: Securing Your Applications](5.%20advanced_architecture_and_industry_practices/28.%20securing_your_applications.ipynb)**
- Common Vulnerabilities (SQL Injection, XSS)
- Protecting Secrets (User Secrets, Azure Key Vault)
- Hashing and Salting Passwords
- Working with Authentication & Authorization (JWT, ASP.NET Core Identity)

**[Chapter 29: The Road Ahead - What's New in C#](5.%20advanced_architecture_and_industry_practices/29.%20the_road_ahead_whats_new_in_c.ipynb)**
- A Look at the Latest Language Features (e.g., Required Members, Raw String Literals, List Patterns)
- Staying Up-to-Date with the Ecosystem

**Appendix**
- A: C# Keywords Quick Reference
- B: Common .NET CLI Commands
- C: Recommended Tools and Libraries
- D: Glossary of Terms

