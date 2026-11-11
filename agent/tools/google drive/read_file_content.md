# read\_file\_content

**Service:** Google Drive connector. **Status:** used often.

## What it does

Returns a readable text version of a file: Google Docs, Sheets and Slides, PDFs, Office files, images, plain text. It can include comments.

## How to call it

fileId; includeComments true when comments matter.

## Observations

- Best for reading and understanding a doc, or reading it aloud.  
- **Unsafe for code.** It returns Markdown, which adds backslashes before underscores, brackets and similar characters, and a blank line after every line. Never commit or run text from this tool. Use download\_file\_content with plain text instead. (voice coding agent: t02.)  
- 2026-11-11: Read the voice coding agent docs (agents.md, communication policy.md, sync.md and others) cleanly for discussion.
