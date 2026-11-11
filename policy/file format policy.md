# file format policy

*How docs and code are uploaded to and read from Drive. Moved from agents.md in run 03 (2026-11-10). Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**fmt-01 (no doctrine yet) Prose as markdown.** Upload prose docs as text/markdown.

**fmt-02 (no doctrine yet) Code and handoff files as plain text.** Upload code and handoff files as text/plain.

**fmt-03 (no doctrine yet) Read code only as plain text.** Read code ONLY with download_file_content and exportMimeType text/plain (returns base64), then decode it with docs_io.decode_export. Never use read_file_content for code: it returns escaped Markdown.

## Changing this policy

New rules go here with the next unused ID (fmt-04, ...). Copy this doc into your run's checkpoints folder before editing it.
