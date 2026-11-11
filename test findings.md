# Voice-First Dev Environment: Test Findings

*Derived claims. Each claim cites its evidence: T01 to T08 are test records in the tested folder; "observed" means seen during the session but without a written test record yet. Strategy and code live in separate docs.*

## Google Docs access

- Claude can find, read, and edit Google Docs in the user's Drive. A fresh agent in a new chat onboards from one spoken sentence pointing it at claude.md. (T08.)
- Edits made by other agents or by the user are visible to Claude on the next read. (Observed.)
- Structural edits work: renaming headings, adding and removing sections, fixing styles. Claude can verify formatting afterward. (Observed; see also T03.)

## Version history

- Google Docs automatically keeps a revision history of every edit, including Claude's.
- Users can view, name, and restore versions through File, then Version history. Named versions work much like git tags. (General knowledge, not tested.)
- Differences from git: a single linear timeline, no branches, and small edits get merged into larger snapshots.
- Correction: Claude cannot list or download past revisions. The Drive tools expose no revision IDs, and downloading by revision returns "not yet supported." Viewing and restoring past versions must be done in the Docs app. Claude keeps its own history instead (see Architecture). (T05.)

## Python sandbox

- Python 3.12 on Linux, with git 2.43 installed. (T01.)
- Files persist between code runs within a single chat. They also survive a voice call reconnecting to the same chat. They do not persist across chats: a new chat starts with an empty sandbox, so the bootstrap must run every session. (T01, T07, T08.)
- PyPI is reachable and packages install, but only with pip install --break-system-packages; a plain pip install is refused. (T01, T06.)
- The GitHub API returned 403 Forbidden, so GitHub appears to be blocked. (T01.)

## Round trip test

A small program, word_stats.py, was written and run in the sandbox, saved to Drive as a Google Doc via plain-text upload, downloaded again, and run successfully with new input. (T02.) The cleanup step was later repeated with the docs_io.py helper (T04), and docs_io.py itself was loaded fresh from Drive and worked, using the bootstrap snippet now in agents.md. (T07.) The same bootstrap also worked cold in a brand new chat. (T08.)

## Formatting behavior

Two different conversions happen, and they behave differently.

### Documents (Markdown to Google Docs)

- Uploading Markdown converts cleanly into headings, bullets, numbered lists, and bold text.
- The only side effect is occasional empty spacer paragraphs before lists. These are cosmetic. (T03.)

### Code (plain text to Google Docs and back)

- Reading code with the natural-language read tool is unsafe: it returns Markdown, adding backslash escapes before underscores, brackets, and similar characters, and inserting blank lines between every line. (T02.)
- Downloading with a plain-text export is safe, with three harmless quirks: a byte order mark at the start, Windows-style line endings, and extra blank lines before function definitions. (T02.)

## Rules

- Write documents as Markdown; write code as plain text.
- Always load code with the download tool and plain-text export, never with the natural-language read tool.
- Clean every loaded program: strip the byte order mark and normalize line endings (handled by docs_io.py).
- Treat the sandbox as scratch space; Docs is the source of truth. Save back after any meaningful change.

## Open questions

- Answered: Drive revision IDs cannot be listed or downloaded with current tools, so Claude cannot diff Google's versions directly. (T05.)
- Answered: sandbox files do not survive across chats. (T08.)
- How does the workflow hold up with a larger, multi-file program?
