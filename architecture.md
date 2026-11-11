# Voice-First Dev Environment: Architecture

*How the pieces fit. Strategy, test findings, and code live in separate docs. Rules live in the policy folder; this doc does not repeat them.*

## Layers

Each layer of the planned architecture in "Voice Coding Agent Prototype" has a stand-in today:

1. **Voice layer:** the Claude app's voice mode. Stands in for Pipecat or LiveKit with speech-to-text and text-to-speech.
2. **Harness and model:** Claude in the chat, running the tool loop and giving speakable summaries. Stands in for the custom harness plus the Anthropic API.
3. **Storage:** the git repo github.com/markreveley/voice-agent-prototype, the only source of truth. A read-only mirror in the Drive folder "voice coding agent" lets voice turns read it. This is the real stand-in for the planned GitHub repo, not an emulation.
4. **Runtime:** the sandbox of a text turn, with a shell, git and Python. Scratch space only; the repo is the source of truth. Stands in for Docker or a hosted sandbox.

## Two kinds of turn

- **Voice turns** reach Drive but have no shell or git (observed, t09). They read the mirror, talk, and plan.
- **Text turns** (Mark types) have the shell and git. They clone, run, edit, commit, push and sync.

## Workflow

1. **Load:** in a text turn, clone the repo (bootstrap.md, skills folder).
2. **Run:** execute code from the clone.
3. **Edit:** change files in the clone.
4. **Commit and push:** one change per commit, then push to main.
5. **Sync:** refresh the Drive mirror (sync.md, skills folder).
6. **Report:** give a short spoken summary of what ran, what changed, and the result.

## Technical limitations

- The sandbox resets between chats, so each session starts by cloning the repo. (T08.)
- Each switch between voice and text costs Mark a moment, and each sync costs several tool calls.
- Pushing git tags is refused, so commits are cited by hash. (T09.)
- The Drive tools cannot replace a doc's content in place, so a sync uploads a new copy and trashes the old one, and Drive IDs change on every sync. Files refer to each other by path. (Observed, run 04.)
- Claude cannot list, read, or restore Google Docs revisions (T05). This no longer matters: git holds the history.

## Next steps

- Done: created the "voice coding agent" Drive folder, now the mirror.
- Done: moved the project into the git repo and dropped the Drive checkpoint system (run 04).
