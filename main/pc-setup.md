# PC Setup
*A personal guide for setting up all programs, tools and configurations for personal use be it work or rest.*

## Definitions
Following statements are crucial to perform [steps from the next section](#steps-to-reproduce).

1. OS $\equiv$ [Linux Mint Cinnamon](linux-mint-setup.md)
2. Cloud $\equiv$ Dropbox
3. Internet Browser $\equiv$ Vivaldi

## Steps to reproduce

### Installing the OS

Please see the OS-specific instructions in a separate note. See [definitions](#definitions).

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

### Configuration

Run the `setup.sh` script from the `/config` directory of this repository to copy various config files to the system.\
See [config](../config/readme.md).

### Programs

1. Install the [Cloud](#definitions) Desktop app.

2. Enable Redshift
   1. Install `redshift` if it is not already installed.
   2. Enable autostart.

3. Install [`snap`](https://snapcraft.io/docs/installing-snap-on-linux-mint)

4. Install Git
   1. `sudo apt install git`
   2. Install [credentials manager](https://stackoverflow.com/questions/36585496/error-when-using-git-credential-helper-with-gnome-keyring-as-sudo/40312117#40312117)
   3. Create new [personal github access token](https://github.com/settings/tokens)
   4. At first login provide the token as the password

5. Install [VS Code](https://code.visualstudio.com/)
    - *Note: __don't__ install it through `apt` or any other package manager as those are not as frequently updated as it is on the official website*.

6. Install Blender
    ```bash
    sudo snap install blender --classic
    ```
    with all the [addons](blender-notes.md#addons).

7. Install GParted `sudo apt install gparted`

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

### Keyboard layout settings

1. Install [IBus](https://forums.linuxmint.com/viewtopic.php?t=160272) to allow using non-western keyboard layouts and allow using more than 4 keyboard layouts at once.
    1.  Should any issues arise, follow instructions provided in [this askubuntu.com answer](https://askubuntu.com/a/793046).

2. For laptops with no dedicated `Menu` key you need to swap `Control_R` with `Menu` to use the `Control_R` key as the `Menu` key:
    ```bash
    xmodmap -e "keycode 105 = Menu"
    xmodmap -e "keycode 135 = Control_R"
    ```
    To view list of all keycodes use `xmodmap -pk`.
    To make this behaviour persistent use [config](../config/readme.md) found in this repository.

### Additional packages

1. Install additional fonts into `/usr/share/fonts/truetype/`
    1.  Fira Sans
    2.  Fira Code
    3.  Fira Mono
    4.  [All above as a package here from Google Fonts](https://fonts.google.com/selection?query=fira&selection.family=Fira+Code%7CFira+Mono%7CFira+Sans)
    5.  [Drogowskaz Classic](http://www.drogowskazclassic.pl/pismo.php)
    6.  *Optional* Change default font ( System Settings $\to$ Font Selection )

### Other system settings

1.  [Setup automount for the rest of the drives present in the system.](https://fossbytes.com/how-to-auto-mount-partitions-on-boot-in-linux-easily/)
