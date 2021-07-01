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

whilst being the `config` directory.

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
