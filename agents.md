# Agents Guide

This repo is meant for rapid experiments—every experiment runs on its own branch and should leave a short paper trail so others can pick it up.

## Session Workflow

Use these skills at the start and end of each session:

| Command | When | What it does |
|---------|------|--------------|
| `/session-start` | Beginning of session | Reads CLAUDE.md, checks git status, orients you |
| `/close-shop` | End of session | Commits work, updates docs, prepares for next session |

## Worktree Structure

Experiments are available as sibling folders via git worktrees:

```
/Users/vishal/code/
├── helloworld/           # main (framework only)
├── gies-agent-demo/      # exp/gies-agent-demo-vishal
├── research-task-force/  # exp/research-task-force-vishal
├── twitter-tracker/      # claude/twitter-follower-tracker-*
└── github-canvas-sync/   # claude/research-realtime-github-sync-*
```

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
