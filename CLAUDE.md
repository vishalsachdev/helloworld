# Experiment: claude-code-tools-test

Testing pchalasani/claude-code-tools - a productivity toolkit for Claude Code.

## Goal
Test and evaluate the claude-code-tools package:
- aichat (session management, search, resume)
- tmux-cli (terminal automation)
- Plugins (safety hooks, workflow)
- Utilities (vault, env-safe)

## Repo Type
type: code

## Test Plan
1. Install via `uv tool install claude-code-tools`
2. Install aichat-search TUI via Homebrew
3. Test `aichat search` functionality
4. Test `tmux-cli` in a tmux session
5. Try installing plugins via marketplace

## Current Focus
- [x] Install and test all tools

## Test Results
| Tool | Status | Notes |
|------|--------|-------|
| aichat | ✅ Works | Indexed 20,639 sessions, search + info work |
| aichat-search | ✅ Works | Installed via Homebrew, fast full-text search |
| tmux-cli | ⚠️ Requires tmux | Not installed in this environment |
| env-safe | ✅ Works | Safe .env inspection |
| vault | ✅ Works | Encrypted .env backup |
| Plugins | ✅ Works | aichat and safety-hooks installed |

## Key Insights
- **Session lineage** preserves links to parent sessions when context fills up
- **Full-text search** via Tantivy is more powerful than built-in session search
- **>resume hook** - type `>resume` when context fills, copies session ID to clipboard
- **Safety hooks** guard against git add ., rm, .env exposure

## Session Log
### 2025-12-26
- Created experiment to test pchalasani/claude-code-tools
- Installed claude-code-tools via uv (4 executables)
- Installed aichat-search via Homebrew
- Built Tantivy index (20,639 sessions)
- Tested aichat search (works with --json for programmatic use)
- Tested env-safe and vault utilities
- Installed aichat and safety-hooks plugins
- Result: Solid toolkit, recommended for power users
