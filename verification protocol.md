# verification protocol

*Mark works by voice and does not check the docs visually, so the work of each development thread is checked by a separate, independent agent. Set by Mark in run 02 (2026-11-09). Status: proposed, not yet tested.*

## The cycle

1. **Development thread** (run NN): an agent does the work, following agents.md.
2. **Wrap-up**: when Mark says "slash end", the agent does the end of session steps, including writing a claims list (below).
3. **Verification thread** (verify NN): Mark opens a fresh chat and says "slash verify" (skills folder, verify.md). The run to verify is the highest-numbered run with no verify folder, so Mark never passes a run number and next.md never mentions verification. That agent audits the claims and does no development work.
4. **Next development thread** (run NN+1): starts by reading the verification report for the previous run.

The development agent never verifies its own run. Within a thread it should still read docs back after editing, but that does not count as verification.

## Claims list (written at wrap-up)

A doc named "run-claims.md" in the run folder. One claim per change. Give each claim a fixed ID written in its text (c01, c02, ...) and use those IDs for cross-references, because Google Docs restarts list numbering in each section. Each claim has:

1. **What changed**: the doc (with its link) and the change in one sentence.
2. **Checkpoint**: the link to the checkpoint copy taken before the edit, or "new doc" if it was created.
3. **Checks**: concrete, testable statements. Example: quote, rule 6 says to say quote and end quote, end quote; quote, no rule mentions beep, end quote.

Also list docs created, renamed, moved, or trashed (snapshot and checkpoint copies included), plus any test record written. Changes made after wrap-up get their own claims, and the thread doc is extended to cover them.

## Verification thread steps

1. Read agents.md, this doc, and the run's summary.md and run-claims.md.
2. Create "verify NN - date" inside the run's folder (agent-runs, then the run folder).
3. For each claim: read the current doc and its checkpoint, compare them by content, and run the checks. Content, not metadata: download both with exportMimeType text/plain and diff them in the sandbox. File sizes and timestamps are never evidence: Drive often reports a size of 1 for Google Docs, and a reordered list keeps the same length. If content can't be compared, mark the claim could not check, never pass. (Added after verify 02 passed an end snapshot on matching sizes when its content was out of date.)
4. Also look for changes the claims list missed: compare the run's end snapshot with the previous run's end snapshot, and list anything changed but not claimed.
5. Check the run against its protocols: a checkpoint before every edit, lowercase titles, .md suffixes, and test findings citing test records.
6. Write "report.md" in the verify folder. For each claim: pass, fail, or could not check, with the evidence. Then unclaimed changes, then protocol breaks.
7. Fix nothing. Report only, so the record stays clean. The next development thread makes the fixes. One exception, set by Mark in run 03: the verification thread may edit next.md (root), for example to add the fixes the next run must make. Checkpoint next.md first, in the verify folder, titled [verify NN checkpoint HH:MM] next.md - reason, and list the edit in report.md.
8. Tell Mark the result by voice, following communication policy.md (root, then policy): how many claims passed, and each failure in one sentence.

## Next development thread

At session start, read the previous run's verification report. Fix any failures first, and record each fix in that run's own claims list.

## Not yet tested

- Whether a fresh agent can do this well from these instructions alone.
- Whether reading docs back through the Drive tools is reliable enough for diffs, or whether plain-text download should be used.
