# Express.js Notes

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
