# PC Setup
  #### A personal guide for setting up all programs, tools and configurations for personal use be it work or rest.

## Definitions
Following statements are crucial to perform [steps from the next section](#steps-to-reproduce).

1. Cloud $\equiv$ Dropbox
2. Internet Browser $\equiv$ Vivaldi
3. Software Manager $\equiv$ Software Manager that is *basically* a GUI for `apt` in Linux Mint

## Steps to reproduce

### Installing the OS

#### Install the Linux Mint Cinnamon distribution.

1. Install it from a prepared bootable USB stick.
2. If no bootable USB stick is available perform following actions:
   1. Download the ISO from [the official website](https://linuxmint.com/download.php).
   2. Install etcher.io on a secondary PC.
   3. Use etcher.io to put the OS ISO on an arbitrary USB stick.
   4. Install the OS by booting the target PC from the USB stick.

### Configuring the Internet browser

   1. Install the [Internet Browser](#definitions).
   2. Install [Bitwarden](https://bitwarden.com/#download).
   3. Install [Dark Reader](https://chrome.google.com/webstore/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh).
   4. Log in to all online services
      1. [**Google**](accounts.google.com/)
      2. [**GitHub**](https://github.com/login)
      3. [WhatsApp](https://web.whatsapp.com/)
      4. [Discord](https://discordapp.com/channels/@me)
      5. [*Facebook Messenger*](https://www.messenger.com/)
   5. Change default browser to the [Internet Browser](#definitions).
   6. *(Opera-only) [Enable DRM to view DRM-content such as Prime Video or Netflix etc.](https://forums.opera.com/topic/28663/widevine-and-opera/29)*

### Programs

1. Install the [Cloud](#definitions) Desktop app.

2. Enable Redshift
   1. Copy the config file from [Cloud](#definitions)`/Settings & Presets/Linux/` to `~/.config/`
   2. Enable autostart

3. Install Git
   1. `sudo apt install git`
   2. Install [credentials manager](https://stackoverflow.com/questions/36585496/error-when-using-git-credential-helper-with-gnome-keyring-as-sudo/40312117#40312117)
   3. Create new [personal github access token](https://github.com/settings/tokens)
   4. At first login provide the token as the password

4. Install [VS Code](https://code.visualstudio.com/)
    - *Note: __don't__ install it through `apt` or anu other package manager as those are not as frequently updated as it is on the official website*.

5. Install [Blender](https://www.blender.org/download/) with all the [addons](blender-notes.md#addons).

6. ~~Install Spotify (Software Manager)~~
   1. *For now, the [web-based app](https://open.spotify.com/collection/playlists) seems to be working fine.*

7. Install [`snap`](https://snapcraft.io/docs/installing-snap-on-linux-mint)

8. ~~Install barrier (Snap)~~

9.  Install GParted from [Software Manager](#definitions) or `sudo apt install gparted`

10. Install the rest of programs from the [software list](software-list.md).

### Configuring the user experience

1.  Configure theme and colours
    1. Install [Canta theme](https://github.com/vinceliuice/Canta-theme)
       1. *__Important note__: If used with sudo the theme will install in /usr/share/themes, not in ~/.themes - this will allow GUI apps (e.g. Files, Terminal) to use that theme when running in the elevated privileges mode.*
    2. Configure theme
       ( Settings $\to$ Themes )
    3. Install icon themes *[how-to](https://itsfoss.com/install-icon-linux-mint/)*
       1. [Flat remix](https://drasite.com/flat-remix )
       2. [Papirus icon theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme#installation)
       <!-- spellchecker: disable-next-line -->
       1. [Quintom Cursors](https://www.gnome-look.org/p/1329799/)

2. Configure the bottom panel
   - //TODO: describe the process

3. Adjust mouse *(and touchpad)* settings ( Settings $\to$ Mouse and Touchpad )

4. Disable system sounds

5. Enable *'Prevent focus stealing'* ( Settings $\to$ Windows )

6. Disable switching between open windows by middle-clicking to avail new tab opening in programs that use that mouse click for some shortcut inside this program ( Settings $\to$ Windows )

7. Disable auto-rotate ( Settings $\to$ General )

8. Disable *'Global hotkey for cycling through thumbnail menus'* from Grouped window list. To access that settings panel, click on an icon of multiple windows in the panel, then Preferences, then Configure. [Details here](https://forums.linuxmint.com/viewtopic.php?t=291898)

9.  Change panel opened programs viewing mode to show all titles.

10. Enable switching between keyboard layouts ( Settings $\to$ Keyboard $\to$ Layouts $\to$ Options ).

11.  Change login page background image ( Administration $\to$ Login Window )

12. *Optional* [Setup switching workspaces via touchpad gestures](https://github.com/Hikari9/comfortable-swipe)

<!-- spellchecker: disable-next-line -->
13. *Optional* [Setup listening to line-in audio at startup `pacmd load-module module-loopback latency_msec=5`](https://unix.stackexchange.com/questions/263274/pipe-mix-line-in-to-output-in-pulseaudio)

### Keyboard layout settings

1. Install [IBus](https://forums.linuxmint.com/viewtopic.php?t=160272) to allow using non-western keyboard layouts and allow using more than 4 keyboard layouts at once.
    1.  Should any issues arise, follow instructions provided in [this askubuntu.com answer](https://askubuntu.com/a/793046).

2. For laptops with no dedicated `Menu` key you need to swap `Control_R` with `Menu` to use the `Control_R` key as the `Menu` key:
    ```bash
    xmodmap -e "keycode 105 = Menu"
    xmodmap -e "keycode 135 = Control_R"
    ```
    To view list of all keycodes use `xmodmap -pk`.
    To make this behaviour persistent put above commands into the `.profile` file.

### Additional packages

1. Install additional fonts into `/usr/share/fonts/truetype/`
    1.  Fira Sans
    2.  Fira Code
    3.  Fira Mono
    4.  [All above as package here from Google Fonts](https://fonts.google.com/selection?query=fira&selection.family=Fira+Code%7CFira+Mono%7CFira+Sans)
    5.  [Drogowskaz Classic](http://www.drogowskazclassic.pl/pismo.php)
    6.  *Optional* Change default font ( System Settings $\to$ Font Selection )

### Other system settings

1.  [Setup automount for the rest of the drives present in the system](https://fossbytes.com/how-to-auto-mount-partitions-on-boot-in-linux-easily/)

## Issues

1. The Cinnamon Desktop Environment currently doesn't support more than four keyboard layouts for some odd reason ([the issue on GitHub](https://github.com/linuxmint/cinnamon/issues/3212#issuecomment-337725452)).
   - However, this issue can be resolved by installing IBus as described above in the [Keyboard layout settings](#keyboard-layout-settings) section.
