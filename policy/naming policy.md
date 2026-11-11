# naming policy

*How files and folders are named and found. Moved from agents.md in run 03 (2026-11-10); updated in run 04 for the git repo. Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**name-01 (serves doc-01) Lowercase titles.** All file and folder names are lowercase, because text to speech spells capitalized names out letter by letter.

**name-02 (serves doc-01) Suffixes show the type.** Text files end in .md, including test records and run summaries. Code keeps its own suffix (e.g. docs_io.py). Drive titles carry the same suffix.

**name-03 (retired) Checkpoint titles.** Retired in run 04: checkpoints were replaced by git commits.

**name-04 (retired) Snapshot titles.** Retired in run 04: end snapshots were replaced by git commits.

**name-05 (no doctrine yet) Confirm the parent.** Never search Drive by title alone and trust the first hit: confirm the file's parent is the folder you expect (root, skills, policy, tested or agent-runs). The archive folder holds old copies with the same titles.

**name-06 (serves doc-01) Same path in the repo and in Drive.** Every file's path from the repo root matches its path in the Drive mirror, so one path said aloud finds the file in both.

## Changing this policy

New rules go here with the next unused ID (name-07, ...). Edit this file in the repo and commit; git keeps the old version.
