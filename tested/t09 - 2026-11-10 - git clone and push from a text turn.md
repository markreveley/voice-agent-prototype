# t09 - git clone and push from a text turn

**Date:** 2026-11-10 (run 04, Pacific). **Agent:** Claude, in a Claude app chat with Mark that mixed typed (text) turns and voice turns.

## What was run

1. Text turn: cloned the empty repo github.com/markreveley/voice-agent-prototype read-only, without attaching it (the session's git proxy serves public repos). Checked the remote with git ls-remote and GitHub's web page.
2. Text turn: called gh api on the repo before attaching it.
3. Text turn: attached the repo with write access (add_repo, access push), cloned it, committed push-test.md and ran git push -u origin main.
4. Cloned the repo again into a fresh folder and read push-test.md back.
5. Committed the Drive import, tagged it, and ran git push --follow-tags; then pushed the branch alone.
6. Voice turn: Mark asked whether the agent could reach the clone.

## Raw output

- Step 1: "warning: You appear to have cloned an empty repository."; ls-remote printed nothing; GitHub's page said "This repository is empty."
- Step 2: HTTP 403, "GitHub access to this repository is not enabled for this session."
- Step 3: no approval prompt appeared. Push output: "* [new branch] main -> main", plus a harmless warning ("push negotiation failed; proceeding anyway"). ls-remote: refs/heads/main at 13f9939.
- Step 4: git log showed "13f9939 Add push test file"; the file's text matched.
- Step 5: with the tag, "error: RPC failed; HTTP 403" and nothing was pushed. Branch alone: "13f9939..f5cf059 main -> main".
- Step 6 (observed): the voice-turn agent said it had no GitHub or code tools in the call, and that the clone lived in a workspace only text turns could reach.

## Observations

- In a text turn, git clone and push to GitHub work once the repo is attached with write access. This contradicts the t01 finding that GitHub appeared blocked, which was made from a voice chat's code sandbox.
- Pushing a tag is refused, so commits are cited by hash (version control rule vc-09).
- Voice turns in the same chat do not have git or the shell (observed, step 6 only).

## Not tested

- Whether add_repo asks for approval in other sessions.
- Whether a voice turn can still read the Drive mirror after a sync (to test after the first sync).
- Pushing to a branch other than main.
