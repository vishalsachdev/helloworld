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
### 2025-12-31
- Completed: Created sw-llm-kb experiment (Simon Willison LLM Knowledge Base)
  - New worktree at ../sw-llm-kb on branch exp/sw-llm-kb-vishal (orphan branch)
  - Built queryable knowledge base with Markdown + YAML frontmatter structure
  - Extracted 4 insights from Simon Willison's "2025: The Year in LLMs" article
  - Created shell-based query tool (./query.sh) with category, tag, and keyword search
  - **Key pattern**: Structured notes with frontmatter enable semantic querying without embedding models
- Next: Add more experiment templates (research, mixed)

### 2025-12-29
- Completed: Graduated kg-learning experiment to standalone repo
  - Initial graduation had issues: helloworld artifacts included, nested folder structure
  - Fixed kg-learning repo: moved content from nested folder to root, removed artifacts
  - Graduated repo: https://github.com/vishalsachdev/kg-learning
- Completed: Fixed experiment graduation workflow in agents.md
  - Updated `new-experiment` to use orphan branches (clean start, no inherited files)
  - Updated `graduate-experiment` with cleanup steps for legacy experiments
  - Added documentation for handling helloworld artifacts
  - **Key insight**: Graduation was broken because experiment branches inherited all helloworld files
- Completed: Created newsletter article about kg-learning journey
  - Written to kg-learning repo: `articles/2025-12-29-when-your-knowledge-graph-graduates.md`
  - Created cover images (LinkedIn, Substack, Twitter)
- Session transcript: https://gistpreview.github.io/?8313283b7d967fa391e52ce941535a47
- Next: Add more experiment templates (research, mixed)

### 2025-12-27 (evening)
- Completed: Created context-graphs experiment and graduated to standalone repo
  - Explored Venkatraman and Foundation Capital frameworks for AI context management
  - Built 3 prototypes:
    - decision_trace_extractor.py - extracts decision traces from Claude Code thinking blocks
    - cross_session_analyzer.py - analyzes patterns across sessions
    - projection_function.py - implements the projection function (datagraph -> context)
  - Key finding: Claude Code thinking blocks ARE decision traces (business-level semantics on execution telemetry)
  - Extracted 165+ decision traces across sessions
  - Generated markdown output documents with relevance scoring
  - **Successfully tested graduate-experiment action** - promoted to standalone repo
  - Graduated repo: https://github.com/vishalsachdev/context-graphs
  - Deleted experiment branch from helloworld after graduation
  - Added sample data and configurable --transcripts flag for portability
- Next: Add more experiment templates (research, mixed)

### 2025-12-27 (morning)
- Completed: Created factorio-skills experiment
  - New worktree at ../factorio-skills on branch exp/factorio-skills-vishal
  - Built "Flow Factory" MVP game with HTML5 Canvas
  - Grid-based world with resource nodes (iron/copper)
  - Conveyor belt placement system (click + R to rotate)
  - Items spawn from nodes and flow along belts to chests
  - Real-time throughput tracking
  - Documented Factorio -> Agentic Coding skill mappings
- Next: Add item backup/bottleneck logic (items stop when path blocked)

### 2025-12-26 (late night)
- Completed: Tested Simon Willison's claude-code-transcripts tool
  - Used `uvx claude-code-transcripts` to convert JSONL transcripts to shareable HTML
  - Created transcript-test/ and transcript-test-large/ with generated outputs
  - Added transcript archiving feature to close-shop agent (meta improvement!)
  - Session transcript: [articles/transcripts/index.html](articles/transcripts/index.html)
- Completed: Version controlled ~/.claude configuration
  - Set up git for ~/.claude (skills, agents, hooks, CLAUDE.md, AGENTS.md)
  - Created .gitignore to exclude 3.5GB of auto-generated files (credstore, todos, projects, settings)
  - Initial commit: 63 files tracked
  - Created private GitHub repo: vishalsachdev/claude-config
  - Added write-article skill and skill-creator integration
  - Archived session to Gist and linked in compound engineering article
  - Gist: https://gistpreview.github.io/?8cd18b1253910d75de05475da5afeea8/index.html
- Next: Test graduate-experiment action

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
