# Experiment: exp-claude-code-tools-test-vishal

- Owner: vishal
- Date: 2025-12-26
- Goal: Test and evaluate pchalasani/claude-code-tools productivity toolkit

## Context
[claude-code-tools](https://github.com/pchalasani/claude-code-tools) is a popular (639 stars) collection of tools for Claude Code:
- **aichat**: Session management with search, resume, trim, rollover
- **tmux-cli**: Terminal automation ("Playwright for terminals")
- **Plugins**: Safety hooks, workflow logging, UI testing
- **Utilities**: vault (.env backup), env-safe (safe .env inspection)

## Plan
- [x] Install claude-code-tools via uv
- [x] Install aichat-search TUI (Homebrew)
- [x] Test aichat search/resume functionality
- [ ] Test tmux-cli in tmux session (requires tmux)
- [x] Try plugin installation

## Changes
- Created experiment worktree at `../claude-code-tools-test/`
- Installed `claude-code-tools` via uv (4 executables: aichat, env-safe, tmux-cli, vault)
- Installed `aichat-search` via Homebrew
- Built Tantivy index (20,639 sessions indexed)
- Installed `aichat` and `safety-hooks` plugins

## Results
| Tool | Status | Notes |
|------|--------|-------|
| aichat | ✅ Works | Session search, info, resume strategies |
| aichat-search | ✅ Works | Fast full-text search via Tantivy |
| tmux-cli | ⚠️ Requires tmux | Not installed in test environment |
| env-safe | ✅ Works | Safe .env inspection |
| vault | ✅ Works | Encrypted .env backup |
| Plugins | ✅ Works | aichat and safety-hooks installed |

**Key features:**
- Session lineage preserves links to parent sessions when context fills up
- `>resume` hook copies session ID to clipboard when context is filling up
- Full-text search is more powerful than built-in session search

## Follow-ups
- Test `tmux-cli` when running inside tmux
- Explore `workflow` plugin for work logging
- Consider making `aichat search --json` part of standard workflow
