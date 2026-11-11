# skill: /end

**Trigger:** Mark says "slash end" (older phrases: "slash wrap up", "wrap up the session").

**What it does:** closes a development run so a verifier and the next agent can pick it up cold. Needs a text turn.

## Steps

1. Write summary.md in your run folder: a permanent record of the run with goal, base commit, what was done, decisions and why, files changed, tests run, mistakes and corrections, and open items.
2. Write run-claims.md in the format given in verification protocol.md. Every change made this run gets a claim with the commit that made it and concrete checks.
3. In next.md, tag every item (agent) or (operator) and list them in the order they should happen. Do not add a verification item: the verify thread finds its run by itself (the highest-numbered run with no verify folder). Tag an item (operator) only when Mark must act before work can go on. next.md lists only open work, so the next session can pick up cold: move every item closed this run from next.md to history.md (root), one line each with the date, the item, run NN and the evidence. Begin next.md with a pointer to your summary.md by path.
4. Write thread.md in your run folder: the spoken exchanges only, with no tool calls and no reasoning.
5. Commit these files (prefix "run NN:", version control rule vc-06), push, and follow sync.md (skills folder) to refresh the Drive mirror.
6. Tell Mark by voice what was written, following communication policy.md (root, then policy), and remind him to start the verification thread.

## Notes

- There are no checkpoints or end snapshots any more: the run's commits are the record.
- Status: rewritten in run 04; not yet tested.
