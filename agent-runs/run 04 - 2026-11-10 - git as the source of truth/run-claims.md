# run 04 claims

*For the verification thread (verification protocol.md, root). Base commit: f5cf059. The run's commits are listed with git log --oneline --grep "^run 04:". Two earlier commits from this run, 13f9939 and f5cf059, have no prefix because version control rule vc-06 did not exist yet. IDs are fixed.*

## Before the import

**c01 Push test.** Commit 13f9939 added push-test.md; f5cf059 deleted it. Checks: git show 13f9939 adds only push-test.md, whose text says "If this file is here, pushing works"; push-test.md does not exist at HEAD; tested/t09 steps 3 and 4 describe this.

**c02 Import of the Drive project.** Commit f5cf059 adds 29 files: 10 root docs, 2 programs, 5 policy files, 4 skills and 8 test records. Checks: every file matches its copy in Drive's root slash archive slash agent-runs slash run 03 - 2026-11-10 - verification fixes, policy, doctrine and history slash end snapshot folder, apart from Drive's markdown escapes, list markers and spacing; next.md and history.md instead match the state after verify 03's edits (verify 03 report.md, section edits by this thread); docs_io.py and word_stats.py parse as Python, and python3 word_stats.py "a b a" prints "3 words"; no agent-runs folder is in this commit.

## Run 04 commits

**c03 Policy and doctrine.** Commit f7b4019. Checks: version control policy.md marks vc-01, vc-02 and vc-03 retired and has vc-04 to vc-09, its next ID is vc-10, and vc-09 cites t09; naming policy.md marks name-03 and name-04 retired and has name-06 ("Same path in the repo and in Drive"); file format policy.md marks fmt-03 retired and has fmt-04 ("Run code only from the clone"); communication policy.md has comm-11 ("Ask for text when git is needed") with next ID comm-12; doctrine.md doc-03 says "commit diff" and no longer says "checkpoint"; no policy file says "checkpoints folder".

**c04 Skills.** Commit 8d2daa3. Checks: bootstrap.md has add_repo with access push and git clone, and no base64 bootstrap code; start-dev.md step 2 follows bootstrap.md and no step creates checkpoints or end snapshot folders; end.md has no end snapshot step, and its step 5 commits, pushes and follows sync.md; verify.md step 1 clones the repo; sync.md is new and its step 4 uploads before trashing.

**c05 Onboarding and verification.** Commit b878cab. Checks: agents.md says the repo is the source of truth and the Drive folder a read-only mirror, and contains no docs.google.com or drive.google.com link; claude.md names both the repo and the mirror; verification protocol.md step 2 uses git log --grep, step 4 uses git diff --stat, step 5 checks the mirror, and its "next development thread" section says "your own run-claims.md".

**c06 Architecture, strategy, findings and t09.** Commit 9ddb6bf. Checks: the t09 test record exists, with raw output for the 403 on the tag push; test findings.md has a section on git and GitHub with a correction citing T09; its round trip section no longer says the bootstrap is "now in agents.md" (verify 03 P3); its rules section is gone; architecture.md has no conventions section (P3) and says storage is the git repo; strategy.md's tradeoff cites t09.

**c07 Handoff files.** Commit d9712bd. Checks: history.md keeps all 16 earlier lines unchanged and adds 8 lines dated 2026-11-10 closed by run 04, including P1's answer; next.md has five items, with item 1 (operator) choosing the stress test, and no item about revision download or "fix any failures first".

**c10 End of run.** The run's last "run 04:" commit adds this folder (summary.md, run-claims.md and thread.md) and changes only next.md's previous-run pointer to this summary. Checks: git show --stat on that commit lists just these four files; next.md's pointer names "agent-runs slash run 04 - 2026-11-10 - git as the source of truth slash summary.md".

## Outside the repo (Drive)

**c08 Archive folder.** Created the archive folder in the Drive root and moved the old agent-runs folder (with runs 01 to 03) into it. Checks: Drive root slash archive slash agent-runs holds the three run folders; there is no agent-runs folder in the Drive root other than the one the end-of-run sync creates for run 04.

**c09 First sync, to d9712bd.** Uploaded the 20 files that changed between f5cf059 and d9712bd, and trashed the 19 old copies (sync.md had no old copy). Trashed: in root, agents.md, architecture.md, claude.md, doctrine.md, history.md, next.md, strategy.md, test findings.md and verification protocol.md; in policy, all five files; in skills, bootstrap.md, end.md, start-dev.md and verify.md. New: tested slash t09 and skills slash sync.md. Created mirror.md. Checks: the live titles in Drive root, policy, skills and tested equal the repo's paths at d9712bd, with no duplicates (mirror.md and the archive folder excepted); each synced doc's text matches its repo file, apart from formatting; Drive search with trashed = true finds the 19 old copies.

**c11 End-of-run sync.** After c10, synced next.md and the three new files of this folder (with new Drive folders agent-runs and the run 04 folder) and replaced mirror.md. Checks: mirror.md's first line names the run's last commit; the Drive copy of next.md has the new pointer; only one live mirror.md exists.

## Not claimed as changes

- The earlier read-only clone at /home/claude/markreveley/voice-agent-prototype (sandbox only).
- Read-backs and the fresh-clone check, which are checks, not changes.
