# Linux Server Maintenance

## Keeping some script/program alive

If you want to keep some script/program alive (e.g. a node.js script) you need to use `crontab`.

The command
```bash
crontab -e
```
opens a crontab jobs file in the default editor that contains all the cron jobs that are being run for current user.

You can add a reference to a bash script that runs desired script/program or normal reference to the script/program that needs to be run. You can set the time conditions confining the moments in which desired script/program will be run.

It is advised that the program is shut down before running it again.
