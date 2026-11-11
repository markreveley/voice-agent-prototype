# update\_file

**Service:** Google Drive connector. **Status:** used.

## What it does

Changes a file's details, not its content: rename, move to another folder, star, lock, change folder colour, set a description.

## How to call it

- **Rename:** fileId and title.  
- **Move:** fileId and parentId (the new folder). This replaces the old parent.

## Observations

- 2026-11-11: Renamed two Google Docs to agents.md. It worked, and they stayed Google Docs.  
- 2026-11-11: Moved folders into another folder. IDs and links stayed the same, and the contents came along.  
- It can't edit content. For Google Docs, use update\_doc. For raw files, upload a new copy with create\_file.
