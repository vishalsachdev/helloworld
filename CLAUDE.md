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

## Current Focus
- [ ] Test graduate-experiment action

## Roadmap
- [x] Set up worktree-based experiment structure
- [x] Add Project Actions pattern
- [x] Document worktree mental model
- [x] Test new-experiment action
- [ ] Test graduate-experiment action

## Backlog
- Add more experiment templates (research, mixed)
- Automation for cleaning up stale worktrees

## Session Log
### 2025-12-26 (night)
- Completed: Tested new-experiment action via claude-code-tools experiment
  - Created exp/claude-code-tools-test-vishal branch + worktree
  - Tested pchalasani/claude-code-tools (aichat, env-safe, vault, plugins)
  - Installed aichat and safety-hooks plugins
  - Built Tantivy search index (20,639 sessions)
- Next: Test graduate-experiment action

### 2025-12-26 (evening)
- Completed: Branch cleanup and worktree maintenance
  - Fixed twitter-tracker worktree (detached HEAD → exp/twitter-tracker-vishal)
  - Deleted 6 stale remote branches (demo-branch, claude/*)
  - Reviewed gies-agent-demo state, committed its CLAUDE.md
  - Explained worktrees + remote branches (educational session)
  - Updated close-shop skill to use `model: opus` for Azure AI Foundry compatibility
- Next: Test new-experiment action

### 2025-12-26
- Completed: Project Actions pattern, worktree documentation, newsletter article
- Next: Test new-experiment action
