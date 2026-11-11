# skill: /start-dev

**Trigger:** Mark says "slash start-dev" at the beginning of a new chat, or "read claude.md", or "read agents.md".

**What it does:** onboards a fresh development agent (development only; verification threads use slash verify) and gets it ready to work.

## Steps

1. Read agents.md. You may find it in Drive or in the repo; both say the same thing.
2. Follow bootstrap.md (skills folder) to clone the repo. This needs a text turn: if you are in voice, ask Mark to type (communication rule comm-11).
3. From the clone, read doctrine.md, verification protocol.md, every file in the policy folder, then next.md and the previous run's summary.md.
4. Read the previous run's verification report (report.md in its verify folder). If none exists, tell Mark the run was not verified and ask whether to go ahead. Fix any failures first, and record each fix in your own run-claims.md.
5. Pick your run folder name: agent-runs/run NN - date - short label, with the next run number and Mark's local date. Git keeps no empty folders, so the folder appears when you commit its first file.
6. Tell Mark by voice, in one short list: verification failures to fix, the (agent) items in next.md, and any (operator) items waiting on him. Then ask what to start with.

## Notes

- Do steps 1 to 5 without asking permission between them; they are routine.
- Runs 01 to 03 predate git: their folders are in the Drive archive folder (root, then archive), not in the repo.
- Status: rewritten in run 04; not yet tested cold.
