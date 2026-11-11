# create\_file

**Service:** Google Drive connector. **Status:** used often.

## What it does

Creates a folder, a blank Google Doc/Sheet/Slides, or uploads content as a new file. It can't change an existing file's content.

## How to call it

- **Folder:** contentMimeType application/vnd.google-apps.folder, title, parentId.  
- **Blank Google Doc:** contentMimeType application/vnd.google-apps.document, no content.  
- **Doc from Markdown:** textContent plus contentMimeType text/markdown. Drive converts it to a Google Doc with headings, lists, bold and tables.  
- **Keep as a raw file:** add disableConversionToGoogleType true. The file stays a .md (or .txt) file.  
- **parentId** places it in a folder; without it, the file goes to the top of My Drive.

## Observations

- 2026-11-11: A raw .md file (conversion disabled) can't be edited in place by any tool. Changing it means uploading a new copy and trashing the old, which changes its ID and link. Converted Google Docs can be edited in place with update\_doc. Prefer converted Docs.  
- 2026-11-11: Markdown converts cleanly: headings, numbered and bulleted lists, bold, italics and tables. Occasional empty spacer paragraphs before lists are cosmetic. (voice coding agent: t03.)  
- 2026-11-11: The doc title comes from the title field, but read\_doc right after creation reported "Untitled". The Drive title was correct.  
- Plain-text uploads (text/plain) also convert to Google Docs unless conversion is disabled. (voice coding agent: t02.)
