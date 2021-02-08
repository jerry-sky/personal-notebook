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
- [Keyboard layouts](#keyboard-layouts)
- [Desktop Environment settings](#desktop-environment-settings)
- [Other system settings](#other-system-settings)
- [Cinnamon DE–related issues](#cinnamon-derelated-issues)

---

## Installing the OS

1. Install it from a prepared bootable USB stick.
2. If no bootable USB stick is available perform following actions:
    1. Download the ISO of [the OS](https://linuxmint.com/download.php).
    2. Install etcher.io on a secondary PC.
    3. Use etcher.io to put the OS ISO on an arbitrary USB stick.
    4. Install the OS by booting the target PC from the USB stick.

---

## Installing programs and copying config files

Use the [*first time setup*](../config/readme.md#first-time-setup) to install the most needed and basic programs such as web browser, editor, and Git.

After running that, this notebook should be located in the `~/notebooks/personal-notebook` directory. Go to the `config` subdirectory of this notebook and run the `setup.sh` script to copy various config files to the system and install additional programs.

See [«config»](../config/readme.md).

---

## Configuring the Internet browser

1. Install [Bitwarden](https://bitwarden.com/#download) and log in.
2. Log in to the browser to enable browser settings synchronization.
3. Log in to all the online services:
    1. [**GitHub**](https://github.com/login),
    2. [WhatsApp](https://web.whatsapp.com/),
    3. [Twitter](https://twitter.com/),
    4. [*Facebook Messenger*](https://www.messenger.com/) *(unfortunately)*.

---

## Keyboard layouts

1. Install [IBus](https://forums.linuxmint.com/viewtopic.php?t=160272) to allow using non-western keyboard layouts and allow using more than 4 keyboard layouts at once.
    1. Should any issues arise, follow instructions provided in [this askubuntu.com answer](https://askubuntu.com/a/793046).

---

## Desktop Environment settings

1. Date format to use in the clock part of the taskbar:

    ```txt
    %A   %Y-%m-%d   %H:%M:%S
    ```

    Example:

    ```txt
    Sonntag 2021-02-07 16:30
    ```

---

## Other system settings

1. [Setup automount for the rest of the drives present in the system.](https://fossbytes.com/how-to-auto-mount-partitions-on-boot-in-linux-easily/)

---

## Cinnamon DE–related issues

1. The Cinnamon Desktop Environment currently doesn't support more than four keyboard layouts for some odd reason ([the issue on GitHub](https://github.com/linuxmint/cinnamon/issues/3212#issuecomment-337725452)).
    - However, this issue can be resolved by installing IBus as described [here](#keyboard-layouts).

2. To enable a program to accept an argument (e.g. a link for the browser) add `%U` to the Menu list entry's command box.

---
