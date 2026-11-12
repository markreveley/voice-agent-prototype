# skill: /commit

**Trigger:** Mark says "slash commit", optionally followed by a message. The end skill also calls it. Written in run 05 (2026-11-11).

**What it does:** copies everything changed in the Drive working copy into the local clone and commits it as one commit (version control rule vc-05). It does not push: that is push.md. Needs a text turn (communication rule comm-11).

## Steps

1. If there is no clone in this chat, make one with pull.md steps 1 to 4\. Don't touch Drive.  
2. Find the Drive working copy by name: the folder Agents, then voice coding agent, and list every doc in it and its subfolders. Confirm parents (naming rule name-05).  
3. Export each changed doc exactly, never with read\_file\_content (it adds escapes; test record t02). Changed means Drive shows it modified later than ten minutes before the last commit (git log \-1 \--format=%cI), or it has no file in the clone; skip the rest (version control rule vc-10):  
   - **.md docs:** download\_file\_content with exportMimeType text/markdown.  
   - **Code (.py and others):** download\_file\_content with exportMimeType text/plain (file format rule fmt-04).  
   - Decode the base64, then clean it with decode\_export from docs\_io.py (root): it strips the byte order mark and turns Windows line endings into Unix ones (test record t04).  
4. Compare each export with the file at the same path in the clone, and build the change list:  
   - changed: doc and file differ, so overwrite the file;  
   - added: doc with no file, so write the file;  
   - deleted: file with no doc, so git rm it. Ignore differences that are only export noise (trailing blank lines, escaped characters that render the same). If unsure, show the diff to Mark in one sentence and ask.  
5. Tell Mark the change list as one short numbered list (comm-02), by file path, and ask him to confirm before committing.  
6. Commit everything as one commit. Message: "run NN:" (vc-06), then a one-line subject, then one line per change: the path and what changed and why (vc-05). Use Mark's message as the subject if he gave one. Don't describe the export (which docs were exported or skipped): list only what changed and why. If git asks for an author identity, ask Mark for his name and email.  
7. Tell Mark it's committed, with the short hash, and that it isn't on GitHub until he says slash push.

## Notes

- Markdown export from Google Docs may not match the original markdown byte for byte (list markers, escapes, blank lines). The first commit will show how noisy this is: record what you find as a test record.  
- Status: tested in run 05 (test record t10).
