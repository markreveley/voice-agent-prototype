# Voice-First Dev Environment: Architecture

*How the pieces fit. Strategy, test findings, and code live in separate docs.*

## Layers

Each layer of the planned architecture in "Voice Coding Agent Prototype" has a stand-in today:

1. **Voice layer:** the Claude app's voice mode. Stands in for Pipecat or LiveKit with speech-to-text and text-to-speech.
2. **Harness and model:** Claude in the chat, running the tool loop and giving speakable summaries. Stands in for the custom harness plus the Anthropic API.
3. **Storage:** Google Docs in Drive, one Doc per program, titled with the filename. Version history provides rollback. Stands in for a GitHub repo.
4. **Runtime:** the Python sandbox. Scratch space only; Docs is the source of truth. Stands in for Docker or a hosted sandbox.

## Workflow

1. **Load:** download the program's Doc as plain text and clean it with docs_io.py.
2. **Run:** execute it in the sandbox.
3. **Edit:** copy the doc into the current run's checkpoints folder first, then change it.
4. **Save:** write it back to its Doc so it persists and enters version history.
5. **Report:** give a short spoken summary of what ran, what changed, and the result.

## Conventions

- Documents are written as Markdown; code is stored as plain text.
- Code is always loaded with the plain-text download, never the natural-language read tool.
- Save back to Docs after any meaningful change.
- All titles are lowercase, because text to speech spells out capitalized names letter by letter.
- History, checkpoints: before every edit to any doc, copy it into the current run's checkpoints folder in agent-runs. A local git repo in the sandbox is optional, for quick diffs within a session.
- History, end of run: at session end, copy every root doc into the run's end snapshot folder, and save the spoken exchanges in its thread folder.
- History, backup layer: Google Docs version history, viewed and restored by hand in the Docs app.

## Technical limitations

- The sandbox resets between chats, so each session starts by reloading code.
- GitHub appears unreachable from the sandbox.
- Each load and save costs several tool calls, adding delay in a voice conversation.
- Docs adds small formatting artifacts to code, so a cleanup step is required on load.
- Claude cannot list, read, or restore Google Docs revisions, which is why it keeps its own history layers.

## Next steps

- Done: created the "voice coding agent" Drive folder, which holds all project docs and program Docs.
- Done: tested revision access. Revisions cannot be listed or downloaded, so the history layers replace them.
