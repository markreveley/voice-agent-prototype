# update\_doc

**Service:** Google Docs connector. **Status:** used often.

## What it does

Edits a Google Doc in place with a list of requests, applied in order. If any request is invalid, none are applied.

## How to call it

documentId and requests. Useful request types:

1. **replaceAllText:** find and replace text. It needs no indexes, so it's the simplest and safest edit.  
2. **insertText:** at location index (1 \= start of the doc) or endOfSegmentLocation (end of the doc).  
3. **deleteContentRange:** delete from startIndex to endIndex.  
4. **createParagraphBullets:** with bulletPreset BULLET\_CHECKBOX for to-do checkboxes.  
5. **deleteParagraphBullets:** removes bullets or checkboxes.  
6. **updateParagraphStyle:** namedStyleType HEADING\_2 etc. for headings.  
7. **updateTextStyle:** fields "link" with a URL to make text a link.

## Observations

- 2026-11-11: Built a to-do doc with checkboxes, headings and a link to a calendar event in one call.  
- 2026-11-11: Text inserted next to a list joins that list. When restructuring, delete the old range, insert the new text, remove bullets, then re-apply styles and bullets by range.  
- 2026-11-11: Appending a changelog line with endOfSegmentLocation picks up the last paragraph's style (e.g. its bullet). That's fine for list-style changelogs.  
- Use read\_doc first for any index-based edit, since earlier edits shift the indexes.  
- Works only on Google Docs, not on raw .md files.
