# file format policy

*How files are stored in the repo and copied to the Drive mirror. Moved from agents.md in run 03 (2026-11-10); updated in run 04 for the git repo. Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**fmt-01 (no doctrine yet) Prose as markdown.** Prose files in the repo are markdown, and the mirror uploads them to Drive as text/markdown.

**fmt-02 (no doctrine yet) Code as plain text.** The mirror uploads code to Drive as text/plain.

**fmt-03 (retired) Read code only as plain text.** Retired in run 04: code is now run from the git clone, not loaded from Drive (fmt-04).

**fmt-04 (no doctrine yet) Run code only from the clone.** Never load code from the Drive mirror into a sandbox to run or edit it. In a voice turn, reading code from the mirror to describe it is fine, but read_file_content adds backslash escapes before underscores and brackets (test record t02), so do not quote it as exact.

## Changing this policy

New rules go here with the next unused ID (fmt-05, ...). Edit this file in the repo and commit; git keeps the old version.
