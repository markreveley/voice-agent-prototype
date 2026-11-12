# communication policy

*How agents speak to Mark in voice mode. Moved from spoken reply rules.md in run 03 (2026-11-10). The principles behind these rules are in doctrine.md (root). Each rule names the doctrine principle it serves. IDs are fixed: never renumber or reuse one; retire an ID by marking it retired.*

## Rules

**comm-01 (serves doc-01) Summarize every pointer.** When you name a test record, doc, run, or other pointer to data, add a one-sentence summary of what it says. Example: root slash tested slash t08.md, which shows a new chat onboards from one sentence and starts with an empty sandbox.

**comm-02 (serves doc-01) No bullet points.** Every spoken list is numbered. Introduce it with "here's a list", read it as item one, item two, item three, and so on, and include every item.

**comm-03 (serves doc-01) More than three items means a list.** Any sentence that would name more than three things becomes a numbered list instead.

**comm-04 (serves doc-01) Folders by full path.** Say the path from root, with the word slash between parts, then the word folder. Example: root slash skills folder.

**comm-05 (serves doc-01) Files by full path, then their job.** Say the path from root, with the word slash between parts, then the file name with its suffix, then "which is" and what the file is for. Examples: root slash agents.md, which is the onboarding guide; root slash tested slash t08.md, which is the cold onboarding test. Always say the path and file name, every time the file comes up, never its job alone (not just "the onboarding guide" or "the history log").

**comm-06 (serves doc-01) Say quote and end quote around quotes.** When quoting words, say quote before them and end quote after them. Example: quote, keep replies short, end quote.

**comm-07 (serves doc-01) Keep spoken replies short.** Describe code instead of reading it aloud.

**comm-08 (retired) Lowercase titles.** Retired in run 03: moved to naming rules name-01 and name-02 (naming policy.md).

**comm-09 (serves doc-01) Name sections.** When you refer to part of a doc, say the word section, then its name, then which doc it is in. Example: section steps, in root slash skills slash verify.md.

**comm-10 (serves doc-01) Name rules by category and ID.** When you mention a rule, say its category, the word rule, its ID, then "which is" and its title. Example: communication rule comm-09, which is name sections. Doctrine works the same way: doctrine principle doc-02, which is keep reading cheap for agents.

**comm-11 (serves doc-01) Ask for text when git is needed.** Voice turns can read and edit the Drive working copy but cannot reach git or the shell. When the next step needs either (clone, run, commit, push or pull), say so in one sentence and ask Mark to type his next message.

**comm-12 (serves doc-01) Explain in plain words, step by step.** When you explain a problem or answer a question, answer the question first. Use plain words instead of jargon (say "only the newest commit", not "shallow clone"). Then go one step at a time: what is happening, why it is fine or not fine, and what you did about it. Do not pack several technical terms into one dense sentence. Added by Mark in verify 04 (2026-11-10); he may move it to its own file later.

*Reference for comm-12, from verify 04, when the verifier explained issue three by voice.*

First explanation, which Mark found hard to follow (verbatim): "Issue three is that root slash skills slash bootstrap.md, which is the clone skill, makes a shallow clone with only the latest commit. In that kind of clone, the verification thread can't see the run's earlier commits or compare them with the base commit."

Mark then asked: "Um, are you saying that the the previous dev thread made a shallow commit of the Git repo?"

Second explanation, which Mark found much clearer (verbatim): "No, the commits on GitHub are complete. The problem is the instructions. Run 04 rewrote the clone skill to say "clone with depth one," which downloads only the newest commit. That's fine for development work. But I follow that same skill, and a verifier needs the whole history to compare the run's commits with its starting point. So I ignored that step and made a full clone."

The verifier's analysis of the difference (verbatim): "The first time, I talked like a git manual: "shallow clone," "base commit," all packed into one dense sentence. The second time, I answered your question first, swapped the jargon for plain words like "only the newest commit," and went step by step: what the instruction says, why it's fine for development, why it breaks verification, and what I did about it."

**comm-13 (serves doc-01) One name per thing.** Call each file, folder and idea by its real name, the same way every time. Don't coin new labels for existing things (not "entry doc" or "rules doc" for an agents.md). If a new name is truly needed, say so and ask Mark first. Added by Mark, 2026-11-11.

**comm-14 (serves doc-01) Say what things are now.** When reporting a change, describe only the new state, not what it was before, unless Mark asks. Example: say quote, comm-11 says voice turns can edit the working copy, end quote; not quote, comm-11 used to say mirror and now says working copy, end quote. Added by Mark, 2026-11-11.

**comm-15 (serves doc-01) Report only what changes meaning.** When reporting work, mention only changes that affect what a doc says or what someone should do. Skip layout and housekeeping, such as where a rule sits in a doc, spacing, or renumbering. Added by Mark, 2026-11-11.

**comm-16 (serves doc-01) Conclusion first.** When a reply weighs something up, say the conclusion or recommendation first, then the analysis behind it. Example: say quote, yes, retire history.md; here's why, end quote; not the reasons first and the verdict at the end. Added by Mark, 2026-11-11.

## Changing this policy

New rules from Mark go here with the next unused ID (comm-17, ...). Edit this file in Drive and commit; git keeps the old version.
