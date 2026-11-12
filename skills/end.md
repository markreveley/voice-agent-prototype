# skill: /end

**Trigger:** Mark says "slash end" (older phrases: "slash wrap up", "wrap up the session").

**What it does:** closes a development run so a verifier and the next agent can pick it up cold. Needs a text turn.

## Steps

1. Write summary.md in your run folder in Agents slash runs (Drive only): a permanent record of the run with goal, base commit, what was done, decisions and why, files changed (including every change made outside the repo), tests run, mistakes and corrections, and open items. For a fixes run, confirm it made only the report's fixes (verification rule ver-03).  
2. Check that every change made this run is either listed in a commit message or in summary.md, since those are the claims a verifier checks (verification rule ver-05, policy folder).  
3. In next.md, tag every item (agent) or (operator) and list them in the order they should happen. Do not add a verification item: the verify thread finds its run by itself (the newest run folder; verification rule ver-04). Tag an item (operator) only when Mark must act before work can go on. next.md lists only open work, so the next session can pick up cold: remove every item closed this run from next.md, and name each one in the commit message with its evidence (version control rule vc-05). An item closed with no repo change goes in summary.md instead. Begin next.md with a pointer to your summary.md by path.  
4. Make sure every change in the Drive working copy is committed: nothing may be left uncommitted at the end of a run.  
5. Commit next.md and any remaining changes with commit.md (skills folder), as one commit with the prefix "run NN:" (version control rule vc-06) that lists every change (vc-05). Then push with push.md (skills folder).  
6. Tell Mark by voice what was written, following communication policy.md (policy folder). Remind him to start the verification thread (slash verify) before the next run, because every run is verified before the next one starts (verification rule ver-03).

## Notes

- There are no checkpoints or end snapshots any more: the run's commits are the record.  
- Status: rewritten in run 04; used in runs 05 and 06; steps 1, 3 and 6 changed in run 07.
