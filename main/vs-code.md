---
lang: 'en-GB'
title: 'VS Code'
author: 'Jerry Sky'
description: 'Notes on VS Code.'
keywords: 'VS Code, code, visual studio code, settings, sync, java'
---

---

- [Settings Sync](#settings-sync)
- [Java Formatter Settings](#java-formatter-settings)

---

## Settings Sync

*To keep the settings synced use this addon.*

Install:
```bash
ext install Shan.code-settings-sync
```
To download/ upload the settings from/ to the Gist use: `SHIFT + ALT + U/D`.

---

## Java Formatter Settings

The Java formatter for VS Code is currently a joke. According to [the official guide](https://github.com/redhat-developer/vscode-java/wiki/Formatter-settings) on how to change the settings of the formatter it is advised to use Eclipse to alter the settings.

The default settings are atrocious - formatter doesn't allow for additional newlines that enable code readability or doesn't align the `case` statements with the `switch` statement properly.

I keep my personal formatter settings file with the rest of the config files in [«config»](../config/readme.md).
