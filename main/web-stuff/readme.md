---
lang: 'en-GB'
title: 'Web stuff'
author: 'Jerry Sky'
description: 'My notes on various web-dev related matters.'
keywords: 'web, development, Angular, NodeJS, ExpressJS, JS, JavaScript, TypeScript, SQL, CSS, SCSS, Sass, links, resources, tcp, port'
---

---

- [Index](#index)
- [Links](#links)
    - [Interesting reads](#interesting-reads)
    - [Useful](#useful)
    - [Entertainment-like](#entertainment-like)
- [Freeing a TCP port](#freeing-a-tcp-port)
- [Classes and Interfaces in TypeScript](#classes-and-interfaces-in-typescript)
- [Extracting a property from a derived class (a proposal)](#extracting-a-property-from-a-derived-class-a-proposal)

## Index

- [Angular Notes](angular-notes.md)
- [NodeJS Notes](nodejs-notes.md)
- [Express.js Notes](express-notes.md)
- [JS (Other) Notes](js-notes.md)
- [Web Errors in general](web-errors.md)
- [CSS/SCSS + HTML](css-scss-html-notes.md)
- [SQL](sql-notes.md)

## Links

### Interesting reads

- [You don't hate JavaScript](https://medium.com/edge-coders/you-dont-hate-javascript-62cd6c609d43)
- [It's all about time](http://web.archive.org/web/20150208203207/http://blog.ircmaxell.com/2014/11/its-all-about-time.html)
- [How to build your own team chat in five days](https://fdietz.github.io/2015/04/13/day-1-how-to-build-your-own-team-chat-in-five-days.html)
- [A Programmer's Guide to Managing Stress](https://simpleprogrammer.com/2015/09/11/a-programmers-guide-to-managing-stress/?utm_source=facebook.com&utm_medium=referral&utm_campaign=i-love-coding)
- [Pivoting in MySQL](http://mysql.rjweb.org/doc.php/pivot)
- [How to stop me harvesting credit card numbers and passwords from your site](https://hackernoon.com/part-2-how-to-stop-me-harvesting-credit-card-numbers-and-passwords-from-your-site-844f739659b9)
- [PHP Cookies security](https://www.simonholywell.com/post/2013/05/improve-php-session-cookie-security/)
- [Remember me Safely](http://wayback.archive.org/web/20150204143440/https://resonantcore.net/blog/2015/02/remember-me-safely-secure-long-term-authentication-strategies)
- [A tale of webpage speed, or throwing away React](https://solovyov.net/blog/2020/a-tale-of-webpage-speed-or-throwing-away-react/)\
    — efficient web app that is not bloated

### Useful

- [**Leaflet** - map plugin](https://leafletjs.com/)
- [anime.js](https://animejs.com/documentation/)
- [Updating XAMPP from MariaDB 10.1 to 10.2](https://stackoverflow.com/a/47490206/4249875)
- [NPM - overriding nested NPM dependency versions](https://stackoverflow.com/a/48524488/4249875)

### Entertainment-like
- [IE-11 end of support countdown](https://death-to-ie11.netlify.com/)
- [Creating Electronic Dance Music with NodeJS](https://www.youtube.com/watch?v=G1bRi4El0iw)


## Freeing a TCP port

Execute bash command
```bash
sudo fuser 80/tcp
```
to see the all of the process listening to HTTP requests on port 80. Add a `-k` option to kill them.
[Source](https://stackoverflow.com/a/750705/4249875)

---

## Classes and Interfaces in TypeScript

Without defining a constructor there is no way to check if a given attribute (of actual type `string`) is in a certain object (that is a member of some given class) if the object is empty. TypeScript doesn't include the properties of a class in the compiled program; to check if a given prop is in a certain object type (in a class definition one can say) you have to use an ad-hoc generated staple object that is a member of this class – this way the constructor will be called and it will initialize all the properties thus `Object.keys` will not return an empty array but an array with all properties initialized by the constructor.

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

If the `constructor` isn’t defined in the `Example` class, the condition in the above `if` statement will always reject any `string` property.

To allow creating objects with custom initializing values you could improve `constructor` by adding an optional argument:
```ts
constructor(example: Partial<Example> = {}) {
    this.one = example.one || 'some';
    this.two = example.two || 'example';
    this.three = example.three || 'data';
}
```
This way you could create a new instance of this class with some custom parameters. However, this argument is optional so it can be omitted: `new Example()`.

It is important to note that defining the argument as optional using the `?` symbol won’t work.
```ts
constructor(example?: Partial<Example>) {...}
```
If the `constructor` is defined as above then creating a new object (`new Example()`) will result in an error of a `TypeError`:
```
TypeError: Cannot read property '...' of undefined
```
as the argument object hasn’t been provided.\
**Setting the default value to `{}` resolves this issue.**

## Extracting a property from a derived class (a proposal)

*This describes a very obscure issue, but it is still important to consider the resolution of this issue.*

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

We want to extract properties that are defined by `Base` class from this `object` and remove all that are defined by the `Derived` class. In this case we want to get an object with only the `one` property.
```ts
const objectExtracted: Base = new Base();
```

The first solution would be to loop through all properties of the `object` properties and assign all values to properties that exist in `objectExtracted`’s type which is the `Base` class.

We need to define a [*predicate function*](https://www.typescriptlang.org/docs/handbook/advanced-types.html#using-type-predicates) that states whether a given string property name is an actual property name:
```ts
class Base {
    ...

    public static hasKey(val: any): val is keyof Base {
        return val in new Base();
    }
}
```
This function creates a staple instance of the `Base` class that contains all of its properties (it is important to define a proper `constructor` for this class – more [here](#classes-and-interfaces-in-typescript)) and checks whether the provided string is an actual object key.

However, the following code isn’t enough:
```ts
for (const prop in object) {
    if(Base.hasKey(prop)) {
        objectExtracted[prop] = object[prop];
    }
}
```
as it will bring up an error that some type can’t be cast to the type “`never`”. This type exists because of uncertainty which type should be used here when accessing a property of `objectExtracted`.

The solution is to define a function which *extracts* a given property from one object to another whilst at the same time **being type-safe**:
```ts
export function ExtractProperty<T1, T2 extends T1, K extends keyof T2>(
  target: T1, source: T2, property: K, hasKey: (val: any) => val is keyof T1): void {
  if (hasKey(property)) {
    target[property] = source[property];
  }
}
```
This function assigns the property value from the `source` object to `target` only if `target` has a property of the same name. This function requires using a predicate which makes sure the object keys are handled properly.

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
