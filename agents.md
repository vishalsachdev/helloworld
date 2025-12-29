# Agents Guide

This repo is meant for rapid experiments—every experiment runs on its own branch and should leave a short paper trail so others can pick it up.

## Project Actions

### new-experiment <name>
Creates a new experiment as an **orphan branch** with worktree for isolated development.

**Why orphan?** Orphan branches start with no files, so experiments don't inherit helloworld artifacts. This makes graduation clean—only experiment files exist.

**Steps:**
1. Create orphan branch `exp/<name>-vishal`: `git checkout --orphan exp/<name>-vishal`
2. Remove all inherited files: `git reset --hard` (clears index without deleting worktree files)
3. Add git worktree at `../<name>/` pointing to the new branch
4. Create `../<name>/CLAUDE.md` from template below
5. Create experiment log at `docs/experiments/exp-<name>-vishal.md` (on main branch)
6. In the worktree, make initial commit with just CLAUDE.md
7. Report: "Experiment ready at ../<name>/"

**Commands:**
```bash
# From helloworld directory
git checkout --orphan exp/<name>-vishal
git reset --hard
git checkout main  # Return to main
git worktree add ../<name>/ exp/<name>-vishal
# Then create CLAUDE.md in ../<name>/ and commit
```

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

**IMPORTANT:** If the experiment was created before orphan branches were standard, it may contain helloworld artifacts. Check and clean before pushing.

**Steps:**
1. Verify worktree exists at `../<name>/`
2. **Check for helloworld artifacts** in the worktree:
   - Known artifacts: `agents.md`, `articles/` (with helloworld articles), `docs/experiments/`, `transcript-test*/`
   - If found, these need to be removed before graduation
3. **Check for nested content**: If experiment content is in `../<name>/<name>/`, it needs to be elevated to root
4. Create new GitHub repo: `gh repo create <name> --public`
5. In the worktree, set remote: `git -C ../<name>/ remote add origin git@github.com:vishalsachdev/<name>.git` (or `set-url` if exists)
6. Push: `git -C ../<name>/ push -u origin HEAD:main`
7. Remove worktree from helloworld: `git worktree remove ../<name>/`
8. Delete the experiment branch from helloworld: `git branch -D exp/<name>-vishal`
9. Update experiment log to mark as "graduated"
10. Report: "Graduated to https://github.com/vishalsachdev/<name>"

**Cleanup for legacy experiments (non-orphan branches):**
```bash
cd ../<name>
# Remove helloworld artifacts (move to TRASH first)
mkdir -p TRASH
mv agents.md docs/ transcript-test* TRASH/ 2>/dev/null
# If content is nested, elevate it
mv <name>/* . 2>/dev/null && mv <name> TRASH/
# Add TRASH to .gitignore
echo -e "\nTRASH/" >> .gitignore
# Commit cleanup
git add -u && git add .gitignore
git commit -m "Clean up: remove helloworld artifacts before graduation"
```

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
