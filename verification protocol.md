# verification protocol

*Mark works by voice and does not check the files visually, so the work of each development thread is checked by a separate, independent agent. Set by Mark in run 02 (2026-11-09). Rewritten in run 04 (2026-11-10) to compare git commits instead of Drive checkpoints. Status: proposed, not yet tested with git.*

## The cycle

1. **Development thread** (run NN): an agent does the work, following agents.md, and commits each change with the prefix "run NN:" (version control rule vc-06).  
2. **Wrap-up**: when Mark says "slash end", the agent follows end.md (skills folder), including writing summary.md, committing and pushing.  
3. **Verification thread** (verify NN): Mark opens a fresh chat and says "slash verify" (skills folder, verify.md). The run to verify is the highest-numbered run folder in Agents slash runs (Drive, outside every repo) with no verify folder, so Mark never passes a run number and next.md never mentions verification. That agent audits the claims and does no development work.  
4. **Next development thread** (run NN+1): starts by reading the verification report for the previous run.

The development agent never verifies its own run. Within a thread it should still check its own work, but that does not count as verification.

## Claims (written as you go)

There is no separate claims file. The claims are:

1. **Commit messages: each commit lists every change in it, by file path, one sentence each, with why (version control rule vc-05).**  
2. **summary.md: names the run's base commit, and lists every change made outside the repo (Drive folders moved or trashed, files in other projects).**  
3. **Checks: the verifier turns each listed change into concrete, testable statements and checks them against the diff.**

Changes made after wrap-up go in a new commit, and summary.md is extended to cover them.

## Verification thread steps

1. Make a full clone with pull.md steps 1 to 4 (skills folder). Read agents.md and this file from Drive, and the run's summary.md from Agents slash runs.  
2. List the run's commits: git log \--oneline \--grep "^run NN:". Check that the first one's parent is the base commit named in summary.md.  
3. For each change listed in the run's commit messages: show its commit (git show HASH), check that the diff matches what the message says, and run the checks against the file as it stands at the run's last commit. Content, not metadata: sizes and timestamps are never evidence. If a check can't be run, mark the claim could not check, never pass.  
4. Look for changes the claims list missed: git diff \--stat BASE LAST shows every file the run changed; list any change that no claim covers. Also list any commit in that range without the "run NN:" prefix.  
5. Check the run against its rules: lowercase names, .md suffixes, every change listed in its commit message, test findings citing test records, and the Drive working copy in step with the repo (no Drive file differs from the run's last commit).  
6. Write report.md in a "verify NN \- date" folder inside the run's folder in Agents slash runs (Drive only, not committed). For each claim: pass, fail, or could not check, with the evidence. Then unclaimed changes, then rule breaks.  
7. Fix nothing. Report only, so the record stays clean. The next development thread makes the fixes. One exception, set by Mark in run 03: the verification thread may edit next.md (root), for example to add the fixes the next run must make, and lists that edit in report.md.  
8. If you edited next.md, commit that edit with commit.md, using the prefix "verify NN:", and push with push.md (skills folder).  
9. Tell Mark the result by voice, following communication policy.md (policy folder): how many claims passed, and each failure in one sentence.

## Next development thread

At session start, read the previous run's verification report. Fix any failures first, and list each fix in your commit messages.

## Not yet tested

- Whether a fresh agent can do this well from these instructions alone.  
- The git-based steps 1 to 5, which replace the Drive checkpoint comparisons verify 02 and verify 03 used.
