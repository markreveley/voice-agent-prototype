# T07 - Fresh load of docs_io.py, and sandbox after reconnect

**Date:** November 9, 2026 **Run by:** Claude, in a Claude app voice chat with Mark

## What was run

1. After the voice call reconnected to the same chat, checked whether /tmp/repo/.git and /tmp/persist_test.txt still existed.
2. Downloaded docs_io.py fresh from Drive with exportMimeType text/plain.
3. Decoded it with a hand-written two-line bootstrap, imported it as a module, and called its functions.
4. Used it to write and run word_stats.py with input "fresh load fresh run".

## Raw output

- Both sandbox files existed after the reconnect: True, True.
- Module imported, exposing decode_export, prepare_upload, write_program, read_program, run_program.
- decode_export on its own export matched the bootstrap decode: True.
- run_program: exit code 0, "4 words; top: [('fresh', 2), ('load', 1), ('run', 1)]".
- Byte-identical to the original source: False (extra blank lines added by Docs).

## Observations

- docs_io.py loads and works straight from Drive.
- The first load needs a bootstrap snippet, now provided in AGENTS.md.
- The sandbox survives a voice reconnect within the same chat. A brand new chat is still not tested.
