# verify 04 report

*Verification of run 04 - 2026-11-10 - git as the source of truth. Done 2026-11-10, about 19:30 to 19:50 Pacific, by a fresh Claude chat following verify.md (skills) and verification protocol.md (root). Run 04 was chosen as the highest-numbered run folder in agent-runs with no verify folder; Mark did not pass a run number. This is the first verification done with git.*

## Result

9 of 11 claims pass and 2 fail. Both failures are wrong counts in the claims, not wrong work: c07 says history.md gained 8 lines (it gained 7), and c09 says 19 old Drive copies were trashed (there were 18, and all 18 are in the trash). No change to the repo went unclaimed, but three rule edits inside claimed commits are not described by any claim (U1). Two problems were found that the next run should fix: the shallow clone in bootstrap.md cannot support verification (P1), and history.md lost its line breaks in the Drive mirror (P2).

## Method

Followed bootstrap.md, except that the clone was a full clone, not --depth 1 (see P1). Read agents.md, verification protocol.md, verify.md, doctrine.md, all five policy files, every skill, next.md, and run 04's summary.md, run-claims.md and thread.md from the clone at 1674906 (git status clean, HEAD equal to origin/main).

For each claim, read the commit with git show and ran the checks against the files at 1674906 with grep, diff and python3. For the Drive claims, listed every Drive folder of the mirror by parent ID, searched the trash, and read docs with read_file_content. Drive content was compared with the repo by reading both in full, side by side, not by a diff in the sandbox, because the Drive connector returns text into the conversation, not into a file. Drive's markdown escapes, list markers and spacing were ignored. No size or timestamp was used as evidence.

## Commit range (steps 2 and 4)

git log --oneline --grep "^run 04:" lists six commits, f7b4019 to 1674906. The parent of f7b4019 is f5cf059, the base commit named in run-claims.md. Every commit from f5cf059 to 1674906 has the "run 04:" prefix. The two commits before the range, 13f9939 and f5cf059, have no prefix; run-claims.md says so, and vc-06 did not exist yet.

## Claims

**c01 pass.** git show 13f9939 adds only push-test.md (3 lines), whose text includes "If this file is here, pushing works". f5cf059 deletes it, and it is not at HEAD. tested/t09 steps 3 and 4 describe the commit, the push and the fresh-clone read-back.

**c02 pass, with one note.** f5cf059 adds 29 files: 10 root docs, 2 programs, 5 policy files, 4 skills and 8 test records, and no agent-runs folder. The run 03 end snapshot folder (archive, then agent-runs, then the run 03 folder) holds 21 copies. The 19 other than next.md and history.md were each read in full and matches its imported file apart from escapes, list markers and spacing. next.md matches the verify 03 checkpoint of next.md plus the two edits verify 03 describes (the summary link target and the fixes in item 1); history.md matches the verify 03 checkpoint of history.md plus the verify 03 line. Both programs parse with python3, and python3 word_stats.py "a b a" prints "3 words; top: [('a', 2), ('b', 1)]". Note: the end snapshot holds no test records, so the claim's check cannot be run as written for t01 to t08. They were compared instead with the live copies in the Drive tested folder, which run 04 did not touch, and all eight match (t08 gains a code fence around its raw output, which is formatting).

**c03 pass.** f7b4019 changes doctrine.md and the five policy files. At 1674906: vc-01 to vc-03 are retired, vc-04 to vc-09 exist, the next ID is vc-10, and vc-09 cites t09; name-03 and name-04 are retired and name-06 is "Same path in the repo and in Drive"; fmt-03 is retired and fmt-04 is "Run code only from the clone"; comm-11 is "Ask for text when git is needed" and the next ID is comm-12; doc-03 says "commit diff", and doctrine.md contains no "checkpoint"; no policy file says "checkpoints folder". No later commit touches these files. See U1 for rule edits this claim does not mention.

**c04 pass.** 8d2daa3 changes the four skills and adds sync.md (git log --diff-filter=A shows sync.md first appears here). bootstrap.md step 2 calls add_repo with access push, step 3 runs git clone, and it has no base64 code. start-dev.md step 2 follows bootstrap.md, and no step creates checkpoints or end snapshot folders. end.md has no end snapshot step, and step 5 commits, pushes and follows sync.md. verify.md step 1 clones the repo. sync.md step 4 uploads the new copy before trashing the old one.

**c05 pass.** b878cab changes agents.md, claude.md and verification protocol.md. agents.md says the repo is the source of truth and the Drive folder a read-only mirror, and has no docs.google.com or drive.google.com link. claude.md names the repo and the Drive mirror. Verification protocol step 2 uses git log --grep, step 4 uses git diff --stat, step 5 checks mirror.md, and the next development thread section says "your own run-claims.md".

**c06 pass.** 9ddb6bf changes architecture.md, strategy.md and test findings.md, and adds tested/t09. t09's raw output for step 5 has "error: RPC failed; HTTP 403" for the tag push. test findings.md has a section git and GitHub whose correction cites T09; its round trip section now says the snippet was "then kept in agents.md" and moved to bootstrap.md; its rules section is gone. architecture.md has no conventions section, and its storage layer is the git repo. strategy.md's tradeoff cites t09.

**c07 fail.** d9712bd changes history.md and next.md. The 16 earlier history.md lines are unchanged (compared line by line with f5cf059), and the P1 answer is there. But the commit adds 7 lines, not 8: history.md goes from 16 dated lines to 23. The next.md part passes: five items, item 1 is the (operator) stress-test choice, and nothing mentions revision download or "fix any failures first".

**c08 pass.** Drive root has five folders: archive, agent-runs, policy, skills and tested. archive holds one agent-runs folder, which holds the run 01, run 02 and run 03 folders. The agent-runs folder in root holds only the run 04 folder.

**c09 fail.** The work is right; the count is wrong. The claim says 20 files were uploaded and 19 old copies trashed, with only sync.md lacking an old copy. But t09 is new too, so there were 18 old copies, and the claim's own list names 18 (9 root, 5 policy, 4 skills). A trash search finds all 18 old copies. summary.md (what was done, item 10) repeats the 19. The other checks pass: the live titles in root, policy, skills and tested equal the repo's paths, with no duplicates, mirror.md and the archive folder aside; and all 20 synced docs, read back in full, match the repo files apart from formatting (next.md as replaced in c11) (see P2 for history.md's formatting).

**c10 pass.** git show --stat 1674906 lists exactly run-claims.md, summary.md, thread.md and next.md. In next.md only the header line and the previous-run pointer change, and the pointer names "agent-runs slash run 04 - 2026-11-10 - git as the source of truth slash summary.md".

**c11 pass.** mirror.md's first line is "mirror of commit 1674906", the run's last commit. The Drive copy of next.md has the new pointer. There is one live mirror.md in root; the first-sync mirror.md and the first-sync next.md are in the trash. The Drive folders agent-runs and the run 04 folder exist, and the Drive copies of summary.md, run-claims.md and thread.md match the repo files.

## Unclaimed changes

git diff --stat f5cf059 1674906 lists 23 files, and every one is covered by c03 to c07 or c10. Nothing was changed outside those commits.

**U1 Rule edits no claim describes.** These are in claimed commits and in the commit messages, but no claim or summary item mentions them, and some change what agents do:

1. naming rule name-05, which is confirm the parent: now also covers the tested and agent-runs folders and warns about the archive (f7b4019).
2. file format rule fmt-02, which is code as plain text: no longer covers handoff files, so next.md and history.md are now uploaded as markdown (f7b4019). This leads to P2.
3. naming rule name-01, which is lowercase titles: now says file and folder names instead of titles (f7b4019).
4. Guidance dropped from skills (8d2daa3): end.md's note to upload long docs in parts and keep to about five tool calls a turn; start-dev.md's case for a previous run with no summary; verify.md's case for a run with no run-claims.md.

## Rule breaks and notes

**P1 bootstrap.md's shallow clone breaks verification.** bootstrap.md step 3 clones with --depth 1, and verification protocol step 1 says to follow bootstrap.md. Tested in this thread: in a --depth 1 clone, git log --grep shows only 1674906, git rev-parse 1674906^ fails with "fatal: Needed a single revision", and git diff --stat f5cf059 1674906 fails with "unknown revision". So steps 2 and 4 cannot run. This thread used a full clone instead. bootstrap.md should say that a verification thread needs a full clone (or fetches back to the base commit).

**P2 history.md is one paragraph in the Drive mirror.** The synced history.md shows all 23 log lines run together in one paragraph, because markdown joins lines that have no blank line between them. Before run 04, history.md was uploaded as plain text (the old fmt-02) and kept its lines. A voice turn reading the mirror now gets one long run-on block. Other synced files kept their structure, because they use lists or blank lines.

**P3 One change per commit (version control rule vc-05).** f7b4019 changes six files across four rule categories plus doctrine, and 9ddb6bf mixes three docs with a new test record. summary.md admits this. Each commit has one theme, but they are not single changes.

**P4 Doctrine changed without Mark.** doc-03 was reworded from checkpoint to commit without asking Mark. The meaning holds, and summary.md says so, but Mark should confirm it.

**P5 Names, suffixes, evidence and the mirror.** Every repo path and Drive title is lowercase, and every file ends in .md or .py. New claims in test findings.md cite T09 or say observed. The mirror is in step: mirror.md names 1674906, the run's last commit, and HEAD equals origin/main.

**P6 Claims format.** Claims c03 to c07 each cover one commit with several files and have no one-sentence what-changed line per file, as the claims list format asks. This made U1 easy to miss.

## Edits by this thread

1. Created this folder (verify 04 - 2026-11-10) and this report.
2. next.md: added one (agent) item at the top listing the fixes below, under step 7's exception.
3. history.md: added one line for this verification.
4. communication policy.md (policy folder): added communication rule comm-12, which is explain in plain words, step by step, with a verbatim reference example, and moved the next ID to comm-13. A verification thread normally changes no policy; Mark asked for this by voice after the report was first written, when he found the verifier's second explanation of P1 much clearer than its first. It is outside step 7's next.md exception and is recorded here so the next run can see it.

Each is its own commit with the prefix "verify 04:". Then pushed and synced the Drive mirror (sync.md).

## Fixes for run 05

1. P1: change bootstrap.md so a verification thread makes a full clone, or fetches back to the base commit, and note it in verification protocol step 1.
2. P2: make history.md keep its lines in Drive, for example with a blank line or a list marker per entry, or upload handoff files as plain text again; then sync and read it back.
3. c07 and c09: record the corrected counts (7 history lines; 18 old copies) in run 05's run-claims.md. Reports and summaries stay as written.
4. P4: ask Mark to confirm the doc-03 rewording, and the U1 rule edits (name-05, fmt-02, name-01).
