import { Plugin } from "obsidian";

export default class EmDasher extends Plugin {
  async onload() {
    console.log("em-dasher loaded");

    // TODO (Task 3.1): listen for edits, find "---" before the cursor.

    // TODO (Task 3.2): replace triple dashes with "—".
  }

  onunload() {
    console.log("em-dasher unloaded");
  }
}
