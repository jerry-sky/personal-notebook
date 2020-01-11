# PC Setup
  #### A personal guide for setting up all programs, tools and configurations for personal use be it work or rest.

## Definitions
Following statements are crucial to perform [steps from the next section](#steps-to-reproduce).

1. Cloud $\equiv$ Dropbox
2. Internet Browser $\equiv$ Vivaldi
3. Software Manager $\equiv$ Software Manager that is *basically* a GUI for `apt` in Linux Mint

## Steps to reproduce

1. Install the [Internet Browser](#definitions)
   1. Install [Bitwarden](https://bitwarden.com/#download)
   2. Install [Dark Reader](https://chrome.google.com/webstore/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh)
   3. Log in to all online services
      1. [**Google**](accounts.google.com/)
      2. [**GitHub**](https://github.com/login)
      3. [WhatsApp](https://web.whatsapp.com/)
      4. [Discord](https://discordapp.com/channels/@me)
      5. [*Facebook Messenger*](https://www.messenger.com/)
   4. Change default browser to [Internet Browser](#definitions)
   5. *(Opera-only) [Enable DRM to view DRM-content such as Prime Video or Netflix etc.](https://forums.opera.com/topic/28663/widevine-and-opera/29)*

2. Install [Cloud](#definitions) Desktop app

3. Enable Redshift
   1. Copy a config file from [Cloud](#definitions)`/Settings & Presets/Linux/` to `~/.config/`
   2. Enable autostart

4. ~~Install Spotify (Software Manager)~~
   1. *For now, the web-based app seems to be working fine.*

5. Install [`snap`](https://snapcraft.io/docs/installing-snap-on-linux-mint)

6. ~~Install barrier (Snap)~~

7. Install GParted from [Software Manager](#definitions)

8. Install Git
   1. `sudo apt install git`
   2. Install [credentials manager](https://stackoverflow.com/questions/36585496/error-when-using-git-credential-helper-with-gnome-keyring-as-sudo/40312117#40312117)
   3. Create new [personal github access token](https://github.com/settings/tokens)
   4. At first login provide the token as the password

9. Install [VS Code](https://code.visualstudio.com/)
   1.  *Note: __don't__ install it through `apt` or anu other package manager as those are not as frequently updated as it is on the official website*.

10. Configure theme and colors
    1. Install [Canta theme](https://github.com/vinceliuice/Canta-theme)
       1. *__Important note__: If used with sudo the theme will install in /usr/share/themes, not in ~/.themes - this will allow GUI apps (e.g. Files, Terminal) to use that theme when running in the elevated privileges mode.*
    2. Configure theme
       ( Settings $\to$ Themes )
    3. Install icon themes *[how-to](https://itsfoss.com/install-icon-linux-mint/)*
       1. [Flat remix](https://drasite.com/flat-remix )
       2. [Papirus icon theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme#installation)
       <!-- spellchecker: disable-next-line -->
       3. [Quintom Cursors](https://www.gnome-look.org/p/1329799/)

11. Configure the bottom panel
    1.  TODO: describe the process

12. Adjust mouse *(and touchpad)* settings ( Settings $\to$ Mouse and Touchpad )

13. Disable system sounds

14. Enable *'Prevent focus stealing'* ( Settings $\to$ Windows )

15. Disable switching between open windows by middle-clicking to avail new tab opening in programs that use that mouse click for some shortcut inside this program ( Settings $\to$ Windows )

16. Disable auto-rotate ( Settings $\to$ General )

17. Add more keyboard layouts (PL, FR, DE)

18. Disable *'Global hotkey for cycling through thumbnail menus'* from Grouped window list. To access that settings panel, click on an icon of multiple windows in the panel, then Preferences, then Configure. [Details here](https://forums.linuxmint.com/viewtopic.php?t=291898)

19. Change panel opened programs viewing mode to show all titles

20. Enable switching between keyboard layouts ( Settings $\to$ Keyboard $\to$ Layouts $\to$ Options )

21. Install additional fonts into `/usr/share/fonts/truetype/`
    1.  Fira Sans
    2.  Fira Code
    3.  Fira Mono
    4.  [All above as package here from Google Fonts](https://fonts.google.com/selection?query=fira&selection.family=Fira+Code%7CFira+Mono%7CFira+Sans)
    5.  [Drogowskaz Classic](http://www.drogowskazclassic.pl/pismo.php)

22. *Optional* Change default font ( System Settings $\to$ Font Selection )

23. [Setup automount for the rest of the drives present in the system](https://fossbytes.com/how-to-auto-mount-partitions-on-boot-in-linux-easily/)

24. *Optional* [Setup switching workspaces via touchpad gestures](https://github.com/Hikari9/comfortable-swipe)

25. Change login page background image ( Administration $\to$ Login Window )
<!-- spellchecker: disable-next-line -->
26. *Optional* [Setup listening to line-in audio at startup `pacmd load-module module-loopback latency_msec=5`](https://unix.stackexchange.com/questions/263274/pipe-mix-line-in-to-output-in-pulseaudio)

27. *Optional* [Japanese keyboard layout](https://forums.linuxmint.com/viewtopic.php?t=160272)
    1.  Note: for now it seems there is no *convenient* way to write in Hiragana or Katakana in Linux. Windows has better support for non-western dialects.

28. Install [Blender](https://www.blender.org/download/) with all the [addons](blender-notes.md#addons).

29. Install the rest of programs from the [software list](software-list.md).

## Issues

1. [The Cinnamon Desktop Environment currently doesn't support more than four keyboard layouts for some odd reason.](https://github.com/linuxmint/cinnamon/issues/3212#issuecomment-337725452)
