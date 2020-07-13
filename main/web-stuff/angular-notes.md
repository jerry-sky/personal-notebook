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
- [Testing components that contain Angular Material components](#testing-components-that-contain-angular-material-components)
- [Using anchor links](#using-anchor-links)
- [Using SVG icons with Angular Material](#using-svg-icons-with-angular-material)

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

---
## Testing components that contain Angular Material components

[ng-material-harnesses]: https://medium.com/@kevinkreuzer/test-your-components-using-angular-materials-component-harnesses-f9c1deebdf5d

When testing a component with some components from Angular Material (e.g. `MatButton` or `MatCard`) you have to include appropriate Angular Material modules to your tests.\
For example, when the component contains a `mat-button` you should add to the `imports` of the test a reference to the `MatButtonModule`:
```ts
beforeEach(async(() => {
    TestBed.configureTestingModule({
        imports: [
            MatButtonModule, // said reference
        ],
        declarations: [
            ...
        ],
    }).compileComponents();
}));
```
otherwise, the test will complain about unidentifiable components.

Secondly, if it is necessary to test the interaction with an Angular Material component (instead of e.g. testing only the function that is invoked by this component) it is advised to use Angular Material's component harnesses.
This method prevents from possible issues due to change in the internal API of Angular Material.

> *“Relying on implementation details of third party libraries is cumbersome because you are vulnerable to refactorings and you need to understand implementation details.”*

Instead of accessing the components in the HTML through invoking the `query` method use mentioned earlier Angular Material's component harnesses.

Setup:
```ts
let loader: HarnessLoader;
let component: [...];

beforeEach(() => {
    fixture = TestBed.createComponent([...]);
    component = fixture.componentInstance;
    loader = TestBedHarnessEnvironment.loader(fixture); // (1)
    fixture.detectedChanges();
})
```
Here we are preparing the `TestBed` for our testing purposes. Notice the `(1)` additional line that loads the harness environment.

Now we can test Angular Material components. Here is an example from the [source article][ng-material-harnesses]:
```ts
it('should filter out the alive characters if we set filter to dead', async () => {

    const deadRadioButton = await loader.getHarness<MatRadioButtonHarness>(
        MatRadioButtonHarness.with({
            label: 'Dead'
        })
    );
    const table = await loader.getHarness<MatTableHarness>(MathTableHarness);

    await deadRadioButton.check();
    const rows = await table.getRows();
    expect(rows.length).toBe(5);

});
```

Sources:
- [Angular Material guide on component harnesses](https://material.angular.io/guide/using-component-harnesses)
- [The original article on Medium by Kevin Kreuzer][ng-material-harnesses]


---

## Using anchor links

Angular has the anchor links disabled by default (at least when the routing is enabled).

Refactoring the module responsible for routing in a given app as follows:
```ts
[...]
const routerOptions: ExtraOptions = {
    useHash: false,
    anchorScrolling: 'enabled',
};

@NgModule({
    imports: [RouterModule.forRoot(routes, routerOptions)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
```
will enable this functionality.

Source: [an answer on Stack Overflow](https://stackoverflow.com/a/52724769/4249875)

---

## Using SVG icons with Angular Material

To add a custom SVG icon that can be used throughout the whole app you need to import `MatIconRegistry`:
```ts
import { MatIconRegistry } from "@angular/material/icon";
```
and the `DomSanitizer`:
```ts
import { DomSanitizer } from "@angular/platform-browser";
```
to resolve the path by trusting the local asset file.

Then, inside of `app.module.ts` inject said dependencies into the class constructor and add the desired icon(s) to the registry:
```ts
constructor(
    private MIR: MatIconRegistry,
    private DS: DomSanitizer
) {
    this.MIR.addSvgIcon(
        'custom_icon',
        this.DS.bypassSecurityTrustResourceUrl("assets/custom-icon.svg")
    )
}
```

Source: [Digital Ocean Article](https://www.digitalocean.com/community/tutorials/angular-custom-svg-icons-angular-material)
