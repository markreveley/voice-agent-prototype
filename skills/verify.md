# skill: /verify

**Trigger:** Mark says "slash verify", with no run number. The run to verify is the highest-numbered run in agent-runs. If it has no verify folder, verify it. If it already has a verify folder with report.md, tell Mark there is nothing to verify. If it has a verify folder but no report.md, tell Mark an earlier verification was interrupted and ask whether to redo it.

**What it does:** an independent audit of one development run. This thread does no development work and fixes nothing, except that it may edit next.md (see step 7 of the verification thread steps in verification protocol.md). When done, it adds one line to history.md (root): the date, Verify run NN, verify NN, and a link to report.md.

## Steps

1. Reach this skill the normal way (claude.md, then agents.md). Read agents.md (for the folder layout and rules), next.md (for context only; it does not name the run to verify), and communication policy.md (root, then policy). Do not create a run folder: this is not a development run.
2. Follow every step under "Verification thread steps" in verification protocol.md (root): <https://docs.google.com/document/d/1BN_8kc-NUDRBU1yGYG3ZA6-VZEILBoZA5DXsB_RgY_M/edit>
3. Report to Mark by voice: how many claims passed, and each failure in one sentence.

## Notes

- If the run has no run-claims.md (runs before run 02 do not), say so, and verify what you can from summary.md and the checkpoints.
- Status: not yet tested.
