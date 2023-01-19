---
lang: 'en-GB'
title: 'Jerry Sky’s personal notebook'
author: 'Jerry Sky'
description: |
    This notebook consists of all personal notes of Jerry Sky including those not related to programming or computer science. \
    View this repository on
    [the web](https://personal.jerry-sky.me)
    or on [GitHub](https://github.com/jerry-sky/personal-notebook).
keywords: 'notebook, notes, personal, python, latex, languages, programming, computer science, linux, jerry-sky'
---



## Computer Science

### Learning platforms

- [foo.bar \(restricted access\)](https://foobar.withgoogle.com/)
- [Exercism](https://exercism.io/)
- [Front-end Mentor](https://www.frontendmentor.io/)
- [Hacker Earth](https://www.hackerearth.com/practice/)
- [Code Wars](https://www.codewars.com/)

### General

- [Environment configuration](config/readme.md)
- [Unix & Linux](general/unix-linux.md)
- [Git](general/git-notes.md)
- [Software issues](general/software-issues.md)
- [VS Code](general/vs-code.md)
- [Cloud](general/cloud.md)

### Web-dev

- [General (TypeScript, NodeJS)](web-dev/general.md)
- [Angular Notes](web-dev/angular-notes.md)
- [CSS/SCSS + HTML](web-dev/css-scss-html-notes.md)
- [Database notes](web-dev/database-notes.md)

### Abstract

- [Linguistics of Computer Science related matters](general/linguistics-related-to-cs.md)
- [Technical specification](general/technical-specification.md)

### Read

- [Ideas that Created the Future: Classic Papers of Computer Science](http://library.lol/main/614F928EDFE94E5935111EC25AFA6FE4)
- [FREE PROGRAMMING BOOKS](https://github.com/EbookFoundation/free-programming-books)
- [ROADMAPS](https://github.com/kamranahmedse/developer-roadmap)
- [ALGORITHMS](https://github.com/TheAlgorithms/Python)
- [SYSTEM DESIGN](https://github.com/donnemartin/system-design-primer)
- [COMPUTER SCIENCE](https://github.com/ossu/computer-science)
- [DATA SCIENCE](https://github.com/ossu/data-science)
- [PAPERS WE LOVE](https://github.com/papers-we-love/papers-we-love)
- [Art of the command line](https://github.com/jlevy/the-art-of-command-line)
- [Type challenges in TypeScript](https://github.com/type-challenges/type-challenges)
- [Build your own X](https://github.com/codecrafters-io/build-your-own-x)
- [AI Roadmap](https://github.com/AMAI-GmbH/AI-Expert-Roadmap)
- [Coding Interviews](https://github.com/jwasham/coding-interview-university)
- [JavaScript best practices](https://github.com/goldbergyoni/nodebestpractices)
- [Machine Learning for software engineers](https://github.com/GokuMohandas/Made-With-ML)
- [Applied Machine Learning](https://github.com/eugeneyan/applied-ml)
- [Awesome free machine learning and AI courses with video lectures.](https://github.com/luspr/awesome-ml-courses)

---



## Curriculum Vitae

*Based on the [AltaCV template](https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv).*

- [PDF](cv/curriculum-vitae.pdf)
- [`.tex`](cv/curriculum-vitae.tex)

---



## Arts

### General

- [Blender Notes](arts/blender-notes.md)
- [Colours](arts/colour-notes.md)

### Adobe

- [After Effects](arts/adobe/after-effects.md)
- [Illustrator](arts/adobe/illustrator.md)

---



## The arbitrary collection

- [Maths](the-arbitrary-collection/arbitrary-math-snippets.md)
- [Music](the-arbitrary-collection/arbitrary-music-things.md)
- [Hilarious stories](the-arbitrary-collection/hilarious-stories.md)
- [2D Animation](the-arbitrary-collection/2d-animation.md)
- [Lifehacks Stack Exchange](https://lifehacks.stackexchange.com/)

---



## [Archive](archive/README.md)

Archived notes.

---



## Some remarks

[m-aio]: https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one
[pandoc]: https://pandoc.org
[pandoc-katex]: https://github.com/xu-cheng/pandoc-katex#readme
[vyrow]: https://github.com/jerry-sky/vyrow#readme


### OneNote

This repository serves the purpose of my main note-taking solution.

A Markdown-based repository is the successor of my previous note-taking solution,
which was OneNote.
I have since abandoned OneNote for a few simple, but compelling reasons:

- I’ve switched to Linux full-time as my main OS which leaves me with
    a very underwhelming browser app and no desktop program for note-taking,
- OneNote is Microsoft’s proprietary technology with poor exporting tools,
- general very slow performance as per usual with Microsoft software.


### Markdown and $\LaTeX$

Not to mention this Markdown-based solution is better because it involves
just normal text documents — basic, but definitely sufficient.

After the switch the only thing I was missing, was the ability to write down mathematical expressions.
In OneNote, this was done by using the handwriting feature.
Frankly, my main form of interaction with this program was through handwriting,
but that does not change anything.

So, the solution that enabled maths in Markdown was $\LaTeX$, because what else would I use.
Of course, $\LaTeX$ is not even mentioned in most specification sheets of various
Markdown flavours, but that also is not a problem.


### Workflow

Because Markdown is very loosely defined, it is not uncommon
in the *Markdown world* to add various features that were not
intended to be added by the original creator.
For example [Pandoc][pandoc], a powerful markup conversion tool,
allows for $\LaTeX$ expressions in Markdown.
You just have to provide some Maths engine that would
render out these expressions when converting from Markdown to HTML for example.
How I deal with that will be explained [later](#website-pipeline).

For editing Markdown documents I use VS Code with the
[Markdown All-in-one extension][m-aio].
This enables me to see my documents in both their raw and rendered out forms,
as this extension adds a Markdown preview tab that understands $\LaTeX$ expressions.
It also gives some useful commands, and automatization tools like auto-generating table of contents.


### Website pipeline

As mentioned above, Pandoc allows for $\LaTeX$ expressions in Markdown documents.
It doesn’t do a great job with converting $\LaTeX$ to HTML by default,
but you can just tell it to use KaTeX or MathJax.

For presenting my Markdown-based notebook repositories I’m using a [GH Action][vyrow]
I created that uses [Pandoc][pandoc] to render Markdown documents into HTML documents.
Apart from [Pandoc][pandoc] it also uses [Pandoc-KaTeX][pandoc-katex]
— a Rust package that renders static HTML pages, instead of leaving
raw expressions and letting the client browser render the $\LaTeX$ expressions.
Such solution is elegant and much more performant, as the output HTML documents
*do not contain any JavaScript*, only CSS that puts the static $\LaTeX$ elements into place.

Both of my notebooks (personal notebook and academic notebook) are rendered
into websites using [VYROW][vyrow] — my GH Action.

You can view them on the web:
- <https://personal.jerry-sky.me>
- <https://academic.jerry-sky.me>


### Figures

When it comes to graph drawing or any type of graphical figures it can be done with OneNote,
GIMP, or Notes on an iPad.

An alternative would be to use `code blocks`.
Characters such as `\`, `|`, `/`, `_`, `<`, `>`, `／`, `＼`, `＿`, `ー`, `「`, `」`, `＜`, and `＞`
all can be used as strokes while regular Latin alphabet characters as e.g. graph nodes.
