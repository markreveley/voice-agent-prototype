# T03 - Markdown to Google Docs conversion

**Date:** November 9, 2026 **Run by:** Claude, in a Claude app voice chat with Mark

## What was run

1. Uploaded a long Markdown document with create_file, contentMimeType text/markdown.
2. Read it back with read_file_content and checked the structure.

## Raw output

- Headings at levels 1 to 3, bullets, numbered lists, nested bullets, bold, and italics all appeared as expected.
- Empty spacer paragraphs appeared before some lists.

## Observations

- Markdown upload is a reliable way to create formatted docs.
- Spacer paragraphs are cosmetic. The original, human-made prototype doc has the same spacers, so they are not unique to Claude's uploads.

## Related checks

- Separately, replacing one bullet's text with several newline-separated lines produced several bullets at the same level, confirmed by a read on the Architecture doc.
