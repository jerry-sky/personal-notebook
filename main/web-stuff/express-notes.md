# Express.js Notes

## Links

  - [Why you should use TypeScript with NodeJS and Express.js](https://medium.com/javascript-in-plain-english/typescript-with-node-and-express-js-why-when-and-how-eb6bc73edd5d)
  - [Use TypeScript to Build a NodeJS API with Express.js](https://developer.okta.com/blog/2018/11/15/node-express-typescript)
  - [How to prevent you NodeJS process from crashing](https://medium.com/dailyjs/how-to-prevent-your-node-js-process-from-crashing-5d40247b8ab2)
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
