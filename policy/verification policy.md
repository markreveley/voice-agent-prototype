# verification policy

*How each run's work is checked. Moved from verification protocol.md in run 06 (2026-11-11); the steps are in verify.md (skills folder). Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**ver-01 (serves doc-01) Independent verification.** A separate agent, in a fresh chat, checks each run's work. The development agent never verifies its own run. It still checks its own work as it goes, but that does not count as verification. Set by Mark in run 02 (2026-11-09); the self-check restored in run 07 (2026-11-11).

**ver-02 (serves doc-01) Every run has a type.** There are two types of run. A fixes run makes the fixes listed in the newest verification report, and nothing else. Ideas for new work that come up during a fixes run go in next.md, for a later dev run. A dev run does new work. The type is in the run folder's name: run NN \- date \- type \- short label. Changed 2026-11-11 (run 08).

**ver-03 (serves doc-03) Every run is verified before the next one starts.** When a run ends, a verification thread checks it and writes a report, and the next run starts only after that. If the report lists fixes, the next run is a fixes run (ver-02), and new work waits for a dev run after it. If the report lists no fixes, the next run is a dev run. A fixes run is verified like any other run, so its fixes are checked before more work builds on them. Changed 2026-11-11 (run 07).

**ver-04 (serves doc-01) Verify the newest run.** The run to verify is the newest run folder in Agents slash runs: it has a summary.md, because the run has ended, and no verify folder yet. Every claim of that run is checked, fixes included (ver-05); no claim is skipped. Mark never passes a run number, and next.md never mentions verification. Changed 2026-11-11 (run 07).

**ver-05 (serves doc-03) The claims are commit messages and summary.md.** Each commit lists every change in it by path, with why (version control rule vc-05). Each run's summary.md names its base commit and lists every change made outside the repo. Changes made after wrap-up go in a new commit, and summary.md is extended to cover them. There is no separate claims file.

**ver-06 (serves doc-03) Content, not metadata.** Claims are checked against the diff and the files as they stand. Sizes and timestamps are never evidence. A claim that can't be checked is marked could not check, never pass.

**ver-07 (serves doc-03) The verifier fixes nothing.** It reports only, so the record stays clean, and the next run, a fixes run, makes the fixes. It does not edit next.md either: any change next.md needs goes in the fixes section of its report, and the fixes run makes it. Changed 2026-11-11 (run 07).

**ver-08 (serves doc-02) One report per run, in that run's folder.** report.md goes in a "verify NN \- date" folder inside the verified run's folder in Agents slash runs (Drive only, not committed), where NN is that run's number. Changed 2026-11-11 (run 07).

## Changing this policy

New rules go here with the next unused ID (ver-09, ...). Edit this file in Drive and commit; git keeps the old version.
