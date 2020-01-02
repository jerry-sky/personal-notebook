# Angular Notes

## Deploying an app

1. Compile the Angular app
  ```bash
  ng build --prod
  ```

~~2. Now, setup a node.js server using [NPM package `express-history-api-fallback`](https://www.npmjs.com/package/express-history-api-fallback)~~

2. Put it on a simple Apache server or use [`angular-universal`](https://angular.io/guide/universal)

## Installing Bootstrap

1. ```bash
   npm install bootstrap
   ```
2. Modify `$WORKING_DIRECTORY/angular.json`:
   ```json
   "styles": [
     "node_modules/bootstrap/dist/css/bootstrap.min.css",
     "styles.css"
   ]
   ```

## NgModel input element inside ngFor

Nested `ngModel` input element inside `ngFor` need to refer to a value inside an `Object`. If it isn't wrapped in an `Object` Angular won't compile the app for some odd reason.
