# Angular Notes

## Links

  - [How to use `reportProgress` in `HttpClient`?](https://stackoverflow.com/a/54899930/4249875)
  - [Shared assets with multiple apps](https://medium.com/@nit3watch/angular-shared-assets-with-multiple-apps-nrwl-nx-b4801c05c771)
  - [`.htaccess` file for serving Angular app](https://stackoverflow.com/a/22740184/4249875)
  - [Alligator.io](https://alligator.io/angular/)
  - [Tracking many files](https://stackoverflow.com/a/56292289/4249875)

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
