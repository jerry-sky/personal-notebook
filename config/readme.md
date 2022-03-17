---
lang: 'en-GB'
title: 'Config'
author: 'Jerry Sky'
description: 'Config files and other utilities that I use every day. Installed automatically using the setup script.'
keywords: 'bash, config, script, utilities, python3, keyboard, markdown, bash aliases'
---

---

- [First time setup](#first-time-setup)
- [Standard setup](#standard-setup)

---

## First time setup

First time setup includes some basic things such as:

- Internet browser (Google Chrome),
- IDE (VS Code),
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

_Please note: this setup assumes the Cinnamon desktop environment is installed in the system._

---


## _Config_ components


### Config files

Contains all configuration files that are not programs or scripts.
They define how a given program or environment behaves.

The most notable one would be the configuration file for the i3 window manager.
I use i3wm (and a few utility programs) as my main desktop environment.


### Hotkeys

Contains a set of scripts that are dispatched using key combinations.

1. Discord-specific scripts to activate the _deafen_ and _mute_ modes.
2. Microphone toggle for turning on or off the microphone system-wide.
3. OBS-specific scripts for switching between scenes and transitions.


### Install scripts

Concerns scripts that install certain programs or environments.


### Utility scripts

Other scripts that do not fit the other categories.


### Xinput

Contains scripts for configuring peripheral devices such as mice and keyboards.

---
