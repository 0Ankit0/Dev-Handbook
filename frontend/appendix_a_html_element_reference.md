# Appendix A: HTML Element Reference

---

## Introduction

HTML (HyperText Markup Language) is composed of elements that structure and define the content of web pages. This appendix provides a comprehensive reference to HTML elements, attributes, and their usage. It is organized to help you quickly find the element you need and understand its purpose, syntax, and any accessibility considerations.

The reference is divided into several sections:

- **Alphabetical Reference** – A‑to‑Z listing of all HTML elements with descriptions and examples.
- **Elements by Category** – Grouping elements by their function (e.g., document metadata, text content, forms).
- **Attributes Reference** – Overview of common and global attributes.
- **Global Attributes** – Attributes that can be used on any HTML element.
- **Event Attributes** – Attributes that define JavaScript event handlers.

This reference is intended as a quick lookup; for in‑depth explanations, refer to the relevant chapters in the main handbook.

---

## Complete Alphabetical Reference

Below is an alphabetical list of HTML elements. For each element, we provide:

- **Description** – What the element represents.
- **Categories** – The content categories it belongs to.
- **Content model** – What kind of content it can contain.
- **Tag omission** – Whether start/end tags can be omitted.
- **DOM interface** – The JavaScript object type.
- **Usage notes** – Important points, often about accessibility or semantics.
- **Example** – A brief code snippet.

---

### `<a>`

**Description:** The anchor element creates a hyperlink to web pages, files, email addresses, or locations within the same page.

**Categories:** Flow content, phrasing content, interactive content, palpable content.

**Content model:** Transparent, but may not contain interactive content (e.g., other `<a>` elements).

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLAnchorElement`

**Usage notes:**
- Use the `href` attribute to specify the link destination.
- Use `target="_blank"` to open in a new tab/window (always add `rel="noopener"` for security).
- For links that trigger downloads, use the `download` attribute.
- Ensure link text is descriptive (avoid "click here").

**Example:**
```html
<a href="https://example.com">Visit Example</a>
<a href="/about">About Us</a>
<a href="mailto:info@example.com">Email us</a>
<a href="#section2">Jump to Section 2</a>
<a href="file.pdf" download>Download PDF</a>
```

---

### `<abbr>`

**Description:** Represents an abbreviation or acronym. The optional `title` attribute provides an expansion.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- When the abbreviation is first used, consider wrapping it in `<abbr>` with a `title` to define it.
- For abbreviations in a language different from the document, use the `lang` attribute.

**Example:**
```html
<abbr title="Cascading Style Sheets">CSS</abbr> is used for styling.
```

---

### `<address>`

**Description:** Provides contact information for its nearest `<article>` or `<body>` ancestor.

**Categories:** Flow content, palpable content.

**Content model:** Flow content, but no heading content, sectioning content, `<header>`, `<footer>`, or another `<address>`.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Typically placed in a `<footer>` or at the end of a document.
- Not for arbitrary postal addresses unless they are contact information for the content.

**Example:**
```html
<address>
    Written by <a href="mailto:jane@example.com">Jane Doe</a>.<br>
    Visit us at: Box 564, Disneyland<br>
    USA
</address>
```

---

### `<area>`

**Description:** Defines a clickable area within an image map (used with `<map>`).

**Categories:** Flow content, phrasing content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLAreaElement`

**Usage notes:**
- Must be a child of a `<map>` element.
- The `shape` attribute defines the area shape: `rect`, `circle`, `poly`, or `default`.
- The `coords` attribute specifies coordinates.
- For accessibility, provide an `alt` attribute describing the link.

**Example:**
```html
<map name="shapes">
    <area shape="rect" coords="0,0,50,50" href="square.html" alt="Square">
    <area shape="circle" coords="100,100,25" href="circle.html" alt="Circle">
</map>
<img usemap="#shapes" src="map.png" alt="Shapes">
```

---

### `<article>`

**Description:** Represents a self‑contained composition that could be distributed independently (e.g., blog post, news story, comment).

**Categories:** Flow content, sectioning content, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Each `<article>` should be identified, typically with a heading (`<h1>`–`<h6>`).
- Can be nested; e.g., a blog post (`<article>`) may contain comments (each `<article>`).

**Example:**
```html
<article>
    <h2>Understanding HTML5</h2>
    <p>HTML5 introduces semantic elements...</p>
    <footer>Posted by John</footer>
</article>
```

---

### `<aside>`

**Description:** Represents content indirectly related to the main content (sidebars, pull quotes, advertising).

**Categories:** Flow content, sectioning content, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- If the `<aside>` is within an `<article>`, its content should be related to that article.
- For screen readers, use ARIA landmarks when needed, but `<aside>` is already a complementary landmark if it's not nested.

**Example:**
```html
<aside>
    <h3>Related Articles</h3>
    <ul>
        <li><a href="#">Article 1</a></li>
        <li><a href="#">Article 2</a></li>
    </ul>
</aside>
```

---

### `<audio>`

**Description:** Embeds sound content. May contain multiple `<source>` elements for different formats.

**Categories:** Flow content, phrasing content, embedded content, palpable content (if it has controls).

**Content model:** If the element has a `src` attribute: zero or more `<track>` elements, then transparent content (but no `<audio>` or `<video>`). Otherwise: zero or more `<source>` elements, then zero or more `<track>` elements, then transparent content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLAudioElement`

**Usage notes:**
- Use the `controls` attribute to show browser‑provided playback controls.
- Include multiple formats for broader compatibility.
- Provide text alternatives (e.g., transcripts) for accessibility.

**Example:**
```html
<audio controls>
    <source src="song.mp3" type="audio/mpeg">
    <source src="song.ogg" type="audio/ogg">
    Your browser does not support the audio element.
</audio>
```

---

### `<b>`

**Description:** Brings attention to text without conveying extra importance. Use for keywords, product names, etc.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Do not use `<b>` for styling bold text; use CSS `font-weight` for that.
- If the text has strong importance, use `<strong>`; if it's stressed, use `<em>`.

**Example:**
```html
<p>This product is <b>new</b> and improved.</p>
```

---

### `<base>`

**Description:** Specifies the base URL for all relative URLs in the document. There can be only one `<base>` element.

**Categories:** Metadata content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLBaseElement`

**Usage notes:**
- Must appear inside the `<head>`.
- The `href` attribute sets the base URL; `target` sets the default browsing context for links.

**Example:**
```html
<head>
    <base href="https://example.com/">
    <base target="_blank">
</head>
```

---

### `<bdi>`

**Description:** Isolates a span of text that might be formatted in a different direction from its surroundings (useful for user‑generated content).

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Useful when displaying text in an unknown direction, e.g., usernames that may contain Arabic or Hebrew.

**Example:**
```html
<p>User <bdi>أحمد</bdi> logged in.</p>
```

---

### `<bdo>`

**Description:** Overrides the current text direction.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLBdoElement`

**Usage notes:**
- The `dir` attribute is required: `ltr` or `rtl`.

**Example:**
```html
<p><bdo dir="rtl">This text will go right‑to‑left.</bdo></p>
```

---

### `<blockquote>`

**Description:** Represents a section quoted from another source.

**Categories:** Flow content, sectioning root, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLQuoteElement`

**Usage notes:**
- The `cite` attribute can reference the source URL.
- For inline quotes, use `<q>`.

**Example:**
```html
<blockquote cite="https://example.com/source">
    <p>The only way to do great work is to love what you do.</p>
    <footer>—Steve Jobs</footer>
</blockquote>
```

---

### `<body>`

**Description:** Represents the content of the HTML document. There can be only one `<body>`.

**Categories:** Sectioning root.

**Content model:** Flow content.

**Tag omission:** Start tag can be omitted if the first thing inside it is not a space character, comment, script, or style. End tag can be omitted if not immediately followed by a comment.

**DOM interface:** `HTMLBodyElement`

**Usage notes:**
- The `<body>` contains all the visible content.
- Event handlers like `onload` can be placed on the `<body>`.

**Example:**
```html
<body>
    <header>...</header>
    <main>...</main>
    <footer>...</footer>
</body>
```

---

### `<br>`

**Description:** Produces a line break in text (carriage‑return).

**Categories:** Flow content, phrasing content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLBRElement`

**Usage notes:**
- Use for line breaks within a paragraph or address; not for separating paragraphs (use `<p>`).
- For spacing, use CSS `margin` or `padding`.

**Example:**
```html
<p>First line<br>Second line</p>
```

---

### `<button>`

**Description:** Represents a clickable button.

**Categories:** Flow content, phrasing content, interactive content, palpable content, form‑associated element.

**Content model:** Phrasing content, but no interactive content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLButtonElement`

**Usage notes:**
- The `type` attribute can be `submit` (default, submits form), `reset` (resets form), or `button` (no default action).
- Always specify a `type` to avoid unexpected behavior inside forms.
- For accessibility, ensure the button has an accessible name (text content or `aria-label`).

**Example:**
```html
<button type="button" onclick="alert('Clicked!')">Click me</button>
<button type="submit">Submit Form</button>
```

---

### `<canvas>`

**Description:** Provides a drawable region for graphics via JavaScript (Canvas API).

**Categories:** Flow content, phrasing content, embedded content, palpable content.

**Content model:** Transparent, but typically contains fallback content for browsers that don't support canvas.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLCanvasElement`

**Usage notes:**
- Set `width` and `height` attributes; if not set, defaults to 300×150.
- Do not style the canvas with CSS `width`/`height` as it will scale the drawing (use attributes for canvas resolution).

**Example:**
```html
<canvas id="myCanvas" width="200" height="100">
    Your browser does not support the canvas element.
</canvas>
<script>
    const canvas = document.getElementById('myCanvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'green';
    ctx.fillRect(10, 10, 50, 50);
</script>
```

---

### `<caption>`

**Description:** Specifies the caption (or title) of a table.

**Categories:** None.

**Content model:** Flow content, but no table content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLTableCaptionElement`

**Usage notes:**
- Must be the first child of a `<table>`.
- Improves accessibility by providing a summary.

**Example:**
```html
<table>
    <caption>Monthly savings</caption>
    <tr><th>Month</th><th>Savings</th></tr>
    <tr><td>January</td><td>$100</td></tr>
</table>
```

---

### `<cite>`

**Description:** Represents the title of a creative work (book, article, song, etc.).

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Do not use for the name of the author; use `<figcaption>` or `<p>` with appropriate markup.

**Example:**
```html
<p>My favorite book is <cite>The Pragmatic Programmer</cite>.</p>
```

---

### `<code>`

**Description:** Displays a fragment of computer code.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Use with `<pre>` for multi‑line code blocks.
- For keyboard input, use `<kbd>`; for program output, use `<samp>`; for variables, use `<var>`.

**Example:**
```html
<p>Use <code>console.log()</code> for debugging.</p>
```

---

### `<col>`

**Description:** Defines a column within a `<colgroup>`.

**Categories:** None.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLTableColElement`

**Usage notes:**
- Used to apply styles to entire columns (e.g., background, width).
- The `span` attribute indicates how many columns the `<col>` applies to.

**Example:**
```html
<table>
    <colgroup>
        <col span="2" style="background-color: lightgray;">
        <col style="background-color: yellow;">
    </colgroup>
    <tr><th>ISBN</th><th>Title</th><th>Price</th></tr>
    <tr><td>123456</td><td>Book1</td><td>$10</td></tr>
</table>
```

---

### `<colgroup>`

**Description:** Groups a set of columns in a table.

**Categories:** None.

**Content model:** If the element has a `span` attribute: empty. Otherwise: zero or more `<col>` elements.

**Tag omission:** Start tag required, end tag may be omitted if followed by a `<col>` or `<tbody>`.

**DOM interface:** `HTMLTableColElement`

**Usage notes:**
- Use `span` to specify how many columns are grouped if no `<col>` children.

**Example:**
```html
<table>
    <colgroup span="2" style="background-color: lightgray;"></colgroup>
    <tr><th>Col1</th><th>Col2</th><th>Col3</th></tr>
</table>
```

---

### `<data>`

**Description:** Links a piece of content with a machine‑readable value.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLDataElement`

**Usage notes:**
- The `value` attribute contains the machine‑readable data.
- Useful for microformats or when you need to attach data to content.

**Example:**
```html
<ul>
    <li><data value="978-3-16-148410-0">The Pragmatic Programmer</data></li>
</ul>
```

---

### `<datalist>`

**Description:** Contains a set of `<option>` elements that represent predefined options for an `<input>`.

**Categories:** Flow content, phrasing content.

**Content model:** Either zero or more `<option>` elements, or zero or more `<script>`/`<template>` elements.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLDataListElement`

**Usage notes:**
- The `<input>` uses the `list` attribute to reference the `<datalist>` by its `id`.
- Users can either type or select from the list.

**Example:**
```html
<label for="browser">Choose a browser:</label>
<input list="browsers" id="browser" name="browser">
<datalist id="browsers">
    <option value="Chrome">
    <option value="Firefox">
    <option value="Safari">
</datalist>
```

---

### `<dd>`

**Description:** Provides the description, definition, or value for a term (`<dt>`) in a description list (`<dl>`).

**Categories:** None.

**Content model:** Flow content.

**Tag omission:** Start tag required, end tag may be omitted if followed by another `<dd>` or `<dt>`.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Must be inside a `<dl>` and follow a `<dt>`.

**Example:**
```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
    <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
</dl>
```

---

### `<del>`

**Description:** Represents text that has been deleted from a document.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Transparent.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLModElement`

**Usage notes:**
- Use `cite` to reference a reason for deletion and `datetime` to indicate when.
- Often paired with `<ins>` for edits.

**Example:**
```html
<p>My favorite color is <del datetime="2024-01-01">blue</del> <ins>green</ins>.</p>
```

---

### `<details>`

**Description:** Creates a disclosure widget that can be toggled open/closed.

**Categories:** Flow content, sectioning root, interactive content, palpable content.

**Content model:** One optional `<summary>` element followed by flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLDetailsElement`

**Usage notes:**
- Use the `open` attribute to show the content by default.
- The `<summary>` provides the visible heading; if omitted, the browser supplies a default ("Details").

**Example:**
```html
<details>
    <summary>More Information</summary>
    <p>Here are the details you requested.</p>
</details>
```

---

### `<dfn>`

**Description:** Represents the defining instance of a term.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content, but no `<dfn>` descendants.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- The term being defined is usually the nearest ancestor content.
- Optionally, the `title` attribute can contain the definition.

**Example:**
```html
<p><dfn>HTML</dfn> is the standard markup language for creating web pages.</p>
```

---

### `<dialog>`

**Description:** Represents a dialog box or other interactive component, such as a modal or alert.

**Categories:** Flow content, sectioning root, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLDialogElement`

**Usage notes:**
- Use the `open` attribute to show the dialog by default.
- JavaScript methods: `show()`, `showModal()`, `close()`.
- For modals, use `showModal()` and ensure focus management.

**Example:**
```html
<dialog id="myDialog">
    <p>Hello, I'm a dialog.</p>
    <button id="close">Close</button>
</dialog>
<button id="show">Show Dialog</button>
<script>
    const dialog = document.getElementById('myDialog');
    document.getElementById('show').onclick = () => dialog.showModal();
    document.getElementById('close').onclick = () => dialog.close();
</script>
```

---

### `<div>`

**Description:** A generic container with no semantic meaning.

**Categories:** Flow content, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLDivElement`

**Usage notes:**
- Use `<div>` only when no other semantic element is appropriate.
- Often used with CSS for styling or with JavaScript for behavior.

**Example:**
```html
<div class="wrapper">
    <p>Content goes here.</p>
</div>
```

---

### `<dl>`

**Description:** Represents a description list, consisting of groups of terms (`<dt>`) and descriptions (`<dd>`).

**Categories:** Flow content, palpable content.

**Content model:** Zero or more groups each consisting of one or more `<dt>` followed by one or more `<dd>`.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLDListElement`

**Usage notes:**
- Also used for metadata, key‑value pairs, or glossaries.

**Example:**
```html
<dl>
    <dt>Firefox</dt>
    <dd>A free, open‑source web browser.</dd>
    <dt>Chrome</dt>
    <dd>Google's web browser.</dd>
</dl>
```

---

### `<dt>`

**Description:** Represents a term (or name) in a description list.

**Categories:** None.

**Content model:** Flow content, but no `<header>`, `<footer>`, sectioning content, or heading content.

**Tag omission:** Start tag required, end tag may be omitted if followed by another `<dt>` or `<dd>`.

**DOM interface:** `HTMLElement`

**Example:** See `<dl>`.

---

### `<em>`

**Description:** Marks text that has stress emphasis. Browsers typically render it in italics.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Use `<em>` for emphasis that changes the meaning of a sentence.
- For stronger emphasis, use `<strong>`; for purely stylistic italics, use `<i>`.

**Example:**
```html
<p>You <em>must</em> read this book.</p>
```

---

### `<embed>`

**Description:** Embeds external content, such as a plugin or interactive content.

**Categories:** Flow content, phrasing content, embedded content, interactive content, palpable content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLEmbedElement`

**Usage notes:**
- Use `src`, `type`, `width`, `height` attributes.
- Fallback content can be provided by the browser's error handling or by using `<object>`.

**Example:**
```html
<embed src="movie.swf" type="application/x-shockwave-flash" width="400" height="300">
```

---

### `<fieldset>`

**Description:** Groups related controls and labels within a form.

**Categories:** Flow content, sectioning root, palpable content, form‑associated element.

**Content model:** Optional `<legend>` element, followed by flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLFieldSetElement`

**Usage notes:**
- Improves accessibility by grouping controls; screen readers announce the `<legend>` when entering the group.
- Can be disabled with the `disabled` attribute, which disables all child controls.

**Example:**
```html
<form>
    <fieldset>
        <legend>Contact Information</legend>
        <label for="name">Name:</label> <input type="text" id="name">
        <label for="email">Email:</label> <input type="email" id="email">
    </fieldset>
</form>
```

---

### `<figcaption>`

**Description:** Represents a caption or legend for a `<figure>` element.

**Categories:** None.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Must be the first or last child of the `<figure>`.

**Example:** See `<figure>`.

---

### `<figure>`

**Description:** Represents self‑contained content, often with a caption (`<figcaption>`).

**Categories:** Flow content, sectioning root, palpable content.

**Content model:** Either one `<figcaption>` followed by flow content, or flow content followed by one `<figcaption>`.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Used for images, code snippets, diagrams, illustrations, etc.
- The content should be referenced from the main text.

**Example:**
```html
<figure>
    <img src="chart.png" alt="Sales chart">
    <figcaption>Quarterly sales increase.</figcaption>
</figure>
```

---

### `<footer>`

**Description:** Represents a footer for its nearest sectioning content or sectioning root. Typically contains author info, copyright, links, etc.

**Categories:** Flow content, palpable content.

**Content model:** Flow content, but no `<footer>` or `<header>` descendants.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Can be used multiple times per page (e.g., site footer, article footer).
- Does not create a landmark when nested; use `aria-label` if needed.

**Example:**
```html
<footer>
    <p>&copy; 2024 My Site</p>
</footer>
```

---

### `<form>`

**Description:** Represents a document section containing interactive controls for submitting information.

**Categories:** Flow content, palpable content.

**Content model:** Flow content, but no `<form>` descendants.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLFormElement`

**Usage notes:**
- Use `action` to specify where to send the data; `method` for HTTP method (get/post).
- For accessibility, each control should have a `<label>`.
- The `novalidate` attribute disables built‑in validation.

**Example:**
```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <button type="submit">Submit</button>
</form>
```

---

### `<h1>` to `<h6>`

**Description:** Represent six levels of section headings, `<h1>` being the highest (most important) and `<h6>` the lowest.

**Categories:** Flow content, heading content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLHeadingElement`

**Usage notes:**
- Use headings to create a document outline; don't skip levels.
- Only one `<h1>` per page is recommended.
- Headings should be descriptive and concise.

**Example:**
```html
<h1>Main Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

---

### `<head>`

**Description:** Contains machine‑readable information (metadata) about the document, like title, scripts, style sheets.

**Categories:** None.

**Content model:** If the document is an HTML document: one `<title>` element, and zero or more metadata elements (`<base>`, `<link>`, `<meta>`, `<style>`, `<script>`, `<template>`).

**Tag omission:** Start tag may be omitted if the first thing inside is an element. End tag may be omitted if not immediately followed by a comment.

**DOM interface:** `HTMLHeadElement`

**Example:**
```html
<head>
    <title>My Page</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
</head>
```

---

### `<header>`

**Description:** Represents introductory content, typically a group of introductory or navigational aids.

**Categories:** Flow content, palpable content.

**Content model:** Flow content, but no `<footer>` or `<header>` descendants.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Can be used multiple times (site header, article header).
- Does not create a landmark when nested; use `aria-label` if needed.

**Example:**
```html
<header>
    <h1>Site Title</h1>
    <nav>...</nav>
</header>
```

---

### `<hgroup>`

**Description:** Represents a heading and associated secondary content, such as subheadings.

**Categories:** Flow content, heading content, palpable content.

**Content model:** Zero or more `<p>` elements, followed by one or more `<h1>`–`<h6>` elements, followed by zero or more `<p>` elements.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- The heading elements inside contribute to the document outline, but the `<hgroup>` itself does not.
- Useful for grouping a title with a subtitle.

**Example:**
```html
<hgroup>
    <h1>The Lord of the Rings</h1>
    <p>The Fellowship of the Ring</p>
</hgroup>
```

---

### `<hr>`

**Description:** Represents a thematic break between paragraph‑level elements (e.g., a shift of topic).

**Categories:** Flow content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLHRElement`

**Usage notes:**
- Not for decorative lines; use CSS borders for that.
- Conveys a break in content.

**Example:**
```html
<p>First section.</p>
<hr>
<p>Second section.</p>
```

---

### `<html>`

**Description:** Represents the root (top‑level element) of an HTML document.

**Categories:** None.

**Content model:** One `<head>` element followed by one `<body>` element.

**Tag omission:** Start tag may be omitted if the first thing inside is not a comment. End tag may be omitted if not immediately followed by a comment.

**DOM interface:** `HTMLHtmlElement`

**Usage notes:**
- Add the `lang` attribute to specify the primary language for accessibility.

**Example:**
```html
<!DOCTYPE html>
<html lang="en">
<head>...</head>
<body>...</body>
</html>
```

---

### `<i>`

**Description:** Represents a span of text in an alternate voice or mood, such as a technical term, foreign phrase, or thought.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Use `<i>` when the text is set off from normal prose but not for emphasis (`<em>`).
- Often rendered in italics by default.

**Example:**
```html
<p>The <i>Felis catus</i> is a domestic cat.</p>
```

---

### `<iframe>`

**Description:** Represents a nested browsing context, embedding another HTML page.

**Categories:** Flow content, phrasing content, embedded content, interactive content, palpable content.

**Content model:** Text (typically fallback content for browsers that don't support iframes).

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLIFrameElement`

**Usage notes:**
- Use `src` for the URL, `width` and `height` for dimensions.
- Security: use `sandbox` to restrict capabilities, and `allow` for permissions.
- For accessibility, provide a title describing the embedded content.

**Example:**
```html
<iframe src="https://example.com" title="Example page" width="400" height="300"></iframe>
```

---

### `<img>`

**Description:** Embeds an image.

**Categories:** Flow content, phrasing content, embedded content, palpable content (if the element has a `src` attribute).

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLImageElement`

**Usage notes:**
- Always include the `alt` attribute with descriptive text (or `alt=""` for decorative images).
- Use `width` and `height` to prevent layout shift.
- For responsive images, use `srcset` and `sizes`.

**Example:**
```html
<img src="photo.jpg" alt="A sunset over the mountains" width="800" height="600">
```

---

### `<input>`

**Description:** Creates an interactive control for web‑based forms to accept data from the user.

**Categories:** Flow content, phrasing content, interactive content, form‑associated element, palpable content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLInputElement`

**Usage notes:**
- The `type` attribute determines the control type: `text`, `password`, `email`, `number`, `checkbox`, `radio`, `file`, `submit`, etc.
- Always pair with a `<label>` for accessibility.
- Use `name` for form submission and `id` for labeling.
- For validation, use attributes like `required`, `pattern`, `min`, `max`.

**Example:**
```html
<label for="username">Username:</label>
<input type="text" id="username" name="username" required>
```

---

### `<ins>`

**Description:** Represents a range of text that has been added to a document.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Transparent.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLModElement`

**Usage notes:**
- Use `cite` and `datetime` similarly to `<del>`.

**Example:** See `<del>`.

---

### `<kbd>`

**Description:** Represents user input, typically keyboard input.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- For multi‑key input, nest `<kbd>` elements.

**Example:**
```html
<p>Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save.</p>
```

---

### `<label>`

**Description:** Represents a caption for an item in a user interface.

**Categories:** Flow content, phrasing content, interactive content, palpable content, form‑associated element.

**Content model:** Phrasing content, but no `<label>` descendants, and no interactive content except labeled control.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLLabelElement`

**Usage notes:**
- Use the `for` attribute to associate with a form control's `id`.
- Alternatively, wrap the control inside the `<label>` (implicit association).
- Clicking the label focuses/activates the associated control.

**Example:**
```html
<label for="email">Email:</label>
<input type="email" id="email" name="email">

<label>
    <input type="checkbox" name="subscribe"> Subscribe to newsletter
</label>
```

---

### `<legend>`

**Description:** Represents a caption for the content of its parent `<fieldset>`.

**Categories:** None.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLLegendElement`

**Example:** See `<fieldset>`.

---

### `<li>`

**Description:** Represents an item in a list (`<ul>`, `<ol>`, `<menu>`).

**Categories:** None.

**Content model:** Flow content.

**Tag omission:** End tag may be omitted if the list item is immediately followed by another `<li>` or if there is no more content in the parent element.

**DOM interface:** `HTMLLIElement`

**Usage notes:**
- In ordered lists, the `value` attribute can set the list number.
- In unordered lists, the `type` attribute (deprecated) was used for bullet style; use CSS instead.

**Example:** See `<ul>`, `<ol>`.

---

### `<link>`

**Description:** Specifies relationships between the current document and an external resource. Most commonly used to link to CSS.

**Categories:** Metadata content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLLinkElement`

**Usage notes:**
- For CSS: `<link rel="stylesheet" href="style.css">`
- For favicon: `<link rel="icon" href="favicon.ico">`
- Other rel values: `preload`, `prefetch`, `canonical`, etc.

**Example:**
```html
<link rel="stylesheet" href="main.css">
<link rel="icon" type="image/png" href="favicon.png">
```

---

### `<main>`

**Description:** Represents the dominant content of the `<body>` of a document. There must be only one `<main>` element per page.

**Categories:** Flow content, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Should not be nested within `<article>`, `<aside>`, `<footer>`, `<header>`, or `<nav>`.
- Helps screen reader users jump directly to the main content.

**Example:**
```html
<body>
    <header>...</header>
    <main>
        <h1>Main Content</h1>
        <p>...</p>
    </main>
    <footer>...</footer>
</body>
```

---

### `<map>`

**Description:** Used with `<area>` elements to define an image map (a clickable link region on an image).

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Any transparent content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLMapElement`

**Usage notes:**
- The `name` attribute gives the map a name to be referenced by the `<img>`'s `usemap` attribute.

**Example:** See `<area>`.

---

### `<mark>`

**Description:** Represents text that is marked or highlighted for reference purposes, due to its relevance in another context.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Typically rendered with a yellow background.
- Use to highlight search terms or quotes.

**Example:**
```html
<p>The word <mark>important</mark> is highlighted.</p>
```

---

### `<menu>`

**Description:** Represents a group of commands that the user can perform. In HTML, it is currently treated as a synonym for `<ul>` (list of items).

**Categories:** Flow content, palpable content.

**Content model:** Zero or more `<li>`, `<script>`, `<template>`.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLMenuElement`

**Usage notes:**
- Historically used for toolbars and context menus, but now largely synonymous with `<ul>`.
- For toolbar semantics, use ARIA roles.

**Example:**
```html
<menu>
    <li><button onclick="copy()">Copy</button></li>
    <li><button onclick="paste()">Paste</button></li>
</menu>
```

---

### `<meta>`

**Description:** Represents metadata that cannot be represented by other HTML elements.

**Categories:** Metadata content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLMetaElement`

**Usage notes:**
- Common uses: `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">`, `<meta name="description" content="...">`.
- Can also set HTTP headers with `http-equiv` (e.g., refresh, content‑security‑policy).

**Example:**
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="A free tutorial for web development">
```

---

### `<meter>`

**Description:** Represents a scalar measurement within a known range, or a fractional value. (e.g., disk usage, relevance of a query result).

**Categories:** Flow content, phrasing content, labelable, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLMeterElement`

**Usage notes:**
- Attributes: `value`, `min`, `max`, `low`, `high`, `optimum`.
- Do not use for progress (use `<progress>` for that).

**Example:**
```html
<label for="fuel">Fuel level:</label>
<meter id="fuel" min="0" max="100" low="20" high="80" optimum="75" value="50"></meter>
```

---

### `<nav>`

**Description:** Represents a section of a page whose purpose is to provide navigation links.

**Categories:** Flow content, sectioning content, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Not all links need to be in `<nav>`; only major navigation blocks.
- Use `aria-label` to distinguish multiple `<nav>` elements.

**Example:**
```html
<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
    </ul>
</nav>
```

---

### `<noscript>`

**Description:** Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is disabled.

**Categories:** Metadata content, flow content, phrasing content.

**Content model:** When scripting is disabled: in a `<head>`: any elements except `<noscript>`; in `<body>`: transparent. When scripting is enabled: text only.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Example:**
```html
<noscript>
    <p>JavaScript is disabled. Please enable it for a better experience.</p>
</noscript>
```

---

### `<object>`

**Description:** Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

**Categories:** Flow content, phrasing content, embedded content, palpable content (if the element has a `usemap` attribute or children).

**Content model:** Zero or more `<param>` elements, then transparent.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLObjectElement`

**Usage notes:**
- Use `data` for the resource URL, `type` for MIME type.
- Fallback content can be placed between tags.

**Example:**
```html
<object type="application/pdf" data="file.pdf" width="400" height="300">
    <p>PDF cannot be displayed. <a href="file.pdf">Download</a></p>
</object>
```

---

### `<ol>`

**Description:** Represents an ordered list of items, typically rendered as a numbered list.

**Categories:** Flow content, palpable content.

**Content model:** Zero or more `<li>` elements.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLOListElement`

**Usage notes:**
- Use `type` to set numbering style (1, A, a, I, i).
- Use `start` to set the starting number.
- Use `reversed` to count down.

**Example:**
```html
<ol>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

---

### `<optgroup>`

**Description:** Groups `<option>` elements within a `<select>` dropdown.

**Categories:** None.

**Content model:** Zero or more `<option>` elements.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLOptGroupElement`

**Usage notes:**
- The `label` attribute is required to provide a group name.
- Can be disabled with the `disabled` attribute.

**Example:**
```html
<select>
    <optgroup label="Fruits">
        <option>Apple</option>
        <option>Banana</option>
    </optgroup>
    <optgroup label="Vegetables">
        <option>Carrot</option>
        <option>Broccoli</option>
    </optgroup>
</select>
```

---

### `<option>`

**Description:** Represents an item in a `<select>`, `<optgroup>`, or `<datalist>`.

**Categories:** None.

**Content model:** Text.

**Tag omission:** End tag optional.

**DOM interface:** `HTMLOptionElement`

**Usage notes:**
- Use `value` for the value submitted; if omitted, the text content is used.
- `selected` makes it preselected.
- For `<datalist>`, `value` is the suggested value.

**Example:** See `<select>`.

---

### `<output>`

**Description:** Represents the result of a calculation or user action.

**Categories:** Flow content, phrasing content, labelable, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLOutputElement`

**Usage notes:**
- Often used with forms; the `for` attribute can reference the inputs that contribute to the result.
- The `name` attribute makes it submit as part of the form.

**Example:**
```html
<form oninput="result.value = parseInt(a.value) + parseInt(b.value)">
    <input type="number" id="a" value="0"> +
    <input type="number" id="b" value="0"> =
    <output name="result" for="a b">0</output>
</form>
```

---

### `<p>`

**Description:** Represents a paragraph.

**Categories:** Flow content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** End tag may be omitted if the paragraph is immediately followed by another `<p>` or if there is no more content.

**DOM interface:** `HTMLParagraphElement`

**Usage notes:**
- Paragraphs are block‑level elements.
- Use for blocks of text; avoid for spacing.

**Example:**
```html
<p>This is a paragraph.</p>
```

---

### `<param>`

**Description:** Defines parameters for an `<object>` element.

**Categories:** None.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLParamElement`

**Usage notes:**
- Use `name` and `value` attributes.

**Example:**
```html
<object data="movie.swf" type="application/x-shockwave-flash">
    <param name="autoplay" value="true">
</object>
```

---

### `<picture>`

**Description:** A container for multiple `<source>` elements and one `<img>` element, enabling responsive images.

**Categories:** Flow content, phrasing content, embedded content, palpable content.

**Content model:** Zero or more `<source>` elements, followed by one `<img>` element, optionally mixed with `<script>` or `<template>`.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLPictureElement`

**Usage notes:**
- The browser selects the most appropriate `<source>` based on media queries and image support.
- Always include a fallback `<img>`.

**Example:**
```html
<picture>
    <source media="(max-width: 600px)" srcset="small.jpg">
    <source media="(max-width: 1200px)" srcset="medium.jpg">
    <img src="large.jpg" alt="Description">
</picture>
```

---

### `<pre>`

**Description:** Represents preformatted text, typically rendered in a monospace font with whitespace preserved.

**Categories:** Flow content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLPreElement`

**Usage notes:**
- Ideal for code blocks, poetry, or any text where spacing matters.
- Often combined with `<code>`.

**Example:**
```html
<pre>
function hello() {
    console.log("Hello, world!");
}
</pre>
```

---

### `<progress>`

**Description:** Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

**Categories:** Flow content, phrasing content, labelable, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLProgressElement`

**Usage notes:**
- Use `value` for current progress and `max` for total.
- If `value` is omitted, the progress bar is indeterminate.

**Example:**
```html
<label for="progress">Downloading...</label>
<progress id="progress" value="30" max="100">30%</progress>
```

---

### `<q>`

**Description:** Represents an inline quotation.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLQuoteElement`

**Usage notes:**
- Browsers typically add quotation marks automatically.
- Use `cite` to reference the source.

**Example:**
```html
<p>He said, <q cite="https://example.com">I'll be back.</q></p>
```

---

### `<rp>`

**Description:** Used to provide fallback parentheses for browsers that do not support ruby annotations.

**Categories:** None.

**Content model:** Text.

**Tag omission:** Both start and end tags required.

**Example:** See `<ruby>`.

---

### `<rt>`

**Description:** Marks the ruby text component of a ruby annotation.

**Categories:** None.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**Example:** See `<ruby>`.

---

### `<ruby>`

**Description:** Represents a ruby annotation, used for showing pronunciation or translation of East Asian characters.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** See specification; generally includes `<rb>`, `<rt>`, `<rp>`.

**Tag omission:** Both start and end tags required.

**Example:**
```html
<ruby>
    漢 <rp>(</rp><rt>Kan</rt><rp>)</rp>
    字 <rp>(</rp><rt>ji</rt><rp>)</rp>
</ruby>
```

---

### `<s>`

**Description:** Represents content that is no longer accurate or relevant (strikethrough).

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Use `<s>` for content that is no longer relevant, not for editorial deletions (use `<del>`).

**Example:**
```html
<p><s>Was $99.99</s> Now $49.99!</p>
```

---

### `<samp>`

**Description:** Represents sample output from a computer program.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Example:**
```html
<p><samp>Error: File not found.</samp></p>
```

---

### `<script>`

**Description:** Embeds executable code or data; typically used to embed or refer to JavaScript.

**Categories:** Metadata content, flow content, phrasing content, script‑supporting.

**Content model:** Dynamic (depending on the `type` attribute).

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLScriptElement`

**Usage notes:**
- Use `src` to reference an external script.
- Use `async` or `defer` to control loading behavior.
- For inline scripts, the content is executed directly.

**Example:**
```html
<script src="app.js" defer></script>
<script>
    console.log('Hello');
</script>
```

---

### `<section>`

**Description:** Represents a generic standalone section of a document, which doesn't have a more specific semantic element. Sections should always have a heading.

**Categories:** Flow content, sectioning content, palpable content.

**Content model:** Flow content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Do not use `<section>` as a generic container; use `<div>` for that.
- The heading inside helps create the document outline.

**Example:**
```html
<section>
    <h2>Chapter 1</h2>
    <p>Content...</p>
</section>
```

---

### `<select>`

**Description:** Represents a control that provides a menu of options.

**Categories:** Flow content, phrasing content, interactive content, form‑associated element, palpable content.

**Content model:** Zero or more `<option>` or `<optgroup>` elements.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLSelectElement`

**Usage notes:**
- Use `multiple` to allow multiple selections.
- The `size` attribute sets the number of visible options.
- For accessibility, always provide a `<label>`.

**Example:**
```html
<label for="cars">Choose a car:</label>
<select id="cars" name="cars">
    <option value="volvo">Volvo</option>
    <option value="bmw">BMW</option>
</select>
```

---

### `<slot>`

**Description:** A placeholder inside a web component that you can fill with your own markup.

**Categories:** Flow content, phrasing content.

**Content model:** Transparent.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLSlotElement`

**Example:** (See Web Components documentation.)

---

### `<small>`

**Description:** Represents side comments or small print, like copyright and legal text.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Not for stylistic small text; use CSS `font-size` for that.

**Example:**
```html
<p><small>Copyright 2024</small></p>
```

---

### `<source>`

**Description:** Specifies multiple media resources for `<picture>`, `<audio>`, or `<video>` elements.

**Categories:** None.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLSourceElement`

**Usage notes:**
- For `<picture>`, use `media`, `srcset`, `sizes`.
- For `<audio>`/`<video>`, use `src` and `type`.

**Example:** See `<picture>`.

---

### `<span>`

**Description:** A generic inline container with no semantic meaning.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLSpanElement`

**Usage notes:**
- Use `<span>` when no other inline semantic element fits.
- Often used with CSS or JavaScript hooks.

**Example:**
```html
<p>This is <span class="highlight">highlighted</span> text.</p>
```

---

### `<strong>`

**Description:** Indicates strong importance, seriousness, or urgency. Browsers typically render it in bold.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Use `<strong>` for content that has strong importance.
- For purely stylistic bold, use CSS or `<b>`.

**Example:**
```html
<p><strong>Warning:</strong> Do not touch.</p>
```

---

### `<style>`

**Description:** Contains style information for a document, usually CSS.

**Categories:** Metadata content.

**Content model:** Text.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLStyleElement`

**Usage notes:**
- Typically placed in `<head>`.
- Use `media` attribute for conditional styles.
- For external stylesheets, use `<link>`.

**Example:**
```html
<style>
    body { background: #f0f0f0; }
</style>
```

---

### `<sub>`

**Description:** Represents subscript text.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Example:**
```html
<p>H<sub>2</sub>O</p>
```

---

### `<summary>`

**Description:** Specifies a summary, caption, or legend for a `<details>` element's disclosure box.

**Categories:** None.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Example:** See `<details>`.

---

### `<sup>`

**Description:** Represents superscript text.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Example:**
```html
<p>x<sup>2</sup> + y<sup>2</sup> = r<sup>2</sup></p>
```

---

### `<table>`

**Description:** Represents tabular data.

**Categories:** Flow content, palpable content.

**Content model:** In this order: optionally `<caption>`, optionally `<colgroup>`, optionally `<thead>`, optionally `<tbody>` or `<tfoot>`.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLTableElement`

**Usage notes:**
- Use `<caption>` for a title.
- Use `<thead>`, `<tbody>`, `<tfoot>` for structural grouping.
- Use `<th>` for headers, with `scope` attribute for accessibility.

**Example:**
```html
<table>
    <caption>Monthly Savings</caption>
    <thead>
        <tr><th>Month</th><th>Savings</th></tr>
    </thead>
    <tbody>
        <tr><td>January</td><td>$100</td></tr>
        <tr><td>February</td><td>$80</td></tr>
    </tbody>
</table>
```

---

### `<tbody>`

**Description:** Encapsulates a set of table rows (`<tr>`), indicating that they comprise the body of the table.

**Categories:** None.

**Content model:** Zero or more `<tr>` elements.

**Tag omission:** Start tag optional, end tag optional.

**DOM interface:** `HTMLTableSectionElement`

**Example:** See `<table>`.

---

### `<td>`

**Description:** Defines a cell of a table that contains data.

**Categories:** Sectioning root.

**Content model:** Flow content.

**Tag omission:** End tag may be omitted if followed by another `<td>` or `<th>`.

**DOM interface:** `HTMLTableDataCellElement`

**Usage notes:**
- Use `colspan` and `rowspan` to span multiple columns/rows.
- For header cells, use `<th>`.

**Example:** See `<table>`.

---

### `<template>`

**Description:** Holds HTML that is not to be rendered immediately but can be cloned and inserted later via JavaScript.

**Categories:** Metadata content, flow content, phrasing content, script‑supporting.

**Content model:** None (but it can contain any HTML).

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLTemplateElement`

**Usage notes:**
- The content is parsed but not rendered.
- Use with the `content` property in JavaScript to access the document fragment.

**Example:**
```html
<template id="card-template">
    <div class="card">
        <img src="" alt="">
        <h3></h3>
    </div>
</template>
<script>
    const template = document.getElementById('card-template');
    const clone = template.content.cloneNode(true);
    clone.querySelector('h3').textContent = 'Title';
    document.body.appendChild(clone);
</script>
```

---

### `<textarea>`

**Description:** Represents a multi‑line plain‑text editing control.

**Categories:** Flow content, phrasing content, interactive content, form‑associated element, palpable content.

**Content model:** Text.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLTextAreaElement`

**Usage notes:**
- Use `rows` and `cols` to set size.
- The initial value is the text content between the tags.
- For placeholder text, use the `placeholder` attribute.

**Example:**
```html
<label for="message">Message:</label>
<textarea id="message" name="message" rows="4" cols="50">
Default text.
</textarea>
```

---

### `<tfoot>`

**Description:** Defines a set of rows summarizing the columns of a table.

**Categories:** None.

**Content model:** Zero or more `<tr>` elements.

**Tag omission:** Start tag optional, end tag optional.

**DOM interface:** `HTMLTableSectionElement`

**Example:**
```html
<table>
    <thead>...</thead>
    <tbody>...</tbody>
    <tfoot>
        <tr><td colspan="2">Total: $180</td></tr>
    </tfoot>
</table>
```

---

### `<th>`

**Description:** Defines a cell as a header for a group of table cells.

**Categories:** None.

**Content model:** Flow content.

**Tag omission:** End tag may be omitted if followed by another `<th>` or `<td>`.

**DOM interface:** `HTMLTableHeaderCellElement`

**Usage notes:**
- Use `scope="col"` or `scope="row"` to associate with columns or rows.
- Use `colspan` and `rowspan` as needed.
- Screen readers use `<th>` to identify headers.

**Example:** See `<table>`.

---

### `<thead>`

**Description:** Encapsulates a set of table rows that are the column headers.

**Categories:** None.

**Content model:** Zero or more `<tr>` elements.

**Tag omission:** Start tag optional, end tag optional.

**DOM interface:** `HTMLTableSectionElement`

**Example:** See `<table>`.

---

### `<time>`

**Description:** Represents a specific period in time, either a date, time, or duration.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLTimeElement`

**Usage notes:**
- The `datetime` attribute provides a machine‑readable version.
- If omitted, the element's text must be a valid date/time string.

**Example:**
```html
<p>The concert is on <time datetime="2024-07-15T20:00">July 15 at 8 PM</time>.</p>
```

---

### `<title>`

**Description:** Defines the document's title that appears in the browser's title bar or tab.

**Categories:** Metadata content.

**Content model:** Text.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLTitleElement`

**Usage notes:**
- Required in every HTML document.
- Should be concise and descriptive.

**Example:**
```html
<title>My Awesome Website</title>
```

---

### `<tr>`

**Description:** Defines a row of cells in a table.

**Categories:** None.

**Content model:** Zero or more `<td>` or `<th>` elements.

**Tag omission:** End tag may be omitted if followed by another `<tr>`.

**DOM interface:** `HTMLTableRowElement`

**Example:** See `<table>`.

---

### `<track>`

**Description:** Used as a child of `<audio>` or `<video>` to specify timed text tracks (e.g., subtitles, captions).

**Categories:** None.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLTrackElement`

**Usage notes:**
- Attributes: `kind` (subtitles, captions, descriptions, chapters, metadata), `src`, `srclang`, `label`, `default`.

**Example:**
```html
<video controls>
    <source src="video.mp4" type="video/mp4">
    <track kind="subtitles" src="subtitles_en.vtt" srclang="en" label="English" default>
</video>
```

---

### `<u>`

**Description:** Represents a span of inline text that should be rendered in a way that indicates that it has a non‑textual annotation (e.g., misspelled word, proper name in Chinese).

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Default styling is underlined, but avoid using it purely for styling.
- Use `<u>` when the underlining has semantic meaning (e.g., red squiggly for spelling).

**Example:**
```html
<p>This word is <u class="spelling">misspelled</u>.</p>
```

---

### `<ul>`

**Description:** Represents an unordered list of items, typically rendered as a bulleted list.

**Categories:** Flow content, palpable content.

**Content model:** Zero or more `<li>` elements.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLUListElement`

**Example:**
```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
```

---

### `<var>`

**Description:** Represents the name of a variable in a mathematical expression or programming context.

**Categories:** Flow content, phrasing content, palpable content.

**Content model:** Phrasing content.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLElement`

**Example:**
```html
<p>The area of a circle is <var>π</var> <var>r</var><sup>2</sup>.</p>
```

---

### `<video>`

**Description:** Embeds a media player for video playback.

**Categories:** Flow content, phrasing content, embedded content, interactive content, palpable content.

**Content model:** If the element has a `src` attribute: zero or more `<track>` elements, then transparent. Otherwise: zero or more `<source>` elements, then zero or more `<track>` elements, then transparent.

**Tag omission:** Both start and end tags required.

**DOM interface:** `HTMLVideoElement`

**Usage notes:**
- Attributes: `src`, `controls`, `autoplay`, `loop`, `muted`, `poster`, `width`, `height`.
- Provide fallback content for unsupported browsers.

**Example:**
```html
<video controls width="640" height="360" poster="poster.jpg">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    <track kind="subtitles" src="subtitles_en.vtt" srclang="en">
    Your browser does not support the video tag.
</video>
```

---

### `<wbr>`

**Description:** Represents a word break opportunity—a position within text where the browser may optionally break a line.

**Categories:** Flow content, phrasing content.

**Content model:** Empty (void element).

**Tag omission:** Void element; no end tag.

**DOM interface:** `HTMLElement`

**Usage notes:**
- Useful for long words or URLs where you want to hint at possible break points.

**Example:**
```html
<p>This is a long word: super<wbr>cali<wbr>fragilistic<wbr>expialidocious.</p>
```

---

## Elements by Category

### Document Metadata
`<base>`, `<head>`, `<link>`, `<meta>`, `<style>`, `<title>`

### Content Sectioning
`<article>`, `<aside>`, `<footer>`, `<header>`, `<h1>`–`<h6>`, `<hgroup>`, `<main>`, `<nav>`, `<section>`

### Text Content
`<blockquote>`, `<dd>`, `<div>`, `<dl>`, `<dt>`, `<figcaption>`, `<figure>`, `<hr>`, `<li>`, `<menu>`, `<ol>`, `<p>`, `<pre>`, `<ul>`

### Inline Text Semantics
`<a>`, `<abbr>`, `<b>`, `<bdi>`, `<bdo>`, `<br>`, `<cite>`, `<code>`, `<data>`, `<dfn>`, `<em>`, `<i>`, `<kbd>`, `<mark>`, `<q>`, `<rp>`, `<rt>`, `<ruby>`, `<s>`, `<samp>`, `<small>`, `<span>`, `<strong>`, `<sub>`, `<sup>`, `<time>`, `<u>`, `<var>`, `<wbr>`

### Image and Multimedia
`<area>`, `<audio>`, `<img>`, `<map>`, `<picture>`, `<track>`, `<video>`

### Embedded Content
`<embed>`, `<iframe>`, `<object>`, `<param>`, `<source>`

### Scripting
`<canvas>`, `<noscript>`, `<script>`, `<template>`

### Demarcating Edits
`<del>`, `<ins>`

### Table Content
`<caption>`, `<col>`, `<colgroup>`, `<table>`, `<tbody>`, `<td>`, `<tfoot>`, `<th>`, `<thead>`, `<tr>`

### Forms
`<button>`, `<datalist>`, `<fieldset>`, `<form>`, `<input>`, `<label>`, `<legend>`, `<meter>`, `<optgroup>`, `<option>`, `<output>`, `<progress>`, `<select>`, `<textarea>`

### Interactive Elements
`<details>`, `<dialog>`, `<summary>`

### Web Components
`<slot>`, `<template>`

---

## Attributes Reference

### Common Attributes (Applicable to Many Elements)

- `class` – Assigns one or more class names (for CSS).
- `id` – Unique identifier for the element.
- `style` – Inline CSS styles.
- `title` – Advisory information (tooltip).
- `lang` – Language of the element's content.
- `dir` – Direction of text: `ltr`, `rtl`, `auto`.
- `tabindex` – Controls keyboard focus order.
- `hidden` – Boolean; hides the element.
- `data-*` – Custom data attributes for storing private information.

### Global Attributes

Global attributes can be used on **any** HTML element, though they may have no effect on some elements.

- `accesskey` – Keyboard shortcut to focus/activate an element.
- `autocapitalize` – Controls automatic capitalization (iOS/mobile).
- `autofocus` – Automatically focus the element on page load.
- `class` – Space‑separated list of CSS classes.
- `contenteditable` – Indicates if the element can be edited by the user.
- `data-*` – Custom data attributes.
- `dir` – Text direction.
- `draggable` – Whether the element can be dragged.
- `enterkeyhint` – Hints what action to present for the Enter key on virtual keyboards.
- `exportparts` – Exports parts of a shadow tree for styling.
- `hidden` – Indicates the element is not yet or no longer relevant.
- `id` – Unique identifier.
- `inert` – Indicates the element and its descendants are inert (not interactive, not selectable, hidden from assistive tech).
- `inputmode` – Hints at the type of data that might be entered (virtual keyboard).
- `is` – Allows you to specify that a standard HTML element should behave like a registered custom built‑in element.
- `itemid`, `itemprop`, `itemref`, `itemscope`, `itemtype` – Microdata attributes.
- `lang` – Language.
- `nonce` – Cryptographic nonce used in Content Security Policy.
- `part` – Names the part(s) of an element for styling via `::part()`.
- `popover` – Indicates the element is a popover element.
- `slot` – Assigns a slot in a shadow DOM.
- `spellcheck` – Indicates if spell checking should be enabled.
- `style` – Inline CSS.
- `tabindex` – Focus order.
- `title` – Advisory information.
- `translate` – Specifies whether the element's attribute values and text content should be translated.

### Event Handler Attributes

These attributes allow you to embed JavaScript code that runs when specific events occur. They are global and can be placed on any element (though some events are only relevant to certain elements).

**Form Events**
- `onblur` – Element loses focus.
- `onchange` – Element value changes (for `<input>`, `<select>`, `<textarea>`).
- `onfocus` – Element gains focus.
- `oninput` – Element receives user input.
- `oninvalid` – Element is invalid during validation.
- `onreset` – Form is reset.
- `onsearch` – User presses Enter in a search field.
- `onselect` – User selects text.
- `onsubmit` – Form is submitted.

**Keyboard Events**
- `onkeydown` – Key is pressed down.
- `onkeypress` – Key is pressed (deprecated).
- `onkeyup` – Key is released.

**Mouse Events**
- `onclick` – Mouse button is clicked.
- `ondblclick` – Mouse button is double‑clicked.
- `onmousedown` – Mouse button is pressed.
- `onmousemove` – Mouse moves over the element.
- `onmouseout` – Mouse leaves the element.
- `onmouseover` – Mouse enters the element.
- `onmouseup` – Mouse button is released.
- `onwheel` – Mouse wheel rotates.

**Drag Events**
- `ondrag` – Element is being dragged.
- `ondragend` – Drag operation ends.
- `ondragenter` – Dragged element enters a drop target.
- `ondragleave` – Dragged element leaves a drop target.
- `ondragover` – Dragged element is over a drop target.
- `ondragstart` – Drag operation starts.
- `ondrop` – Element is dropped.

**Clipboard Events**
- `oncopy` – Content is copied.
- `oncut` – Content is cut.
- `onpaste` – Content is pasted.

**Media Events** (for `<audio>`, `<video>`)
- `onabort` – Loading is aborted.
- `oncanplay` – Browser can start playback (may need to buffer).
- `oncanplaythrough` – Browser estimates it can play through without stopping.
- `oncuechange` – Text track cue changes.
- `ondurationchange` – Duration changes.
- `onemptied` – Media becomes empty.
- `onended` – Playback ends.
- `onerror` – Error occurs.
- `onloadeddata` – Media data is loaded.
- `onloadedmetadata` – Metadata is loaded.
- `onloadstart` – Loading starts.
- `onpause` – Playback is paused.
- `onplay` – Playback starts.
- `onplaying` – Playback is ready after pause/buffering.
- `onprogress` – Loading is in progress.
- `onratechange` – Playback rate changes.
- `onseeked` – Seek operation completes.
- `onseeking` – Seek operation begins.
- `onstalled` – Loading is stalled.
- `onsuspend` – Loading is suspended.
- `ontimeupdate` – Current playback position changes.
- `onvolumechange` – Volume changes.
- `onwaiting` – Playback stops due to buffering.

**Window/Document Events**
- `onafterprint` – Document is printed.
- `onbeforeprint` – Document is about to be printed.
- `onbeforeunload` – Document is about to be unloaded.
- `onerror` – Error occurs (on `window`).
- `onhashchange` – Fragment identifier changes.
- `onload` – Document or resource has loaded.
- `onmessage` – Message is received (WebSocket, Web Worker).
- `onoffline` – Browser goes offline.
- `ononline` – Browser goes online.
- `onpagehide` – Page is hidden.
- `onpageshow` – Page is shown.
- `onpopstate` – History entry changes.
- `onresize` – Document view is resized.
- `onstorage` – Storage area changes.
- `onunload` – Document is unloaded.

**Animation Events**
- `onanimationend` – CSS animation ends.
- `onanimationiteration` – CSS animation repeats.
- `onanimationstart` – CSS animation starts.

**Transition Events**
- `ontransitionend` – CSS transition ends.

**Miscellaneous**
- `ontoggle` – `<details>` element is toggled.
- `onscroll` – Element scrollbar is scrolled.
- `onwheel` – Mouse wheel rotates.

---

## Global Attributes

(Already covered above; see "Global Attributes" under Attributes Reference.)

---

## Event Attributes

(Already covered above; see "Event Handler Attributes" under Attributes Reference.)

---

This appendix provides a comprehensive reference to HTML elements and attributes. For the latest specifications and more detailed information, consult the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML) or the [WHATWG HTML Living Standard](https://html.spec.whatwg.org/).