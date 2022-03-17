---
lang: 'en-GB'
title: 'KBCT'
description: |
    [KBCT](https://github.com/samvel1024/kbct) is used to remap keys and
    add keyboard layouts to implement keys that are not physically available
    on a given keyboard.
---


## Config file

The YAML config file defines all key remaps and the secondary keyboard layouts
accessible via given modifier keys.

- [KBCT GitHub repository](https://github.com/samvel1024/kbct)
- [Key name list](https://gist.githubusercontent.com/samvel1024/02e5675e04f9d84f098e98bcd0e1ea12/raw/e18d950ce571b4ff5c832cc06406e9a6afece132/keynames.txt)

---


## Current implementation

Main reason that I’m even using KBCT is the keyboard layout of my laptop.
It is a compact US international keyboard with a short left _Shift_ key
and a tall _Enter_ key.
Another drawback of this specific layout is the lack of useful function keys,
e.g. no media keys apart from volume control.
Lack of dedicated _PageUp_, _PageDown_, and _Insert_ keys is the most aggravating one.

This configuration addresses these issues.
