# threads.md

Status of every Claude chat thread in the voice coding agent's run and verify sequence. Runs and verifies alternate: each run is checked by a verify thread before the next run builds on it. Kept by the orchestrator; linked from the Orchestrator Hub in the Agents folder. Each thread name links to its verbatim transcript in Agents/Threads/voice coding agent where one exists (so far run 01), and otherwise to the chat in the Claude app.

Last updated: 2026-11-13.

## Current state

- **Newest thread:** run 09 (2026-11-13), a dev run started out of order. It supersedes verify 08 as the latest step.  
- **Recommended next:** verify 09, to check run 09\. Then a dev run (run 10), starting with the next.md item marked do this first. That run should also correct a date error: decisions made after run 08 are dated 2026-11-13 but were made on 2026-11-12, in next.md items 6 and 7 and in run 08's summary.md.  
- **Possibly pending:** verify 08 reported that Google Drive disconnected before it could save its report. It asked Mark to send any message so it could create Agents/runs/run 08/verify 08 \- 2026-11-12/report.md. Check whether that report exists.

## Sequence

* [run 01 \- architecture, testing, and handoff protocol](https://docs.google.com/document/d/1Plxj0zoNFnY0kIoErhiclULCV_g-fJVlTzkeve1dZu8/edit) (2026-11-09, dev, done): Wrote the voice-first dev environment strategy and architecture docs; created the handoff files (CLAUDE.md, AGENTS.md, NEXT-AGENT.txt, NEXT-OPERATOR.txt).  
* verify 01 (likely never existed): The verification protocol was created in run 02, so run 01 was not verified separately.  
* [run 02 \- cold start, spoken rules, verification and skills](https://claude.ai/chat/de0325cb-5d68-41f5-b539-4cbbfe9c2f03) (2026-11-09, dev, done): Cold start from claude.md; spoken reply rules; the verification protocol and skills; run-claims.md; next.md replaced the two handoff docs.  
* [verify 02 \- 2026-11-09](https://claude.ai/chat/008c4647-2f27-4bfd-b75f-51aa954861a7) (2026-11-09, verify, done): 15 of 18 checkable claims passed, one failed. Protocol now compares content, not metadata; fixed claim IDs; fixes (a) to (h) and a history.md item for run 03\.  
* [run 03 \- 2026-11-10 \- verification fixes, policy, doctrine and history folder](https://claude.ai/chat/b9b0a7ae-e6bc-4fe9-9e31-81b65ff0da6e) (2026-11-10, dev, done): Made the verify 02 fixes; added policy, doctrine and history.md; 22 claims (c01 to c22) and an end snapshot of 21 docs.  
* [verify 03 \- 2026-11-10](https://claude.ai/chat/50f5b5fe-602c-47a6-bc37-66d10ace190f) (2026-11-10, verify, done): Verified run 03\. Found the new GitHub repo empty and push access blocked; the move to GitHub was left to the next dev run.  
* [run 04 \- 2026-11-10 \- git as the source of truth](https://claude.ai/chat/6f2d76cb-7bc4-42cc-b775-1073e4b3120c) (2026-11-10, dev, done): Moved the project into github.com/markreveley/voice-agent-prototype and made Drive a read-only mirror; verification now compares git commits. Final commit 1674906\.  
* [verify 04 \- 2026-11-10](https://claude.ai/chat/4699ab7f-bafb-439d-94f1-e09fde7ed43d) (2026-11-10, verify, done): First audit using git. Added communication rule comm-12 at Mark's request; pushed 308c43a.  
* [run 05 \- 2026-11-11 \- drive working copy and git skills](https://claude.ai/chat/f08ceaad-9d39-4471-ad97-d268f71c8bf5) (2026-11-11, dev, done): Made Drive the working copy with git skills; root agents.md became a routing doc; the agent folder moved into voice coding agent; cleaned out six misplaced items; closed the verify 04 item (24ed810).  
* [verify 05 \- 2026-11-11](https://claude.ai/chat/16c3759b-a48c-42b8-ba75-282f06b3a812) (2026-11-11, verify, done): Report lists eight fixes for run 06, two needing Mark's answer (fix 3 and fix 8).  
* [run 06 \- 2026-11-11 \- fixes \- verify 05 findings](https://claude.ai/chat/9ed6a88a-cad3-4e0e-a91c-4e873233fb12) (2026-11-11, fixes, done): Made the eight verify 05 fixes (0a77688); added rule vc-10 and run types; split the verification protocol into policy/verification policy.md and skills/verify.md; ver rule changes in b3e01c2 and 3558f8e.  
* [verify 06 \- 2026-11-11](https://claude.ai/chat/eb9b2316-a2f5-4339-bed4-e362affdc2ff) (2026-11-11, verify, done): First use of the rewritten verify skill. Report's fixes for run 07 include checking every run before the next one starts.  
* [run 07 \- 2026-11-11 \- fixes \- verify 06 findings](https://claude.ai/chat/39b2274a-edd6-4d9f-bde4-6b73a27b59ba) (2026-11-11, fixes, done): Made all eight verify 06 fixes; added the plain-words "how work is done" section to agents.md and the three-part report format; one run at a time. Commits e2401f7, 2d675f2, 038cce0.  
* [verify 07 \- 2026-11-11](https://claude.ai/chat/400e67b3-a455-4eb8-94bb-adb92e371243) (2026-11-11, verify, done): First check under one run at a time. Report lists fixes for run 08 plus ten notes on the verify skill.  
* [run 08 \- 2026-11-11 \- fixes \- verify 07 findings](https://claude.ai/chat/2c1e63bb-256a-4fcc-b4d3-3c6ecedab61d) (2026-11-11, fixes, done): Made the verify 07 fixes, keeping fixes runs strict; three later commits added items 6 and 7 to next.md.  
* [Voice coding agent verify run 08](https://claude.ai/chat/c34a4c5b-a55c-41ed-ac1d-2e59936eb812) (2026-11-13, verify, report save pending): 41 claims checked: 36 pass, 2 fail (the same wrong date), 3 could not be checked. No fixes; recommends a dev run next.  
* run 09 \- 2026-11-13 \- orchestrator, threads index and transcripts (2026-11-13, dev, wrapping up): Started out of order from an orchestrator chat, superseding verify 08 as the latest step. Built this threads.md and the Orchestrator Hub; created Agents/Threads with run 01's verbatim transcript as the sample; added the edit-in-place and no-tables decisions to next.md.

## Notes

- Thread names follow the pattern "run NN \- date \- kind \- topic" and "verify NN \- date". Verify 08's thread is titled differently and could be renamed to "verify 08 \- 2026-11-12".  
- New threads show up most reliably in the recent chats list; search by title works once the index catches up.
