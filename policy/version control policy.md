# version control policy

*How changes are recorded so they can be audited and undone. Moved from agents.md (history protocol) in run 03 (2026-11-10). Rewritten in run 04 (2026-11-10), when the git repo replaced Drive as the store and checkpoints were dropped. Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**vc-01 (retired) Checkpoint before every edit.** Retired in run 04: every change is now a git commit (vc-04), so git keeps the old version.

**vc-02 (retired) Local git is optional.** Retired in run 04: the repo itself is now the store (vc-04).

**vc-03 (retired) Google version history is the last resort.** Retired in run 04: the Drive folder is now a mirror, so its version history is not needed.

**vc-04 (serves doc-03) Git is the record; Drive is the working copy.** The repo github.com/markreveley/voice-agent-prototype holds every project file. The Drive folder (Agents, then voice coding agent) is its working copy: edit there, by voice or text, then commit and push. Drive is the only place edits happen; never change the repo any other way. Changed 2026-11-11.

**vc-05 (serves doc-03) One commit per commit command.** Each commit holds everything changed since the last one, with a message that lists every change and why, and every next.md item it closes with its evidence, so a verifier can check each listed change against the diff. Changed 2026-11-11.

**vc-06 (serves doc-04) Prefix every commit with its thread.** Commit messages start with "run NN:" naming the run that made them (verification threads do not commit; verification rule ver-07), so a verifier can list a run's commits with git log \--grep.

**vc-07 (serves doc-03) Push early, and always before the session ends.** The sandbox resets between chats, so a commit that was not pushed is lost.

**vc-08 (retired) Sync the Drive mirror after every push.** Retired 2026-11-11: Drive is now the working copy, and changes move between Drive and git with the pull and commit skills (skills folder).

**vc-09 (serves doc-04) Cite commits by hash, not by tag.** Pushing tags from the sandbox is refused (test record t09), so summaries, claims and reports name commits by their short hash.

**vc-10 (serves doc-03) Export only changed docs.** At commit time, export a Drive doc only if Drive shows it modified later than ten minutes before the last commit, or it has no file in the clone. Find deleted docs by comparing the Drive listing with git ls-files. A doc Drive shows unedited since then is taken to match the repo, because every edit happens in Drive (vc-04). Added by Mark, 2026-11-11.

**vc-11 (serves doc-01) Report a refused repo attach at once.** If attaching the repo is refused, copy the exact error message, tell Mark at once so he can approve or fix access while the chat is still open, and record the message in the run's summary.md. Never work around a refusal. Added by Mark in run 07 (2026-11-11).

## Changing this policy

New rules go here with the next unused ID (vc-12, ...). Edit this file in Drive and commit; git keeps the old version.
