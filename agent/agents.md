# agents.md — agent environment

What the assistant's working environment is like: what it can reach, what changes between voice and text, and where to find notes on each tool. Read this when you need to know whether something is possible before trying it.

## Folder layout

- **agents.md** (this doc): an overview of the environment.  
- **tools** folder: one folder per connected service (google drive, google docs, google calendar). Inside each, one doc per tool, named after the tool (e.g. search\_files.md), with what it does, how to call it, and observations.

## The environment in brief

1. **Chat app, voice or text.** Mark talks to the assistant in the Claude app, mostly by voice.  
2. **Voice turns and text turns have different tools.** In voice turns, the connectors (Drive, Docs, Calendar) work, but there's no git or shell. In text turns, the code sandbox has git and can push to GitHub. (voice coding agent: test record t09.)  
3. **Connector tools are loaded on demand.** Most connector tools must be loaded with tool search before the first call in a session. The set of tools offered can change when a voice call reconnects.  
4. **The sandbox starts empty in every new chat.** Files persist within a chat, and survive a voice reconnect, but not across chats. (voice coding agent: t01, t07, t08.)  
5. **There are two calendar paths.** The Google Calendar connector (used for Mark's calendar so far) and the device calendar tools, which write to the phone's Calendar app. Use the Google Calendar connector unless Mark says otherwise.

## Rules for the tools folder

- One doc per tool, named after the tool, with a .md suffix. Docs are Google Docs so they can be edited in place.  
- Record observations as they happen: date, what was tried, what happened. Cite a test record when there is one.  
- Mark a tool "not used yet" until it has been tried; don't guess at behavior.
