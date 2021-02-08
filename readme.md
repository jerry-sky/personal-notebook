---
lang: 'en-GB'
title: 'Jerry Sky’s personal notebook'
author: 'Jerry Sky'
description: 'This notebook consists of all personal notes of Jerry Sky including those not related to programming or computer science.'
keywords: 'notebook, notes, personal, python, latex, languages, programming, computer science, linux, jerry-sky'
---

---

View this repository on [the web](https://personal.jerry-sky.me) or on [GitHub](https://github.com/jerry-sky/personal-notebook).

---

- [Index](#index)
    - [Environment](#environment)
    - [Main](#main)
    - [Life (Ω)](#life-ω)
    - [Languages](#languages)
    - [Ideas (Ω)](#ideas-ω)
    - [The arbitrary collection](#the-arbitrary-collection)
    - [Adobe](#adobe)
    - [Videos](#videos)
    - [Other (Ω)](#other-ω)
- [Some remarks](#some-remarks)

*Please note: to view some private notes (marked with (Ω)) you need to have access to the private part of this repository.*

## Index

### Environment

- [PC Setup](main/pc-setup.md)
- [*Software List (deprecated, to-be-deleted)*](main/software-list.md)
- [Config](config/readme.md)

### Main

- [Unix & Linux](main/unix-linux.md)
- [Git](main/git-notes.md)
- [VS Code](main/vs-code.md)
- [Software issues](main/software-issues.md)
- [Blender Notes](main/blender-notes.md)
- [Web stuff](main/web-stuff/readme.md)
- [Software Engineering](main/software-engineering/readme.md)
- [Curriculum Vitae](cv/readme.md)
- [Linguistics of Computer Science related matters](main/linguistics-related-to-cs.md)
- [$\LaTeX$](main/latex-notes.md)
- [Colours](main/colour-notes.md)

### Life (Ω)

- [Thoughts (Ω)](private/life/thoughts/readme.md)
- [Books (Ω)](private/life/books/readme.md)
- [Journal (Ω)](private/life/journal/readme.md)
- [Life Programming (Ω)](private/life/life-programming/readme.md)

### Languages

- [English](languages/english/readme.md)
- [German](languages/deutsch/readme.md)
- [French](languages/français/readme.md)
- [Japanese](languages/日本語/readme.md)

### Ideas (Ω)

- [Calendar app (Ω)](private/ideas/calendar-app.md)
- [Todo app (Ω)](private/ideas/todo-app.md)
- [Notes app (Ω)](private/ideas/notes-app.md)

### The arbitrary collection

- [Maths](the-arbitrary-collection/arbitrary-math-snippets.md)
- [Music](the-arbitrary-collection/arbitrary-music-things.md)
- [Hilarious IT stories](the-arbitrary-collection/hilarious-it-stories.md)
- [2D Animation](the-arbitrary-collection/2d-animation.md)

### Adobe

- [After Effects](adobe/after-effects.md)
- [Illustrator](adobe/illustrator.md)

### [Videos](videos/readme.md)

### [Other (Ω)](private/other/readme.md)

---

## Some remarks

The reason this repository came to exist is all the shortcomings of OneNote. Here’s a couple:

- *very poor performance of the browser-based app*
- *no Linux-based app*
- *proprietary technology*
- *very error-prone exporting tools*

The only area in which OneNote is better than any other note-taking app is **handwriting**. Unfortunately, there is no other solution that has all the capabilities of OneNote and a nice, performant Linux app.

The partial solution would be to use Github repositories, just like this one, as the main solution for note taking. However, plain text is not always enough to create good notes. Visual aids and math equations are very often crucial for a given note.

Some Markdown renderers allow $\LaTeX$ in Markdown documents — e.g. the [Markdown All-in-one extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) for VS Code renders Markdown documents with $\LaTeX$ math when previewing Markdown documents in VS Code. This extension uses the [`markdown-it`](https://www.npmjs.com/package/markdown-it) package with a plugin that supports $\LaTeX$ syntax. The package uses the [‘CommonMark’ spec](https://commonmark.org/) which is the preferred Markdown spec. Which means VS Code (with appropriate extensions) is *the* program to use for note taking.

When it comes to graph drawing or any type of graphical figures it can be done with OneNote. However, if it can be done with e.g. GIMP or any other graphics program *OneNote should not be used*.\
An alternative to this is to use `code blocks`. Characters such as `\`, `|`, `/`, `_`, `<`, `>`, `／`, `＼`, `＿`, `ー`, `「`, `」`, `＜`, and `＞` (Japanese characters) all can be used as strokes while regular latin alphabet characters as e.g. graph nodes.

---
