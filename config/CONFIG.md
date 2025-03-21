---
lang: 'en-GB'
title: 'Config'
author: 'Jerry Sky'
description: 'Config files and other utilities that I use every day.'
keywords: 'bash, config, script, utilities, python3, keyboard, markdown, bash aliases'
---

## First time setup

First time setup includes some basic things such as:

- Internet browser (Google Chrome),
- NeoVim,
- Git (with GitHub configuration).

Run

```bash
curl -L fts.jerry-sky.me | bash
```

to download the script and run it on a new system.

---



## Standard setup

Standard setup is not as crucial as the first time setup, but still includes
some very much necessary things such as a proper desktop environment.

It also includes a list of various scripts that:

- install programs,
- install utilities,
- link or copy config files,
- set up environment extensions.

Run

```bash
./setup.sh
```

whilst being in the `config` directory.

---



## _Config_ components


### Config files

Contains all configuration files that are not programs or scripts.
They define how a given program or environment behaves.

Notes:
- [KBCT](doc/kbct.md)


### Hotkeys

Contains a set of scripts that are dispatched using key combinations.

1. Discord-specific scripts to activate the _deafen_ and _mute_ modes.
2. Microphone toggle for turning on or off the microphone system-wide.
3. [OBS-specific scripts for switching between scenes and transitions](doc/obsws.md).


### Install scripts

Concerns scripts that install certain programs or environments.


### Source files

_Config Entries_ break the whole setup into easy-to-install pieces.


### Utility scripts

Other scripts that do not fit the other categories.


### Xinput

Contains scripts for configuring peripheral devices such as mice and keyboards.

---
