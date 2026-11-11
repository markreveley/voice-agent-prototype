# version control policy

*How changes to docs are backed up so they can be audited and undone. Moved from agents.md (history protocol) in run 03 (2026-11-10). Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**vc-01 (serves doc-03) Checkpoint before every edit.** Before EVERY edit to any doc, copy it into your run's checkpoints folder first. No exceptions.

**vc-02 (serves doc-03) Local git is optional.** You may also commit docs to a local git repo at /tmp/repo for quick diffs within the session. It does not survive the chat.

**vc-03 (serves doc-03) Google version history is the last resort.** Only Mark can view or restore it, so never rely on it in place of a checkpoint.

## Changing this policy

New rules go here with the next unused ID (vc-04, ...). Copy this doc into your run's checkpoints folder before editing it.
