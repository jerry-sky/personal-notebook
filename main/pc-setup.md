# PC Setup

*A personal guide for setting up all programs, tools and configuration files for personal use.*

- [Definitions](#definitions)
- [Guide](#guide)
  - [Installing the OS](#installing-the-os)
  - [Configuration](#configuration)
  - [Configuring the Internet browser](#configuring-the-internet-browser)
  - [Programs](#programs)
  - [Configuring the user experience](#configuring-the-user-experience)
  - [Keyboard layouts](#keyboard-layouts)
  - [Fonts](#fonts)
  - [Other system settings](#other-system-settings)

## Definitions

*Software solutions currently used.*

1. OS $\equiv$ Linux Mint Cinnamon ([OS-specific setup](linux-mint-setup.md))
2. Cloud $\equiv$ [InSync](https://www.insynchq.com/)
3. Internet Browser $\equiv$ [Opera](https://www.opera.com/de/download)

## Guide

### Installing the OS

Please see the OS-specific instructions in a separate note. See [definitions](#definitions).

### Configuration

Copy this repository to `~/notebooks/personal-notebook` using `git clone`.

Run the `setup.sh` script from the `/config` directory of this repository to copy various config files to the system.\
See [«config»](../config/readme.md).

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
   6. *(Opera-only) – if Opera doesn't play some video content use one of these solutions:*
      - [Enable DRM to view DRM-content such as Prime Video or Netflix etc.](https://forums.opera.com/topic/28663/widevine-and-opera/29)
      - [Fix `libffmpeg.so`](https://forums.opera.com/topic/30254/solved-video-playback-issues/7)

### Programs

1. Install the [Cloud](#definitions) desktop app.

2. Enable Redshift
   1. Install `redshift` if it is not already installed.
   2. Enable autostart.

3. Install [`snap`](https://snapcraft.io/docs/installing-snap-on-linux-mint)

4. Configure Git
   1. Install the [credentials manager](https://stackoverflow.com/questions/36585496/error-when-using-git-credential-helper-with-gnome-keyring-as-sudo/40312117#40312117).
   2. Create a new [personal github access token](https://github.com/settings/tokens).
   3. At first login provide the newly generated token as the password.

5. Install VS Code\
   Using
   ```sh
   apt list -a code-insiders | less
   ```
   and
   ```sh
   apt install code-insiders=«version from the list; e.g. “1.48.0-1596120937”»
   ```
   establish what version is currently free of irritating Electron-related issues (e.g. white flashes) and install it.

6. Install Blender
    1. Download it from the [downloads page](https://www.blender.org/download/).
    2. Unpack it:
    ```sh
    tar -xf «archive filename»
    ```
    3. Move the contents to `/opt/blender`.
    4. Link the executable:
    ```sh
    ln -s /opt/blender/blender /usr/bin/blender
    ```
    5. Install the [addons](blender-notes.md#addons) if necessary.

7. Install GParted `apt install gparted`

8.  Install the rest of programs from the [software list](software-list.md).

### Configuring the user experience

1. Disable icons on the desktop.

2.  Install themes and cursor packs
    1. Install [Canta theme](https://github.com/vinceliuice/Canta-theme)
       1. *__Important note__: If used with sudo the theme will install in /usr/share/themes, not in ~/.themes - this will allow GUI apps (e.g. Files, Terminal) to use that theme when running in the elevated privileges mode.*
    2. Install icon themes *[how-to](https://itsfoss.com/install-icon-linux-mint/)*
       1. [Flat remix](https://drasite.com/flat-remix )
       2. [Papirus icon theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme#installation)
          <!-- spellchecker: disable-next-line -->
       3. [Quintom Cursors](https://www.gnome-look.org/p/1329799/)

3. Adjust mouse *(and touchpad)* settings.

4. Disable system sounds.

5. Follow the rest of the steps of this section in the OS-specific notes. See [definitions](#definitions).

    <!-- spellchecker: disable-next-line -->
6. *Optional* [Setup listening to line-in audio at startup `pacmd load-module module-loopback latency_msec=5`](https://unix.stackexchange.com/questions/263274/pipe-mix-line-in-to-output-in-pulseaudio)

### Keyboard layouts

1. Install [IBus](https://forums.linuxmint.com/viewtopic.php?t=160272) to allow using non-western keyboard layouts and allow using more than 4 keyboard layouts at once.
    1.  Should any issues arise, follow instructions provided in [this askubuntu.com answer](https://askubuntu.com/a/793046).

2. For laptops with no dedicated `Menu` key you need to swap `Control_R` with `Menu` to use the `Control_R` key as the `Menu` key:
    ```bash
    xmodmap -e "keycode 105 = Menu"
    xmodmap -e "keycode 135 = Control_R"
    ```
    To view list of all keycodes use `xmodmap -pk`.
    To make this behaviour persistent use [config](../config/readme.md) found in this repository.

### Fonts

1. Install additional fonts into `/usr/share/fonts/truetype/`
    1.  Fira Sans
    2.  Fira Code
    3.  Fira Mono
    4.  [All above as a package here from Google Fonts](https://fonts.google.com/selection?query=fira&selection.family=Fira+Code%7CFira+Mono%7CFira+Sans)
    5.  [Drogowskaz Classic](http://www.drogowskazclassic.pl/pismo.php)

### Other system settings

1.  [Setup automount for the rest of the drives present in the system.](https://fossbytes.com/how-to-auto-mount-partitions-on-boot-in-linux-easily/)
