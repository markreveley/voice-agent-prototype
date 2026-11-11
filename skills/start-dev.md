# skill: /start-dev

**Trigger:** Mark says "slash start-dev" at the beginning of a new chat, or "read claude.md", or "read agents.md".

**What it does:** onboards a fresh development agent (development only; verification threads use slash verify) and gets it ready to work.

## Steps

1. Read agents.md. Read it in Drive, the working copy.  
2. No clone is needed for voice work. Clone only when a step needs git (pull.md steps 1 to 4, skills folder); that needs a text turn (communication rule comm-11).  
3. From Drive, read doctrine.md, verification protocol.md, every file in the policy folder, then next.md and the previous run's summary.md in Agents slash runs.  
4. Read the previous run's verification report (report.md in its verify folder). If none exists, tell Mark the run was not verified and ask whether to go ahead. Fix any failures first, and list each fix in your commit messages.  
5. Create your run folder in Agents slash runs: run NN \- date \- short label, with the next run number and Mark's local date.  
6. Tell Mark by voice, in one short list: verification failures to fix, the (agent) items in next.md, and any (operator) items waiting on him. Then ask what to start with.

## Notes

- Do steps 1 to 5 without asking permission between them; they are routine.  
- Run folders live in Agents slash runs, outside every repo, because a run can touch several projects.  
- Status: rewritten in run 04; not yet tested cold.
