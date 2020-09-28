# $\LaTeX$ Notes

- [Links](#links)
- [Using SVG files with `inkscape`](#using-svg-files-with-inkscape)
- [Installing TeX Live](#installing-tex-live)

## Links

- [Can't locate perl dependencies issue](https://github.com/cmhughes/latexindent.pl/issues/104)

---

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

---

## Installing TeX Live

Installing `texlive` packages using `apt` results in outdated *(by some described as ancient)* software.

Instead of that, you should use the official installer that can be acquired from [the official TUG (TeX Users Group) website](https://tug.org/texlive/acquire-netinstall.html).

After unpacking the installer run
```bash
perl install-tl
```
and choose the `i` option for installing.

*Installation takes about an hour to complete.*

After it’s done you need to add the directory of TeX Live binaries to your `PATH`:
```bash
PATH="/usr/local/texlive/2020/bin/x86_64-linux:$PATH"
```

Source: [Quick install guide on tug.org](https://www.tug.org/texlive/quickinstall.html)
