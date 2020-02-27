# Unix & Linux

## Index

  - [Keeping some script/program alive](#keeping-some-scriptprogram-alive)
  - [ANSI Text Attributes](#ansi-text-attributes)
  - [Customizing `bash` prompt](#customizing-bash-prompt)

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

## Customizing `bash` prompt

When configuring the `bash` prompt you would use ANSI escape sequences to enhance the [text formatting](#ansi-text-attributes) to make it more visually appealing. However, inserting an ANSI escape sequence is a lot of characters that amount to special usage and *no physical characters*. That's why we need to mark these sequences as *zero-length* to prevent the bash from being confused where does the actual prompt end.\
Every time you insert an ANSI escape sequence wrap it inside `\[<prompt>\]`.\
[Source](https://unix.stackexchange.com/a/28828)
