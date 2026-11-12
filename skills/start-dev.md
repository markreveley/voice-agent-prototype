# skill: /start-dev

**Trigger:** Mark says "slash start-dev" at the beginning of a new chat, or "read claude.md", or "read agents.md".

**What it does:** onboards a fresh development agent (development only; verification threads use slash verify) and gets it ready to work.

## Steps

1. Read agents.md. Read it in Drive, the working copy.  
2. No clone is needed for voice work. Clone only when a step needs git (pull.md steps 1 to 4, skills folder); that needs a text turn (communication rule comm-11).  
3. From Drive, read doctrine.md, every file in the policy folder (verification policy.md says how runs are checked and typed), then next.md and the previous run's summary.md in Agents slash runs.  
4. Check that the newest run folder in Agents slash runs holds a verify folder with report.md. If it does not, stop and tell Mark that run must be verified first (verification rule ver-03). Otherwise read that report.md. If its fixes section lists fixes, this run is a fixes run (verification rule ver-02): make those fixes and nothing else, list each in your commit messages, and do no new development work; that waits for a dev run after this run is verified. If the report lists no fixes, this run is a dev run.  
5. Create your run folder in Agents slash runs: run NN \- date \- type \- short label, with the next run number, Mark's local date, and the type from step 4 (fixes or dev).  
6. Tell Mark by voice, in one short list: verification failures to fix, the (agent) items in next.md, and any (operator) items waiting on him. Then ask what to start with.

## Notes

- Do steps 1 to 5 without asking permission between them; they are routine.  
- Run folders live in Agents slash runs, outside every repo, because a run can touch several projects.  
- Status: rewritten in run 04; not yet tested cold.
