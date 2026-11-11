# T02 - Code round trip and read methods

**Date:** November 9, 2026 **Run by:** Claude, in a Claude app voice chat with Mark

## What was run

1. Wrote word_stats.py (counts words, lists the three most common) and ran it in the sandbox.
2. Uploaded it to Drive with create_file, contentMimeType text/plain. Drive converted it to a Google Doc.
3. Read it back with read_file_content (natural-language read).
4. Read it back with download_file_content, exportMimeType text/plain, and decoded the base64.
5. Compared the decoded text to the original and ran the downloaded copy with a new input.

## Raw output

- Original run: "12 words; top: [('the', 4), ('doc', 2), ('voice', 1)]"
- read_file_content: Markdown, with backslashes before underscores, brackets, exclamation marks, and greater-than signs, and a blank line after every line of code.
- download_file_content: base64 text starting with a UTF-8 byte order mark, using CRLF line endings, with extra blank lines before def and if blocks.
- Identical to original after stripping: False
- Downloaded copy run with "Docs as storage, sandbox as runtime, docs win": "8 words; top: [('docs', 2), ('as', 2), ('storage', 1)]", exit code 0.

## Observations

- The natural-language read is not safe for code.
- The plain-text download is safe; its differences from the original do not affect Python.
