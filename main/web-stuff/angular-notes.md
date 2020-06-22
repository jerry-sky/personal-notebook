# Angular Notes

- [Links](#links)
- [Deploying an app](#deploying-an-app)
- [Installing Bootstrap](#installing-bootstrap)
- [NgModel input element inside ngFor](#ngmodel-input-element-inside-ngfor)
- [`Router` vs. `Location`](#router-vs-location)
- [Ending an `Observable`](#ending-an-observable)
- [Upload progress](#upload-progress)
- [The `.htaccess` file](#the-htaccess-file)
- [Tracking many files](#tracking-many-files)

## Links

  - [Alligator.io](https://alligator.io/angular/)

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

## `Router` vs. `Location`

When using Angular navigation use the `Router`'s `navigate` function. The `Location`'s `go` function is meant to interact with URL, not navigate in application routes.
[Source](https://stackoverflow.com/a/42858854/4249875)

## Ending an `Observable`

To complete the `Observable` use `return of()`. It will stop propagating any further notifications as `of` with no arguments will complete right away and not emit any notifications.

## Upload progress

To get notifications about a file being uploaded use `reportProgress: true` in any `HTTP` method's additional options object.

[Source](https://stackoverflow.com/a/54899930/4249875)

## The `.htaccess` file

For serving a static Angular app on a standard Apache server you need to setup a `.htaccess` file [like so](web-errors.md#corb--cors).

[StackOverflow answer without `https` CORB issue solution](https://stackoverflow.com/a/22740184/4249875)

## Tracking many files

When dealing with multiple Angular projects or Angular projects mixed with some other opened at once the system can be overwhelmed with the amount of files to track as the code editor is trying to observe every single file in all of the projects. The solution seems to be to alter a default number of files the system is allowed to track.

<!-- spell-checker: disable-next-line -->
1. Open `/etc/sysctl.conf` and add line `fs.inotify.max_user_watches=524288`.
<!-- spell-checker: disable-next-line -->
2. Execute `sudo sysctl -p`.
<!-- spell-checker: disable-next-line -->
3. View `/proc/sys/fs/inotify/max_user_watches` and verify that the output number is equals to `524288`.
