# Software issues

## Index

  - [Fix *MariaDB plugin `unix_socket` is not loaded* issue](#fix-mariadb-plugin-unixsocket-is-not-loaded-issue)

## Fix *MariaDB plugin `unix_socket` is not loaded* issue

Add
```config
plugin-load-add = auth_socket.so
```
under `[mysqld]` section in file
```bash
/etc/mysql/mariadb.conf.d/50-server.cnf
```

Then, restart the MariaDB service
```bash
sudo systemctl restart mariadb.service
```
[Source](https://websiteforstudents.com/fix-mariadb-plugin-unix_socket-is-not-loaded-error-on-ubuntu-17-04-17-10/)
