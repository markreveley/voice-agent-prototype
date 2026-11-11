# T05 - Drive revision access

**Date:** November 9, 2026 **Run by:** Claude, in a Claude app voice chat with Mark

## What was run

1. Searched the available Drive tools for a revision listing tool.
2. Called get_file_metadata with rich metadata on "Voice Coding Agent Prototype".
3. Called download_file_content on the same doc with revisionId "1".

## Raw output

- No Drive tool lists revisions.
- Metadata returned title, times, owner, last modifying user, and an etag, but no revision IDs.
- download_file_content error: "Attempting to download a file at a given revision is not yet supported. Coming soon!"

## Observations

- Claude cannot list, read, or restore Google Docs revisions with current tools.
- This contradicted an earlier unverified claim, which was corrected in Test Findings.
- The error says "coming soon", so retest later.

## Side note

- The Google Docs read_doc tool returns the current revisionId, but only the current one.
