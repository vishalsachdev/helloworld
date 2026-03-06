# helloworld

Experiment framework for rapid prototyping with Claude Code tooling.

## Repo Type
type: code

## Quick Reminder

**Experiments are SIBLING FOLDERS, not subfolders!**

```
/Users/vishal/code/
├── helloworld/            ← YOU ARE HERE (main)
├── gies-agent-demo/       ← cd ../gies-agent-demo
├── research-task-force/   ← cd ../research-task-force
└── ...other experiments
```

Run `git worktree list` to see all experiments.

## Project Actions

This repo has custom actions defined in `agents.md`:
- `new-experiment <name>` - Create a new experiment
- `graduate-experiment <name>` - Promote to standalone repo

## Recommended Tools

Session management tools tested in [exp-claude-code-tools-test](docs/experiments/exp-claude-code-tools-test-vishal.md):

| Tool | Purpose | Command |
|------|---------|---------|
| `aichat search` | Find past sessions by keyword | `aichat search "topic"` |
| `aichat search --json` | Programmatic search for agents | `aichat search --json "error" \| head` |
| `>resume` | Quick escape when context fills | Type `>resume` in session |
| `transcripts` | Export session to shareable HTML | `uvx claude-code-transcripts local --gist` |

**Key insight:** `aichat` finds sessions (for you), `transcripts` shares them (for others).

## Current Focus
- [ ] Add more experiment templates (research, mixed)

## Roadmap
- [x] Set up worktree-based experiment structure
- [x] Add Project Actions pattern
- [x] Document worktree mental model
- [x] Test new-experiment action
- [x] Test graduate-experiment action

## Backlog
- Add more experiment templates (research, mixed)
- Automation for cleaning up stale worktrees

## Session Log
### 2026-03-05
- Completed: Created openai-api skill for Claude Code
  - Modeled after Anthropic's `claude-api` skill from `anthropics/skills` repo
  - 23 files: SKILL.md routing layer + Python/TypeScript deep coverage + Java/Go/C#/cURL light coverage
  - Covers Chat Completions API, Responses API, Agents SDK, structured outputs, tool use, batches
  - Current model tables (GPT-5.4 flagship, o-series reasoning), research-verified pricing
  - Committed to `~/.claude` (claude-config repo) and pushed to github.com/vishalsachdev/claude-config
  - Design doc saved to `docs/plans/2026-03-05-openai-api-skill-design.md`
- Next: Add more experiment templates (research, mixed)

<!-- Older session logs (2025-12-26 through 2025-12-31) archived — see git history -->
