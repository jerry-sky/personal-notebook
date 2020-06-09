# $\LaTeX$ Notes

- [$\LaTeX$ Notes](#math-xmlnshttpwwww3org1998mathmathmlsemanticsmrowmtextlatexmtextmrowannotation-encodingapplicationx-texlatexannotationsemanticsmathlatex-notes)
  - [Links](#links)
  - [Using SVG files with `inkscape`](#using-svg-files-with-inkscape)

## Links

  - [Can't locate perl dependencies issue](https://github.com/cmhughes/latexindent.pl/issues/104)

## Using SVG files with `inkscape`

To prepare a SVG image to be used in a $\LaTeX$ document use
```bash
inkscape -D -z --file=image.svg --export-pdf=image.pdf --export-latex
```
and import it in the document using
```tex
\input{image.pdf_tex}
```
inside a `figure`.

[Source](https://tex.stackexchange.com/a/2107)
