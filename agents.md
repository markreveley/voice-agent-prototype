agents.md - onboarding for any agent working in this folder

what this is

A prototype of a strictly voice-driven coding agent. The operator (Mark) talks to an agent in the Claude chat app's voice mode. Google Docs in this folder are storage; the agent's Python sandbox is the runtime.

rules and principles

- Rules (policy) live in the policy folder (root, then policy: https://drive.google.com/drive/folders/1foS3VtMDjj4FSF7NhCTXkHQByxvsVG2-), one doc per category. Each rule has a fixed ID with a category prefix (e.g. comm-01) and names the doctrine principle it serves. Read every doc in the policy folder before working; they are short.
- Principles (doctrine) live in doctrine.md (in root: https://docs.google.com/document/d/1H5yRLJdy40p7tL6g6s6X3M1LrF0XmOiNU7hANvpjVM0/edit). Policy says what to do and can be checked; doctrine says why, and guides judgment where no rule applies.
- Before speaking to Mark, read communication policy.md (root, then policy: https://docs.google.com/document/d/1ibPYBiW5aidljH2-bFMGjMxpMV96itbAxrKLxCm-Etw/edit) and follow it in every reply.
- Decision records (what was chosen, when, and why) go in run summaries, not in policy or doctrine.

skills

When Mark says "slash" and a name, open the doc of that name in the skills folder (root, then skills: https://drive.google.com/drive/folders/1AB2BMf7vq5EpbAeBSFyqWeNuShwWNV42) and follow it. If no skill has that name, say so. Step-by-step procedures (starting a development session, loading the sandbox helper, ending a session, verifying a run) live in the skills, not here, so they are read only when needed.

verification

Every run is audited afterward by a separate verification thread: see verification protocol.md (in root: https://docs.google.com/document/d/1BN_8kc-NUDRBU1yGYG3ZA6-VZEILBoZA5DXsB_RgY_M/edit). If you were opened to verify a run, follow that doc and the verify skill instead of the development steps.

read in this order

1. next.md - the ordered list of open actions, each tagged (agent) or (operator). Do the (agent) items that apply to you and mention the (operator) items to Mark. When an item is done, remove it from next.md and add a line to history.md (root), the add-only log of completed items. It begins with a pointer to the previous run's summary: read that too.
2. the previous run's verification report (report.md in its verify folder), if it exists.
3. strategy.md - why.
4. architecture.md - how.
5. test findings.md - claims, each cited to a record in tested.

voice coding agent prototype.md is the planned production design.

folder layout

- Root (the "voice coding agent" folder): the live project docs, program Docs (titled with filenames, e.g. docs_io.py), handoff files, and doctrine.md. ONLY files directly in root, plus the policy and skills folders, are current. Copies elsewhere are history.
- policy: one doc per rule category.
- skills: one doc per voice command.
- tested: one record per test run (t01, t02, ...): date, what was run, raw output, observations, what was not tested.
- agent-runs: one folder per session, e.g. "run 01 - 2026-11-09 - short label". Each holds:
  - checkpoints: a copy of a doc taken just before each edit (version control rule vc-01).
  - end snapshot: a full copy of every current doc at session end.
  - thread: the spoken exchanges of the session.
  - summary.md and run-claims.md: what the run did and why, and every change with checks, for the verification thread.
  - verify NN - date: created by the verification thread; holds report.md.
