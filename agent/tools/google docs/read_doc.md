# read\_doc

**Service:** Google Docs connector. **Status:** used.

## What it does

Returns a Google Doc's full structure as JSON: every paragraph with its start and end positions (indexes), styles, list types, tabs and named styles.

## How to call it

documentId (the same as the Drive file ID). commentsIncluded true if comments are needed.

## Observations

- 2026-11-11: The output is very long, mostly style definitions. Use it only when you need exact indexes for an edit. To just read the text, use read\_file\_content (Drive) instead.  
- 2026-11-11: Needed before index-based edits (deleting a range, styling a heading, adding a link), because update\_doc works by position.  
- 2026-11-11: A doc created by create\_file from Markdown reported its title as "Untitled" here, even though Drive showed the right title.  
- Indexes count from 1\. The last paragraph's final newline can't be deleted.
