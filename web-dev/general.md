---
lang: 'en-GB'
title: 'Web dev'
author: 'Jerry Sky'
description: 'My notes on various web-dev related matters.'
keywords: 'web, development, Angular, NodeJS, ExpressJS, JS, JavaScript, TypeScript, SQL, CSS, SCSS, Sass, links, resources, tcp, port'
---

---

- [Resources](#resources)
    - [Security](#security)
    - [Interesting](#interesting)
    - [Building](#building)
    - [Abstract](#abstract)
    - [Useful](#useful)
    - [Entertainment-like](#entertainment-like)
- [NodeJS + Apache server (`.htaccess`)](#nodejs--apache-server-htaccess)
- [Freeing a TCP port](#freeing-a-tcp-port)
- [CORB & CORS](#corb--cors)
- [Samsung Internet browser webpage scroll position](#samsung-internet-browser-webpage-scroll-position)
- [Classes and Interfaces in TypeScript](#classes-and-interfaces-in-typescript)
- [Extracting a property from a derived class (a proposal)](#extracting-a-property-from-a-derived-class-a-proposal)

---

## Resources

### **Crucial**

- [Strict mode in TypeScript \|\| help your compiler help you — an article by Andrey Goncharov](https://blog.goncharov.page/strict-mode-in-typescript-or-help-your-compiler-help-you)

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

### Entertainment-like

- [IE-11 end of support countdown](https://death-to-ie11.netlify.com/)
- [Creating Electronic Dance Music with NodeJS](https://www.youtube.com/watch?v=G1bRi4El0iw)

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

## Classes and Interfaces in TypeScript

Without defining a constructor there is no way to check if a given attribute
(of actual type `string`) is in a certain object (that is a member of some given class)
if the object is empty.
TypeScript doesn't include the properties of a class in the compiled program;
to check if a given prop is in a certain object type (in a class definition one can say)
you have to use an ad-hoc generated staple object that is a member of this class
— this way the constructor will be called and it will initialize all
the properties thus `Object.keys` will not return an empty array but
an array with all properties initialized by the constructor.

Below is an example class with a constructor that initializes all class’ attributes.

```ts
class Example {
    one: string;
    two: number;
    three: number[];

    constructor() {
        this.one = 'some';
        this.two = 'example';
        this.three = 'data';
    }
}
```

Now, to check if a given string is an attribute use:

```ts
if (attr in new Example) {
    console.log(attr, 'is a property in `Example`');
}
```

If the `constructor` isn’t defined in the `Example` class,
the condition in the above `if` statement will always reject any `string` property.

To allow creating objects with custom initializing values you could improve `constructor` by adding an optional argument:

```ts
constructor(example: Partial<Example> = {}) {
    this.one = example.one || 'some';
    this.two = example.two || 'example';
    this.three = example.three || 'data';
}
```

This way you could create a new instance of this class with some custom parameters.
However, this argument is optional so it can be omitted: `new Example()`.

It is important to note that defining the argument as optional using the `?` symbol won’t work.

```ts
constructor(example?: Partial<Example>) {...}
```

If the `constructor` is defined as above then creating a new object
(`new Example()`) will result in an error of a `TypeError`:

```log
TypeError: Cannot read property '...' of undefined
```

as the argument object hasn’t been provided.\
**Setting the default value to `{}` resolves this issue.**

---

## Extracting a property from a derived class (a proposal)

*An obscure issue, but still a valuable one to consider.*

We have two classes of which one is derived from the other:

```ts
class Base {
    one: string;

    constructor() {
        this.one = 'data';
    }
}

class Derived extends Base {
    two: number;

    constructor() {
        super();
        this.two = 27;
    }
}
```

an instance of the `Derived` class:

```ts
const object: Derived = new Derived();
```

We want to extract properties that are defined by `Base` class from
this `object` and remove all that are defined by the `Derived` class.
In this case we want to get an object with only the `one` property.

```ts
const objectExtracted: Base = new Base();
```

The first solution would be to loop through all properties of
the `object` properties and assign all values to properties that exist
in `objectExtracted`’s type which is the `Base` class.

We need to define a [*predicate function*](https://www.typescriptlang.org/docs/handbook/advanced-types.html#using-type-predicates) that states whether a given string property name is an actual property name:

```ts
class Base {
    ...

    public static hasKey(val: any): val is keyof Base {
        return val in new Base();
    }
}
```

This function creates a staple instance of the `Base` class that contains
all of its properties (it is important to define a proper `constructor`
for this class — more [here](#classes-and-interfaces-in-typescript))
and checks whether the provided string is an actual object key.

However, the following code isn’t enough:

```ts
for (const prop in object) {
    if(Base.hasKey(prop)) {
        objectExtracted[prop] = object[prop];
    }
}
```

as it will bring up an error that some type can’t be cast to the type “`never`”.
This type exists because of uncertainty which type should be used here when accessing a property of `objectExtracted`.

The solution is to define a function which *extracts* a given property
from one object to another whilst at the same time **being type-safe**:

```ts
export function ExtractProperty<T1, T2 extends T1, K extends keyof T2>(
  target: T1, source: T2, property: K, hasKey: (val: any) => val is keyof T1): void {
  if (hasKey(property)) {
    target[property] = source[property];
  }
}
```

This function assigns the property value from the `source` object
to `target` only if `target` has a property of the same name.
This function requires using a predicate which makes sure the object keys are handled properly.

*This function essentially moves the problem to an abstract level at which it resolves the type uncertainty issue.*

Now, we can rewrite our loop:

```ts
for (const prop in object) {
    if(Base.hasKey(prop)) {
        ExtractProperty(objectExtracted, object, prop, Base.hasKey);
    }
}
```

so it uses the `ExtractProperty` function.

---
