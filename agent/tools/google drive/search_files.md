# search\_files

**Service:** Google Drive connector. **Status:** used often.

## What it does

Finds files and folders with a query, and returns IDs, titles, parents and, optionally, text snippets.

## How to call it

- query clauses: title contains 'x', fullText contains 'x', mimeType \= '...', parentId \= 'ID' (use 'root' for the top of My Drive), trashed \= false. Combine them with and, or, not.  
- **List a folder:** parentId \= 'FOLDER\_ID'.  
- **Find folders only:** mimeType \= 'application/vnd.google-apps.folder'.  
- **excludeContentSnippets true** keeps results small when only names and IDs are needed.  
- pageSize sets the number of results; nextPageToken gets more.

## Observations

- 2026-11-11: Name searches also return old snapshot and checkpoint copies from archive folders (e.g. "\[run 03 snapshot\] ..."). Check the parent folder before trusting a result.  
- 2026-11-11: Found the voice coding agent folder by title and folder type, and listed its contents by parentId.  
- Find folders by name or ID, never assume they're at the top of My Drive. Folders can move (project folders were reorganised on 2026-11-11).
