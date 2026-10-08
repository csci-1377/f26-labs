This week's assignment focuses on thinking about hyper-textual structure and how we can augment readers with new and powerful functionality using the affordances of the medium! To do so, you'll explore Notion workspaces and then spend the week implementing an Obsidian plugin to help legal scholars. 

But before you can run, you need to walk! This lab will teach you the absolute basics of TypeScript and Obsidian, and familiarize you with some core concepts from the MDN web docs you may find useful in your implementation. 

## Part I: Introduction to Typescript

### On Background
this—

**This lab will assume you have a basic familiarity with object-oriented languages, and some notion of what a 'type' is (though we can argue about that all day).** You don't NEED to have seen JavaScript before, but it sure is helpful, and we'll be introducing TypeScript in a manner mostly contextualized by JavaScript.

![[Pasted image 20261007005922.png]]
- us, for the purposes of this lab.

This segment of the lab will also make use of a TypeScript playground you can write functions in. **Please follow this link: [https://www.typescriptlang.org/play/](https://www.typescriptlang.org/play/?#code/PTAEHUFMBsGMHsC2lQBd5oBYoCoE8AHSAZVgCcBLA1UABWgEM8BzM+AVwDsATAGiwoBnUENANQAd0gAjQRVSQAUCEmYKsTKGYUAbpGF4OY0BoadYKdJMoL+gzAzIoz3UNEiPOofEVKVqAHSKymAAmkYI7NCuqGqcANag8ABmIjQUXrFOKBJMggBcISGgoAC0oACCbvCwDKgU8JkY7p7ehCTkVDQS2E6gnPCxGcwmZqDSTgzxxWWVoASMFmgYkAAeRJTInN3ymj4d-jSCeNsMq-wuoPaOltigAKoASgAywhK7SbGQZIIz5VWCFzSeCrZagNYbChbHaxUDcCjJZLfSDbExIAgUdxkUBIursJzCFJtXydajBBCcQQ0MwAUVWDEQC0gADVHBQGNJ3KAALygABEAAkYNAMOB4GRonzFBTBPB3AERcwABS0+mM9ysygc9wASmCKhwzQ8ZC8iHFzmB7BoXzcZmY7AYzEg-Fg0HUiQ58D0Ii8fLpDKZgj5SWxfPADlQAHJhAA5SASPlBFQAeS+ZHegmdWkgR1QjgUrmkeFATjNOmGWH0KAQiGhwkuNok4uiIgMHGxCyYrA4PCCJSAA)**

### So, what's TypeScript?

TypeScript, as the name suggests, is a language built on top of JavaScript with the additional enforcement of strong typing rules (well, most of the time). TypeScript means to eschew the many type-based bugs that can occur with JavaScript's much more... shall we say... [quirks](https://github.com/denysdovhan/wtfjs) and make code more explicit for readers, easier to test, and easier to maintain. 

A core idea in TypeScript is that of explicit types; variables are declared with a type if it can be determined at instantiation, or if they can vary, they are explicitly marked as type `any`. TypeScript can also support implicit types, but we'll discuss explicit typing for now.

#### Declaring Variables

In TypeScript, variables are declared with an accompanying type, as seen in the code example below.

```ts
let user_name: string = "ditto";
let grade: number = 42;
let class_name: any = "csci1377";
const animal: string = "cat"
```

Variables are bound using `let`. These can be reassigned to different values of the same type. Variables set with type `any` are not bound by type restriction, but should be handled carefully, as they bypass safety checks that rely on strong typing. Variables declared as `const` are not able to be reassigned. Some examples:

```ts
let my_name: string = "Ditto";
my_name = "Sophie"; // This is okay!
my_name = 42; // Not okay :(
my_name = String(42); // This is okay because 42 is coerced to "42".

const will_name: string = "Will Crichton"
will_name = "Alex" // Not okay!
```

### Arrays

Arrays are declared similarly to variables, just with brackets after the type declaration.

```ts
let grades: number[] = [98, 86, 74]; 
```

### Functions

Functions are declared using the `function` keyword and have inputs that are typed in a similar manner to declared variables and constants. Notice in the example below that the function itself is typed with its expected return type.

```ts
function add(x: number, y: number) : number {
	return x + y;
}
```

Functions can have optional arguments, annotated with a `?`. They can also be given a default value with an `=` in the inputs.

```ts
function greet(name: string, greeting: string = "Hello", punct?: string): void {
	console.log(greeting + ", " + name + (punct ?? "!"));
}

greet("Ditto"); // "Hello, Ditto!"
greet("Ditto", "Hi", "?");  // "Hi, Ditto?"
```

Arrow functions are an alternative syntax for functions. With a one-line body, they will return without a `return` statement.

```ts
const add_arrow = (x: number, y: number): number => x + y;
const square = (x: number) => x * x; // The return type here is inferred as a number given x is a number.

const log_twice = (msg: string): void => {
	console.log(msg);
	console.log(msg);
};
```

The arrow syntax is particularly useful for anonymous functions, which have no name and are typically passed into other functions.

```ts
const subtract = function (x: number, y: number): number {
	return x - y;
};

let curved: number[] = grades.map((g) => g + 5);
let passing: number[] = grades.filter((g) => g >= 80);
grades.forEach((g, i) => console.log(i, g));
```

### Objects

We all love 'em or hate 'em, but TypeScript has 'em. TypeScript objects can be defined primarily using the `class` and `type` keywords. A “?” after a variable in the type signifies that it is an optional value.

```ts
type BirdType = {
	wings: number;
	color?: string;
};

const bird1: BirdType = { wings: 2 }; // Excludes the optional color parameter

```

An `interface` lists the members an object must have. A `class` that `implements` it must provide them. `private` members are only visible inside the class while `readonly` members cannot change after construction.

```ts
interface Pokemon {
	name: string;
	attack(): string;
}

class Ditto implements Pokemon {
	name: string;
	private hp: number;
	readonly color: string;

	constructor(name: string, hp: number, color: string = "pink") {
		this.name = name;
		this.hp = hp;
		this.color = color;
	}

	attack(): string {
		return this.name + " used Transform!";
	}

	getHp(): number {
		return this.hp;
	}
}

const ditto = new Ditto("Ditto", 48);
ditto.attack();       // "Ditto used Transform!"
ditto.hp;             // Error: hp is private
ditto.color = "blue"; // Error: can't change a readonly!
```

A class can `extends` another class. `super` calls the parent's constructor or methods. You'll see this in Part III with `TFile` and `TAbstractFile`!

```ts
class ShinyDitto extends Ditto {
	constructor(name: string) {
		super(name, 48, "blue");
	}

	attack(): string {
		return super.attack() + " It sparkles!";
	}
}

const shiny: Pokemon = new ShinyDitto("Shiny Ditto");
shiny.attack(); // "Shiny Ditto used Transform! It sparkles!"
```

A union type like `Pokemon | null` allows either type. You can coerce it to a single type progressively using `===` and `instanceof`. 

```ts
function describe(p: Pokemon | null): string {
	if (p === null) {
		return "nothing here";
	}
	if (p instanceof ShinyDitto) {
		return p.name + " is shiny"; // p is coerced to ShinyDitto.
	}
	return p.name;
}
```

### Relaxation

Woooohhhookayokayokay. That was a lot. Let's take a quick break.

![[ice-cream-on-beach-3853031791.jpg|700]]

mmm.

**BREAK TIME OVER! BACK TO WORK!**

The below tasks are written into this document, but you can copy them over to the **[TypeScript Playground!](https://www.typescriptlang.org/play/?#code/PTAEHUFMBsGMHsC2lQBd5oBYoCoE8AHSAZVgCcBLA1UABWgEM8BzM+AVwDsATAGiwoBnUENANQAd0gAjQRVSQAUCEmYKsTKGYUAbpGF4OY0BoadYKdJMoL+gzAzIoz3UNEiPOofEVKVqAHSKymAAmkYI7NCuqGqcANag8ABmIjQUXrFOKBJMggBcISGgoAC0oACCbvCwDKgU8JkY7p7ehCTkVDQS2E6gnPCxGcwmZqDSTgzxxWWVoASMFmgYkAAeRJTInN3ymj4d-jSCeNsMq-wuoPaOltigAKoASgAywhK7SbGQZIIz5VWCFzSeCrZagNYbChbHaxUDcCjJZLfSDbExIAgUdxkUBIursJzCFJtXydajBBCcQQ0MwAUVWDEQC0gADVHBQGNJ3KAALygABEAAkYNAMOB4GRonzFBTBPB3AERcwABS0+mM9ysygc9wASmCKhwzQ8ZC8iHFzmB7BoXzcZmY7AYzEg-Fg0HUiQ58D0Ii8fLpDKZgj5SWxfPADlQAHJhAA5SASPlBFQAeS+ZHegmdWkgR1QjgUrmkeFATjNOmGWH0KAQiGhwkuNok4uiIgMHGxCyYrA4PCCJSAA)**
### Task 1.1: Type that function!

> **Task:** Using TypeScript, write a function that takes in an array of numbers and returns the sum of every number in the array. Make sure to explicitly type your parameters and variables. 

Test it (replace `sum` with your function name):

```ts
console.log(sum([1, 2, 3])); // 6
console.log(sum([])); // 0
console.log(sum([-5, 5, 10])); // 10
sum(["1", 2]); // should error
```
### Task 1.2: *Type* that function!

> **Task:** Below is a JavaScript function that has some unexpected behavior due to JavaScript's quirks. Explicitly type it so it returns an expected number value. 

```ts
function addTax(price, taxRate) {
	let tax = price * taxRate;
	return price + tax;
}

console.log(addTax(20, 0.1));
console.log(addTax("20", 0.1));
```

After you add types, the first call prints `22` and the string call is a type error:

```ts
console.log(addTax(20, 0.1)); // 22
console.log(addTax(100, 0)); // 100
addTax("20", 0.1); // should error
```

### Asynchronous Programming

A **promise** is a value that might not be available right away, but will be at some point. Knowing we expect the value to become available, we can write code that uses the future result of this future event to trigger other code. A promise can be either pending, fulfilled, or rejected. 

To illustrate this, imagine I want to bake a cake. However, I don’t have the ingredients to bake one, so I need to go to the grocery store first. My roommate promises me that she will drive me to the store. Once my friend drives me, I am able to get the groceries I need and bake the cake. 

Promises (and asynchronous programming generally) are handled in TypeScript using the `Promise` class and `async`, `await` keywords. Functions declared `async` will return a promise, even without the `Promise` explicitly included within the return statement. Note that `Promise`s, like anything in TypeScript, can be parametrized by a type, as in `Promise<T>` representing a value of type `T` that will be available in the future. The `await` keyword says to pause execution of an async function until a `Promise` is settled, returning the fulfilled value or throwing the rejection reason.

Here's an example illustrating the grocery trip we discussed:
```ts
type Ride = {
	driver: string;
	car: string;
};

const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

async function friendDrivesMe(friend: string, willShowUp: boolean): Promise<Ride> {
	await sleep(1000); // while waiting for friend

	if (!willShowUp) {
		throw new Error(`${friend} got stuck at work.`);
	}

	return { driver: friend, car: "subaru" };
}

async function buyGroceries(ride: Ride): Promise<string[]> {
	await sleep(500); // while shopping
	return ["milk", "eggs", "flour"];
}

async function groceryTrip(): Promise<void> {
	try {
		const ride = await friendDrivesMe("Olivia", true);

		const groceries = await buyGroceries(ride);
	} catch (err) {
		console.log("Plan B: take the B.U.S.", (err as Error).message);
	}
}

groceryTrip();
```

### Task 1.3: (a)Wait for me, I'm coming!

**Task:** Write an async function titled `showUsers(ids: number[])` that fetches every user with the `fetchUser(id)` function below at the same time (hint: `Promise.all`) and logs `Found: <name>` for each one. Add an explicit return type. 

```ts
type User = {id: number; name: string};

function fetchUser(id: number): Promise<User> {
	return new Promise((resolve) => {
		setTimeout(() => resolve({id, name: `User #${id}`}), 500);
	});
}
```

Test it (add after your function):

```ts
showUsers([1, 2, 3]); // Found: User #1, #2, #3
```

Great job! You now (hopefully) know all the TypeScript you'll need for this lab and assignment. Feel free to come back to this lab as future reference for your TypeScript needs, or (even better) ask a TA!

## Part II: Some Useful Functions/APIs

While working on assignment 4, you'll spend a fair amount of time inspecting documentation---primarily the Obsidian and MDN Web Docs. This part of the lab will focus on the Obsidian docs and illustrating some useful functions, models, and interaction modes for plugin development. 
### Docs!

Relevant documentation can be found in the two links below, though your TA will also be guiding you through these to some extent. Become familiar with navigating them.

- [Obsidian's Documentation](https://docs.obsidian.md/Home)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)

### Task 2.1: Booting Up the Console

Before you start writing code to interact with the Obsidian API, it's a good idea to become familiar with the interface through scripting. 

You can open up the Obsidian console by pressing `Ctrl-Shift-i`. You should see a console window that says 'Obsidian Developer Console' pop up. Try declaring a few variables and checking their values.

> **Task:** In the console, declare a variable that holds your name and print it with `console.log`. Then type `app` and press Enter. Expand the object that prints and find the `vault` and `workspace` properties. Note that the console runs JavaScript, not TypeScript, so leave off the type annotations!

#### Apps, Vaults, and Workspaces  - Oh, My!

> This section should be read along with a TA on a projector, but is fleshed out primarily so students can complete it offline if needed

Obsidian employs an API model of scriptable global classes. The top-level object you'll be interacting with is the `App`, which has the following properties: 

- `vault: Vault`: files/folders and file manipulation in the vault.
- `fileManager: FileManager`: file operations that keep links and frontmatter up to date.
- `workspace: Workspace`: the panes, tabs, and views open in the window.
- `metadataCache: MetadataCache`: parsed links, headings, tags, and frontmatter for each file.
- `keymap: Keymap`: the registry of hotkeys.
- `scope: Scope`: the root scope for keyboard shortcuts.
- `lastEvent: UserEvent | null`: the most recent mouse or keyboard event.
- `isDarkMode(): boolean`: whether the dark theme is on.
- `loadLocalStorage(key)` / `saveLocalStorage(key, data)`: per-vault local storage.

This is a lot, so we will not cover all of it here. Below, we've highlighted some of the more useful members of the `Vault` and `Workspace` that you might find useful as reference in the lab and assignment. Check the docs for the rest---you'll need to access some other places, too!

##### `TAbstractFile`, `TFile`, and `TFolder`

Most of the Obsidian API revolves around file and folder interactions in the form of `TFile`s and associated classes. These classes act as handles to files without directly handling their contents.

- `TAbstractFile`: the abstract parent class of files and folders.
	- `path: string`: file path relative to the vault root (e.g. `notes/shoppinglist.md`).
	- `name: string`: file or folder name with extension.
	- `parent: TFolder | null`: the folder that contains this file (or null if at root).
- `TFile extends TAbstractFile`: a file.
	- `basename: string`: file name without extension.
	- `extension: string`: file extension (e.g. `md`).
	- `stat: FileStats`: creation time (`ctime`), modification time (`mtime`), and `size`.
- `TFolder extends TAbstractFile`: a folder.
	- `children: TAbstractFile[]`: files and folders inside the folder.
	- `isRoot(): boolean`: true if vault root.

When a function returns a `TAbstractFile`, you can use `instanceof TFile` or `instanceof TFolder` to narrow the type.

##### `Vault`

`Vault` is a property that gives access to files and folders within the vault and serves as an interface for reading/modifying/creating files. You'll interact with it when you want to manipulate files and change vault structure.

- `getMarkdownFiles(): TFile[]`: all `.md` files in the vault.
- `getRoot(): TFolder`: returns root folder. Follow `children` to walk the folder tree.
- `getFileByPath(path): TFile | null`: the file at a vault-relative path.
- `getAbstractFileByPath(path): TAbstractFile | null`: the file or folder at a path.
- `read(file): Promise<string>`: the contents of a file from disk.
- `cachedRead(file): Promise<string>`: the contents of a file from the cache.
- `create(path, data): Promise<TFile>`: makes a new file.
- `modify(file, data): Promise<void>`: replaces the contents of a file.
- `process(file, fn): Promise<string>`:  Atomic read/modify/write on a file.
- `on('create' | 'modify' | 'delete' | 'rename', callback)`: events for file changes.

##### `Workspace`

The `Workspace` is a property that allows for manipulation of Obsidian's UI. You'll use it when finding out what tab a user is focusing on, following links, and running callbacks on user actions.

- `activeLeaf: WorkspaceLeaf | null`: the focused leaf. A leaf is one tab that holds one view.
- `activeEditor: MarkdownFileInfo | null`: focused editor or `null`.
- `getActiveFile(): TFile | null`:  file open in the focused leaf.
- `getActiveViewOfType(type): T | null`: the focused view of class `type` (for example, `MarkdownView`) or `null`.
- `getLeaf(newLeaf?): WorkspaceLeaf`: a leaf to open something (current tab, new tab, split, or window).
- `openLinkText(linktext, sourcePath, newLeaf?): Promise<void>`: opens a link.
- `on('file-open', callback)`: runs `callback` on `TFile` open.
- `on('editor-change', callback)`: runs `callback` with the `Editor` after file edit.

### Task 2.2: Exploring with the Console

> **Task:** Use the `app` object in the console and the reference lists above to answer the questions below. Write down the line of code you used for each answer.
> 
> 1. How many Markdown files are in this vault?
> 2. What is the basename of the file you have open right now?
> 3. How many files and folders are directly inside the vault root?
> 4. How many characters long is the file you have open? (Hint: reading a file returns a `Promise`, so you will need `await`.)
> 5. Is dark mode on?

**Your LOC here:**

```js
// Comment which line did which task

```

## Part III: Plugging in

### Installing/Enabling Plugins

Plugins in Obsidian can be obtained through the community plugins catalog or manually installed. After installation, plugins are located in the `.obsidian/plugins` folder in your vault. The `.` at the beginning indicates a hidden file, so you can either navigate to it by `cd`ing into your vault directory and typing `cd .obsidian` or looking up your platform-specific means of showing hidden files in your file manager.

After adding a plugin to `.plugins,` navigate to the settings wheel in the bottom left corner of your UI: 

![[Pasted image 20261008161543.png]]

Then, click 'community plugins' on the left bar and choose to enable them. After that, you can toggle on your plugins! We have included two already—hot reload, which makes your in-development plugins reload on code changes. The other, em-dasher, is one you'll implement!

## Building a Plugin

### Alex needs your help!

For this part of the lab, you'll be making a plugin: "em-dasher!" Alex loves the em dash more than life itself, but doesn't like having to go to the internet to copy the symbol from a random website (he refuses to learn the code). He would like it if typing three dashes sequentially ("---") would replace those dashes with an em-dash—a feature you'll be implementing!

#### The `Editor`

The `Editor` is the text of the open note and can be retrieved as the first argument of the `editor-change` callback, or from `app.workspace.getActiveViewOfType(MarkdownView)?.editor`.  You'll want to use this for changing note text on edit, which your em-dash plugin will have to do.

- `EditorPosition`: a zero-indexed place in the text, as `{ line: number, ch: number }`.
- `getCursor(): EditorPosition`: the position of the cursor.
- `getLine(line): string`: the text of one line.
- `getRange(from, to): string`: the text between two positions.
- `getValue(): string`: the full text of the note.
- `lineCount(): number`: the number of lines.
- `getSelection(): string`: the selected text.
- `replaceSelection(replacement)`: replaces the selected text or inserts at the cursor.
- `replaceRange(replacement, from, to?)`: replaces text between two positions. Without `to`, inserts starting at `from`.
- `setCursor(pos)`: moves the cursor.
- `posToOffset(pos): number` / `offsetToPos(offset): EditorPosition`: converts between a position and a character index into `getValue()`.

### Task 3.1: Finding on the Page

Your plugin will need to be able to find instances of `---` on the page. To do this, you will use the `Editor` described above.

> **Task:** In `onload`, use `this.registerEvent` to listen for the workspace's `editor-change` event. Each time the note changes, get the text on the cursor's line up to the cursor. If that text ends with `---`, log a message to the console of your choosing. Type a few `---`s into a note and watch the console to check your work.

### Task 3.2: Page Injection

> **Task:** Instead of just logging, replace the `---` before the cursor with an em dash (`—`). Use `replaceRange` with the start and end positions of the three dashes. Test it by typing a `---` into a note between two words.

### Task 3.3: Edge cases

> **Task:** Try typing `---` on an empty line. What does a line with only `---` mean in Markdown? (Hint: switch to reading view, or try it on the very first line of a note.). Unless you've already accounted for this, you should fix this edge case.
>
> Think of at least one more edge case and write it down. If you can, fix it!

**Your edge cases here:**
1. 

## Good Job!

You've made it through the lab and are now ready for your adventure into the wonderful world of Obsidian plugin development! This was one of the heaviest labs code-wise, so pat yourself on the back. Have fun on assignment 4! - Your 1377 TAs <3

## Resources

- [Obsidian Docs](https://docs.obsidian.md/Home)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
