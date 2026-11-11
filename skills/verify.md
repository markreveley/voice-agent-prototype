# skill: /verify

**Trigger:** Mark says "slash verify", with no run number. The run to verify is the highest-numbered run folder in agent-runs in the repo. If it has no verify folder, verify it. If it already has a verify folder with report.md, tell Mark there is nothing to verify. If it has a verify folder but no report.md, tell Mark an earlier verification was interrupted and ask whether to redo it.

**What it does:** an independent audit of one development run. This thread does no development work and fixes nothing, except that it may edit next.md (step 7 of section verification thread steps, in verification protocol.md). When done, it adds one line to history.md (root): the date, Verify run NN, verify NN, and the path to report.md.

## Steps

1. Reach this skill the normal way (agents.md). Follow bootstrap.md (skills folder) to clone the repo; this needs a text turn. From the clone, read agents.md, next.md (for context only; it does not name the run to verify), and communication policy.md (root, then policy). Do not start a development run.
2. Follow every step under section verification thread steps, in verification protocol.md (root).
3. Report to Mark by voice: how many claims passed, and each failure in one sentence.

## Notes

- Runs 01 to 03 predate git; their records are in the Drive archive folder (root, then archive).
- Status: rewritten in run 04; not yet tested.
