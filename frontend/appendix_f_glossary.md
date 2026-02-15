# Appendix F: Glossary

---

## Introduction

This glossary defines key terms and concepts used throughout the handbook and in frontend development generally. Whether you're reviewing a term you encountered earlier or looking up a new concept, this reference will help clarify the terminology.

The glossary is organized alphabetically, with terms grouped loosely by category (HTML, CSS, JavaScript, and general web development) but presented in a single A‑to‑Z list for ease of use.

---

## A

**Absolute URL**
A full web address that includes the protocol (e.g., `https://`) and domain name, pointing to a resource regardless of the current page's location. Compare with *Relative URL*.

**Accessibility (a11y)**
The practice of making websites usable by as many people as possible, including those with disabilities, by following guidelines such as WCAG and using semantic HTML, ARIA, and keyboard navigation.

**AJAX (Asynchronous JavaScript and XML)**
A technique for sending and receiving data from a server asynchronously without reloading the page. Modern implementations typically use the Fetch API or XMLHttpRequest with JSON instead of XML.

**API (Application Programming Interface)**
A set of rules and protocols that allows different software applications to communicate. In web development, often refers to web APIs that return data (e.g., REST, GraphQL).

**ARIA (Accessible Rich Internet Applications)**
A set of attributes that enhance the accessibility of web content, especially dynamic content and custom widgets, by providing additional semantics to assistive technologies.

**Array**
A JavaScript data structure that stores ordered collections of values, accessed by numeric indices. Arrays have many built‑in methods for iteration and manipulation.

**Async/Await**
Modern JavaScript syntax for working with Promises, allowing asynchronous code to be written in a more synchronous, readable style. `async` functions always return a Promise, and `await` pauses execution until a Promise settles.

**Attribute**
In HTML, additional values that configure elements or adjust their behavior (e.g., `href`, `src`, `class`). In CSS, a selector type that matches elements based on their attributes.

---

## B

**BEM (Block Element Modifier)**
A naming convention for CSS classes that promotes modularity and reusability by structuring names as `block__element--modifier`.

**Block Element**
In HTML, an element that occupies the full width available and starts on a new line (e.g., `<div>`, `<p>`, `<h1>`). Compare with *Inline Element*.

**Boolean**
A primitive data type in JavaScript with only two possible values: `true` or `false`.

**Box Model**
The CSS concept that every element is represented as a rectangular box consisting of content, padding, border, and margin. Understanding the box model is fundamental to layout.

**Breakpoint**
In responsive design, a point at which the layout changes to accommodate different screen sizes, typically defined with media queries.

**Browser**
A software application for accessing the World Wide Web (e.g., Chrome, Firefox, Safari, Edge). Browsers render HTML, CSS, and JavaScript.

**Browser API**
Built‑in interfaces provided by the browser for JavaScript to interact with the browser environment (e.g., DOM API, Fetch API, Geolocation API).

**Byte**
A unit of digital information consisting of 8 bits. File sizes are often measured in kilobytes (KB), megabytes (MB), etc.

---

## C

**Cache**
A temporary storage location for copies of files (HTML pages, images, scripts) to reduce load time and bandwidth usage. Browsers use HTTP caching; service workers enable more advanced caching strategies.

**Callback**
A function passed as an argument to another function, to be executed later, often after an asynchronous operation completes. Callbacks can lead to "callback hell" when nested deeply.

**Cascade**
The CSS algorithm that determines which styles apply to an element when multiple rules conflict. It considers importance, specificity, and source order.

**CDN (Content Delivery Network)**
A geographically distributed network of servers that deliver content (like CSS, JavaScript, images) to users from the nearest server, improving load times.

**Class**
In CSS, a reusable selector (prefixed with a dot) that can be applied to multiple HTML elements. In JavaScript, a blueprint for creating objects with shared properties and methods.

**Client**
In client‑server architecture, the device or application (typically a web browser) that requests and displays resources from a server.

**Closure**
A JavaScript function that retains access to its outer (enclosing) scope even after the outer function has returned. Closures are used for data privacy and creating function factories.

**CMS (Content Management System)**
Software that allows users to create, manage, and modify content on a website without technical expertise (e.g., WordPress, Drupal).

**Color Space**
A specific organization of colors; in CSS, common color spaces include sRGB, HSL, and LAB. Modern CSS supports multiple color spaces via functions like `color()`.

**Combinator**
In CSS, a character that specifies the relationship between selectors (e.g., space for descendant, `>` for child, `+` for adjacent sibling).

**Comment**
Text in code that is ignored by the browser or interpreter, used to explain or annotate the code. HTML comments: `<!-- ... -->`, CSS/JS comments: `//` or `/* ... */`.

**Compression**
Reducing the size of files (images, code, etc.) to improve load times. Lossless compression preserves all data; lossy compression discards some data for smaller file sizes.

**Concatenation**
Joining strings together, often using the `+` operator or template literals in JavaScript.

**Console**
A tool in browser DevTools for logging messages and executing JavaScript. It provides methods like `console.log()`, `console.error()`, etc.

**Const**
A JavaScript keyword for declaring block‑scoped variables that cannot be reassigned (though objects declared with `const` can have their properties modified).

**Constructor**
A special method in a JavaScript class that is called when a new instance is created. It initializes the object's properties.

**Content Security Policy (CSP)**
An HTTP header that allows you to restrict which resources (scripts, styles, images) the browser can load, helping to prevent XSS attacks.

**Cookie**
Small pieces of data stored by the browser, often used for session management, personalization, and tracking. Cookies are sent with every request to the domain.

**Core Web Vitals**
A set of specific performance metrics (LCP, INP, CLS) that Google considers important for user experience and uses in its ranking algorithm.

**CRUD (Create, Read, Update, Delete)**
The four basic operations for persistent storage. In frontend apps, often implemented via API calls to a backend.

**CSS (Cascading Style Sheets)**
The language used to describe the presentation of a document written in HTML, including layout, colors, fonts, and animations.

**CSS Grid**
A two‑dimensional layout system in CSS that allows you to create complex grid‑based layouts with rows and columns.

---

## D

**Data Attribute**
In HTML, custom attributes prefixed with `data-` (e.g., `data-user-id`) that store private information for a page or application, accessible via JavaScript.

**Data Type**
The classification of data that tells the interpreter how to use it. JavaScript has primitive types (string, number, boolean, null, undefined, symbol, bigint) and reference types (object, array, function).

**Debugging**
The process of finding and fixing errors in code. Tools include browser DevTools, `console.log`, breakpoints, and linters.

**Declaration**
In CSS, a property‑value pair (e.g., `color: red;`). In JavaScript, a statement that creates a variable or function (e.g., `let x;`, `function foo() {}`).

**Defer**
An attribute for `<script>` tags that tells the browser to download the script in parallel while parsing HTML, and execute it only after parsing is complete. Helps improve page load performance.

**Destructuring**
A JavaScript syntax that unpacks values from arrays or properties from objects into distinct variables (e.g., `const {name, age} = user;`).

**DevTools**
Developer tools built into browsers, providing panels for inspecting HTML/CSS, debugging JavaScript, analyzing network activity, and profiling performance.

**Display**
A CSS property that defines how an element is displayed in the layout. Common values: `block`, `inline`, `inline-block`, `flex`, `grid`, `none`.

**DNS (Domain Name System)**
The system that translates human‑readable domain names (like `example.com`) into IP addresses that computers use to identify each other on the network.

**DOM (Document Object Model)**
A programming interface for HTML documents that represents the page as a tree of nodes, allowing JavaScript to manipulate the structure, style, and content.

**Dynamic Typing**
JavaScript's property where variable types are determined at runtime, and the same variable can hold values of different types.

---

## E

**ECMAScript**
The standard specification that JavaScript is based on. New versions (e.g., ES6, ES2024) introduce new language features.

**Element**
In HTML, a component of the document, consisting of a start tag, content, and an end tag (or a self‑closing tag). In the DOM, an object representing an HTML element.

**Em**
A relative CSS unit based on the font size of the element. For example, `2em` means twice the current font size.

**Emmet**
A plugin for text editors that allows you to write HTML and CSS using abbreviations that expand into full code (e.g., `ul>li*5` expands to an unordered list with five list items).

**Encoding**
The process of converting data into a specific format for transmission or storage. In web development, often refers to character encoding (e.g., UTF‑8) or URL encoding.

**ES6 (ECMAScript 2015)**
A major update to JavaScript that introduced many new features: `let`, `const`, arrow functions, classes, template literals, destructuring, modules, and more.

**Event**
An action or occurrence detected by the browser, such as a mouse click, key press, or page load, to which JavaScript can respond.

**Event Delegation**
A technique where a single event listener on a parent element handles events for multiple children, leveraging event bubbling. Useful for dynamic content.

**Event Listener**
A function that waits for a specific event to occur on a target element and then executes in response. Added via `addEventListener()`.

**Event Loop**
The mechanism in JavaScript that handles asynchronous operations. It continuously checks the call stack and callback queue, pushing callbacks to the stack when it's empty.

**Exception**
A runtime error that disrupts the normal flow of execution. Exceptions can be thrown and caught using `try...catch`.

---

## F

**Fetch API**
A modern, promise‑based JavaScript interface for making HTTP requests, replacing the older XMLHttpRequest.

**Flexbox**
A one‑dimensional layout model in CSS that distributes space and aligns items within a container, making it ideal for responsive designs.

**Float**
A CSS property that takes an element out of the normal flow and places it to the left or right of its container, allowing text to wrap around it. Largely replaced by Flexbox and Grid for layout.

**Focus**
The state of an element (like a link or input) when it is selected to receive keyboard input. Visible focus indicators are essential for accessibility.

**Font Stack**
A list of fonts in the `font-family` property, providing fallbacks if the first choice is not available.

**Footer**
A semantic HTML element (`<footer>`) typically containing closing information about its section, such as author info, copyright, or related links.

**For Loop**
A JavaScript loop that repeats a block of code a specified number of times, with initialization, condition, and increment expressions.

**Framework**
A pre‑written collection of code (libraries, tools, conventions) that provides a foundation for building applications. Examples: React, Vue, Angular.

**Function**
A reusable block of JavaScript code that performs a specific task, defined with the `function` keyword or as an arrow function.

---

## G

**Git**
A distributed version control system for tracking changes in source code during software development.

**Global Variable**
A variable declared outside any function, accessible anywhere in the script. Overuse can lead to naming conflicts and hard‑to‑debug code.

**GPU (Graphics Processing Unit)**
A specialized processor for rendering graphics. Modern browsers use the GPU to accelerate painting and compositing, especially for animations and transitions.

**Gradient**
A smooth transition between two or more colors, created in CSS with functions like `linear-gradient()` and `radial-gradient()`.

**Grid**
See *CSS Grid*.

---

## H

**Hash**
In URLs, the part after the `#` symbol, often used to navigate to a specific section within a page. Also used in routing for single‑page applications.

**Header**
A semantic HTML element (`<header>`) representing introductory content, typically containing headings, logos, and navigation.

**Heading**
HTML elements `<h1>` through `<h6>` that define section headings, with `<h1>` being the highest (most important) level.

**Hoisting**
JavaScript's behavior where variable and function declarations are moved to the top of their containing scope during compilation, before code execution. `let` and `const` are hoisted but not initialized.

**HTTP (Hypertext Transfer Protocol)**
The protocol used for transferring web pages and other resources over the internet. HTTPS is the secure version (encrypted).

**HTTP Method**
Indicates the desired action for a request. Common methods: `GET` (retrieve), `POST` (submit), `PUT` (update), `DELETE` (remove).

**HTTP Status Code**
A three‑digit response from the server indicating the result of the request (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).

**HTTPS**
HTTP over TLS/SSL, encrypting the communication between browser and server to ensure privacy and data integrity.

---

## I

**ID**
An HTML attribute (`id`) that uniquely identifies an element within a page. IDs must be unique and are often used for JavaScript targeting or anchor links.

**IIFE (Immediately Invoked Function Expression)**
A JavaScript function that runs as soon as it is defined, often used to create a private scope.

**Image Optimization**
The process of reducing image file sizes while maintaining acceptable quality, using techniques like compression, choosing the right format, and responsive images.

**Infinite Scroll**
A technique where more content is loaded automatically as the user scrolls down the page, often implemented with Intersection Observer.

**Inline Element**
An HTML element that does not start on a new line and only takes up as much width as necessary (e.g., `<span>`, `<a>`, `<strong>`).

**Input**
An HTML element (`<input>`) for creating interactive form controls, such as text fields, checkboxes, and buttons.

**Intersection Observer**
A browser API that asynchronously observes changes in the intersection of a target element with an ancestor or the viewport, used for lazy loading, infinite scroll, and animations.

**IP Address**
A unique string of numbers separated by periods (IPv4) or colons (IPv6) that identifies a device on the internet or a local network.

---

## J

**JavaScript**
A high‑level, interpreted programming language that enables interactive web pages. It is an implementation of the ECMAScript standard.

**JSON (JavaScript Object Notation)**
A lightweight data‑interchange format based on JavaScript object syntax, commonly used for transmitting data between a server and a web application.

---

## K

**Keyframe**
In CSS animations, a point in an animation timeline where specific property values are defined, using the `@keyframes` rule.

**Keyboard Accessibility**
Ensuring that all functionality on a web page can be operated via a keyboard alone, essential for users with motor disabilities and power users.

---

## L

**Label**
An HTML element (`<label>`) that defines a caption for a form control, improving accessibility and usability by associating text with its input.

**Landmark**
Regions of a web page (such as `<header>`, `<nav>`, `<main>`, `<footer>`) that assistive technologies use to help users navigate.

**Largest Contentful Paint (LCP)**
A Core Web Vital measuring loading performance: the time from page start to when the largest content element (image, video, or text block) is rendered within the viewport.

**Layout Shift**
An unexpected movement of page content after it has already been painted, often caused by images or ads without dimensions, negatively impacting Cumulative Layout Shift (CLS).

**Lazy Loading**
A technique that defers loading of non‑critical resources (like images or scripts) until they are needed, improving initial page load time.

**Let**
A JavaScript keyword for declaring block‑scoped variables that can be reassigned.

**Lighthouse**
An open‑source tool integrated into Chrome DevTools for auditing web pages for performance, accessibility, best practices, SEO, and PWA readiness.

**Linter**
A tool that analyzes code for potential errors, stylistic issues, and suspicious patterns. ESLint is the standard linter for JavaScript.

**LocalStorage**
A web storage API that stores key‑value pairs persistently in the browser, with no expiration date. Data survives page reloads and browser restarts.

**Loop**
A programming construct that repeats a block of code while a condition is true. JavaScript has `for`, `while`, and `do...while` loops.

---

## M

**Main**
A semantic HTML element (`<main>`) representing the dominant content of the `<body>`. There should be only one `<main>` per page.

**Margin**
The CSS property that creates space around an element, outside of its border. Margins are transparent.

**Media Query**
A CSS feature that applies styles conditionally based on media features such as viewport width, device orientation, or resolution, enabling responsive design.

**Metadata**
Data about the document, contained in the `<head>` section, such as title, character set, description, and links to stylesheets.

**Method**
A function that is a property of an object. In JavaScript, many built‑in objects (like arrays and strings) have methods.

**Middleware**
In software development, code that sits between the request and response, often used in server‑side frameworks. In frontend, sometimes refers to interceptors for HTTP requests.

**Minification**
The process of removing unnecessary characters (whitespace, comments, newlines) from code without changing its functionality, reducing file size for faster downloads.

**Mobile‑First**
A design approach where you start by styling for mobile devices, then progressively enhance for larger screens using media queries.

**Module**
A reusable piece of JavaScript code that exports functionality to be imported elsewhere. ES6 modules use `export` and `import`.

**Mutation Observer**
A browser API that watches for changes to the DOM tree (node additions/removals, attribute changes) and executes a callback when changes occur.

---

## N

**NaN (Not a Number)**
A special numeric value in JavaScript representing an unrepresentable or undefined numerical result (e.g., `0/0`).

**Nav**
A semantic HTML element (`<nav>`) representing a section of a page with navigation links.

**Network Panel**
A part of browser DevTools that shows all network requests made by the page, including their headers, timing, and responses.

**Node**
In the DOM, any object in the document tree (elements, text nodes, comments, etc.). In development, Node.js is a runtime for executing JavaScript on the server.

**Normalize**
A CSS technique (Normalize.css) that makes browsers render all elements more consistently and in line with modern standards, as opposed to a full reset.

**Null**
A primitive JavaScript value representing the intentional absence of any object value.

---

## O

**Object**
A JavaScript data type that stores collections of key‑value pairs. Almost everything in JavaScript is an object or can be treated as one.

**Observer**
A browser API that watches for specific events (Intersection Observer, Mutation Observer, Resize Observer) and executes callbacks when they occur.

**Operator**
A symbol that performs an operation on one or more operands (e.g., `+`, `-`, `&&`, `===`).

**Optional Chaining**
A JavaScript operator (`?.`) that allows safe access to nested object properties without throwing an error if an intermediate property is `null` or `undefined`.

---

## P

**Padding**
The CSS property that creates space inside an element, between its content and its border.

**Performance Budget**
A set of limits on metrics such as page weight, load time, or number of requests that a team agrees not to exceed, helping maintain performance.

**Phrasing Content**
HTML content category that includes text and inline markup (e.g., `<span>`, `<a>`, `<strong>`). It can only contain other phrasing content.

**Pixel**
The smallest addressable element on a display. In CSS, the `px` unit is a reference pixel, not necessarily corresponding to a physical screen pixel.

**Placeholder**
Text shown inside a form input before the user types, using the `placeholder` attribute. Not a substitute for a `<label>`.

**Position**
A CSS property that determines how an element is positioned in the document flow. Values: `static`, `relative`, `absolute`, `fixed`, `sticky`.

**Preprocessor**
A tool that extends CSS with variables, nesting, mixins, and functions, compiling to standard CSS. Examples: Sass, Less, Stylus.

**Preload / Prefetch / Preconnect**
Resource hints (`<link rel="preload">`, `prefetch`, `preconnect`) that tell the browser to fetch or connect to resources early, improving performance.

**Primitive**
A basic data type in JavaScript that is not an object and has no methods. There are 7 primitives: `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`.

**Promise**
A JavaScript object representing the eventual completion (or failure) of an asynchronous operation, allowing chaining with `.then()` and `.catch()`.

**Property**
In CSS, a characteristic of an element that can be styled (e.g., `color`, `font-size`). In JavaScript, a value associated with an object.

**Prototype**
The mechanism by which JavaScript objects inherit properties and methods from other objects. Each object has a hidden `[[Prototype]]` property.

**Pseudo‑Class**
A CSS keyword added to a selector that specifies a special state of the element (e.g., `:hover`, `:focus`, `:nth-child()`).

**Pseudo‑Element**
A CSS keyword added to a selector that lets you style a specific part of an element (e.g., `::before`, `::after`, `::first-line`).

---

## Q

**Query String**
The part of a URL after the `?` that contains data to be sent to the server, typically in key‑value pairs (e.g., `?page=2&sort=asc`).

**Quirks Mode**
A browser rendering mode for old pages that were written before web standards, emulating non‑standard behavior. Triggered by missing or incorrect DOCTYPE.

---

## R

**Reflow**
The process by which the browser recalculates the positions and geometries of elements in the document, often triggered by DOM changes. Frequent reflows can hurt performance.

**Regex (Regular Expression)**
A sequence of characters that defines a search pattern, used for pattern matching in strings. In JavaScript, represented by the `RegExp` object.

**Relative URL**
A URL that points to a resource relative to the current page's location (e.g., `images/photo.jpg`). Compare with *Absolute URL*.

**Rem**
A CSS unit relative to the font size of the root (`<html>`) element. Useful for consistent scaling across a page.

**Render**
The process of converting HTML, CSS, and JavaScript into pixels on the screen. It involves parsing, layout, paint, and compositing.

**Repaint**
When the browser redraws pixels that have changed (e.g., after changing background color), without affecting layout. Less expensive than reflow.

**Resize Observer**
A browser API that watches for changes to an element's size and executes a callback when the size changes.

**Resolution**
The number of pixels per unit area (e.g., dots per inch – DPI). In media queries, resolution is used to target high‑DPI screens.

**Responsive Design**
An approach to web design that makes pages render well on a variety of devices and window sizes, using fluid grids, flexible images, and media queries.

**REST (Representational State Transfer)**
An architectural style for designing networked applications, often using HTTP methods and JSON/XML responses.

**Root**
In the DOM, the topmost node, usually the `document` object. In CSS, the `:root` pseudo‑class targets the `<html>` element.

**Runtime**
The time during which a program is executing. JavaScript runtime refers to the environment (browser or Node.js) where the code runs.

---

## S

**Same‑Origin Policy**
A critical security mechanism that restricts how a document or script loaded from one origin can interact with a resource from another origin.

**Sanitization**
The process of cleaning user input to remove or escape potentially dangerous content, such as malicious scripts, to prevent XSS attacks.

**Scope**
The context in which variables are accessible. JavaScript has global, function, and block scope.

**Screen Reader**
Assistive technology that reads aloud the content of a screen for users with visual impairments. Examples: NVDA, JAWS, VoiceOver.

**Script**
A block of JavaScript code, either embedded in HTML with `<script>` tags or linked as an external file.

**Section**
A semantic HTML element (`<section>`) representing a standalone section of content, typically with a heading.

**Security Header**
HTTP headers that enhance the security of a website, such as Content‑Security‑Policy, Strict‑Transport‑Security, and X‑Frame‑Options.

**Selector**
A pattern in CSS that selects which elements to style. Selectors can be based on element type, class, ID, attributes, and more.

**Semantic HTML**
Using HTML elements that convey meaning about the structure and content (e.g., `<article>`, `<nav>`, `<header>`) rather than just presentational elements like `<div>`.

**Server**
A computer or program that provides services or resources to clients over a network. In web development, it hosts websites and processes HTTP requests.

**Service Worker**
A script that runs in the background, separate from the web page, enabling features like offline support, push notifications, and advanced caching.

**SessionStorage**
A web storage API similar to `localStorage` but data persists only for the duration of the page session (until the tab is closed).

**Set**
A JavaScript built‑in object that stores unique values of any type.

**Single‑Page Application (SPA)**
A web application that loads a single HTML page and dynamically updates content as the user interacts, without full page reloads.

**Specificity**
The algorithm by which browsers determine which CSS rule applies when multiple rules target the same element. It is calculated based on selector types (IDs, classes, elements).

**Spread Operator**
A JavaScript syntax (`...`) that expands an iterable (like an array) into individual elements, or copies properties from one object to another.

**State**
The data that determines the current condition of a user interface. In frontend frameworks, state management is a key concept.

**Static Typing**
A language feature where variable types are known at compile time. TypeScript adds static typing to JavaScript.

**String**
A primitive JavaScript data type representing a sequence of characters, enclosed in quotes or backticks.

**SVG (Scalable Vector Graphics)**
An XML‑based format for vector images that can scale infinitely without loss of quality, often used for icons and illustrations.

**Syntax**
The set of rules that defines correctly structured statements in a language. Syntax errors occur when code violates these rules.

---

## T

**Tabindex**
An HTML attribute that specifies the order in which an element participates in keyboard navigation (tabbing). `tabindex="0"` adds an element to the natural tab order.

**Tag**
In HTML, the markup that defines an element, enclosed in angle brackets (e.g., `<div>`, `</div>`). Start tags may contain attributes.

**Template Literal**
A JavaScript string literal that allows embedded expressions and multi‑line strings, enclosed by backticks (`` ` ``). Expressions are inserted with `${expression}`.

**Third‑Party Script**
A script hosted on a different domain, often used for analytics, ads, or embeds. They can impact performance and security.

**Throttling**
A technique to limit the rate at which a function is executed (e.g., in response to scroll events). Useful for performance optimization.

**Time to First Byte (TTFB)**
A performance metric measuring the time between the browser requesting a page and receiving the first byte of the response.

**Transition**
A CSS effect that smoothly changes property values over a given duration.

**Tree Shaking**
A build optimization that removes unused code from bundles, reducing file size.

**Try...Catch**
A JavaScript statement for handling exceptions. Code in the `try` block is executed; if an error occurs, execution passes to the `catch` block.

**Type Coercion**
The automatic or implicit conversion of values from one data type to another (e.g., `"5" + 3` results in the string `"53"`).

**TypeScript**
A typed superset of JavaScript that compiles to plain JavaScript, adding optional static types, interfaces, and modern features.

---

## U

**Undefined**
A primitive JavaScript value automatically assigned to variables that have been declared but not yet initialized.

**Unicode**
A character encoding standard that covers most of the world's writing systems. UTF‑8 is the most common encoding for web pages.

**URL (Uniform Resource Locator)**
The address of a resource on the web (e.g., `https://example.com/page`).

**User Agent**
Software that acts on behalf of a user, typically a web browser. The `navigator.userAgent` property provides information about the browser.

**UTF‑8**
A variable‑width character encoding for Unicode, capable of encoding all 1,112,064 valid code points in Unicode. It is the dominant encoding for the web.

---

## V

**Validation**
The process of checking whether data meets specified criteria. In forms, validation can be done on the client (for UX) and must be done on the server (for security).

**Value**
In CSS, the assigned setting for a property (e.g., `red`, `16px`, `block`). In JavaScript, any piece of data assigned to a variable.

**Var**
The old JavaScript keyword for declaring function‑scoped or globally‑scoped variables, largely superseded by `let` and `const`.

**Variable**
A named storage location for data in JavaScript, declared with `let`, `const`, or `var`.

**Viewport**
The visible area of a web page within the browser window. The viewport meta tag (`<meta name="viewport">`) controls how the page is scaled on mobile devices.

**Void Element**
An HTML element that cannot have any content (e.g., `<img>`, `<br>`, `<input>`). Also called an empty element or self‑closing element.

---

## W

**WCAG (Web Content Accessibility Guidelines)**
The international standards for making web content accessible to people with disabilities, organized around four principles: Perceivable, Operable, Understandable, and Robust (POUR).

**Web Storage**
The browser APIs `localStorage` and `sessionStorage` for storing key‑value pairs.

**Web Worker**
A JavaScript feature that allows scripts to run in background threads, separate from the main execution thread, preventing UI blocking.

**WebP**
A modern image format developed by Google, providing superior lossless and lossy compression compared to JPEG and PNG.

**While Loop**
A JavaScript loop that executes a block of code as long as a specified condition is true. Checks the condition before each iteration.

**Whitespace**
Characters like spaces, tabs, and newlines that are used to format code but are often ignored by the browser (except in `<pre>` or `white-space` properties).

**World Wide Web (WWW)**
An information system where documents and other web resources are identified by URLs and can be accessed via the internet.

---

## X

**XHR (XMLHttpRequest)**
A browser API used to make HTTP requests from JavaScript, now largely replaced by the Fetch API but still widely supported.

**XSS (Cross‑Site Scripting)**
A security vulnerability where attackers inject malicious scripts into web pages viewed by other users. Prevented by output encoding and Content Security Policy.

---

## Y

**Yarn**
A popular package manager for JavaScript, an alternative to npm.

---

## Z

**Z‑Index**
A CSS property that controls the stacking order of positioned elements (those with a `position` value other than `static`). Higher values appear on top.

---

This glossary covers the essential terminology used throughout the handbook. As you continue your journey in frontend development, you'll encounter many more terms, but this foundation will serve you well.