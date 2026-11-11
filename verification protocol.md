# verification protocol

*Mark works by voice and does not check the files visually, so the work of each development thread is checked by a separate, independent agent. Set by Mark in run 02 (2026-11-09). Rewritten in run 04 (2026-11-10) to compare git commits instead of Drive checkpoints. Status: proposed, not yet tested with git.*

## The cycle

1. **Development thread** (run NN): an agent does the work, following agents.md, and commits each change with the prefix "run NN:" (version control rule vc-06).
2. **Wrap-up**: when Mark says "slash end", the agent follows end.md (skills folder), including writing a claims list (below), pushing, and syncing the Drive mirror.
3. **Verification thread** (verify NN): Mark opens a fresh chat and says "slash verify" (skills folder, verify.md). The run to verify is the highest-numbered run folder in agent-runs with no verify folder, so Mark never passes a run number and next.md never mentions verification. That agent audits the claims and does no development work.
4. **Next development thread** (run NN+1): starts by reading the verification report for the previous run.

The development agent never verifies its own run. Within a thread it should still check its own work, but that does not count as verification.

## Claims list (written at wrap-up)

A file named run-claims.md in the run folder. It begins with the run's base commit (the commit the run started from, recorded by bootstrap.md step 5). One claim per change. Give each claim a fixed ID written in its text (c01, c02, ...) and use those IDs for cross-references. Each claim has:

1. **What changed**: the file (by path) and the change in one sentence.
2. **Commit**: the short hash of the commit that made it.
3. **Checks**: concrete, testable statements. Example: quote, rule 6 says to say quote and end quote, end quote; quote, no rule mentions beep, end quote.

Also list files created, renamed, moved or deleted, any test record written, and anything changed outside the repo (such as Drive folders moved or trashed). Changes made after wrap-up get their own claims, and thread.md is extended to cover them.

## Verification thread steps

1. Follow bootstrap.md (skills folder) to clone the repo. From the clone, read agents.md, this file, and the run's summary.md and run-claims.md.
2. List the run's commits: git log --oneline --grep "^run NN:". Check that the first one's parent is the base commit named in run-claims.md.
3. For each claim: show its commit (git show HASH), check that the diff matches what the claim says, and run the checks against the file as it stands at the run's last commit. Content, not metadata: sizes and timestamps are never evidence. If a check can't be run, mark the claim could not check, never pass.
4. Look for changes the claims list missed: git diff --stat BASE LAST shows every file the run changed; list any change that no claim covers. Also list any commit in that range without the "run NN:" prefix.
5. Check the run against its rules: lowercase names, .md suffixes, one change per commit, test findings citing test records, and the Drive mirror in step with the repo (mirror.md names the run's last commit or a later one).
6. Write report.md in a "verify NN - date" folder inside the run's folder. For each claim: pass, fail, or could not check, with the evidence. Then unclaimed changes, then rule breaks.
7. Fix nothing. Report only, so the record stays clean. The next development thread makes the fixes. One exception, set by Mark in run 03: the verification thread may edit next.md (root), for example to add the fixes the next run must make, and lists that edit in report.md.
8. Commit report.md and any next.md edit with the prefix "verify NN:", add the history.md line (verify.md), push, and follow sync.md (skills folder).
9. Tell Mark the result by voice, following communication policy.md (policy folder): how many claims passed, and each failure in one sentence.

## Next development thread

At session start, read the previous run's verification report. Fix any failures first, and record each fix in your own run-claims.md.

## Not yet tested

- Whether a fresh agent can do this well from these instructions alone.
- The git-based steps 1 to 5, which replace the Drive checkpoint comparisons verify 02 and verify 03 used.
