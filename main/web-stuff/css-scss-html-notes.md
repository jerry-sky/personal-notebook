# CSS/SCSS + HTML

- [Links](#links)
  - [Animations](#animations)
  - [Archived *(sentimental)*](#archived-sentimental)
- [Web-kit scrollbar styling](#web-kit-scrollbar-styling)
- [Bootstrap & Sass](#bootstrap--sass)
- [Nested (layered) links](#nested-layered-links)
- [Website design with respect to keyboard users](#website-design-with-respect-to-keyboard-users)

## Links

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

## Bootstrap & Sass

The idea is to not use the *classic* Bootstrap classes on HTML elements, but rather to compose a singular class of an element from Bootstrap's `@mixin`s.

Instead of attaching these `col` classes like so:
```html
<div class="container">
  <div class="row">
    <div class="banana col-sm-6 col-md-4">
      <p>banana 🍌 content</p>
    </div>
  </div>
</div>
```
create a class that defines that element by using `@mixin`s:
```scss
.banana {
  @include make-col-ready;
  @include media-breakpoint-up(sm) {
    @include make-col(6);
  }
  @include media-breakpoint-up(md) {
    @include make-col(4);
  }
  p {
    font-size: 3rem;
    color: yellow;
    font-weight: 600;
  }
}
```

To use these `@mixin`s and other Bootstrap's functionalities it is necessary to import them:
```scss
@import "~bootstrap/scss/functions";
@import "~bootstrap/scss/variables";
@import "~bootstrap/scss/mixins";
```

Since there is no need for these *classic* classes to be used in HTML you can turn them off by changing a variable in the `_variables.css` file:
```css
$enable-grid-classes: false !default;
```
or just not to include the Bootstrap css file in your app config e.g. Angular (`angular.json`).

Read more in the [source](https://medium.com/@erik_flowers/how-youve-been-getting-the-bootstrap-grid-all-wrong-and-how-to-fix-it-6d97b920aa40).


## Nested (layered) links

[nested-links]: https://www.sarasoueidan.com/blog/nested-links/#my-implementation

To create a link inside a `div` (that could be e.g. a post) which itself is a separate link you could use a solution [described here by Sara Soueidan][nested-links].\
Essentially, the header of, in this case, an article is stretched over a `div` representing a description of a given article. Of course, this header is a link to this article. Now, we can incorporate another link inside this description and making it hover over the article link (using `z-index`).

Here is a piece of code [from previously mentioned article][nested-links] that presents an example solution to this problem:
```scss
.the-post {
    /* elevate the links up */
    a {
        position: relative;
        z-index: 1;
    }
}

.the-post-title {
    /* ... */

    a {
        position: static;
        /* expand the pseudo-element to cover the post area */
        &::before {
            content: "";
            position: absolute;
            z-index: 0;
            top: ...;
            left: ...;
            width: ...;
            height: ...;
            /* ... */
        }
    }
}
```

## Website design with respect to keyboard users

[design-respect-to-keyboards]: https://www.sarasoueidan.com/blog/keyboard-friendlier-article-listings/

Most website designs are not optimized for keyboard users that facilitate the Tab key for navigating websites. The problem is, many websites have redundant links (multiple links referring to the same resource) that generate excess Tab keystrokes to navigate through e.g. articles on a website, as described [here by Sara Soueidan][design-respect-to-keyboards]. However, a fix to this problem is quite simple:
```html
<a href="cool-subpage.html" tabindex="-1" aria-hidden="true">Cool subpage</a>
```
The `tabindex` attribute set to `-1` renders this element invisible to keyboard users navigating using the Tab key. This element will be skipped.\
The `aria-hidden` attribute set to `true` makes this element invisible to screen readers thus preventing from exposing this unreachable element to the user.
