# download\_file\_content

**Service:** Google Drive connector. **Status:** used in earlier chats (voice coding agent tests), not in this one.

## What it does

Downloads a file's exact content. For a Google Doc, it exports it in a chosen format, e.g. plain text. Same as File, then Download, then Plain text in Google Docs.

## How to call it

fileId and exportMimeType text/plain for Google Docs. The result comes back base64-encoded; decode it in Python.

## Observations

- **Safe for code.** The plain-text export holds the doc's exact characters, with three harmless quirks: (voice coding agent: t02.)  
  1. a byte order mark (a hidden marker) at the start,  
  2. Windows-style line endings,  
  3. extra blank lines before function definitions.  
- None of these breaks Python. decode\_export in docs\_io.py (voice coding agent root) strips the first two, and the cleaned file ran. (voice coding agent: t04, t07.)  
- Downloading a past revision returns "not yet supported". (voice coding agent: t05.)  
- Use this, not read\_file\_content, for anything that will be committed or run.
