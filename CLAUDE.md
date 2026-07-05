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
### 2026-03-31
- Graduated hermes-makerlab experiment to standalone repo: [makerlab-infra](https://github.com/vishalsachdev/makerlab-infra)
  - Installed Hermes agent on MakerLab iMac (Tailscale SSH, GPT-5.4, Telegram gateway)
  - Set up Cloudflare Tunnel with 5 subdomains on illinihunt.org (lab, db, sql, bot, admin)
  - Installed PostgreSQL 16.8, pgAdmin4, SQL API — all user-space (no sudo)
  - Migrated BADM 554 databases from AWS RDS MySQL → self-hosted PostgreSQL (4 DBs, 85K+ rows)
  - Deleted AWS RDS instance (saving ~$100/mo)
  - Built SQL API at sql.illinihunt.org for Google Colab student access
  - Created Canvas page "Database Access (New - PostgreSQL)" for students
  - Consolidated Cloudflare reference: ~/.claude/references/cloudflare-illinihunt.md
  - Wrote newsletter article: "From Cloud to Campus"
- Next: Deploy badm554-bot, install Portainer, add more iMacs to Tailscale

*Older entries archived to `docs/session-archive.md`*

