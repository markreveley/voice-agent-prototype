# Voice-First Dev Environment: Strategy

*Why we're doing this. Architecture, test findings, and code live in separate docs.*

## Goal

Prototype a strictly voice-engaged coding agent: the user speaks, the agent answers aloud, and the agent can store, run, and change code, with no screen required.

## Why the Claude chat app

Claude Code has native GitHub and sandbox access, but only the Claude chat app offers two-way voice: speech in and speech back out. With Claude Code, the user could speak in but would have to read replies. Since the goal is strictly voice, the chat app is currently the best platform for prototyping the experience.

## The tradeoff we accept

We give up native GitHub access and a persistent dev machine in exchange for real two-way voice today.

## The core idea

Build nothing yet. Use what the chat app already provides as stand-ins for each layer of the planned architecture, and learn from using it.

## What we want to learn

The hardest questions in a voice coding agent are about the experience, not the infrastructure:

- How to describe code aloud instead of reading it.
- How to review and approve a change you cannot see.
- What the agent should say after running code or making an edit.
- How to navigate and refer to code by voice.

What we learn carries directly into the real build described in "Voice Coding Agent Prototype."

## Possibilities

- A working voice-driven dev environment today, with no infrastructure built.
- UX research for the real product before investing in the full stack.
- Prototyping harness components in Python, such as a tool loop, a code-to-speech summarizer, or a diff explainer.
- A persistent code library in Drive that Claude loads at the start of each chat.

## Next steps

- Try a real, multi-file program to stress the approach.
- Keep notes on what works in voice UX and feed them back into the main prototype doc.
