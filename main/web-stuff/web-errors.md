# Web Errors in general

- [CORB & CORS](#corb--cors)

## CORB & CORS

CORB might be a potential hiccup when attempting to load resources from different origin (CORS). The problem can appear when a website requests additional data, but the user used different links to the same website: the one with `www.` prefix and without. Browser then remembers that the resource had the `Access-Control-Allow-Origin` set to the website link with `www.` prefix. That’s why when accessing the website without the prefix, browser blocks the CORS connection, because it remembers the resource had the header set to a different value.

[Further reading](https://www.siteground.com/kb/how_to_redirect_www_urls_to_nonwww/)

The code attached below is an example `.htaccess` file from the `wroczynski.pl` web-server showing redirections from http and/or www to https non-www version of the domain including Angular SPA redirect to main index file:

```htaccess
RewriteEngine on
# all non https links redirected to https non-www domain
RewriteCond %{HTTPS} off
RewriteRule ^(.*) https://wroczynski.pl/index.html [NC,L,R=301]

# www https links redirected to https non-www domain
RewriteCond %{HTTP_HOST} ^www\.wroczynski\.pl [NC]
RewriteRule ^(.*) https://wroczynski.pl/index.html [NC,L,R=301]

# if the link contains a file that doesn't exist redirect to index.html (Angular SPA)
RewriteCond %{REQUEST_FILENAME} -s [OR]
RewriteCond %{REQUEST_FILENAME} -l [OR]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^.*$ - [NC,L]
RewriteRule ^(.*) /index.html [NC]
```
