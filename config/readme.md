# Config

- [Setup](#setup)
- [Utility scripts](#utility-scripts)

---

## Setup

In the same directory as this document there is a file called `setup.sh` which copies various config files into all sorts of locations.
It's part of the [standard JRS PC Setup](../main/pc-setup.md) to configure the system and its programs.
Execute it whilst being in the `/config` directory to setup a proper workspace.
```bash
./setup.sh
```

---

### Keyboard volume knob configuration

The config setup script allows to copy some utility scripts that enable to override the default behaviour of Volume Media keys. Some keyboards have a scrollable knob that normally controls the volume. Because of these scripts (and properly configured keyboard shortcuts to these scripts) this volume knob can be utilised as mouse scroll wheel or volume knob. The *mute* button switches between `scroll` and `volume` modes.

---

## Utility scripts

The `utility-scripts` directory contains some other useful scripts that are sometimes very handy.

- [`fix-iso-date-file-contents.sh`](utility-scripts/fix-iso-date-file-contents.sh) & [`fix-iso-date-filenames.sh`](utility-scripts/fix-iso-date-filenames.sh) – these scripts fix all pseudo ISO-like dates that don't have a leading zero before a single-digit day number (e.g. 2020-04-**4** instead of 2020-04-**04**)
- [`cinnamon-keyboard-shortcuts-dump.sh`](utility-scripts/cinnamon-keyboard-shortcuts-dump.sh) – dumps all the keyboard shortcuts settings into a `.conf` file for archival and later repurpose (it is used when [running `./setup.sh`](#setup))
