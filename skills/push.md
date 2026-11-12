# skill: /push

**Trigger:** Mark says "slash push". The end skill also calls it. Written in run 05 (2026-11-11).

**What it does:** sends local commits to GitHub. Needs a text turn (communication rule comm-11).

## Steps

1. Check git status is clean. If not, run commit.md first, or ask Mark.  
2. Run git fetch, then compare: if GitHub has commits that the clone doesn't, stop and tell Mark. The repo changed somewhere other than Drive, which breaks version control rule vc-04. Never force-push.  
3. Run git push origin main.  
4. Check: git rev-parse HEAD equals git rev-parse origin/main.  
5. Tell Mark it's pushed, with the short hash and the commit's subject line.

## Notes

- No Drive step is needed after a push: the pushed commits came from Drive.  
- Pushing tags is refused, so commits are cited by hash (version control rule vc-09, test record t09).  
- Push before the chat ends: the sandbox resets between chats (vc-07).  
- Status: tested as a skill in run 05 (test record t10). Not yet tested: what happens when GitHub has newer commits (step 2).
