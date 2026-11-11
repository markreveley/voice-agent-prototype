# skill: /start-dev

**Trigger:** Mark says "slash start-dev" at the beginning of a new chat, or "read claude.md".

**What it does:** onboards a fresh development agent (development only; verification threads use slash verify) and gets it ready to work.

## Steps

1. Read claude.md, then agents.md, then doctrine.md and verification protocol.md (in root), then communication policy.md (root, then policy).
2. Follow the read order in agents.md: next.md, then the previous run's summary.md.
3. Read the previous run's verification report (report.md in its verify folder). If none exists, tell Mark the run was not verified and ask whether to go ahead. Fix any failures first, and record each fix in your own run-claims.md. If the previous run has no summary or end snapshot, tell Mark and fill in what you can.
4. Create your run folder in agent-runs with the next run number (e.g. run 04 - 2026-11-11 - short label), plus its checkpoints, end snapshot, and thread subfolders.
5. Follow bootstrap.md (skills folder) to load docs_io.py into the sandbox.
6. Tell Mark by voice, in one short list: verification failures to fix, the (agent) items in next.md, and any (operator) items waiting on him. Then ask what to start with.

## Notes

- Do steps 1 to 5 without asking permission between them; they are routine.
- Status: not yet tested.
