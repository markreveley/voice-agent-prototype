# skill: /sync

**Trigger:** Mark says "slash sync", or right after any push (version control rule vc-08), or another skill (end, verify) calls it. Added in run 04 (2026-11-10).

**What it does:** makes the Drive folder "voice coding agent" a read-only copy of the repo's main branch, so voice turns, which can reach Drive but not git, read the current state. Needs a text turn.

## Steps

1. In the clone, check that everything is pushed: git status is clean and git rev-parse HEAD equals git rev-parse origin/main.
2. Read mirror.md in the Drive root. Its first line names the commit the mirror shows. If mirror.md is missing, every file counts as changed.
3. List what changed since then: git diff --name-status MIRROR_COMMIT HEAD. A means added, M modified, D deleted, R renamed (treat a rename as a delete plus an add).
4. For each added or modified file: upload the repo file to the same path in Drive with create_file (naming rule name-06), as text/markdown for .md files and text/plain for code (file format rules fmt-01 and fmt-02). Upload from the file itself (a file reference such as sha256:HASH:/path, if the tool offers it) rather than retyping it. Create any missing folder first. Then, for a modified file, find the old Drive doc by title, confirm its parent (naming rule name-05) and trash it. Upload the new copy before trashing the old one, so the mirror never lacks a file.
5. For each deleted file: find its Drive doc, confirm the parent, and trash it.
6. Replace mirror.md: upload a new one, then trash the old. It says: the mirror shows commit HASH (short hash and subject line), synced at TIME UTC; it is read-only; and to change anything, edit the repo in a text turn.
7. Spot-check: read one changed doc back from Drive and compare its text with the repo file.

## Notes

- Drive IDs change on every sync, so docs refer to each other by path, never by Drive link.
- mirror.md lives only in Drive; it is not in the repo. The archive folder (root, then archive) is not part of the mirror and is never changed by a sync.
- Status: first run in run 04.
