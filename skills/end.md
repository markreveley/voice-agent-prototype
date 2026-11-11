# skill: /end

**Trigger:** Mark says "slash end" (older phrases: "slash wrap up", "wrap up the session").

**What it does:** closes a development run so a verifier and the next agent can pick it up cold.

## Steps

1. Write summary.md in your run folder: a permanent record of the run with goal, what was done, decisions and why, files changed, tests run, mistakes and corrections, and open items. Then do the remaining steps in order.
2. Write run-claims.md in the format given in verification protocol.md. Every change made this run gets a claim with its checkpoint link and concrete checks.
3. In next.md, tag every item (agent) or (operator) and list them in the order they should happen. Do not add a verification item: the verify thread finds its run by itself (the highest-numbered run with no verify folder). Tag an item (operator) only when Mark must act before work can go on. next.md lists only open work, so the next session can pick up cold: move every item closed this run from next.md to history.md (root), one line each with the date, the item, run NN and a link to the evidence. Begin it with a pointer to your summary: your run folder name and a link to summary.md.
4. Copy every current doc (root, skills folder and policy folder) into your run's end snapshot folder, titled per naming rule name-04.
5. Write thread.md in your run's thread folder: the spoken exchanges only, with no tool calls and no reasoning. Upload long threads in parts.
6. Tell Mark by voice what was written, following communication policy.md (root, then policy), and remind him to start the verification thread.

## Notes

- Upload long docs in parts, and keep tool calls to about five per turn.
- Status: not yet tested.
