# skill: /verify

**Trigger:** Mark says "slash verify", with no run number. The run to verify is the highest-numbered run folder in Agents slash runs (Drive, outside every repo). If it has no verify folder, verify it. If it already has a verify folder with report.md, tell Mark there is nothing to verify. If it has a verify folder but no report.md, tell Mark an earlier verification was interrupted and ask whether to redo it.

**What it does:** an independent audit of one development run. This thread does no development work and fixes nothing, except that it may edit next.md (step 7 of section verification thread steps, in verification protocol.md). Its result is report.md, in the run's verify folder.

## Steps

1. Reach this skill the normal way (agents.md). From Drive, read agents.md, next.md (for context only; it does not name the run to verify), and communication policy.md (root, then policy). Then make a full clone with pull.md steps 1 to 4 (skills folder); this needs a text turn. Do not start a development run.  
2. Follow every step under section verification thread steps, in verification protocol.md (root).  
3. Report to Mark by voice: how many claims passed, and each failure in one sentence.

## Notes

- Runs 01 to 03 predate git; their summaries and reports are in Agents slash runs.  
- Status: rewritten in run 04; not yet tested.
