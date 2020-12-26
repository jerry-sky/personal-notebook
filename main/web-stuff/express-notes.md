---
lang: 'en-GB'
title: 'Express.js Notes'
author: 'Jerry Sky'
description: 'Notes on ExpressJS.'
keywords: 'ExpressJS, notes, web, development, JavaScript, TypeScript, authentication'
---

---

- [Links](#links)
- [Server error and listening](#server-error-and-listening)
- [Using TypeScript with Express.js](#using-typescript-with-expressjs)
    - [Starter repository](#starter-repository)
    - [Setup it manually](#setup-it-manually)

## Links

- [Your NodeJS authentication tutorial is (probably) wrong](https://hackernoon.com/your-node-js-authentication-tutorial-is-wrong-f1a3bf831a46)
- [Repository of `secure-password`](https://github.com/emilbayes/secure-password)

## Server error and listening

```javascript
function server_on_error(error) {

    if (error.syscall !== 'listen') {
        console.log('\n');
        console.log('\n');
        console.error(error);
        console.log('\n');
        console.log('\n');
    }
    let bind = typeof port === 'string'
        ? 'Pipe ' + port
        : 'Port ' + port;

    // handle specific listen errors with friendly messages
    switch (error.code) {
        case 'EACCES':
            console.error(bind + ' requires elevated privileges');
            // process.exit(1);
            break;
        case 'EADDRINUSE':
            console.error(bind + ' is already in use');
            // process.exit(1);
            break;
        default:
            throw error;
    }
}

function server_listening() {

    let addr = server.address();
    let bind = typeof addr === 'string'
        ? 'pipe ' + addr
        : 'port ' + addr.port;
    debug('Listening on ' + bind);

    let date = new Date();

    console.log('--- New server run ---', '\nstarted on', date.toLocaleString(), '\n\n');

}
```

## Using TypeScript with Express.js

There are two ways to setup an Express.js app with TypeScript.

### Starter repository

Download example [TypeScript Node Starter *hackathon-style*](https://github.com/microsoft/TypeScript-Node-Starter) repository and update the packages. There is enough boilerplate to get you running *quickly*, but probably there are packages you don't really need.

### Setup it manually

1. `npm init`
2. `npm install --save-dev typescript`
3. Run `tsc --init` to create the `tsconfig.json` file.
4. `npm install express`
5. For every package you should attempt to download the `types` package - e.g. for `express` package install `@types/express` alongside with the `--save-dev` option.
6. A basic starter script would look like:
    ```typescript
    import Express from 'express';
    const app = Express();

    app.get('/', (req, res, next) => {
      res.send('Hello World!');
    });

    app.listen(3000, () => {
      console.log('Example app listening on port 3000!');
    });
    ```
7. To run the app you need to compile it and run:
    ```bash
    tsc && node build/app.js
    ```
   or run it through `nodemon` with `ts-node`:
   ```bash
   nodemon --watch . ts,json --exec ts-node app.ts
   ```
8. `npm install --save-dev tslint`
9. Setup a `tslint.json` config file. An example config file with Angular-recommended rules is attached to this document.
10. Put above commands into `package.json` as `npm` commands.

Sources:
- [An Okta article](https://developer.okta.com/blog/2018/11/15/node-express-typescript)
- [*An article with questionable solutions*](https://medium.com/javascript-in-plain-english/typescript-with-node-and-express-js-why-when-and-how-eb6bc73edd5d)
- *self*
