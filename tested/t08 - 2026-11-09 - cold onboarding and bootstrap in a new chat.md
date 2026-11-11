# t08 - cold onboarding and bootstrap in a new chat

**Date:** 2026-11-09 (run 02). **Agent:** Claude, Claude app voice chat with Mark.

## What was run

1. Mark opened a new chat and said: "read claude.md in google docs". No other context was given.
2. The agent searched Drive for "claude", found claude.md in root, read it, and followed the pointer to agents.md (it confirmed the parent was the root folder).
3. It read next-agent, next-operator, and the run 01 summary.
4. It checked the run 01 folder for its summary, end snapshot (10 docs) and thread doc. All three exist.
5. It created run 02 in agent-runs, with its checkpoints, end snapshot and thread subfolders.
6. Before writing any sandbox files, it checked for leftovers from the previous chat.
7. It downloaded docs_io.py with exportMimeType text/plain and ran the bootstrap from agents.md, then ran a smoke test.

## Raw output

```
pre-existing: {'/tmp/docs_io.py': False, '/tmp/programs': False, '/tmp/repo': False}
functions: ['decode_export', 'prepare_upload', 'read_program', 'run_program', 'write_program']
(0, 'hello from run 02\n', '')
roundtrip ok: True
3.12.3
```

The smoke test: write_program("hello.py", ...) then run_program on it. "roundtrip ok" compares decode_export(b64) with prepare_upload(src).

## Observations

- **Cold onboarding works.** One spoken sentence was enough for a fresh agent to find and follow the handoff files.
- **No sandbox files survived from the previous chat.** The sandbox starts empty in a new chat, so the bootstrap must run every session.
- **The bootstrap code in agents.md works as written.** The download included a byte order mark and Windows line endings, and the bootstrap handled both.
- **Two small frictions (observed):** the agent asked Mark before each step instead of running the whole read order, and the run 01 summary listed the snapshot and thread as open because it was written before they existed.
- **The run numbering question** (does the earlier onboarding chat count as run 02?) was settled by Mark: no, this chat is run 02.

## Not tested

- Whether the run 01 thread doc is complete (only its existence was checked).
- Loading any program other than docs_io.py and a one-line test.
- Saving a program back to a Doc from this chat.
- Whether a git repo at /tmp/repo would survive within this chat.
