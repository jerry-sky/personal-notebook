---
lang: 'en-GB'
title: 'JS (other) Notes'
author: 'Jerry Sky'
description: 'Notes on general JS-related stuff.'
keywords: 'JavaScript, node, scroll, Samsung'
---

---

- [Links](#links)
    - [Archived *(sentimental)*](#archived-sentimental)
- [Parsing numbers in bases other than base-10](#parsing-numbers-in-bases-other-than-base-10)
- [Samsung Internet webpage scroll position](#samsung-internet-webpage-scroll-position)

## Links

- [The Post JavaScript Apocalypse](https://www.youtube.com/watch?v=99Zacm7SsWQ)

### Archived *(sentimental)*

- [SVGPan - a JS SVG map-like viewer](http://www.vleo.net/svgpan-a-javascript-svg-panzoomdrag-library/)

## Parsing numbers in bases other than base-10

To convert a `number` to a string in the target `base` use:

```javascript
number.toString(base)
```

To parse a `string` containing a number in a given `base` use:

```javascript
parseInt(string, base)
```

## Samsung Internet webpage scroll position

Samsung Internet doesn't output scroll position through `document.documentElement.scrollTop`, instead use `document.body.scrollTop`. However, unfortunately the second option isn't supported in other major browsers. Therefore the best implementation of `scrollTop` would be to check the value from both sources to ensure thorough browser support.
