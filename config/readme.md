---
lang: 'en-GB'
title: 'Config'
author: 'Jerry Sky'
description: 'Config files and other utilities that I use every day. Installed automatically using the setup script.'
keywords: 'bash, config, script, utilities, python3, keyboard, markdown, bash aliases'
---

---

- [Setup](#setup)
    - [First time setup](#first-time-setup)
    - [The rest of the setup](#the-rest-of-the-setup)
- [The setup includes things as:](#the-setup-includes-things-as)
    - [Keyboard volume knob configuration](#keyboard-volume-knob-configuration)
    - [Utility scripts](#utility-scripts)

---

## Setup

### First time setup

To run the script for setting up the most basic of environments run:

```bash
bash -c "$(curl -s https://raw.githubusercontent.com/jerry-sky/personal-notebook/master/config/first-time-setup.sh)"
```

---

### The rest of the setup

In the same directory as this document there is a file called `setup.sh` which copies various config files into all sorts of locations.
It's part of the [standard JRS PC Setup](../main/pc-setup.md) to configure the system and its programs.
Execute it whilst being in the `/config` directory to set up a proper workspace.

```bash
./setup.sh
```

---

## The setup includes things as:

### Keyboard volume knob configuration

The config setup script allows to copy some utility scripts that enable to override the default behaviour of Volume Media keys. Some keyboards have a scrollable knob that normally controls the volume. Because of these scripts (and properly configured keyboard shortcuts to these scripts) this volume knob can be utilized as mouse scroll wheel or volume knob. The *mute* button switches between `scroll` and `volume` modes.

---

### Utility scripts

The `utility-scripts` directory contains some very specific but useful scripts that are sometimes very handy.

- [`fix-iso-date-file-contents.sh`](utility-scripts/fix-iso-date-file-contents.sh) & [`fix-iso-date-filenames.sh`](utility-scripts/fix-iso-date-filenames.sh) – these scripts fix all pseudo ISO-like dates that don't have a leading zero before a single-digit day number (e.g. 2020-04-**4** instead of 2020-04-**04**)
- [`resize-last-window-to-1920x1080.sh`](utility-scripts/resize-last-window-to-1920x1080.sh) — resizes the last open window to a standard resolution of 1920×1080 (requires `wmctrl`)
- [`front-matter-ify-markdown-document.sh`](utility-scripts/front-matter-ify-markdown-document.sh) — converts a document that has a header at the beginning with the title of the document and converts it into a front matter metadata block with some additional metadata like date and description that may be within the first five lines of the document
