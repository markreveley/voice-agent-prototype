# agents.md \- onboarding for any agent working on this project

## what this is

A prototype of a strictly voice-driven coding agent. The operator (Mark) talks to an agent in the Claude chat app, mostly in voice mode, and types when a step needs git.

## where the project lives

- **The git repo is the record:** github.com/markreveley/voice-agent-prototype, branch main. Every project file lives there, and every change is a commit (version control rule vc-04).  
- **The Drive folder (Agents, then voice coding agent) is the working copy of the repo.** Edit there, by voice or text, then commit and push in a text turn. Drive is the only place edits happen (version control rule vc-04). The pull, commit and push skills (skills folder) move changes between Drive and the repo. The repo is public: keep personal data out (doctrine principle doc-07).  
- **Voice turns and text turns have different tools.** In a voice turn you can read and edit Drive but you have no shell or git. In a text turn you have a shell and git: clone the repo to run code, commit and push, but make edits in Drive, not in the clone. When the next step needs git, ask Mark to type (communication rule comm-11).  
- **To start work, read from Drive; no clone is needed for voice work.** When a step needs git, clone in a text turn with pull.md steps 1 to 4 (skills folder), which make a full clone. The sandbox starts empty in every new chat (test record t08).

## rules and principles

- Rules (policy) live in the policy folder, one file per category. Each rule has a fixed ID with a category prefix (e.g. comm-01) and names the doctrine principle it serves. Read every file in the policy folder before working; they are short.  
- Principles (doctrine) live in doctrine.md (root). Policy says what to do and can be checked; doctrine says why, and guides judgment where no rule applies.  
- Before speaking to Mark, read communication policy.md (policy folder) and follow it in every reply.  
- Decision records (what was chosen, when, and why) go in run summaries, not in policy or doctrine.  
- Refer to files by path from the root (this project's folder), never by Drive link: paths survive moves and match in Drive and the repo.

## skills

When Mark says "slash" and a name, open the file of that name in the skills folder and follow it. If no skill has that name, say so. Step-by-step procedures (starting a development session, cloning the repo, ending a session, verifying a run) live in the skills, not here, so they are read only when needed.

## verification

Every run is audited afterward by a separate verification thread: its rules are in verification policy.md (policy folder) and its steps in verify.md (skills folder). If you were opened to verify, follow the verify skill instead of the development steps.

## read in this order

1. next.md \- the ordered list of open actions, each tagged (agent) or (operator). Do the (agent) items that apply to you and mention the (operator) items to Mark. When an item is done, remove it from next.md and name it in the commit message, with its evidence (version control rule vc-05). Git history is the record of finished work. next.md begins with a pointer to the previous run's summary: read that too.  
2. the newest verification report (report.md in a verify folder, in Agents slash runs).  
3. strategy.md \- why.  
4. architecture.md \- how.  
5. test findings.md \- claims, each cited to a record in tested.

voice coding agent prototype.md is the planned production design.

## folder layout

The repo root and the Drive root have the same layout (naming rule name-06):

- Root: the project docs, programs (e.g. docs\_io.py), the handoff file (next.md) and doctrine.md.  
- policy: one file per rule category.  
- skills: one file per voice command.  
- agent: the assistant's environment (agents.md) and notes on each connected tool (tools folder). Check a tool's notes before using it, and add what you learn.  
- tested: one record per test run (t01, t02, ...): date, what was run, raw output, observations, what was not tested.  
- Run records are not in this project: they live in Agents slash runs, one folder per run, named with its type, fixes or dev (summary.md, and, once the run is verified, a "verify NN \- date" folder with report.md), because a run can touch several projects.

Runs 01 to 03 predate git.
