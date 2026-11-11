# trash\_file

**Service:** Google Drive connector. **Status:** used.

## What it does

Moves a file or folder to the Drive trash. It doesn't delete it for good.

## How to call it

fileId only. It returns an empty response when it works.

## Observations

- 2026-11-11: Used to retire old copies of agents.md after uploading replacements.  
- Trashed files can be restored from the Drive trash, which keeps them for 30 days (Drive's standard behaviour, not tested here).  
- There's no tool to restore from the trash. Mark has to do that in the Drive app.
