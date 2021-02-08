#!/bin/bash

source "dconf-prefix.sh"

# dump only the `/` (root) part of the Cinnamon settings
dconf_prefix org/cinnamon | perl -nle 'if ( /.+/g ) { print $& } elsif ( /^$/g ) { print ""; exit 0 }' > other-settings.conf

# dump the rest of the settings
dconf_prefix org/cinnamon/sounds >> other-settings.conf
dconf_prefix org/cinnamon/settings-daemon >> other-settings.conf
dconf_prefix org/cinnamon/desktop/background >> other-settings.conf
dconf_prefix org/cinnamon/desktop/media-handling >> other-settings.conf
dconf_prefix org/cinnamon/desktop/screensaver >> other-settings.conf
dconf_prefix org/cinnamon/desktop/sound >> other-settings.conf
