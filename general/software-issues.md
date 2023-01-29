---
lang: 'en-GB'
title: 'Software issues'
author: 'Jerry Sky'
description: 'Notes on some of the software issues that I’ve encountered.'
keywords: 'SQL, MariaDB, issues, database, plugin'
---



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



---

## DirectX for older games

For running some older games an additional installation of Microsoft provided
redistributales is required.

- [Microsoft DirectX® End-User Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=35)
    > The Microsoft DirectX® End-User Runtime installs a number of runtime libraries from the legacy DirectX SDK for some games that use D3DX9, D3DX10, D3DX11, XAudio 2.7, XInput 1.3, XACT, and/or Managed DirectX 1.1. Note that this package does not modify the DirectX Runtime installed on your Windows OS in any way.

- [Microsoft Visual C++ Redistributable latest supported downloads](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)
    > The Visual C++ Redistributable installs Microsoft C and C++ (MSVC) runtime libraries. These libraries are required by many applications built by using Microsoft C and C++ tools. If your app uses those libraries, a Microsoft Visual C++ Redistributable package must be installed on the target system before you install your app. The Redistributable package architecture must match your app's target architecture. The Redistributable version must be at least as recent as the MSVC build toolset used to build your app. We recommend you use the latest Redistributable available for your version of Visual Studio, with some exceptions noted later in this article.
