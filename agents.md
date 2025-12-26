# Agents Guide

This repo is meant for rapid experiments—every experiment runs on its own branch and should leave a short paper trail so others can pick it up.

## Project Actions

### new-experiment <name>
Creates a new experiment branch with worktree for isolated development.

**Steps:**
1. Create branch `exp/<name>-vishal` from main
2. Add git worktree at `../<name>/` pointing to the new branch
3. Create `../<name>/CLAUDE.md` from template below
4. Create experiment log at `docs/experiments/exp-<name>-vishal.md`
5. Report: "Experiment ready at ../<name>/"

**CLAUDE.md template for new experiment:**
```markdown
# Experiment: <name>

## Goal
[To be filled in]

## Repo Type
type: code

## Current Focus
- [ ] Initial setup

## Session Log
### <today's date>
- Created experiment
- Next: Define goal and first steps
```

**Experiment log template:**
```markdown
# Experiment: exp-<name>-vishal
- Owner: vishal
- Date: <today's date>
- Goal: [To be defined]

## Plan
- [ ] Step 1

## Changes
- Initial setup

## Results
- [Pending]

## Follow-ups
- [Pending]
```

**To run:** Ask Claude to "create new experiment called <name>"

### graduate-experiment <name>
Promotes an experiment to its own standalone repository.

**Steps:**
1. Verify worktree exists at `../<name>/`
2. Create new GitHub repo: `gh repo create <name> --public --source=../<name>/`
3. Update remote: `git -C ../<name>/ remote set-url origin git@github.com:vishalsachdev/<name>.git`
4. Push: `git -C ../<name>/ push -u origin HEAD:main`
5. Remove worktree: `git worktree remove ../<name>/`
6. Report: "Graduated to https://github.com/vishalsachdev/<name>"

**To run:** Ask Claude to "graduate experiment <name> to its own repo"

## Session Workflow

Use these skills at the start and end of each session:

| Command | When | What it does |
|---------|------|--------------|
| `/session-start` | Beginning of session | Reads CLAUDE.md, checks git status, orients you |
| `/close-shop` | End of session | Commits work, updates docs, prepares for next session |

## Worktree Structure

**Key insight:** Experiments are **sibling folders**, not subfolders. They live alongside helloworld, not inside it.

```
/Users/vishal/code/
│
├── helloworld/            ← YOU ARE HERE (main branch)
│   ├── agents.md
│   ├── articles/
│   └── docs/experiments/
│
├── gies-agent-demo/       ← cd ../gies-agent-demo (exp/gies-agent-demo-vishal)
├── research-task-force/   ← cd ../research-task-force (exp/research-task-force-vishal)
├── twitter-tracker/       ← cd ../twitter-tracker
└── github-canvas-sync/    ← cd ../github-canvas-sync
```

### Mental Model

```
┌─────────────────────────────────────────────────────────────────┐
│                     ONE GIT HISTORY                             │
│                   (shared .git database)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   helloworld/          gies-agent-demo/      twitter-tracker/   │
│   ┌──────────┐         ┌──────────┐          ┌──────────┐      │
│   │  main    │         │ exp/gies │          │ claude/* │      │
│   │  branch  │         │  branch  │          │  branch  │      │
│   └──────────┘         └──────────┘          └──────────┘      │
│        │                    │                     │             │
│        └────────────────────┴─────────────────────┘             │
│                    All share same commits                       │
└─────────────────────────────────────────────────────────────────┘
```

### Quick Reference

| To do this... | Run this... |
|---------------|-------------|
| See all experiments | `git worktree list` |
| Jump to an experiment | `cd ../gies-agent-demo` |
| See which branch you're on | `git branch --show-current` |
| Create new experiment | Ask Claude: "create new experiment called X" |

### Why This Structure?

- **Isolation:** Each experiment has its own folder, no conflicts
- **Shared history:** All experiments share the same git log
- **Easy switching:** Just `cd` to another folder, no branch switching
- **Clean main:** The `helloworld/` folder stays clean (framework only)

Each folder has its own `CLAUDE.md` with project context. Changes in any folder commit to the correct branch automatically.

### Working with Worktrees

```bash
# List all worktrees
git worktree list

# Add a new experiment as worktree
git checkout -b exp/new-thing-vishal
git worktree add ../new-thing exp/new-thing-vishal

# Remove a worktree (keeps the branch)
git worktree remove ../old-experiment
```

## Experiment Workflow

1. **Create branch:** `git checkout -b exp/<topic>-<owner>`
2. **Add worktree:** `git worktree add ../<folder-name> exp/<topic>-<owner>`
3. **Add CLAUDE.md:** Copy template and customize for your experiment
4. **Record notes:** Update `docs/experiments/<branch>.md`
5. **When done:** Push branch, optionally open PR or keep as reference

## Experiment Logs

Browse `docs/experiments/` for documentation on each experiment:
- [Template](docs/experiments/README.md)
- [Gies Agent Demo](docs/experiments/exp-gies-agent-demo-vishal.md) - on experiment branch
- [Research Task Force](docs/experiments/exp-research-task-force-vishal.md) - on experiment branch
- [Twitter Tracker](docs/experiments/claude-twitter-follower-tracker.md)
- [GitHub-Canvas Sync](docs/experiments/claude-research-realtime-github-sync.md)

## Repo Types

Experiments can be code, research, or mixed. Declare in CLAUDE.md:

```yaml
## Repo Type
type: code      # or: research, mixed
```

This affects how `/session-start` and `/close-shop` behave.

## Commit Style

```bash
exp: <topic> - <action>
```

Examples:
- `exp: gies-demo - Add faculty endpoint`
- `exp: research - Update synthesis document`

## Graduating to Own Repo

When an experiment is ready to become its own repository:

```bash
cd /Users/vishal/code/<experiment-folder>
git remote set-url origin git@github.com:vishalsachdev/<new-repo-name>.git
git push -u origin main
```
