---
lang: 'en-GB'
title: 'Linux Mint Setup'
author: 'Jerry Sky'
description: 'A part of the PC Setup that contains steps specific to Linux Mint.'
keywords: 'linux, linux mint, setup, steps, config, customization'
---

---

These settings are specific to Linux Mint system. For more see [PC Setup](pc-setup.md).

### Install the Linux Mint Cinnamon distribution

1. Install it from a prepared bootable USB stick.
2. If no bootable USB stick is available perform following actions:
   1. Download the ISO from [the official website](https://linuxmint.com/download.php).
   2. Install etcher.io on a secondary PC.
   3. Use etcher.io to put the OS ISO on an arbitrary USB stick.
   4. Install the OS by booting the target PC from the USB stick.

### Configuring the user experience

1. Configure theme and colours
   1. [Download themes and cursor packs](pc-setup.md#configuring-the-user-experience)
   2. Configure theme ( Settings $\to$ Themes ).

2. Configure the bottom panel

3. Enable *'Prevent focus stealing'* ( Settings $\to$ Windows )

4. Disable switching between open windows by middle-clicking to avail new tab opening in programs that use that mouse click for some shortcut inside this program ( Settings $\to$ Windows )

5. Disable auto-rotate ( Settings $\to$ General )

6.  Disable *'Global hotkey for cycling through thumbnail menus'* from Grouped window list. To access that settings panel, click on an icon of multiple windows in the panel, then Preferences, then Configure. [Details here](https://forums.linuxmint.com/viewtopic.php?t=291898)

7. Change panel opened programs viewing mode to show all titles.

8. Change login page background image ( Administration $\to$ Login Window )

9. Disable *'Allow floating clock'* ( Settings $\to$ Screensaver $\to$ Customization ).

10. Prolong the screensaver timeout ( Settings $\to$ Screensaver )

11. *Optional* [Setup switching workspaces via touchpad gestures](https://github.com/Hikari9/comfortable-swipe)

    <!-- spellchecker: disable-next-line -->
12. *Optional* [Setup listening to line-in audio at startup `pacmd load-module module-loopback latency_msec=5`](https://unix.stackexchange.com/questions/263274/pipe-mix-line-in-to-output-in-pulseaudio)

13. *Optional* Change default font ( System Settings $\to$ Font Selection )

## Issues

1. The Cinnamon Desktop Environment currently doesn't support more than four keyboard layouts for some odd reason ([the issue on GitHub](https://github.com/linuxmint/cinnamon/issues/3212#issuecomment-337725452)).
   - However, this issue can be resolved by installing IBus as described in the [Keyboard layout settings](pc-setup.md#keyboard-layout-settings) section in the PC setup note.

2. To enable a program to accept an argument (e.g. a link for the browser) add `%U` to the Menu list entry's command box.
