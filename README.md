---
lang: 'en-GB'
title: 'Jerry Sky’s personal notebook'
author: 'Jerry Sky'
description: |
    Software is cool. \
    View this repository on
    [the web](https://personal.jerry-sky.me)
    or on [GitHub](https://github.com/jerry-sky/personal-notebook).
keywords: 'notebook, notes, personal, dotfiles, python, latex, languages, programming, computer science, linux'
---



## Computer Science

### Environment configuration

[_My outlook on how to setup a Linux-based Operating System. The “dotfiles” part of this repository._](config/readme.md)


### Plumbing notes

_Notes on various issues that came up during my work_
_and solutions with applicable tools that help in handling them._

- [Unix & Linux](plumbing/unix-linux.md)
- [Git](plumbing/git-notes.md)
- [Software issues](plumbing/software-issues.md)


### DevOps

_Sysadmin, Linux, virtual infrastructure, tooling, all that jazz._

- [Cloud](devops/cloud.md)


### Web-dev

_Everything web development._

- [General](web-dev/general.md)
- [TypeScript](web-dev/typescript.md)
- [Angular](web-dev/angular-notes.md)
- [CSS/SCSS + HTML](web-dev/css-scss-html-notes.md)
- [Database](web-dev/database-notes.md)


### Meta

_Not directly related to a specific technology, meta talk._

- [Linguistics of Computer Science related matters](meta/linguistics-related-to-cs.md)
- [Technical specification](meta/technical-specification.md)


### Read

_List of valuable sources of knowledge._

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


### Learning platforms

_Interactive way of learning stuff._

- [foo.bar \(restricted access\)](https://foobar.withgoogle.com/)
- [Exercism](https://exercism.io/)
- [Front-end Mentor](https://www.frontendmentor.io/)
- [Hacker Earth](https://www.hackerearth.com/practice/)
- [Code Wars](https://www.codewars.com/)

---



## Curriculum Vitae

_Based on the_
_[AltaCV template](https://www.overleaf.com/latex/templates/altacv-template/trgqjpwnmtgv)._

- [Human readable form (PDF)](cv/curriculum-vitae.pdf)
- [Source code (TeX)](cv/curriculum-vitae.tex)

---



## Arts

- [Blender Notes](arts/blender-notes.md)
- [Colours](arts/colour-notes.md)
- [Adobe After Effects](arts/adobe/after-effects.md)
- [Adobe Illustrator](arts/adobe/illustrator.md)

---



## The arbitrary collection

- [Maths](the-arbitrary-collection/arbitrary-math-snippets.md)
- [Music](the-arbitrary-collection/arbitrary-music-things.md)
- [Hilarious stories](the-arbitrary-collection/hilarious-stories.md)
- [2D Animation](the-arbitrary-collection/2d-animation.md)
- [Lifehacks Stack Exchange](https://lifehacks.stackexchange.com/)
- [Crazy software](the-arbitrary-collection/crazy-software.md)

---



## Archive

[_Archived notes._](archive/README.md)

---



## Some remarks

[m-aio]: https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one
[pandoc]: https://pandoc.org
[pandoc-katex]: https://github.com/xu-cheng/pandoc-katex#readme
[vyrow]: https://github.com/jerry-sky/vyrow#readme
[nebo]: https://www.nebo.app/


This repository serves the purpose of one of my main note-taking solutions.
Almost all notes on the tools I use and issues that I encounter are documented here,
alongside with multiple lists of valuable external resources.

> For a long time, I thought that this notebook would be my designated
> final note-taking solution that will replace all the others.
> I was wrong, as handwritten notes are still better in some use-cases,
> or they serve the purpose of being a buffer containing raw thoughts that
> are not article-worthy yet.
>
> One field where hand-written notes are better is language learning.
> Freedom of an open non-linear infinite physical space to save pen strokes
> is very important to me.


### OneNote

A Markdown-based repository is the successor of my previous note-taking solution,
which was OneNote.
I have since abandoned OneNote for a few simple, but compelling reasons:

- I’ve switched to Linux full-time as my main OS which leaves me with
    a very underwhelming browser app and no desktop program for note-taking,
- OneNote is Microsoft’s proprietary technology with poor exporting tools,
- general very slow performance as per usual with Microsoft software.

For handwritten notes I use [Nebo][nebo] on my iPad.
It has excellent set of features amongst which the handwriting recognition feature
is most appealing to me, as one can search through a notebook contents
like it was written using a keyboard.


### Markdown and $\LaTeX$

A Markdown-based solution is better because it involves just normal text documents
— basic, but in most cases sufficient.

After the switch the only thing I was missing, was the ability to write down mathematical expressions.
So, the solution that enabled maths in Markdown was $\LaTeX$,
because this is the industry standard when it comes to writing maths using a keyboard.
Of course, $\LaTeX$ is not even mentioned in most specification sheets of various
Markdown flavours, but that also is not a problem.


### Workflow

Because Markdown is very loosely defined, it is not uncommon
in the _Markdown world_ to add various features that were not
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
_do not contain any JavaScript_, only CSS that puts the static $\LaTeX$ elements into place.

Both of my notebooks (personal notebook and academic notebook) are rendered
into websites using [VYROW][vyrow] — my GH Action.

You can view them on the web:
- <https://personal.jerry-sky.me>
- <https://academic.jerry-sky.me>


### Figures

When it comes to graph drawing or any type of graphical figures it can be done with OneNote,
GIMP, any other graphical program or e.g. a note-taking app on a tablet.

An alternative would be to use `code blocks`.
Characters such as `\`, `|`, `/`, `_`, `<`, `>`, `／`, `＼`, `＿`, `ー`, `「`, `」`, `＜`, and `＞`
all can be used as strokes while regular Latin alphabet characters as e.g. graph nodes.
