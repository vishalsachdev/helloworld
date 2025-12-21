# Experiment Sandbox

A repository for running isolated experiments. Each experiment lives on its own branch with documentation.

## Workflow

1. **Create a branch**: `git checkout -b exp/<topic>-<owner>`
2. **Do your work**: Keep commits scoped and frequent
3. **Log progress**: Document in `docs/experiments/<branch>.md` using the [template](docs/experiments/README.md)
4. **Share or archive**: Open a PR to merge, or keep the branch as a reference spike

See [agents.md](agents.md) for a checklist tailored for AI/automation agents.

## Active Experiments

| Branch | Description | Status |
|--------|-------------|--------|
| `exp/gies-agent-demo-vishal` | Agent-friendly API for Gies Business School | Active |
| `exp/research-task-force-vishal` | AI curriculum task force research | In Progress |
| `claude/twitter-follower-tracker-*` | Twitter follower tracking web app | Reference |
| `claude/research-realtime-github-sync-*` | GitHub-Canvas sync feasibility | Research Complete |

## Experiment Logs

Browse `docs/experiments/` for documentation on each experiment:
- [Experiment Template](docs/experiments/README.md)
- [Twitter Follower Tracker](docs/experiments/claude-twitter-follower-tracker.md)
- [GitHub-Canvas Sync](docs/experiments/claude-research-realtime-github-sync.md)

## Getting Started

```bash
# Clone and create your experiment branch
git clone https://github.com/vishalsachdev/helloworld.git
cd helloworld
git checkout -b exp/my-experiment-vishal

# Start experimenting, then document
cp docs/experiments/README.md docs/experiments/exp-my-experiment-vishal.md
# Edit the template with your notes
```
