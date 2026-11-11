# version control policy

*How changes are recorded so they can be audited and undone. Moved from agents.md (history protocol) in run 03 (2026-11-10). Rewritten in run 04 (2026-11-10), when the git repo replaced Drive as the store and checkpoints were dropped. Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**vc-01 (retired) Checkpoint before every edit.** Retired in run 04: every change is now a git commit (vc-04), so git keeps the old version.

**vc-02 (retired) Local git is optional.** Retired in run 04: the repo itself is now the store (vc-04).

**vc-03 (retired) Google version history is the last resort.** Retired in run 04: the Drive folder is now a mirror, so its version history is not needed.

**vc-04 (serves doc-03) Git is the only source of truth.** The repo github.com/markreveley/voice-agent-prototype holds every project file. Change files only by committing to its main branch. Never edit the Drive mirror: it is overwritten on every sync.

**vc-05 (serves doc-03) One change per commit.** Each commit makes one change, with a message that says what changed and why.

**vc-06 (serves doc-04) Prefix every commit with its thread.** Commit messages start with "run NN:" in a development run and "verify NN:" in a verification thread, so a verifier can list a run's commits with git log --grep.

**vc-07 (serves doc-03) Push early, and always before the session ends.** The sandbox resets between chats, so a commit that was not pushed is lost.

**vc-08 (serves doc-01) Sync the Drive mirror after every push.** Follow sync.md (skills folder), so voice turns, which can reach Drive but not git, read the current state.

**vc-09 (serves doc-04) Cite commits by hash, not by tag.** Pushing tags from the sandbox is refused (test record t09), so summaries, claims and reports name commits by their short hash.

## Changing this policy

New rules go here with the next unused ID (vc-10, ...). Edit this file in the repo and commit; git keeps the old version.
