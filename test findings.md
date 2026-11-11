# Voice-First Dev Environment: Test Findings

*Derived claims. Each claim cites its evidence: T01 to T09 are test records in the tested folder; "observed" means seen during the session but without a written test record yet. Strategy and code live in separate docs.*

## Google Docs access

- Claude can find, read, and edit Google Docs in the user's Drive. A fresh agent in a new chat onboards from one spoken sentence pointing it at claude.md. (T08.)  
- Edits made by other agents or by the user are visible to Claude on the next read. (Observed.)  
- Structural edits work: renaming headings, adding and removing sections, fixing styles. Claude can verify formatting afterward. (Observed; see also T03.)

## Version history

- Google Docs automatically keeps a revision history of every edit, including Claude's.  
- Users can view, name, and restore versions through File, then Version history. Named versions work much like git tags. (General knowledge, not tested.)  
- Differences from git: a single linear timeline, no branches, and small edits get merged into larger snapshots.  
- Correction: Claude cannot list or download past revisions. The Drive tools expose no revision IDs, and downloading by revision returns "not yet supported." Viewing and restoring past versions must be done in the Docs app. (T05.) Since run 04 this does not matter: the git repo holds the history.

## Python sandbox

- Python 3.12 on Linux, with git 2.43 installed. (T01.)  
- Files persist between code runs within a single chat. They also survive a voice call reconnecting to the same chat. They do not persist across chats: a new chat starts with an empty sandbox, so the repo must be cloned every session. (T01, T07, T08.)  
- PyPI is reachable and packages install, but only with pip install \--break-system-packages; a plain pip install is refused. (T01, T06.)  
- In a voice chat's code sandbox, the GitHub API returned 403 Forbidden. (T01.)

## Git and GitHub

- Correction: GitHub is not blocked everywhere. In a text turn, the sandbox can clone the repo and push to main once the repo is attached with write access. (T09; this corrects the earlier claim that GitHub appeared blocked, from T01.)  
- Pushing a git tag is refused with HTTP 403\. (T09.)  
- Voice turns in the same chat have no git or shell. (Observed; T09 step 6.)

## Round trip test

A small program, word\_stats.py, was written and run in the sandbox, saved to Drive as a Google Doc via plain-text upload, downloaded again, and run successfully with new input. (T02.) The cleanup step was later repeated with the docs\_io.py helper (T04), and docs\_io.py itself was loaded fresh from Drive and worked, using a bootstrap snippet then kept in agents.md. (T07.) The same bootstrap also worked cold in a brand new chat. (T08.) That snippet moved to bootstrap.md in run 03, and in run 04 bootstrap.md was rewritten to clone the git repo instead, so this Drive round trip left the workflow. Since 2026-11-11 it is part of it again: code edited in the Drive working copy reaches the repo by plain-text download (file format rule fmt-04).

## Formatting behavior

Two different conversions happen, and they behave differently.

### Documents (Markdown to Google Docs)

- Uploading Markdown converts cleanly into headings, bullets, numbered lists, and bold text.  
- The only side effect is occasional empty spacer paragraphs before lists. These are cosmetic. (T03.)

### Code (plain text to Google Docs and back)

- Reading code with the natural-language read tool is unsafe: it returns Markdown, adding backslash escapes before underscores, brackets, and similar characters, and inserting blank lines between every line. (T02.)  
- Downloading with a plain-text export is safe, with three harmless quirks: a byte order mark at the start, Windows-style line endings, and extra blank lines before function definitions. (T02.)

## Open questions

- Answered: Drive revision IDs cannot be listed or downloaded with current tools, so Claude cannot diff Google's versions directly. (T05.)  
- Answered: sandbox files do not survive across chats. (T08.)  
- How does the workflow hold up with a larger, multi-file program?
