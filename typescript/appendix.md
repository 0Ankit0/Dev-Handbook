# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: TypeScript Quick Reference

### Type Annotations

```typescript
// Primitive types
let name: string = "Alice";
let age: number = 30;
let isAdmin: boolean = true;
let nothing: null = null;
let notAssigned: undefined = undefined;

// Arrays
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b"];

// Tuple — fixed-length array with known types at each position
let point: [number, number] = [10, 20];
let entry: [string, number] = ["Alice", 30];

// Object type inline
let person: { name: string; age: number } = { name: "Alice", age: 30 };

// any — opts out of type checking (avoid when possible)
let dynamic: any = "could be anything";

// unknown — safer than any; must narrow before use
let input: unknown = getUserInput();
if (typeof input === "string") {
  input.toUpperCase();  // OK — narrowed to string
}

// never — a value that never occurs (exhaustive checks, infinite loops)
function fail(message: string): never {
  throw new Error(message);
}
```

### Interfaces and Type Aliases

```typescript
// Interface — describes object shape; can be extended
interface User {
  id: number;
  name: string;
  email?: string;         // optional property
  readonly createdAt: Date;  // read-only
}

// Extending an interface
interface Admin extends User {
  role: "admin" | "superadmin";
  permissions: string[];
}

// Type alias — can describe any type, not just objects
type ID = string | number;
type Status = "active" | "inactive" | "pending";

// Type alias for object (similar to interface, but cannot be re-opened)
type Point = {
  x: number;
  y: number;
};

// When to use interface vs type:
// - Use interface for objects that might be extended
// - Use type for unions, intersections, primitives, or when you need flexibility
```

### Functions

```typescript
// Typed function
function add(a: number, b: number): number {
  return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// Optional parameter
function greet(name: string, greeting?: string): string {
  return `${greeting ?? "Hello"}, ${name}!`;
}

// Rest parameters
function sum(...numbers: number[]): number {
  return numbers.reduce((acc, n) => acc + n, 0);
}

// Function type
type Handler = (event: Event) => void;
let onClick: Handler = (e) => console.log(e.type);

// Overloads
function format(value: string): string;
function format(value: number): string;
function format(value: string | number): string {
  return String(value).trim();
}
```

### Union and Intersection Types

```typescript
// Union — one of several types
type StringOrNumber = string | number;

function display(value: StringOrNumber) {
  if (typeof value === "string") {
    console.log(value.toUpperCase());
  } else {
    console.log(value.toFixed(2));
  }
}

// Intersection — combines multiple types
type Timestamped = { createdAt: Date; updatedAt: Date };
type Named = { name: string };

type TimestampedUser = User & Timestamped;  // has all User properties + timestamps

// Discriminated union — a union with a common "tag" field
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number }
  | { kind: "triangle"; base: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":    return Math.PI * shape.radius ** 2;
    case "rectangle": return shape.width * shape.height;
    case "triangle":  return 0.5 * shape.base * shape.height;
  }
}
```

### Generics

```typescript
// Generic function — works with any type
function identity<T>(value: T): T {
  return value;
}
identity<string>("hello");  // T = string
identity(42);               // T inferred as number

// Generic interface
interface Repository<T> {
  findById(id: number): T | undefined;
  findAll(): T[];
  save(item: T): void;
  delete(id: number): void;
}

// Generic constraint — T must have a .length property
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}
longest("hello", "hi");     // OK — strings have .length
longest([1, 2, 3], [1]);    // OK — arrays have .length

// Utility types (built-in generics)
type PartialUser = Partial<User>;       // all fields optional
type RequiredUser = Required<User>;     // all fields required
type PickedUser = Pick<User, "id" | "name">;  // only id and name
type OmittedUser = Omit<User, "password">;    // everything except password
type ReadonlyUser = Readonly<User>;     // all fields read-only
type UserRecord = Record<string, User>; // dict-like object
```

### Classes

```typescript
class Animal {
  readonly name: string;
  private sound: string;
  protected legs: number;

  constructor(name: string, sound: string, legs: number) {
    this.name = name;
    this.sound = sound;
    this.legs = legs;
  }

  speak(): string {
    return `${this.name} says ${this.sound}`;
  }
}

class Dog extends Animal {
  #breed: string;  // private class field (ES2022)

  constructor(name: string, breed: string) {
    super(name, "Woof", 4);
    this.#breed = breed;
  }

  getBreed(): string {
    return this.#breed;
  }
}

// Short-hand constructor parameter initialization
class Point {
  constructor(
    public readonly x: number,
    public readonly y: number,
  ) {}

  distanceTo(other: Point): number {
    return Math.sqrt((this.x - other.x) ** 2 + (this.y - other.y) ** 2);
  }
}
```

### Enums

```typescript
// Numeric enum (values 0, 1, 2, ...)
enum Direction {
  Up,      // 0
  Down,    // 1
  Left,    // 2
  Right,   // 3
}

// String enum (explicit, recommended for debugging)
enum Status {
  Active   = "ACTIVE",
  Inactive = "INACTIVE",
  Pending  = "PENDING",
}

// Const enum — inlined at compile time (no runtime object)
const enum Color {
  Red,
  Green,
  Blue,
}

// Alternative: use a union type (often preferred over enums)
type Direction2 = "up" | "down" | "left" | "right";
```

### Type Guards and Narrowing

```typescript
// typeof guard
function process(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase();   // value is string here
  }
  return value.toFixed(2);        // value is number here
}

// instanceof guard
function handle(error: Error | string) {
  if (error instanceof Error) {
    console.error(error.message);  // Error object
  } else {
    console.error(error);          // string
  }
}

// Custom type guard (predicate)
interface Cat { meow(): void }
interface Dog { bark(): void }

function isCat(animal: Cat | Dog): animal is Cat {
  return "meow" in animal;
}

// in operator guard
if ("name" in obj) {
  console.log(obj.name);  // TypeScript knows obj has .name
}
```

---

## Appendix B: tsconfig.json Reference

### Recommended Strict Configuration

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ES2022", "DOM"],

    // Strictness (enable all for best type safety)
    "strict": true,                    // enables all strict* flags below
    "noUncheckedIndexedAccess": true,  // index access can be undefined
    "exactOptionalPropertyTypes": true, // optional ≠ | undefined by default

    // Output
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,               // generate .d.ts files
    "sourceMap": true,                 // enable debugging

    // Module
    "esModuleInterop": true,           // smoother CommonJS interop
    "resolveJsonModule": true,         // import JSON files
    "allowSyntheticDefaultImports": true,

    // Quality
    "noUnusedLocals": true,            // error on unused variables
    "noUnusedParameters": true,        // error on unused function params
    "noImplicitReturns": true,         // all code paths must return
    "noFallthroughCasesInSwitch": true // no fallthrough in switch
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### Key Options Explained

| Option | What It Does |
|--------|-------------|
| `strict` | Enables strict null checks, no implicit any, strict function types |
| `target` | JavaScript version to output (`ES5`, `ES2020`, `ESNext`) |
| `module` | Module system (`CommonJS` for Node, `ESNext` for bundlers) |
| `moduleResolution` | How TypeScript finds module files |
| `declaration` | Generates `.d.ts` type declaration files |
| `sourceMap` | Maps compiled JS back to TS source for debugging |
| `esModuleInterop` | Allows `import fs from 'fs'` instead of `import * as fs from 'fs'` |

---

## Appendix C: Glossary

**Compiler / Transpiler**
TypeScript is technically a transpiler: it converts TypeScript source code into JavaScript source code (not native machine code). The TypeScript compiler (`tsc`) performs type checking and emits `.js` output.

**Type Inference**
TypeScript can often figure out types automatically without explicit annotations. `const x = 42` infers `x: number`. You only need annotations where inference can't help or where you want to be explicit.

**Declaration File (.d.ts)**
A file containing only type information (no runtime code). Used to add TypeScript types to JavaScript libraries that weren't written in TypeScript. DefinitelyTyped (`@types/...` packages on npm) provides these for popular libraries.

**Type Narrowing**
The process of refining a broader type to a more specific one within a conditional block. TypeScript tracks control flow and narrows types in `if`, `switch`, and `while` statements.

**Structural Typing**
TypeScript uses structural (duck) typing: if an object has the required properties, it's compatible — regardless of its name or where it was defined. This differs from nominal typing (like Java/C#) where two types with the same shape but different names are not interchangeable.

**Discriminated Union**
A union of object types where each type has a common "tag" field with a unique literal value. TypeScript uses the tag to determine which type you're working with inside a switch or if statement.

---

## Appendix D: Further Resources

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/) — official documentation
- [TypeScript Playground](https://www.typescriptlang.org/play) — try TypeScript in the browser
- [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) — type definitions for JS libraries
- [Matt Pocock's Total TypeScript](https://www.totaltypescript.com/) — excellent advanced content
- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/) — free online book
