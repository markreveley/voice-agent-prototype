# file format policy

*How files are stored in the repo and in the Drive working copy. Moved from agents.md in run 03 (2026-11-10); updated in run 04 for the git repo. Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**fmt-01 (no doctrine yet) Prose as markdown.** Prose files in the repo are markdown, and they live in Drive as Google Docs converted from text/markdown.

**fmt-02 (no doctrine yet) Code as plain text.** Code goes to Drive as text/plain, converted to a Google Doc.

**fmt-03 (retired) Read code only as plain text.** Retired in run 04: code is now run from the git clone, not loaded from Drive (fmt-04). On 2026-11-11 fmt-04 brought the plain-text rule back, since code is edited in Drive again.

**fmt-04 (no doctrine yet) Move code with the plain-text download.** Code can be edited in the Drive working copy. Whenever code goes from Drive into the sandbox, to run it or to commit it, use download\_file\_content with plain text and clean the export with docs\_io.py (root; test records t02 and t04). Reading code with read\_file\_content adds backslash escapes before underscores and brackets (test record t02), so do not quote it as exact.

## Changing this policy

New rules go here with the next unused ID (fmt-05, ...). Edit this file in the repo and commit; git keeps the old version.
