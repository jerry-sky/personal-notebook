import Express from 'express'

/**
 * Port which will the server run on.
 */
const port = process.env.PORT || 3000

// initialize the express app
const express = Express()

// The server will probably run in some sort of a box.
express.set('trust proxy', 1)

// Origin access: check if origin is approved to connect.
express.use((req, res, next) => {
    const origin = req.headers.origin
    if (!origin) {
        // turn off `next()` and turn on `res.end()` to make the Origin header obligatory
        next()
        // res.end()
        return
    }

    const originsWithAccess: string[] = [
        // input approved list of origins here
    ]
    // optional origins with access for local testing
    if (process.env.NODE_ENV !== 'production') {
        originsWithAccess.push('http://localhost:4200')
        originsWithAccess.push('https://web.postman.co/')
    }
    // check if origin is on the list
    if (originsWithAccess.indexOf(origin) > -1) {
        res.header('Access-Control-Allow-Origin', origin)
        res.header('Access-Control-Allow-Credentials', 'true')
        res.header('Access-Control-Allow-Headers', 'Content-Type,X-XSRF-TOKEN')
        res.header('X-Content-Type-Options', 'nosniff')
        res.header(
            'Access-Control-Allow-Methods',
            'POST, OPTIONS, GET, DELETE, PUT'
        )
        res.header('Accept', 'application/json')
    }

    next()
})

// Example route.
express.get('/', async (_, res, next) => {
    res.json({ hello: 'world' })
    next()
})

// Start the server.
express.listen(port, () => {
    const date = new Date()
    console.log(
        '\n\x1b[1mNew server run (port ' + port + ')\x1b[0m',
        '\ninitialized on',
        date.toString(),
        '\n'
    )
})
