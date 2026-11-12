# skill: /verify

**Trigger:** Mark says "slash verify". The run to verify is the newest run folder in Agents slash runs (Drive, outside every repo; verification rule ver-04). If it already holds a verify folder with report.md, tell Mark there is nothing to verify. If it has no summary.md, the run has not ended: tell Mark and stop. If Mark names a run other than the newest, ask him which he means. If the newest run folder has a verify folder but no report.md, tell Mark an earlier verification was interrupted and ask whether to redo it.

**What it does:** an independent audit of one run, the newest. The rules are in verification policy.md (policy folder). This thread does no development work and fixes nothing and edits nothing, not even next.md (ver-07). Its result is report.md, in a verify folder in that run's folder (ver-08).

## Steps

1. From Drive, read agents.md, doctrine.md, next.md (for context only; it does not name the run to verify) and every file in the policy folder. From Agents slash runs, read the run's summary.md and, for a fixes run, the report.md it answers (in the verify folder of the run before it). Then make a full clone with pull.md steps 1 to 4 (skills folder); this needs a text turn (communication rule comm-11). Do not start a development run.  
2. List the run's commits: git log \--oneline \--grep "^run NN:". Check that its first commit has as its parent the base commit named in its summary.md. Below, BASE is that base commit and LAST is the run's last commit.  
3. For each change listed in the run's commit messages: show its commit (git show HASH), check that the diff matches what the message says, and turn the change into concrete, testable statements checked against the file as it stands at LAST (ver-06). For a fixes run, also check that every item in the fixes section of the report it answers was done. Wherever a claim rests on a decision by Mark, ask Mark to confirm it before marking it pass, because the run's own record of his decision is not independent evidence. Notes in commit messages about which docs were exported are not claims: skip them.  
4. Look for changes the claims missed: git diff \--stat BASE LAST shows every file the run changed; list any change that no claim covers. Also list any commit in that range whose prefix does not name the run. Check the run's summary.md for its changes outside the repo (ver-05).  
5. Check the run against its rules: lowercase names, .md suffixes, every change listed in a commit message, test findings citing test records, and the Drive working copy in step with the repo. For that, check that the list of doc paths in Drive matches git ls-files at LAST, and that every doc the run changed matches its file at LAST by content (export it as commit.md step 3 describes). Docs the run did not change are taken to match, as version control rule vc-10 assumes; say so in the report.  
6. Write report.md (ver-08). For each claim: pass, fail, or could not check, with the evidence. Then unclaimed changes, then rule breaks, then a section named fixes for run NN, listing what the next run, a fixes run, must do.  
7. Fix nothing and edit nothing, not even next.md (ver-07). Put any change next.md needs in the fixes section of report.md.  
8. Tell Mark the result by voice, following communication policy.md (policy folder): how many claims passed, and each failure in one sentence.

## Notes

- Runs 01 to 03 predate git; their summaries and reports are in Agents slash runs.  
- Status: used in verify 05 and verify 06; changed to one run per check in run 07. Not yet tested: whether a fresh agent can do this well from these instructions alone.
