# CSS/SCSS

## Index

  - [Links](#links)
  - [Web-kit scrollbar styling](#web-kit-scrollbar-styling)

## Links

  - [How you've been getting the Bootstrap grid all wrong](https://medium.com/@erik_flowers/how-youve-been-getting-the-bootstrap-grid-all-wrong-and-how-to-fix-it-6d97b920aa40)
  - [Practical CSS Scroll Snapping](https://css-tricks.com/practical-css-scroll-snapping/)
  - [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
  - [Easings cheatsheet](https://easings.net/)
  - [CSS Grid Changes EVERYTHING](https://www.youtube.com/watch?v=7kVeCqQCxlk)

### Animations

  - [Animate.css](https://daneden.github.io/animate.css/)
  - [Magic Animations CSS3](https://www.minimamente.com/project/magic/)
  - [AniJS](http://anijs.github.io/)
  - [Motion UI](https://zurb.com/playground/motion-ui)
  - [vivus.js - SVG animations](http://maxwellito.github.io/vivus/)

### Archived *(sentimental)*
  - [The Shapes of CSS](https://css-tricks.com/the-shapes-of-css/)

## Web-kit scrollbar styling

As the webkit browser have very ugly scrollbars and there is no front-runner when it comes to JS-based scrollbar frameworks - the best solution seems to just style them using CSS/SCSS directly.

```scss
/* width */
::-webkit-scrollbar {
  background: lighten(#333, 3.5%);
}
/* Handle */
::-webkit-scrollbar-thumb {
  background: lighten(#333, 9%);
}
/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: lighten(#333, 30%);
}
/* Corner */
::-webkit-scrollbar-corner {
  background: lighten(#333, 3.5%);
}
/* Resizer */
::-webkit-resizer {
  background: lighten(#333, 8%);
}
```
