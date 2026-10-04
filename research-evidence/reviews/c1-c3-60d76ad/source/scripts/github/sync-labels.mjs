#!/usr/bin/env node
// Syncs .github/labels.json to the GitHub repository using the gh CLI.
// Usage: node scripts/github/sync-labels.mjs [--prune]
//   --prune  deletes repository labels that are not declared in labels.json

import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..", "..");
const declared = JSON.parse(readFileSync(resolve(root, ".github", "labels.json"), "utf8"));
const prune = process.argv.includes("--prune");

const gh = (args) => execFileSync("gh", args, { encoding: "utf8", stdio: ["ignore", "pipe", "inherit"] });

for (const label of declared) {
  gh(["label", "create", label.name, "--color", label.color, "--description", label.description, "--force"]);
  console.log(`synced  ${label.name}`);
}

if (prune) {
  const existing = JSON.parse(gh(["label", "list", "--limit", "200", "--json", "name"]));
  const names = new Set(declared.map((l) => l.name));
  for (const { name } of existing) {
    if (!names.has(name)) {
      gh(["label", "delete", name, "--yes"]);
      console.log(`deleted ${name}`);
    }
  }
}
