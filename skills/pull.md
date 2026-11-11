# skill: /pull

**Trigger:** Mark says "slash pull", or another skill needs a clone (steps 1 to 4 only). Written in run 05 (2026-11-11).

**What it does:** gets the latest repo from GitHub into the sandbox, and, if the repo changed somewhere other than Drive, brings the Drive working copy up to date. Needs a text turn (communication rule comm-11).

Normally the Drive working copy already matches GitHub, because every change goes Drive, then commit, then push (version control rule vc-04). So most of the time this skill only clones (steps 1 to 4), and steps 5 to 8 find nothing to do.

## Steps

### Clone (steps 1 to 4: also used by commit, verify and start-dev)

1. Check you are in a text turn. In a voice turn, ask Mark to type (comm-11).  
2. Attach the repo with write access: call add\_repo with owner markreveley, repo voice-agent-prototype and access push. If no such tool exists, a read-only clone still works, but you cannot push: tell Mark.  
3. Make a full clone (never depth one, so verification can see history): git clone [https\://github.com/markreveley/voice-agent-prototype](https://github.com/markreveley/voice-agent-prototype) PATH, using the path the tool gives (usually /home/claude/voice-agent-prototype). Allow up to ten minutes. If a clone already exists in this chat, run git pull instead.  
4. Check it: git log \--oneline \-3 shows recent commits and git status is clean. Note the latest commit (git rev-parse \--short HEAD): it is the base for this session.

### Bring Drive up to date (steps 5 to 8: only when Mark says slash pull)

5. Find the Drive working copy by name: the folder Agents, then voice coding agent. Confirm each parent (naming rule name-05); never assume IDs.  
6. **Safety check.** Compare every Drive doc with the matching file in the clone, exporting each doc the way commit.md step 3 describes. Any difference is an uncommitted voice edit. If there are any, stop, tell Mark which files, and ask: commit them first (commit.md), or discard them.  
7. For each repo file that differs from Drive or is missing there: upload it to the same path in Drive with create\_file (text/markdown for .md files, text/plain for code; file format rules fmt-01 and fmt-02), creating any missing folder first. Then trash the old Drive doc, after the new one exists. For each Drive doc with no repo file, trash it. Leave Drive-only items alone (agents.md and runs in the Agents folder, and Life, are outside this repo).  
8. Spot-check: read one changed doc back and compare it with the repo file.

## Notes

- Uploading a new copy gives the doc a new Drive ID, so docs refer to each other by path, never by link.  
- Status: steps 1 to 4 tested in run 04 (test record t09, then as bootstrap.md). Steps 5 to 8 not yet tested.
