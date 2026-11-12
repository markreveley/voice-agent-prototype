# Voice-First Dev Environment: Architecture

*How the pieces fit. Strategy, test findings, and code live in separate docs. Rules live in the policy folder; this doc does not repeat them.*

## Layers

Each layer of the planned architecture in "Voice Coding Agent Prototype" has a stand-in today:

1. **Voice layer:** the Claude app's voice mode. Stands in for Pipecat or LiveKit with speech-to-text and text-to-speech.  
2. **Harness and model:** Claude in the chat, running the tool loop and giving speakable summaries. Stands in for the custom harness plus the Anthropic API.  
3. **Storage:** the git repo github.com/markreveley/voice-agent-prototype, the record. The Drive folder (Agents, then voice coding agent) is the working copy, where voice turns read and edit. This is the real stand-in for the planned GitHub repo, not an emulation.  
4. **Runtime:** the sandbox of a text turn, with a shell, git and Python. Scratch space only; the repo is the source of truth. Stands in for Docker or a hosted sandbox.

## Two kinds of turn

- **Voice turns** reach Drive but have no shell or git (observed, t09). They read and edit the Drive working copy, talk, and plan.  
- **Text turns** (Mark types) have the shell and git. They clone, run, commit and push.

## Workflow

1. **Edit:** change files in the Drive working copy, by voice.  
2. **Run:** in a text turn, clone the repo and run code, taking it from Drive by plain-text download (file format rule fmt-04).  
3. **Commit:** copy the changed Drive files into the clone and commit them.  
4. **Push:** push to main.  
5. **Pull:** if the repo changed elsewhere, refresh Drive from it. Steps 3 to 5 are the commit, push and pull skills (skills folder).  
6. **Report:** give a short spoken summary of what ran, what changed, and the result.

## Technical limitations

- The sandbox resets between chats, so each session starts by cloning the repo. (T08.)  
- Each switch between voice and text costs Mark a moment, and each commit or pull costs several tool calls.  
- Pushing git tags is refused, so commits are cited by hash. (T09.)  
- Google Docs can be edited in place with the Google Docs tools; plain files in Drive cannot, so changing one means uploading a new copy with a new ID. Files refer to each other by path. (Observed 2026-11-11; see the agent folder's tool notes.)  
- Claude cannot list, read, or restore Google Docs revisions (T05). This no longer matters: git holds the history.

## Next steps

- Done: created the "voice coding agent" Drive folder, now the working copy.  
- Done: moved the project into the git repo and dropped the Drive checkpoint system (run 04).
