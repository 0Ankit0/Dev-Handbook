# Appendix B: CSS Property Reference

---

## Introduction

Cascading Style Sheets (CSS) is the language used to describe the presentation of a document written in HTML. This appendix provides a comprehensive reference to CSS properties, values, selectors, at‑rules, and functions. It is organized to help you quickly find the property or concept you need, with descriptions, syntax, and examples.

The reference is divided into several sections:

- **Properties by Category** – Grouped by function (layout, typography, backgrounds, etc.).
- **Values and Units** – Lengths, colors, angles, time, etc.
- **Selectors Reference** – Complete list of selectors with examples.
- **Pseudo‑Classes Reference** – Dynamic, structural, form, and other pseudo‑classes.
- **Pseudo‑Elements Reference** – `::before`, `::after`, `::first-line`, etc.
- **At‑Rules Reference** – `@media`, `@keyframes`, `@font-face`, and others.
- **Functions Reference** – `calc()`, `var()`, `rgb()`, `url()`, and more.

This reference assumes a working knowledge of CSS; for in‑depth explanations, refer to the relevant chapters in the main handbook.

---

## Properties by Category

### Box Model

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `width` | Sets the width of an element. | `<length>`, `<percentage>`, `auto`, `max-content`, `min-content`, `fit-content` | `width: 300px;` |
| `height` | Sets the height of an element. | Same as `width` | `height: 50%;` |
| `min-width` | Minimum width. | `<length>`, `<percentage>`, `max-content`, etc. | `min-width: 200px;` |
| `max-width` | Maximum width. | Same | `max-width: 100%;` |
| `min-height` | Minimum height. | Same | `min-height: 100vh;` |
| `max-height` | Maximum height. | Same | `max-height: 500px;` |
| `padding` | Shorthand for padding on all sides. | `[ <length> \| <percentage> ]{1,4}` | `padding: 10px 20px;` |
| `padding-top` | Top padding. | `<length>`, `<percentage>` | `padding-top: 1em;` |
| `padding-right` | Right padding. | Same | `padding-right: 5%;` |
| `padding-bottom` | Bottom padding. | Same | – |
| `padding-left` | Left padding. | Same | – |
| `margin` | Shorthand for margin on all sides. | `[ <length> \| <percentage> \| auto ]{1,4}` | `margin: 0 auto;` |
| `margin-top` | Top margin. | Same | – |
| `margin-right` | Right margin. | Same | – |
| `margin-bottom` | Bottom margin. | Same | – |
| `margin-left` | Left margin. | Same | – |
| `border` | Shorthand for border width, style, and color. | `<line-width> \|\| <line-style> \|\| <color>` | `border: 1px solid black;` |
| `border-top` | Top border. | Same | – |
| `border-right` | Right border. | Same | – |
| `border-bottom` | Bottom border. | Same | – |
| `border-left` | Left border. | Same | – |
| `border-width` | Shorthand for border widths. | `<line-width>{1,4}` | `border-width: 2px 1px;` |
| `border-style` | Shorthand for border styles. | `<line-style>{1,4}` | `border-style: dashed solid;` |
| `border-color` | Shorthand for border colors. | `<color>{1,4}` | `border-color: red blue;` |
| `border-radius` | Rounds the corners. | `[ <length> \| <percentage> ]{1,4} [ / [ <length> \| <percentage> ]{1,4} ]?` | `border-radius: 10px;` `border-radius: 10px 20px / 20px;` |
| `border-collapse` | Collapses table borders. | `collapse \| separate` | `border-collapse: collapse;` |
| `border-spacing` | Space between table cells. | `<length> <length>?` | `border-spacing: 2px 5px;` |
| `box-sizing` | How the total width/height is calculated. | `content-box \| border-box` | `box-sizing: border-box;` |

### Layout & Positioning

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `display` | Defines the display type of an element. | `block`, `inline`, `inline-block`, `flex`, `grid`, `inline-flex`, `inline-grid`, `table`, `table-row`, `table-cell`, `none`, `contents`, `list-item`, etc. | `display: flex;` |
| `position` | Positioning method. | `static`, `relative`, `absolute`, `fixed`, `sticky` | `position: absolute;` |
| `top` | Offset from top. | `<length>`, `<percentage>`, `auto` | `top: 10px;` |
| `right` | Offset from right. | Same | – |
| `bottom` | Offset from bottom. | Same | – |
| `left` | Offset from left. | Same | – |
| `z-index` | Stacking order. | `auto`, `<integer>` | `z-index: 10;` |
| `float` | Floats an element. | `left`, `right`, `none` | `float: left;` |
| `clear` | Clears floated elements. | `none`, `left`, `right`, `both` | `clear: both;` |
| `overflow` | Controls content overflow. | `visible`, `hidden`, `scroll`, `auto` | `overflow: auto;` |
| `overflow-x` | Horizontal overflow. | Same | – |
| `overflow-y` | Vertical overflow. | Same | – |
| `visibility` | Visibility of an element. | `visible`, `hidden`, `collapse` | `visibility: hidden;` |
| `flex` | Shorthand for `flex-grow`, `flex-shrink`, `flex-basis`. | `none \| [ <flex-grow> <flex-shrink>? \|\| <flex-basis> ]` | `flex: 1 0 auto;` |
| `flex-grow` | Growth factor. | `<number>` | `flex-grow: 2;` |
| `flex-shrink` | Shrink factor. | `<number>` | `flex-shrink: 1;` |
| `flex-basis` | Initial main size. | `auto`, `<length>`, `<percentage>` | `flex-basis: 200px;` |
| `flex-direction` | Direction of flex items. | `row`, `row-reverse`, `column`, `column-reverse` | `flex-direction: column;` |
| `flex-wrap` | Wrap flex items. | `nowrap`, `wrap`, `wrap-reverse` | `flex-wrap: wrap;` |
| `justify-content` | Alignment on main axis. | `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly` | `justify-content: center;` |
| `align-items` | Alignment on cross axis. | `stretch`, `flex-start`, `flex-end`, `center`, `baseline` | `align-items: stretch;` |
| `align-self` | Alignment for individual item. | `auto`, `stretch`, `flex-start`, `flex-end`, `center`, `baseline` | `align-self: flex-end;` |
| `align-content` | Alignment of lines in multi‑line flex container. | `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `stretch` | `align-content: space-between;` |
| `gap`, `row-gap`, `column-gap` | Gutters between flex/grid items. | `<length>`, `<percentage>` | `gap: 20px;` |
| `grid` | Shorthand for grid container properties. | – | (See grid reference) |
| `grid-template-columns` | Defines columns in grid. | `none`, `<track-list>` | `grid-template-columns: 1fr 2fr;` |
| `grid-template-rows` | Defines rows in grid. | Same | `grid-template-rows: auto 100px;` |
| `grid-template-areas` | Defines named grid areas. | `none`, `<string>+` | `grid-template-areas: "header header" "main sidebar";` |
| `grid-column-start` | Start column line. | `auto`, `<custom-ident>`, `<integer>`, `span <integer>` | `grid-column-start: 2;` |
| `grid-column-end` | End column line. | Same | – |
| `grid-row-start` | Start row line. | Same | – |
| `grid-row-end` | End row line. | Same | – |
| `grid-column` | Shorthand for `grid-column-start` / `grid-column-end`. | `<grid-line> [ / <grid-line> ]?` | `grid-column: 1 / 3;` |
| `grid-row` | Shorthand for `grid-row-start` / `grid-row-end`. | Same | `grid-row: 2 / 4;` |
| `grid-area` | Assigns a name or grid lines. | `<name> \| <row-start> / <column-start> / <row-end> / <column-end>` | `grid-area: header;` |
| `justify-items` | Aligns items inside their grid cells (inline axis). | `start`, `end`, `center`, `stretch` | `justify-items: center;` |
| `align-items` | Aligns items inside their grid cells (block axis). | Same | – |
| `justify-self` | Aligns a single item. | Same | – |
| `align-self` | Aligns a single item. | Same | – |
| `place-items` | Shorthand for `align-items` `justify-items`. | `<align-items> <justify-items>?` | `place-items: center start;` |
| `place-self` | Shorthand for `align-self` `justify-self`. | `<align-self> <justify-self>?` | `place-self: center;` |
| `place-content` | Shorthand for `align-content` `justify-content`. | `<align-content> <justify-content>?` | `place-content: space-between center;` |

### Typography & Text

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `font` | Shorthand for font properties. | `[ [ <font-style> \|\| <font-variant> \|\| <font-weight> ]? <font-size> [ / <line-height> ]? <font-family> ]` | `font: 16px/1.5 Arial, sans-serif;` |
| `font-family` | Specifies the typeface. | `<family-name>`, `<generic-name>` | `font-family: "Helvetica", sans-serif;` |
| `font-size` | Sets the size of the font. | `<absolute-size>`, `<relative-size>`, `<length>`, `<percentage>` | `font-size: 1.2rem;` |
| `font-weight` | Sets the weight (boldness). | `normal`, `bold`, `bolder`, `lighter`, `<number> (100-900)` | `font-weight: 700;` |
| `font-style` | Sets the style (normal, italic, oblique). | `normal`, `italic`, `oblique` | `font-style: italic;` |
| `font-variant` | Controls small‑caps, etc. | `normal`, `small-caps`, etc. | `font-variant: small-caps;` |
| `line-height` | Sets the line height. | `normal`, `<number>`, `<length>`, `<percentage>` | `line-height: 1.5;` |
| `text-align` | Horizontal alignment. | `left`, `right`, `center`, `justify` | `text-align: center;` |
| `text-decoration` | Shorthand for decoration. | `none`, `underline`, `overline`, `line-through`, `blink` (deprecated) | `text-decoration: underline wavy red;` |
| `text-decoration-line` | Type of line. | `none`, `underline`, `overline`, `line-through` | – |
| `text-decoration-color` | Color of decoration. | `<color>` | – |
| `text-decoration-style` | Style of line. | `solid`, `double`, `dotted`, `dashed`, `wavy` | – |
| `text-decoration-thickness` | Thickness of line. | `auto`, `<length>`, `<percentage>` | – |
| `text-transform` | Changes capitalization. | `none`, `capitalize`, `uppercase`, `lowercase` | `text-transform: uppercase;` |
| `text-indent` | Indents the first line. | `<length>`, `<percentage>` | `text-indent: 2em;` |
| `letter-spacing` | Space between characters. | `normal`, `<length>` | `letter-spacing: 0.1em;` |
| `word-spacing` | Space between words. | `normal`, `<length>` | `word-spacing: 0.2em;` |
| `white-space` | Handles whitespace inside an element. | `normal`, `nowrap`, `pre`, `pre-wrap`, `pre-line`, `break-spaces` | `white-space: nowrap;` |
| `word-break` | Line breaking rules for non‑CJK scripts. | `normal`, `break-all`, `keep-all` | `word-break: break-all;` |
| `overflow-wrap` (formerly `word-wrap`) | Wraps long words. | `normal`, `break-word` | `overflow-wrap: break-word;` |
| `text-shadow` | Adds shadow to text. | `none \| <shadow>#` | `text-shadow: 2px 2px 4px rgba(0,0,0,0.5);` |
| `direction` | Text direction. | `ltr`, `rtl` | `direction: rtl;` |
| `unicode-bidi` | Handles bidirectional text. | `normal`, `embed`, `bidi-override`, `isolate`, `isolate-override`, `plaintext` | – |

### Colors & Backgrounds

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `color` | Sets the text color. | `<color>` | `color: #333;` |
| `background` | Shorthand for all background properties. | `[ <bg-layer> , ]* <final-bg-layer>` | `background: #fff url("bg.png") no-repeat center;` |
| `background-color` | Background color. | `<color>` | `background-color: rgba(255,0,0,0.5);` |
| `background-image` | Background image(s). | `none \| <image>#` | `background-image: url("image.jpg");` |
| `background-repeat` | How the image repeats. | `repeat-x`, `repeat-y`, `repeat`, `space`, `round`, `no-repeat` | `background-repeat: no-repeat;` |
| `background-position` | Position of the image. | `<position>` | `background-position: top right;` |
| `background-size` | Size of the image. | `auto`, `cover`, `contain`, `<length>`, `<percentage>` | `background-size: cover;` |
| `background-attachment` | Whether the image scrolls with the page. | `scroll`, `fixed`, `local` | `background-attachment: fixed;` |
| `background-clip` | How far the background extends. | `border-box`, `padding-box`, `content-box`, `text` | `background-clip: text;` |
| `background-origin` | Positioning area of the background. | `border-box`, `padding-box`, `content-box` | – |
| `opacity` | Transparency of an element. | `<number>` (0–1) | `opacity: 0.5;` |

### Borders & Outlines

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `border` | Shorthand (see Box Model). | – | – |
| `border-image` | Uses an image as border. | `<border-image-source> \|\| <border-image-slice> [ / <border-image-width> \| / <border-image-width>? / <border-image-outset> ]? \|\| <border-image-repeat>` | `border-image: url("border.png") 30 round;` |
| `border-image-source` | Source image. | `none`, `<image>` | – |
| `border-image-slice` | Slice the image. | `<number> \| <percentage>]{1,4} && fill?` | – |
| `border-image-width` | Width of border image. | `<length> \| <percentage> \| <number> \| auto]{1,4}` | – |
| `border-image-outset` | Amount by which border image area extends beyond the border box. | `<length> \| <number>]{1,4}` | – |
| `border-image-repeat` | How the image repeats. | `stretch`, `repeat`, `round`, `space` | – |
| `outline` | Shorthand for outline around an element (does not affect layout). | `<outline-width> \|\| <outline-style> \|\| <outline-color>` | `outline: 2px dashed red;` |
| `outline-width` | Width of outline. | `<line-width>` | – |
| `outline-style` | Style of outline. | `auto`, `<line-style>` | – |
| `outline-color` | Color of outline. | `<color>` | – |
| `outline-offset` | Space between outline and element edge. | `<length>` | `outline-offset: 5px;` |

### Lists

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `list-style` | Shorthand for list style properties. | `<list-style-type> \|\| <list-style-position> \|\| <list-style-image>` | `list-style: square inside;` |
| `list-style-type` | Marker type. | `disc`, `circle`, `square`, `decimal`, `lower-roman`, `upper-roman`, `lower-alpha`, `upper-alpha`, `none`, etc. | `list-style-type: upper-roman;` |
| `list-style-position` | Position of marker. | `inside`, `outside` | `list-style-position: inside;` |
| `list-style-image` | Image as marker. | `none`, `<url>` | `list-style-image: url("bullet.png");` |

### Tables

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `border-collapse` | (See Box Model) | – | – |
| `border-spacing` | (See Box Model) | – | – |
| `caption-side` | Position of table caption. | `top`, `bottom` | `caption-side: bottom;` |
| `empty-cells` | Show/hide borders on empty cells. | `show`, `hide` | `empty-cells: hide;` |
| `table-layout` | Algorithm for table layout. | `auto`, `fixed` | `table-layout: fixed;` |
| `vertical-align` | Vertical alignment of inline or table‑cell content. | `baseline`, `sub`, `super`, `text-top`, `text-bottom`, `middle`, `top`, `bottom`, `<percentage>`, `<length>` | `vertical-align: middle;` (commonly used in table cells) |

### Transitions & Animations

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `transition` | Shorthand for transition effects. | `<single-transition>#` | `transition: all 0.3s ease-in-out;` |
| `transition-property` | Names of CSS properties to transition. | `none`, `all`, `<custom-ident>#` | `transition-property: opacity, transform;` |
| `transition-duration` | Duration of the transition. | `<time>#` | `transition-duration: 0.5s;` |
| `transition-timing-function` | Timing function (easing). | `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out`, `step-start`, `step-end`, `steps()`, `cubic-bezier()` | `transition-timing-function: cubic-bezier(0.1, 0.7, 1.0, 0.1);` |
| `transition-delay` | Delay before transition starts. | `<time>#` | `transition-delay: 0.1s;` |
| `animation` | Shorthand for animation properties. | `<single-animation>#` | `animation: slidein 3s ease-in 1s infinite alternate;` |
| `animation-name` | Name of `@keyframes` rule. | `none`, `<keyframes-name>` | `animation-name: slidein;` |
| `animation-duration` | Duration of one cycle. | `<time>#` | `animation-duration: 2s;` |
| `animation-timing-function` | Timing function. | Same as `transition-timing-function` | – |
| `animation-delay` | Delay before animation starts. | `<time>#` | – |
| `animation-iteration-count` | Number of times the animation repeats. | `infinite`, `<number>` | `animation-iteration-count: 3;` |
| `animation-direction` | Direction of animation. | `normal`, `reverse`, `alternate`, `alternate-reverse` | – |
| `animation-fill-mode` | Styles applied before/after animation. | `none`, `forwards`, `backwards`, `both` | – |
| `animation-play-state` | Pause or play the animation. | `running`, `paused` | – |

### Transforms

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `transform` | Applies a 2D or 3D transformation. | `none`, `<transform-function>+` | `transform: rotate(45deg) scale(1.2);` |
| `transform-origin` | Origin of transformation. | `[ <length-percentage> \| left \| center \| right \| top \| bottom ]{1,3}` | `transform-origin: top left;` |
| `transform-style` | Preserves 3D transformations. | `flat`, `preserve-3d` | `transform-style: preserve-3d;` |
| `perspective` | Sets perspective for 3D transformed children. | `none`, `<length>` | `perspective: 1000px;` |
| `perspective-origin` | Origin of perspective. | `<position>` | `perspective-origin: center;` |
| `backface-visibility` | Shows/hides the back face of an element. | `visible`, `hidden` | `backface-visibility: hidden;` |

### Flexbox & Grid (already covered under Layout)

### Generated Content & Counters

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `content` | Inserts generated content (used with `::before`/`::after`). | `normal`, `none`, `<string>`, `<url>`, `<counter>`, `attr()`, `open-quote`, `close-quote`, etc. | `content: "Note: ";` |
| `quotes` | Specifies quotation marks. | `none`, `[ <string> <string> ]+` | `quotes: "“" "”" "‘" "’";` |
| `counter-reset` | Resets or creates counters. | `[ <custom-ident> <integer>? ]+ \| none` | `counter-reset: section 0;` |
| `counter-increment` | Increments counters. | `[ <custom-ident> <integer>? ]+ \| none` | `counter-increment: section;` |
| `counter-set` | Sets counters to a specific value. | `[ <custom-ident> <integer>? ]+ \| none` | – |

### Miscellaneous

| Property | Description | Values | Example |
|----------|-------------|--------|---------|
| `cursor` | Mouse cursor appearance. | `auto`, `default`, `pointer`, `wait`, `text`, `move`, `help`, `not-allowed`, `grab`, `url()`, etc. | `cursor: pointer;` |
| `pointer-events` | Whether the element responds to pointer events. | `auto`, `none`, `visiblePainted`, etc. | `pointer-events: none;` |
| `user-select` | Controls text selection. | `auto`, `text`, `none`, `contain`, `all` | `user-select: none;` |
| `resize` | Whether an element is resizable by the user. | `none`, `both`, `horizontal`, `vertical` | `resize: both;` |
| `object-fit` | How an `<img>` or `<video>` fits its container. | `fill`, `contain`, `cover`, `none`, `scale-down` | `object-fit: cover;` |
| `object-position` | Position of replaced content. | `<position>` | `object-position: top left;` |
| `filter` | Applies graphical effects (blur, grayscale, etc.). | `none`, `<filter-function>+` | `filter: blur(5px) grayscale(50%);` |
| `backdrop-filter` | Applies filter to area behind an element. | Same as `filter` | `backdrop-filter: blur(10px);` |
| `clip-path` | Clips an element to a basic shape or SVG path. | `<clip-source>`, `<basic-shape>`, `none` | `clip-path: circle(50%);` |
| `mask` | Shorthand for masking. | – | – |
| `isolation` | Creates a new stacking context. | `auto`, `isolate` | `isolation: isolate;` |
| `mix-blend-mode` | How an element blends with its background. | `<blend-mode>` | `mix-blend-mode: multiply;` |
| `contain` | Limits the scope of layout, paint, and style. | `none`, `strict`, `content`, `size`, `layout`, `style`, `paint` | `contain: layout paint;` |
| `will-change` | Hints to the browser about expected changes. | `auto`, `<animateable-feature>#` | `will-change: transform, opacity;` |
| `aspect-ratio` | Preferred aspect ratio. | `auto`, `<ratio>` | `aspect-ratio: 16 / 9;` |
| `scroll-behavior` | Smooth scrolling behavior. | `auto`, `smooth` | `scroll-behavior: smooth;` |
| `scroll-snap-type` | Defines snap container and axis. | `none`, `[ x \| y \| block \| inline \| both ] [ mandatory \| proximity ]?` | `scroll-snap-type: y mandatory;` |
| `scroll-snap-align` | Snap alignment of child elements. | `none`, `start`, `end`, `center` | `scroll-snap-align: start;` |

---

## Values and Units

### Length Units

**Absolute lengths** (physical units):

| Unit | Name | Equivalent |
|------|------|------------|
| `cm` | centimeters | 1cm = 96px/2.54 |
| `mm` | millimeters | 1mm = 1/10th of 1cm |
| `in` | inches | 1in = 2.54cm = 96px |
| `px` | pixels | 1px = 1/96th of 1in |
| `pt` | points | 1pt = 1/72 of 1in |
| `pc` | picas | 1pc = 12pt |

**Relative lengths**:

| Unit | Relative to |
|------|-------------|
| `em` | font size of the element |
| `rem` | font size of the root element (`<html>`) |
| `vw` | 1% of viewport width |
| `vh` | 1% of viewport height |
| `vmin` | 1% of the smaller dimension of viewport |
| `vmax` | 1% of the larger dimension of viewport |
| `%` | percentage of parent element's value |
| `ex` | x‑height of the element's font |
| `ch` | width of the "0" (zero) character |
| `lh` | line height of the element |
| `rlh` | line height of the root element |

### Color Values

| Notation | Example | Description |
|----------|---------|-------------|
| Named colors | `red`, `blue`, `transparent` | Predefined color names (around 140) |
| Hexadecimal | `#ff0000`, `#f00` | RGB in hex; shorthand for 3 or 6 digits |
| RGB / RGBA | `rgb(255,0,0)`, `rgba(255,0,0,0.5)` | Red, green, blue (0‑255) and alpha (0‑1) |
| HSL / HSLA | `hsl(0,100%,50%)`, `hsla(0,100%,50%,0.5)` | Hue (0‑360), saturation (%), lightness (%), alpha |
| `currentColor` | `color: currentColor;` | The computed value of the `color` property |

### Other Values

| Type | Description | Examples |
|------|-------------|----------|
| `<integer>` | Whole numbers | `5`, `-3` |
| `<number>` | Real numbers | `3.14`, `-2.5` |
| `<percentage>` | Percentage | `50%` |
| `<time>` | Time in seconds or milliseconds | `2s`, `500ms` |
| `<angle>` | Angle in degrees, gradians, radians, turns | `45deg`, `1.5rad`, `0.25turn` |
| `<frequency>` | Frequency (rare) | `100Hz` |
| `<resolution>` | Resolution (for media queries) | `300dpi` |
| `<string>` | Quoted text | `"Hello"` |
| `<url>` | URL reference | `url("image.png")` |
| `<custom-ident>` | User‑defined identifier (e.g., animation name) | `slidein` |

---

## Selectors Reference

| Selector | Pattern | Description | Example |
|----------|---------|-------------|---------|
| Universal | `*` | Selects all elements. | `* { margin: 0; }` |
| Type | `element` | Selects elements by tag name. | `p { color: red; }` |
| Class | `.classname` | Selects elements by class. | `.highlight { background: yellow; }` |
| ID | `#idname` | Selects element by ID. | `#header { font-size: 2em; }` |
| Attribute | `[attr]` | Elements with attribute `attr`. | `[disabled] { opacity: 0.5; }` |
| Attribute equals | `[attr="value"]` | Exact attribute value. | `[type="checkbox"] { margin: 0; }` |
| Attribute begins | `[attr^="value"]` | Attribute value starts with `value`. | `a[href^="https"] { color: green; }` |
| Attribute ends | `[attr$="value"]` | Attribute value ends with `value`. | `a[href$=".pdf"] { font-weight: bold; }` |
| Attribute contains | `[attr*="value"]` | Attribute value contains `value`. | `a[href*="example"] { }` |
| Attribute word | `[attr~="value"]` | Attribute value is a whitespace‑separated list containing `value`. | `[data-tags~="featured"] { }` |
| Attribute hyphen | `[attr\|="value"]` | Attribute value equals `value` or starts with `value-`. | `[lang\|="en"] { }` |
| Descendant | `A B` | Selects B inside A (any depth). | `div p { }` |
| Child | `A > B` | Selects B as a direct child of A. | `ul > li { }` |
| Adjacent sibling | `A + B` | Selects B immediately following A. | `h2 + p { }` |
| General sibling | `A ~ B` | Selects all B that follow A. | `h2 ~ p { }` |
| Grouping | `A, B` | Selects A and B. | `h1, h2, h3 { }` |

### Pseudo‑Classes

| Selector | Description | Example |
|----------|-------------|---------|
| `:hover` | When the mouse hovers over an element. | `a:hover { }` |
| `:active` | When an element is being activated (clicked). | `button:active { }` |
| `:focus` | When an element has focus. | `input:focus { }` |
| `:focus-visible` | When focus should be visible (e.g., keyboard focus). | `button:focus-visible { }` |
| `:focus-within` | When the element itself or any descendant has focus. | `form:focus-within { }` |
| `:target` | When the element's ID matches the URL fragment. | `section:target { }` |
| `:visited` | For visited links. | `a:visited { }` |
| `:link` | For unvisited links. | `a:link { }` |
| `:enabled` | Form element that is enabled. | `input:enabled { }` |
| `:disabled` | Form element that is disabled. | `input:disabled { }` |
| `:checked` | Checked checkbox or radio. | `input:checked { }` |
| `:indeterminate` | Indeterminate state (e.g., checkbox, progress). | `progress:indeterminate { }` |
| `:default` | Default form element (e.g., default button, selected option). | `input:default { }` |
| `:valid` | Form element with valid content. | `input:valid { }` |
| `:invalid` | Form element with invalid content. | `input:invalid { }` |
| `:in-range` | Number input within range. | `input:in-range { }` |
| `:out-of-range` | Number input outside range. | `input:out-of-range { }` |
| `:required` | Required form element. | `input:required { }` |
| `:optional` | Optional form element. | `input:optional { }` |
| `:read-only` | Element with readonly attribute. | `input:read-only { }` |
| `:read-write` | Element that is editable. | `input:read-write { }` |
| `:placeholder-shown` | Input showing placeholder text. | `input:placeholder-shown { }` |
| `:empty` | Element with no children (including text nodes). | `div:empty { display: none; }` |
| `:first-child` | First child of its parent. | `li:first-child { }` |
| `:last-child` | Last child of its parent. | `li:last-child { }` |
| `:first-of-type` | First of its type among siblings. | `p:first-of-type { }` |
| `:last-of-type` | Last of its type among siblings. | `p:last-of-type { }` |
| `:nth-child(n)` | Nth child (an+b formula). | `li:nth-child(odd) { }` |
| `:nth-last-child(n)` | Nth child counting from end. | `li:nth-last-child(2) { }` |
| `:nth-of-type(n)` | Nth of its type. | `img:nth-of-type(3) { }` |
| `:nth-last-of-type(n)` | Nth of its type counting from end. | – |
| `:only-child` | Element that is the only child. | `p:only-child { }` |
| `:only-of-type` | Element that is the only of its type among siblings. | `img:only-of-type { }` |
| `:root` | Root element (`<html>`). | `:root { --main-color: black; }` |
| `:not(selector)` | Negation. | `input:not([type="submit"]) { }` |
| `:is(selector-list)` | Matches if any of the selectors match (forgiving). | `:is(section, article) h2 { }` |
| `:where(selector-list)` | Same as `:is` but with zero specificity. | `:where(h1, h2) { }` |
| `:has(selector)` | Matches if any descendant matches selector. | `a:has(> img) { }` |
| `:lang(language)` | Element in given language. | `p:lang(fr) { }` |
| `:dir(direction)` | Element with text direction. | `div:dir(rtl) { }` |

### Pseudo‑Elements

| Selector | Description | Example |
|----------|-------------|---------|
| `::before` | Inserts content before an element. | `p::before { content: "» "; }` |
| `::after` | Inserts content after an element. | `p::after { content: " «"; }` |
| `::first-letter` | First letter of a block. | `p::first-letter { font-size: 2em; }` |
| `::first-line` | First line of a block. | `p::first-line { font-weight: bold; }` |
| `::selection` | Portion selected by the user. | `::selection { background: yellow; }` |
| `::placeholder` | Placeholder text in inputs. | `input::placeholder { color: gray; }` |
| `::marker` | Marker of a list item. | `li::marker { color: red; }` |
| `::backdrop` | Background behind modal dialog or fullscreen element. | `dialog::backdrop { background: rgba(0,0,0,0.5); }` |
| `::file-selector-button` | Button of file input. | `input[type="file"]::file-selector-button { }` |
| `::slotted()` | Slot content in shadow DOM. | `::slotted(span) { }` |
| `::part()` | Part of a shadow tree. | `::part(confirm) { }` |

---

## At‑Rules Reference

| At‑rule | Description | Example |
|---------|-------------|---------|
| `@charset` | Defines character set. | `@charset "utf-8";` |
| `@import` | Imports another stylesheet. | `@import url("extra.css");` |
| `@namespace` | Declares an XML namespace. | `@namespace svg "http://www.w3.org/2000/svg";` |
| `@media` | Conditional styles based on media queries. | `@media (max-width: 600px) { ... }` |
| `@supports` | Conditional styles based on feature support. | `@supports (display: grid) { ... }` |
| `@document` | (Deprecated) Matches based on URL. | – |
| `@page` | Styles for printed pages. | `@page { margin: 1in; }` |
| `@font-face` | Defines custom fonts. | `@font-face { font-family: "MyFont"; src: url("myfont.woff2"); }` |
| `@keyframes` | Defines animation keyframes. | `@keyframes slidein { from { left: 0; } to { left: 100%; } }` |
| `@counter-style` | Defines custom list counter styles. | `@counter-style circled { system: fixed; symbols: ① ② ③; }` |
| `@property` | Defines custom CSS properties (Houdini). | `@property --my-color { syntax: "<color>"; inherits: false; initial-value: black; }` |
| `@layer` | Defines cascade layers. | `@layer base, theme;` `@layer base { ... }` |
| `@scope` | Scopes style rules to a subtree. | `@scope (.card) { ... }` |
| `@container` | Container queries. | `@container (min-width: 400px) { ... }` |
| `@starting-style` | Defines styles before an element is first styled. | – |

---

## Functions Reference

| Function | Description | Example |
|----------|-------------|---------|
| `calc()` | Performs calculations. | `width: calc(100% - 20px);` |
| `min()` | Selects the smallest value. | `width: min(100%, 500px);` |
| `max()` | Selects the largest value. | `width: max(300px, 50%);` |
| `clamp()` | Clamps a value between min and max. | `font-size: clamp(1rem, 5vw, 2rem);` |
| `var()` | Inserts a custom property value. | `color: var(--main-color, black);` |
| `attr()` | Returns attribute value of the element. | `content: attr(data-tooltip);` |
| `url()` | References a resource. | `background-image: url("bg.png");` |
| `rgb()`, `rgba()` | Defines colors. | `color: rgb(255,0,0);` |
| `hsl()`, `hsla()` | Defines colors. | `background: hsl(120,50%,50%);` |
| `color()` | (Modern) Color function with predefined color spaces. | – |
| `color-mix()` | Mixes two colors. | `background: color-mix(in srgb, red, blue 50%);` |
| `light-dark()` | Returns color based on light/dark scheme. | `background: light-dark(white, black);` |
| `linear-gradient()` | Creates a linear gradient image. | `background: linear-gradient(to right, red, blue);` |
| `radial-gradient()` | Creates a radial gradient. | `background: radial-gradient(circle, red, blue);` |
| `conic-gradient()` | Creates a conic gradient. | `background: conic-gradient(red, yellow, green);` |
| `repeating-linear-gradient()` | Repeats linear gradient. | – |
| `repeating-radial-gradient()` | Repeats radial gradient. | – |
| `repeating-conic-gradient()` | Repeats conic gradient. | – |
| `image-set()` | Chooses image based on resolution. | `background-image: image-set("img.png" 1x, "img-2x.png" 2x);` |
| `element()` | Uses an element as an image. | `background: element(#myElement);` (limited support) |
| `cross-fade()` | Blends two or more images. | – |
| `shape()` | Defines a shape for `clip-path` or `shape-outside`. | – |
| `circle()` | Defines a circle shape. | `clip-path: circle(50%);` |
| `ellipse()` | Defines an ellipse shape. | `clip-path: ellipse(50% 30%);` |
| `inset()` | Defines an inset rectangle. | `clip-path: inset(10px 20px);` |
| `polygon()` | Defines a polygon. | `clip-path: polygon(0% 0%, 100% 0%, 50% 100%);` |
| `path()` | Defines an SVG path. | `clip-path: path("M0,0 L100,0 L50,100 Z");` |
| `blur()`, `brightness()`, `contrast()`, `drop-shadow()`, `grayscale()`, `hue-rotate()`, `invert()`, `opacity()`, `saturate()`, `sepia()` | Filter functions. | `filter: blur(5px) grayscale(50%);` |
| `rotate()`, `scale()`, `skew()`, `translate()`, `matrix()` | Transform functions. | `transform: rotate(45deg) scale(1.5);` |
| `perspective()` | Sets perspective for 3D transforms. | `transform: perspective(500px) rotateY(45deg);` |
| `steps()`, `cubic-bezier()` | Timing functions. | `transition-timing-function: cubic-bezier(0.1, 0.7, 1.0, 0.1);` |
| `counter()`, `counters()` | Inserts counters. | `content: counter(section) ". ";` |

---

This appendix provides a broad overview of CSS properties, values, selectors, and functions. For the most current and detailed information, consult the [MDN Web Docs CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) or the [W3C CSS Specifications](https://www.w3.org/Style/CSS/).