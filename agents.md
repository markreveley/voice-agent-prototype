# agents.md - onboarding for any agent working on this project

## what this is

A prototype of a strictly voice-driven coding agent. The operator (Mark) talks to an agent in the Claude chat app, mostly in voice mode, and types when a step needs git.

## where the project lives

- **The git repo is the source of truth:** github.com/markreveley/voice-agent-prototype, branch main. Every project file lives there, and every change is a commit (version control rule vc-04).
- **The Drive folder "voice coding agent" is a read-only mirror** of the repo, refreshed after every push by sync.md (skills folder). mirror.md in the Drive root says which commit it shows. Never edit the mirror: the next sync overwrites it.
- **Voice turns and text turns have different tools.** In a voice turn you can read Drive but you have no shell or git, so you can read the mirror and talk. In a text turn you have a shell and git: clone the repo and work from the clone. When the next step needs git, ask Mark to type (communication rule comm-11).
- **To start work, clone the repo:** follow bootstrap.md (skills folder) in a text turn. The sandbox starts empty in every new chat (test record t08), so do it every session.

## rules and principles

- Rules (policy) live in the policy folder, one file per category. Each rule has a fixed ID with a category prefix (e.g. comm-01) and names the doctrine principle it serves. Read every file in the policy folder before working; they are short.
- Principles (doctrine) live in doctrine.md (root). Policy says what to do and can be checked; doctrine says why, and guides judgment where no rule applies.
- Before speaking to Mark, read communication policy.md (policy folder) and follow it in every reply.
- Decision records (what was chosen, when, and why) go in run summaries, not in policy or doctrine.
- Refer to files by path from the root, never by Drive link: Drive IDs change on every sync.

## skills

When Mark says "slash" and a name, open the file of that name in the skills folder and follow it. If no skill has that name, say so. Step-by-step procedures (starting a development session, cloning the repo, syncing the mirror, ending a session, verifying a run) live in the skills, not here, so they are read only when needed.

## verification

Every run is audited afterward by a separate verification thread: see verification protocol.md (root). If you were opened to verify a run, follow that file and the verify skill instead of the development steps.

## read in this order

1. next.md - the ordered list of open actions, each tagged (agent) or (operator). Do the (agent) items that apply to you and mention the (operator) items to Mark. When an item is done, remove it from next.md and add a line to history.md (root), the add-only log of completed items. next.md begins with a pointer to the previous run's summary: read that too.
2. the previous run's verification report (report.md in its verify folder), if it exists.
3. strategy.md - why.
4. architecture.md - how.
5. test findings.md - claims, each cited to a record in tested.

voice coding agent prototype.md is the planned production design.

## folder layout

The repo root and the Drive root have the same layout (naming rule name-06):

- Root: the project docs, programs (e.g. docs_io.py), handoff files (next.md, history.md) and doctrine.md.
- policy: one file per rule category.
- skills: one file per voice command.
- tested: one record per test run (t01, t02, ...): date, what was run, raw output, observations, what was not tested.
- agent-runs: one folder per development run from run 04 on, e.g. "run 04 - 2026-11-10 - short label". Each holds summary.md, run-claims.md and thread.md (the spoken exchanges), and later a "verify NN - date" folder with report.md from the verification thread.

Drive also has two things the repo does not: mirror.md (which commit the mirror shows) and the archive folder, which holds the records of runs 01 to 03 from before git, including their checkpoints and end snapshots. The archive is history; nothing in it is current.
