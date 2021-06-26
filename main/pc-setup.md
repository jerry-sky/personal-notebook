---
lang: 'en-GB'
title: 'PC Setup'
author: 'Jerry Sky'
description: 'A personal guide for setting up all programs, tools and configuration files for personal use.'
keywords: 'bash, linux, configuring, configuration, keyboard, internet, browser, definitions, system, os, user, experience'
---

---

- [Installing the OS](#installing-the-os)
- [Installing programs and copying config files](#installing-programs-and-copying-config-files)
- [Configuring the Internet browser](#configuring-the-internet-browser)
- [Other system settings](#other-system-settings)

---

## Installing the OS

1. Download the ISO of [the OS](https://linuxmint.com/download.php).
2. Install etcher.io.
3. Use etcher.io to put the OS ISO on an arbitrary USB stick that is at least 4 GB of size.
4. Install the OS by booting the target PC from the USB stick and following on-screen instructions.

---

## Installing programs and copying config files

Use the [*first time setup*](../config/readme.md#first-time-setup)
to install the most needed and basic programs such as web browser, editor, and Git.

After running that, this notebook should be located in the
`~/notebooks/personal-notebook` directory.
Go to the `config` subdirectory of this notebook and run the `setup.sh`
script to copy various config files to the system and install additional programs.

See [«config»](../config/readme.md).

---

## Configuring the Internet browser

1. Install [Bitwarden](https://bitwarden.com/#download) and log in.
2. Log in to the browser to enable browser settings synchronization.
3. Log in to all the online services.

---

## Other system settings

1. [Setup automount for the rest of the drives present in the system.](https://fossbytes.com/how-to-auto-mount-partitions-on-boot-in-linux-easily/)

---
