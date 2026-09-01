---
name: learn
description: Explain the concepts behind a given day of the Hybrid Evidence Search Engine project outline, for understanding only. Use when the user asks to learn/understand a day's topic before building it (e.g. "/learn day3", "explain today's concepts").
---

# Learn

Teach the concepts listed under a day's **Learn:** section in `documents/project_outline.md`, before any building happens.

## Steps

1. Read `documents/project_outline.md` in this repo. Find the requested day (the argument passed to this skill, e.g. "day3"; if no day is given, infer it from the most recent `documents/dayN.md` file or ask the user which day).
2. Take that day's **Learn:** bullet list and explain each concept clearly, in your own words:
   - What the concept is and why it matters for this project specifically (not a generic textbook definition).
   - How it connects to the concepts from prior days, if relevant.
   - Keep it concise — a few sentences to a short paragraph per bullet, not an essay.
3. Do **not** write or edit any code in this mode. This is understanding-only, mirroring the project's own "learn first, build second" workflow.
4. End by asking if the user is ready to move to the build step (the `build` skill) or wants any concept expanded further.

## Notes

- This is a solo learning project (see the project outline's "Definition of done" and scope constraints) — keep explanations grounded in what's actually needed for BM25 / dense / hybrid / reranking, not tangents into unrelated ML topics.
- If asked about a day not yet reached in the outline, still explain it, but note that it builds on unimplemented prior work if relevant.
