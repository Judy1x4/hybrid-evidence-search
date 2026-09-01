---
name: build
description: Give step-by-step instructions for the user to follow to implement a given day of the Hybrid Evidence Search Engine project outline. Use when the user asks to build/implement a day's tasks after learning the concepts (e.g. "/build day3", "give me build instructions").
---

# Build

Turn a day's **Build:** section in `documents/project_outline.md` into a step-by-step instruction list for the user to follow themselves.

## Steps

1. Read `documents/project_outline.md` and find the requested day (the argument passed to this skill, e.g. "day3"; if no day is given, infer it from the most recent `documents/dayN.md` file or ask the user which day).
2. Check the current repo state first (`src/`, `scripts/`, `tests/`, `results/`) to see what's already implemented for that day, so instructions don't repeat finished work.
3. Turn that day's **Build:** bullets into a concrete, ordered checklist: which file(s) to create/edit, what function/class to add, what the end-of-day target output should look like (referencing the day's target metrics/results where the outline specifies them).
4. Give instructions for the user to implement themselves — do **not** write the implementation code unless the user explicitly asks you to write it instead of guiding them. Default to guidance, not authorship.
5. Point out relevant existing code/conventions already in the repo (e.g. an existing retriever's structure) so new code stays consistent.
6. End by noting what "done" looks like for the day (the outline's "End-of-day target" line) and how to verify it (e.g. which script to run, which metric to check).

## Notes

- This mirrors the project's own "learn first, build second" workflow — pair with the `learn` skill, which should typically run first for the same day.
- Keep scope tight to what the outline specifies for that day; don't pull in later days' work early.
