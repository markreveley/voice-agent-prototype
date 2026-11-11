# skill: /bootstrap

**Trigger:** Mark says "slash bootstrap", or another skill (start-dev, verify) calls it, or the clone is missing mid-session. Rewritten in run 04 (2026-11-10): it used to load docs_io.py from Drive; it now clones the git repo.

**What it does:** puts a working, pushable clone of the repo in the sandbox. Do this before any other work.

## Steps

1. Check that you are in a text turn: you need a shell and git. In a voice turn, ask Mark to type his next message (communication rule comm-11).
2. Attach the repo with write access: call add_repo with owner markreveley, repo voice-agent-prototype and access push. If no such tool exists, a read-only clone still works (step 3) but you cannot push: tell Mark.
3. Clone it to the path the tool gives (usually /home/claude/voice-agent-prototype): git clone --depth 1 https://github.com/markreveley/voice-agent-prototype PATH. Allow up to ten minutes.
4. Check the clone: git log --oneline -3 shows recent commits, and git status is clean.
5. Write down the base commit (git rev-parse --short HEAD). A development run records it in summary.md; a verification thread compares against it.
6. Read the rest of the project from the clone, not from Drive: the clone is the current state, and the mirror may lag.

## Notes

- Push a branch with git push origin main. Pushing tags is refused (test record t09).
- Install packages with pip install --break-system-packages NAME (test record t06).
- docs_io.py is no longer needed to load code; it stays in the repo as a test program.
- Status: steps 2 to 4 tested in run 04 (t09).
