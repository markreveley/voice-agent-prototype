# next

*Updated 2026-11-10 by run 04 at slash end. Open work only, in order. Each item is tagged (agent) or (operator); (operator) means Mark must act before work can go on. When an item is done, remove it here and add a line to history.md (root). Verification is never listed: the verify thread finds its own run. Every agent follows the files in the policy folder in every reply.*

Previous run: run 04 - 2026-11-10 - git as the source of truth. Summary: root slash agent-runs slash run 04 - 2026-11-10 - git as the source of truth slash summary.md. Runs 01 to 03 predate git; their records are in the Drive archive folder only.

1. **(agent)** Fix what verify 04 found (root slash agent-runs slash run 04 - 2026-11-10 - git as the source of truth slash verify 04 - 2026-11-10 slash report.md, section fixes for run 05): (a) bootstrap.md's --depth 1 clone has no history, so a verification thread cannot run git log or git diff against the base commit; make verification use a full clone; (b) history.md shows as one run-on paragraph in the Drive mirror, because markdown joins its lines; give each entry its own paragraph or list item, sync, and read it back; (c) record the corrected counts for claims c07 (7 history lines, not 8) and c09 (18 old copies, not 19) in your run-claims.md; (d) ask Mark to confirm the doc-03 rewording and the unclaimed rule edits to name-01, name-05 and fmt-02.
2. **(operator)** Decide what real, multi-file program to build as the stress test.
3. **(agent)** Build that program in the repo, to stress the clone, run, commit, push and sync workflow and the switching between voice and text turns.
4. **(agent)** Test the new onboarding cold: in a fresh chat, one spoken sentence leads to agents.md in the Drive mirror, then a typed message runs start-dev and bootstrap. Write it up as a test record.
5. **(agent)** Propose doctrine for the rules marked "no doctrine yet" (naming rule name-05 and file format rules fmt-01, fmt-02 and fmt-04), and ask Mark to approve.
6. **(agent)** Propose whether verification protocol.md should be split into a verification policy file (policy folder) and the verify skill, and ask Mark.
