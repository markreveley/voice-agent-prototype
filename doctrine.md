# doctrine

*The principles behind this project's policies. Policy says what to do and can be checked. Doctrine says why, and guides judgment where no policy applies. Decision records (what was chosen, when, and why) belong in run summaries, not here. Started in run 03 (2026-11-10). IDs are fixed: never renumber or reuse one.*

## Principles

**doc-01 Mark listens; he does not read.** Mark works by voice and does not check docs visually. Every reply goes through text to speech, so structure must be audible, and trust in written work comes from independent verification, not from Mark reviewing it.

**doc-02 Keep reading cheap for agents.** Every file an agent opens is a separate tool call. Group related material so a fresh agent can onboard in a few reads, rather than splitting it into many tiny files.

**doc-03 Keep every change small enough to audit.** A change should touch as little as possible, so its commit diff stays small and a verifier can confirm it by content.

**doc-04 Give things IDs that never change.** Lists get reordered and Google Docs restarts list numbering, so anything other docs refer to gets a fixed ID that survives reordering.

**doc-05 Separate what from why.** Policy holds the checkable rules, doctrine holds the reasons, and run summaries hold the history. Each can then change without disturbing the others.

**doc-06 Prefer clean removal over leftovers.** When something moves or is retired, delete the old copy and fix the links, rather than leaving stubs. An agent that hits a dead link reports it to Mark.
