# Voice Coding Agent Prototype

## Goal

A fully verbal, hands-free coding assistant on a phone. The user speaks, the agent answers out loud, and the agent can read and change GitHub repos and run code.

## Architecture Overview

The system has five layers: a phone client, a voice layer, a harness (the orchestrator at the center), the model, and tools (GitHub and code execution). Everything except the model runs on one modest cloud server.

## 1. Phone Client

Two entry points, both connecting to the same server agent.

**Option A: Phone number (Twilio)**

- Rent a Twilio number (about $1 to $2 per month).
- Twilio answers the call and streams the audio to the server.
- Pros: no app needed, works from any phone, good for driving.
- Cons: lower audio quality, slightly worse transcription, a bit more latency.

**Option B: Custom iOS app**

- Built in Swift / SwiftUI using the LiveKit iOS SDK.
- Streams audio over WebRTC (clearer audio, lower latency).
- Minimal UI: start/stop button, speaking indicator, scrolling transcript for glancing at code.
- Background audio mode enabled so it keeps running with the screen locked.

LiveKit supports both WebRTC clients and telephony (SIP), so one agent can serve both options.

## 2. Voice Layer

Runs on the server using a voice agent framework such as **Pipecat** or **LiveKit Agents**.

- **Speech-to-text:** Deepgram or Whisper (via API).
- **Text-to-speech:** ElevenLabs or Cartesia (via API).
- The framework handles the hard parts: detecting when the user has finished speaking and allowing interruptions mid-reply.

## 3. Harness (the Orchestrator)

- **Harness:** the user's server code. It manages conversation history, defines the tools Claude can use, runs tool calls, returns results to Claude, and passes final replies to the voice layer. It is the hub: the voice layer, the model, and the tools each connect to it, not to each other.
- **Tool loop:** user text goes to Claude with a tool list, Claude answers or requests a tool, the harness runs it and returns the result, and this repeats until Claude has a final answer.
- **Voice-friendly instructions:** the system prompt tells Claude to keep replies short and speakable and to describe code instead of reading it aloud.
- **Shortcut:** the **Claude Agent SDK** (Claude Code's engine) has built-in tools for shell commands, file editing, and git. It bundles a ready-made harness tightly with the model. Tradeoff: it is tied to Claude as the model.

## 4. Model

- **Model:** Claude, called through the Anthropic API. It runs on Anthropic's infrastructure and is stateless: it only sees what the harness sends on each call. If the harness is model-agnostic, the model can be swapped.

## 5. Tools

**GitHub access**

- *GitHub MCP server* (official): ready-made tools for reading files, searching code, issues, and pull requests. Authenticated with a GitHub personal access token.
- *Clone and git CLI:* the harness clones the repo into the sandbox and Claude runs git commands directly. This is more powerful for real coding work.
- Recommended: use both. Use git in the sandbox for code work and the MCP server for GitHub-website tasks.

**Code execution**

- Claude gets a "run command" tool. The harness runs the command and returns the output and errors.
- Must be isolated:
  - *Self-hosted:* a cloud server with work running inside Docker containers.
  - *Hosted sandbox:* E2B, Modal, or Daytona (a fresh disposable machine per session).

## End-to-End Flow

1. The user speaks into the iOS app or calls the Twilio number.
2. Audio streams to the server, where the voice agent transcribes it.
3. The transcript goes to the harness, which sends it to Claude through the API.
4. Claude uses tools as needed (reading the repo, editing files, running tests), and the harness runs them in the sandbox.
5. Claude produces a short, speakable summary.
6. Text-to-speech converts it to audio and streams it back to the phone.

## Open Decisions

- Phone number, iOS app, or both first?
- Pipecat vs. LiveKit Agents?
- Agent SDK (fast, Claude-only) vs. a custom harness (model-agnostic)?
- Self-hosted Docker vs. a hosted sandbox?
- Speech-to-text and text-to-speech providers.

## Next Steps

- Estimate running costs (API usage, voice services, hosting).
- Choose a starting slice, for example a Twilio number, Pipecat, the Agent SDK, and Docker on a single server.
- Build a minimal loop: call in, ask a question about a repo, hear an answer.
