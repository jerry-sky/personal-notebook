
# this function prefixes all `dconf` sections with the given dump source
#
# example:
#
# [relative-settings]
# variable=value
#
# would be converted to
#
# [org/some-parent-settings/relative-settings]
# variable=value
#
function dconf_prefix() {
    dconf dump "/$1/" | \
        perl -nle '
            if ( /^\[\/\]$/g ) { print "['$1']" }
            elsif ( /^(\[)(.+)/g ) { print "['$1'/$2" }
            elsif ( /^$/g ) { print "" }
            elsif ( /.+/g ) { print $& }
        '
    printf "\n"
}
