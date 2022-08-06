---
lang: 'en-GB'
title: 'Unix & Linux'
author: 'Jerry Sky'
description: 'Notes related to Unix-based operating systems.'
keywords: 'linux, notes, unix, bash, wget, ansi, customizing, custom, customization, script, program, dns, server'
---

---

- [Keeping some script/program alive](#keeping-some-scriptprogram-alive)
- [ANSI Text Attributes](#ansi-text-attributes)
    - [Text effects](#text-effects)
- [Customizing `bash` prompt](#customizing-bash-prompt)
- [Redirecting `stdout` to `stderr`](#redirecting-stdout-to-stderr)
- [Downloading a whole website using `wget`](#downloading-a-whole-website-using-wget)
- [Permanently setting the DNS server](#permanently-setting-the-dns-server)
- [Fixing broken packages (downloaded from an external PPA) by forcefully overwriting `apt` packages](#fixing-broken-packages-downloaded-from-an-external-ppa-by-forcefully-overwriting-apt-packages)
- [Useful PDF tools](#useful-pdf-tools)
- [Pass URL/ file argument to program defined by a `.desktop` file](#pass-url-file-argument-to-program-defined-by-a-desktop-file)
- [Routing VLC audio output to a specific PulseAudio sink](#routing-vlc-audio-output-to-a-specific-pulseaudio-sink)
- [Pretty printing JSON data](#pretty-printing-json-data)
- [Compressing images](#compressing-images)

---

## Keeping some script/program alive

If you want to keep some script/program alive (e.g. a node.js script) you need to use `crontab`.

The command

```bash
crontab -e
```

opens a crontab jobs file in the default editor that contains all the cron jobs that are being run for current user.

You can add a reference to a bash script that runs desired script/program or normal reference to the script/program that needs to be run. You can set the time conditions confining the moments in which desired script/program will be run.

It is advised that the program is shut down before running it again.

---

## ANSI Text Attributes

<!-- spellchecker: disable-next-line -->
`Esc[Value;...;Valuem`

### Text effects

| Code    | Effect                       | Note                                                                   |
| ------- | ---------------------------- | ---------------------------------------------------------------------- |
| 0       | Reset / Normal               | all attributes off                                                     |
| 1       | Bold or increased intensity  |                                                                        |
| 2       | Faint (decreased intensity)  | Not widely supported.                                                  |
| 3       | Italic                       | Not widely supported. Sometimes treated as inverse.                    |
| 4       | Underline                    |                                                                        |
| 5       | Slow Blink                   | less than 150 per minute                                               |
| 6       | Rapid Blink                  | MS-DOS ANSI.SYS; 150+ per minute; not widely supported                 |
| 7       | [[reverse video]]            | swap foreground and background colors                                  |
| 8       | Conceal                      | Not widely supported.                                                  |
| 9       | Crossed-out                  | Characters legible, but marked for deletion.  Not widely supported.    |
| 10      | Primary(default) font        |                                                                        |
| 11–19   | Alternate font               | Select alternate font `n-10`                                           |
| 20      | Fraktur                      | hardly ever supported                                                  |
| 21      | Bold off or Double Underline | Bold off not widely supported; double underline hardly ever supported. |
| 22      | Normal color or intensity    | Neither bold nor faint                                                 |
| 23      | Not italic, not Fraktur      |                                                                        |
| 24      | Underline off                | Not singly or doubly underlined                                        |
| 25      | Blink off                    |                                                                        |
| 27      | Inverse off                  |                                                                        |
| 28      | Reveal                       | conceal off                                                            |
| 29      | Not crossed out              |                                                                        |
| 30–37   | Set foreground color         | See color table below                                                  |
| 38      | Set foreground color         | Next arguments are `5;n` or `2;r;g;b`, see below                       |
| 39      | Default foreground color     | implementation defined (according to standard)                         |
| 40–47   | Set background color         | See color table below                                                  |
| 48      | Set background color         | Next arguments are `5;n` or `2;r;g;b`, see below                       |
| 49      | Default background color     | implementation defined (according to standard)                         |
| 51      | Framed                       |                                                                        |
| 52      | Encircled                    |                                                                        |
| 53      | Overlined                    |                                                                        |
| 54      | Not framed or encircled      |                                                                        |
| 55      | Not overlined                |                                                                        |
| 60      | ideogram underline           | hardly ever supported                                                  |
| 61      | ideogram double underline    | hardly ever supported                                                  |
| 62      | ideogram overline            | hardly ever supported                                                  |
| 63      | ideogram double overline     | hardly ever supported                                                  |
| 64      | ideogram stress marking      | hardly ever supported                                                  |
| 65      | ideogram attributes off      | reset the effects of all of 60-64                                      |
| 90–97   | Set bright foreground color  | aixterm (not in standard)                                              |
| 100–107 | Set bright background color  | aixterm (not in standard)                                              |

Using `\033[38;5;206m` you're accessing the 256-colour-palette. Replace `38` with `48` and you'll be altering the background colour.

To get even more colours use `\033[38;2;R;G;Bm` to use full RGB spectrum by replacing `R`, `G` and `B` with values from range of `0-255`.

[Source](https://stackoverflow.com/a/33206814/4249875)

---

## Customizing `bash` prompt

When configuring the `bash` prompt you would use ANSI escape sequences to enhance the [text formatting](#ansi-text-attributes) to make it more visually appealing. However, inserting an ANSI escape sequence is a lot of characters that amount to special usage and *no physical characters*. That's why we need to mark these sequences as *zero-length* to prevent the bash from being confused where does the actual prompt end.\
Every time you insert an ANSI escape sequence wrap it inside `\[«ANSI escape sequence»\]`.

[Source](https://unix.stackexchange.com/a/28828)

---

## Redirecting `stdout` to `stderr`

To redirect `stdout` to `stderr` just add `>&2 echo 'error` at the end of the command you want to execute.

---

## Downloading a whole website using `wget`

Using `wget` you can download a whole webpage with all the resources that are referenced through links on that webpage.
It can be a very useful tool for archiving websites.

Executing

```bash
wget -rpl1 --tries=3 https://example.com
```

will download the webpage and all PDFs, images and other resources that appear on that webpage to a folder called `example.com`.

There is a possibility that above command will not work on first try.
For example the HTML file containing the markup may have been downloaded,
but the resources that appear on that webpage couldn't have been downloaded.
Then, using this website in HTML (or otherwise) form we can download the rest of the resources.

```bash
wget -rpl1 --tries=3 --base=https://example.com/subpage --force-html --relative -i example.com/subpage/index.html
```

Executing above command will download all resources that appear on this subpage.
All relative links will be preceded with the URL provided with the `--base` option.

---

## Permanently setting the DNS server

First, we need to install the `resolvconf` package:

```bash
sudo apt update
sudo apt install resolvconf
```

Now, let's add the IP address of the desired DNS server.\
Edit following file:

```bash
sudo nvim /etc/resolvconf/resolv.conf.d/head
```

adding line below to make `1.1.1.1` the DNS server:

```txt
nameserver 1.1.1.1
```

[Source](https://www.tecmint.com/set-permanent-dns-nameservers-in-ubuntu-debian/)

---

## Fixing broken packages (downloaded from an external PPA) by forcefully overwriting `apt` packages

Sometimes adding external PPAs results in broken packages and the infamous error:

```log
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
```

One solution would be to remove that PPA

```bash
sudo add-apt-repository --remove ‹PPA›
```

and to forcefully overwrite the broken packages from software sources that were already present in the system.

```bash
sudo apt install -o Dpkg::Options::="--force-overwrite" --fix-broken
```

[Source](https://unix.stackexchange.com/a/624842)

---

## Useful PDF tools

1. PDF to PNG:
    ```bash
    pdftoppm pdf.pdf result -png
    ```
    [Source](https://askubuntu.com/a/50180)

2. Merge two PDFs side-by-side:
    ```bash
    pdfjam one.pdf two.pdf --nup 2x1 --landscape --outfile merged.pdf
    ```
    [Source](https://superuser.com/q/917190/746117)

---

## Pass URL/ file argument to program defined by a `.desktop` file

Programs can accept links/ paths to remote/ local files as arguments.
The `.desktop` files handles that by adding `%u` or `%U` at the end of the `Exec` parameter.

- `%u` — only one URL can be passed
- `%U` — multiple URLs can be passed

Usage example:

```desktop
[Desktop Entry]
Name=Google Chrome
Exec=/usr/bin/google-chrome-stable %U
Type=Application
Categories=Network;WebBrowser;
# […]
```

Source: [Desktop specification — The Exec key](https://specifications.freedesktop.org/desktop-entry-spec/latest/ar01s07.html)

---

## Routing VLC audio output to a specific PulseAudio sink

To force VLC to play audio to a device different from the default one
run it with temporarily set Pulse sink variable like so:

```bash
PULSE_SINK=$sink_id cvlc file.mp3
```

Source: [Answer on SuperUser](https://superuser.com/a/494404)

---

## Pretty printing JSON data

Example:

```bash
echo '{
    "items": [
        {
            "name": "One",
            "description": "the one and only",
            "labels": [
                "Not funny",
                "A label"
            ]
        },
        {
            "name": "Two",
            "description": "the sequel",
            "labels": [
                "Yup"
            ]
        }
    ]
}' \
| jq -j '.items[] | .name, " (", .description, ") [ ", (.labels | join(", ")), " ]\n"'
```

Sources: self, [Answer on Unix StackExchange](https://unix.stackexchange.com/a/451499)

---

## Compressing images

```bash
convert -strip -interlace Plane -gaussian-blur 0.05 -quality 85% source.jpg result.jpg
```

Using `convert` from the `imagemagick` package you can cut down on size for image files.

Source: [Answer on StackOverflow](https://stackoverflow.com/a/7262050)

---



## Nvidia + Intel flickering

To resolve flickering for laptops with Nvidia+Intel graphics turn off PSR.

PSR is Intel’s Panel Self Refresh setting which caches some frames to display them later.
This functionality may cause these flickering problems because of some
memory leaking from the frame buffer, causing the display to show unsynced content.

To verify PSR is turned on run
```bash
cat /sys/kernel/debug/dri/0/i915_edp_psr_status
```
with root privileges.

If it is indeed turned on, modify `/etc/default/grub`:
```diff
-GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
+GRUB_CMDLINE_LINUX_DEFAULT="quiet splash i915.enable_psr=0"
```
and run
```bash
update-grub
```
with root privileges to turn this feature off and reboot the computer to apply the changes.


Source: [Lj Miranda](https://ljvmiranda921.github.io/notebook/2021/09/01/linux-thinkpad-screen-flicker/)
