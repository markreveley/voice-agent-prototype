# naming policy

*How docs and folders are titled and found. Moved from agents.md in run 03 (2026-11-10). Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**name-01 (serves doc-01) Lowercase titles.** All titles are lowercase, because text to speech spells capitalized names out letter by letter.

**name-02 (serves doc-01) Suffixes show the type.** Text docs end in .md, including test records and run summaries. Code keeps its own suffix (e.g. docs_io.py). Drive titles carry the same suffix.

**name-03 (serves doc-03) Checkpoint titles.** "[run NN checkpoint HH:MM] doc name - reason", with the time in UTC.

**name-04 (serves doc-03) Snapshot titles.** "[run NN snapshot] doc name".

**name-05 (no doctrine yet) Confirm the parent.** Never search Drive by title alone and trust the first hit: confirm the file's parent is the folder you expect (root, skills or policy).

## Changing this policy

New rules go here with the next unused ID (name-06, ...). Copy this doc into your run's checkpoints folder before editing it.
