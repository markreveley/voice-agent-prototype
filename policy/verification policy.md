# verification policy

*How each run's work is checked. Moved from verification protocol.md in run 06 (2026-11-11); the steps are in verify.md (skills folder). Each rule names the doctrine principle it serves (doctrine.md, root). IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**ver-01 (serves doc-01) Independent verification.** A separate agent, in a fresh chat, checks each run's work. The development agent never verifies its own run; checking its own work within a run does not count as verification. Set by Mark in run 02 (2026-11-09).

**ver-02 (serves doc-01) Every run has a type.** A run is a fixes run, which makes the fixes from the newest verification report (any other change it makes falls under ver-03), or a dev run, which does new work. The type is in the run folder's name: run NN \- date \- type \- short label.

**ver-03 (serves doc-03) Fixes come first, in their own run.** After a verification report, the next run is a fixes run, and new work starts in a new dev run. A fixes run that only made the report's fixes needs no verification before the next dev run. A fixes run that did anything the report did not ask for, such as new or changed rules, skills or doctrine, is verified before the next dev run starts, because later runs depend on those changes. Changed 2026-11-11 (run 06).

**ver-04 (serves doc-01) Verify every run since the last verification.** The runs to verify are every run folder in Agents slash runs numbered after the newest one that holds a verify folder with report.md. Mark never passes a run number, and next.md never mentions verification.

**ver-05 (serves doc-03) The claims are commit messages and summary.md.** Each commit lists every change in it by path, with why (version control rule vc-05). Each run's summary.md names its base commit and lists every change made outside the repo. Changes made after wrap-up go in a new commit, and summary.md is extended to cover them. There is no separate claims file.

**ver-06 (serves doc-03) Content, not metadata.** Claims are checked against the diff and the files as they stand. Sizes and timestamps are never evidence. A claim that can't be checked is marked could not check, never pass.

**ver-07 (serves doc-03) The verifier fixes nothing.** It reports only, so the record stays clean, and the next run, a fixes run, makes the fixes. One exception, set by Mark in run 03: the verifier may edit next.md, commits that edit with the prefix "verify NN:", and lists it in report.md.

**ver-08 (serves doc-02) One report, in the newest run's folder.** report.md goes in a "verify NN \- date" folder inside the newest verified run's folder in Agents slash runs (Drive only, not committed), where NN is that run's number. It names every run it covers, and the older runs it covers get no verify folder of their own.

## Changing this policy

New rules go here with the next unused ID (ver-09, ...). Edit this file in Drive and commit; git keeps the old version.
