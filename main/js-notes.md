# JS (other) Notes

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

