# VS Code

- [Settings Sync](#settings-sync)
- [Java Formatter Settings](#java-formatter-settings)

## Settings Sync

Install:
```bash
ext install Shan.code-settings-sync
```

- SHIFT + ALT + U/D $\equiv$ upload/download settings to/from gist

## Java Formatter Settings

The Java formatter for VS Code is currently a joke. According to [the official guide](https://github.com/redhat-developer/vscode-java/wiki/Formatter-settings) on how to change the settings of the formatter it is advised to use Eclipse to alter the settings.

The default settings are atrocious - formatter doesn't allow for additional newlines that enable code readability or doesn't align the `case` statements with the `switch` statement properly. As the result of that, I keep my personal formatter settings file in my [Cloud Storage solution](pc-setup.md#definitions).

