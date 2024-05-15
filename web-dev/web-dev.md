---
lang: 'en-GB'
title: 'Web dev'
author: 'Jerry Sky'
description: 'My notes on various web-dev related matters.'
keywords: 'web, development, Angular, NodeJS, ExpressJS, JS, JavaScript, TypeScript, SQL, CSS, SCSS, Sass, links, resources, tcp, port'
---



## Resources


### Security

- [Your NodeJS authentication tutorial is (probably) wrong](https://hackernoon.com/your-node-js-authentication-tutorial-is-wrong-f1a3bf831a46)
- [`secure-password`](https://github.com/emilbayes/secure-password)
- [How to stop me harvesting credit card numbers and passwords from your site](https://hackernoon.com/part-2-how-to-stop-me-harvesting-credit-card-numbers-and-passwords-from-your-site-844f739659b9)
- [PHP Cookies security](https://www.simonholywell.com/post/2013/05/improve-php-session-cookie-security/)
- [Remember me Safely](http://wayback.archive.org/web/20150204143440/https://resonantcore.net/blog/2015/02/remember-me-safely-secure-long-term-authentication-strategies)


### Interesting

- [You don't hate JavaScript](https://medium.com/edge-coders/you-dont-hate-javascript-62cd6c609d43)
- [The Post JavaScript Apocalypse](https://www.youtube.com/watch?v=99Zacm7SsWQ)


### Building

- [How to build your own team chat in five days](https://fdietz.github.io/2015/04/13/day-1-how-to-build-your-own-team-chat-in-five-days.html)
- [A tale of webpage speed, or throwing away React](https://solovyov.net/blog/2020/a-tale-of-webpage-speed-or-throwing-away-react/)\
    — an efficient web app that is not bloated, *imagine that*


### Abstract

- [A Programmer's Guide to Managing Stress](https://simpleprogrammer.com/2015/09/11/a-programmers-guide-to-managing-stress/?utm_source=facebook.com&utm_medium=referral&utm_campaign=i-love-coding)
- [It's all about time](http://web.archive.org/web/20150208203207/http://blog.ircmaxell.com/2014/11/its-all-about-time.html)


### Useful

- [**Leaflet** — map plugin](https://leafletjs.com/)
- [NPM — overriding nested NPM dependency versions](https://stackoverflow.com/a/48524488/4249875)
- [Makefile over NPM scripts](https://spin.atomicobject.com/2021/03/22/makefiles-vs-package-json-scripts/)


### Fun

- [IE-11 end of support countdown](https://death-to-ie11.netlify.com/)
- [Creating Electronic Dance Music with NodeJS](https://www.youtube.com/watch?v=G1bRi4El0iw)
- [Music Player with physics-based seekbar](https://github.com/samir-dahal/MusicPlayer)

---



## NodeJS + Apache server (`.htaccess`)

To use a NodeJS app on an Apache server you can setup the `.htaccess` file to redirect any request to the NodeJS server:

```htaccess
DirectoryIndex disabled
RewriteEngine On
RewriteCond %{HTTPS} on
RewriteRule ^$ http://127.0.0.1:**PORT**/ [P,L]
RewriteCond %{HTTPS} on
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ http://127.0.0.1:**PORT**/$1 [P,L]

RewriteCond %{HTTPS} !=on
RewriteCond %{REQUEST_URI} !^/[0-9]+\..+\.cpaneldcv$
RewriteCond %{REQUEST_URI} !^/[A-F0-9]{32}\.txt(?:\ Comodo\ DCV)?$
RewriteCond %{REQUEST_URI} !^/\.well-known/acme-challenge/[0-9a-zA-Z_-]+$
RewriteCond %{REQUEST_URI} !^/\.well-known/pki-validation/[A-F0-9]{32}\.txt(?:\ Comodo\ DCV)?$
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

Obviously, you would replace the `**PORT**` fields with actual port on which the desired NodeJS app runs.

For WebSocket support use:

```htaccess
RewriteCond %{REQUEST_URI} ^/socket.io [NC]
RewriteCond %{QUERY_STRING} transport=websocket [NC]
RewriteRule /(.*) ws://localhost:**PORT**/$1 [P,L]
```

Again, replace `**PORT**` with an actual port.

Source: [original article *in polish*](http://web.archive.org/web/20180625042814/https://www.smarthost.pl/instalacja-i-uruchomienie-nodejs-na-koncie-hostingowym-smarthost)

---



## Freeing a TCP port

Execute bash command

```bash
sudo fuser 80/tcp
```

to see all the processes listening to HTTP requests on port 80.
Add the `-k` option to kill them.

[Source](https://stackoverflow.com/a/750705/4249875)

---



## CORB & CORS

CORB might be a potential hiccup when attempting to load resources from different origin (CORS).
The problem can occur when a website (SPA) requests additional data,
but the user accessed the website using two different links one with `www.` and one without the prefix.
Browser then remembers that the resource had the `Access-Control-Allow-Origin`
set to the website link with `www.` prefix for example.
That’s why when accessing the website without the prefix, browser blocks the CORS connection,
because it remembers the resource had the header set to a different domain.
The domains `www.example.com` and `example.com` are two different domains.

[Further reading](https://www.siteground.com/kb/how_to_redirect_www_urls_to_nonwww/)

The code snippet attached below is an example `.htaccess` file
implementing necessary redirections from http and/or www addresses
to https non-www version of the domain including SPA redirect to the main index file.

```htaccess
RewriteEngine on
# redirect all non https links to https non-www domain
RewriteCond %{HTTPS} off
RewriteRule ^(.*) https://example.com/index.html [NC,L,R=301]

# redirect www https links to https non-www domain
RewriteCond %{HTTP_HOST} ^www\.example\.com [NC]
RewriteRule ^(.*) https://example.com/index.html [NC,L,R=301]

# if the link contains a file that doesn't exist redirect to index.html (SPA)
RewriteCond %{REQUEST_FILENAME} -s [OR]
RewriteCond %{REQUEST_FILENAME} -l [OR]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^.*$ - [NC,L]
RewriteRule ^(.*) /index.html [NC]
```

---



## Samsung Internet browser webpage scroll position

Samsung Internet doesn't output scroll position through `document.documentElement.scrollTop`,
instead use `document.body.scrollTop`.
However, unfortunately the second option isn't supported in other major browsers.
Therefore, the best implementation of `scrollTop` would be to check the value
from both sources to ensure thorough browser support.

---


