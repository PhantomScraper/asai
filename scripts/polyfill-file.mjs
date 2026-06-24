// Node 18 lacks the global `File` constructor that newer `undici` (pulled in by
// cheerio) references at load time. Define a minimal stub before cheerio loads.
import { Blob } from "node:buffer";

if (!globalThis.File) {
  globalThis.File = class File extends Blob {
    constructor(chunks, name, options = {}) {
      super(chunks, options);
      this.name = String(name);
      this.lastModified = options.lastModified ?? Date.now();
    }
  };
}
