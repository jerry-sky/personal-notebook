# NodeJS Notes

- [Configuring `.htaccess`](#configuring-htaccess)

## Configuring `.htaccess`

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

[Original Source *in polish*](http://web.archive.org/web/20180625042814/https://www.smarthost.pl/instalacja-i-uruchomienie-nodejs-na-koncie-hostingowym-smarthost)
