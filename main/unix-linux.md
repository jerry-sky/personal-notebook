# Unix & Linux

## Index

  - [Keeping some script/program alive](#keeping-some-scriptprogram-alive)
  - [ANSI Text Attributes](#ansi-text-attributes)

## Keeping some script/program alive

If you want to keep some script/program alive (e.g. a node.js script) you need to use `crontab`.

The command
```bash
crontab -e
```
opens a crontab jobs file in the default editor that contains all the cron jobs that are being run for current user.

You can add a reference to a bash script that runs desired script/program or normal reference to the script/program that needs to be run. You can set the time conditions confining the moments in which desired script/program will be run.

It is advised that the program is shut down before running it again.


## ANSI Text Attributes

<!-- spellchecker: disable-next-line -->
`Esc[Value;...;Valuem`

### Text effects
 Code | Description
------|----------------------------
 0    | All attributes off
 1    | Bold on
 4    | Underscore (on monochrome display adapter only)
 5    | Blink on
 7    | Reverse video on
 8    | Concealed on

### Text colours
#### Foreground colors
 Code | Description
------|----------------------------
 30   | Black
 31   | Red
 32   | Green
 33   | Yellow
 34   | Blue
 35   | Magenta
 36   | Cyan
 37   | White

#### Background colors
 Code | Description
------|----------------------------
 40   | Black
 41   | Red
 42   | Green
 43   | Yellow
 44   | Blue
 45   | Magenta
 46   | Cyan
 47   | White

*Parameters 30 through 47 meet the ISO 6429 standard.*

[Source](https://github.com/drmingdrmer/cheatsheet/blob/master/sheets/bash/ansi-escape-sequence)

