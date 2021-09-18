#!/bin/bash -i

# print messages
ECHO="printf \033[1m%s\033[0m\n"


# the fix that disables the notification toasts from appearing
fix='<style> .notifications-toasts { display: none !important; } </style>'


# get the version of VS Code the user is using (can be either `code` or `code-insiders`)
code_version=$(alias | grep ' c=')

if [ "$?" -ne 0 ]; then
    $ECHO 'You need to have the `c` alias set to “fix” VS Code. (e.g. `alias c=code`)'
    $ECHO 'Provide the VS Code version you’re using: (usually `code` or `code-insiders`)'
    read code_version
else
    # extract the VS Code version from the alias output
    code_version=$(echo "$code_version" | awk -F"'" '{print $2}')
fi

code_root=$(whereis $code_version | awk '{print $3}')

if [ -z "$code_root" ]; then
    $ECHO 'The root directory of VS Code could not be established. Please provide one:'
    read code_root
fi

if [ -z "$code_root" ]; then
    $ECHO 'The root directory of VS Code could not be established.'
    exit 1
fi

# the main entrypoint of VS Code
file="$code_root/resources/app/out/vs/code/electron-browser/workbench/workbench.html"

# check if the fix is already there
grep "$fix" "$file" >/dev/null
if [ "$?" -ne 0 ]; then
    # apply the “fix”
    echo "$fix" | sudo tee -a "$file" >/dev/null
else
    $ECHO 'The fix is already applied.'
    exit 0
fi
