# skill: /verify

**Trigger:** Mark says "slash verify", with no run number. The runs to verify are every run folder in Agents slash runs (Drive, outside every repo) numbered after the newest one that holds a verify folder with report.md (verification rule ver-04). If there are none, tell Mark there is nothing to verify. If the newest run folder has a verify folder but no report.md, tell Mark an earlier verification was interrupted and ask whether to redo it.

**What it does:** an independent audit of every run since the last verification, usually a fixes run and the dev run after it. The rules are in verification policy.md (policy folder). This thread does no development work and fixes nothing except next.md (ver-07). Its result is report.md, in a verify folder in the newest run's folder, naming every run it covers (ver-08).

## Steps

1. From Drive, read agents.md, next.md (for context only; it does not name the runs to verify) and every file in the policy folder. From Agents slash runs, read the summary.md of every run being verified. Then make a full clone with pull.md steps 1 to 4 (skills folder); this needs a text turn (communication rule comm-11). Do not start a development run.  
2. List each run's commits: git log \--oneline \--grep "^run NN:", once per run. Check that each run's first commit has as its parent the base commit named in that run's summary.md. Below, BASE is the oldest run's base commit and LAST is the newest run's last commit.  
3. For each change listed in the commit messages of the runs being verified: show its commit (git show HASH), check that the diff matches what the message says, and turn the change into concrete, testable statements checked against the file as it stands at LAST (ver-06). For a fixes run, also check that every item in the fixes section of the report it answers was done, or was decided by Mark.  
4. Look for changes the claims missed: git diff \--stat BASE LAST shows every file the runs changed; list any change that no claim covers. Also list any commit in that range whose prefix names none of the runs being verified. Check each run's summary.md for its changes outside the repo (ver-05).  
5. Check the runs against their rules: lowercase names, .md suffixes, every change listed in a commit message, test findings citing test records, and the Drive working copy in step with the repo (no Drive file differs from LAST).  
6. Write report.md (ver-08). For each claim: pass, fail, or could not check, with the evidence. Then unclaimed changes, then rule breaks, then a section named fixes for run NN, listing what the next run, a fixes run, must do.  
7. Fix nothing (ver-07). If you edited next.md, commit that edit with commit.md, using the prefix "verify NN:", and push with push.md (skills folder).  
8. Tell Mark the result by voice, following communication policy.md (policy folder): how many claims passed, and each failure in one sentence.

## Notes

- Runs 01 to 03 predate git; their summaries and reports are in Agents slash runs.  
- Status: used for one run in verify 05\. Not yet tested: covering several runs at once (added in run 06), and whether a fresh agent can do this well from these instructions alone.
