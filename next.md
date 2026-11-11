# next

*Updated 2026-11-10 by run 03. Open work only, in order. Each item is tagged (agent) or (operator); (operator) means Mark must act before work can go on. When an item is done, remove it here and add a line to history.md (root). Verification is never listed: the verify thread finds its own run. Every agent follows the docs in the policy folder (root, then policy) in every reply.*

Previous run: run 03 - 2026-11-10 - verification fixes, policy, doctrine and history (agent-runs). Summary: <https://docs.google.com/document/d/1VxGFV2twDePD6DIt_hGQHFdRhNASIg9p_ZeS9CGUjsk/edit>

1. **(agent)** Development thread: read the previous run's summary and its verification report (report.md in its verify folder). Fix any failures first, and record each fix in your own run-claims.md. Verify 03 (report.md: https://docs.google.com/document/d/132Lw7YWC9ZmYEAEcdRszC9roYBsw3G-OnHx13WEem5A/edit) left these for run 04: (a) check the run 03 chat for whether verify.md and verification protocol.md were edited twice with only one checkpoint, and record the answer; (b) fix the stale references in test findings.md (section round trip test says the bootstrap is in agents.md; it is in bootstrap.md) and architecture.md (section conventions says copy every root doc; end.md says root, skills and policy), checkpoints first; (c) optional: log in history.md the three next.md items run 03 dropped (the project-instructions line and the two slash end reminders), and decide whether this item belongs in next.md. Verify 03 already fixed the summary link above.
2. **(operator)** Decide what real, multi-file program to build as the stress test.
3. **(agent)** Build that program to stress the load, run and save workflow.
4. **(agent)** Retest revision download (t05 found it not yet supported).
5. **(agent)** Propose doctrine for the rules marked "no doctrine yet" (naming rule name-05 and file format rules fmt-01 to fmt-03), and ask Mark to approve.
6. **(agent)** Propose whether verification protocol.md should be split into a verification policy doc (policy folder) and the verify skill, and ask Mark.
