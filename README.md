# Mini RAG Bot Simulator – Mesh Network Onboarding Assistant

This is a foundational prototype of a user-facing Retrieval-Augmented Generation (RAG) bot. Built entirely using open-source tools, this bot is designed to assist users in understanding decentralized digital MESH networks — especially those headquartered in New York, but serving the broader United States.
> The goal is to simplify organizational intuition, lower onboarding barriers, and propagate mesh network utility democratizing commons.

---

## What It Does (Currently)
This version simulates a RAG system:
- Loads context from a static file (`context.txt`)
- Accepts a user question via terminal input
- Returns a "generated" answer by formatting your question with the context

No AI models, no internet required — lightweight by design.

---

## Project Structure
```bash
.
├── context.txt          # Editable knowledge base (currently static)
├── main.py              # Entry point – runs the bot
├── pyproject.toml       # Project & dependency info (Replit style)
├── uv.lock              # Package lock file (auto-generated)
├── generated-icon.png   # Optional UI branding
