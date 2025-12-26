# Teaching Claude Code to Remember For You

*Building self-documenting AI workflows that guide instead of require memorization*

---

It started with a simple question: "Should I consolidate my 44 repositories into a monorepo?"

It ended with something more valuable: a system that remembers my workflow preferences so I don't have to.

This is a story about how a conversation with Claude evolved from answering a question to building infrastructure—and what it reveals about the emerging practice of using AI to improve how we work with AI.

## The Question That Wasn't

I asked Claude to analyze my repository structure across four directories: `/code`, `/research`, `/admin`, and `/teaching`. Forty-four repositories. A mix of Node.js and Python. Next.js apps, FastAPI services, research documents, teaching materials.

The analysis was thorough:
- 11 Node.js projects (9 using TypeScript, 8 using React, 6 using Supabase)
- 15 Python projects
- Zero cross-repo dependencies
- Different deployment targets (Vercel, Docker, GitHub Pages)
- Different audiences (students, researchers, public users)

The verdict was clear: **keep separate repos**. Monorepos solve problems I don't have—shared code between packages, atomic cross-package changes, unified CI/CD. My projects have independent lifecycles. Forcing them together would mean running CI for research code when I push a web app fix.

But that wasn't the interesting part.

## The Pivot

While exploring my codebase, Claude noticed something I'd forgotten: my `/helloworld` repo already had a clever structure for experiments. It used **git worktrees** to give each experiment its own folder while sharing a single git history.

```
/Users/vishal/code/
├── helloworld/           # main (framework only)
├── gies-agent-demo/      # exp/gies-agent-demo-vishal
├── research-task-force/  # exp/research-task-force-vishal
└── twitter-tracker/      # experiment branch as worktree
```

This raised a new question: if I want to run Claude tooling experiments, should they all live in this repo? And if so, should there be automation to create new experiments?

I already had `/session-start` and `/close-shop` skills for beginning and ending work sessions. Maybe I needed a `/new-experiment` skill too?

But then came the real question: **if this skill only makes sense inside `/helloworld`, where should it live?**

## Global vs. Local

This is where the conversation got interesting. We'd stumbled into an architectural question about Claude Code itself:

- **Global skills** (like `/session-start`) work in any repository
- **Project-specific workflows** (like creating an experiment) only make sense in certain repos

Should a `/new-experiment` skill be global, cluttering the namespace for every project? Or should it somehow be scoped to just the repos where it applies?

The answer emerged through dialogue: **project-specific workflows belong with the project**.

Instead of creating a global skill, we created a **Project Actions Pattern**. Now any project can define custom actions in its `agents.md` file:

```markdown
## Project Actions

### new-experiment <name>
Creates a new experiment branch with worktree for isolated development.

**Steps:**
1. Create branch `exp/<name>-vishal` from main
2. Add git worktree at `../<name>/`
3. Create CLAUDE.md from template
4. Report: "Experiment ready at ../<name>/"

**To run:** Ask Claude to "create new experiment called <name>"
```

When I run `/session-start` in that project, Claude now surfaces these actions: "Available actions: `new-experiment`, `graduate-experiment`"

The workflow travels with the repository. Clone the repo, get the workflows.

## The Guardrails Philosophy

But here's where I pushed back: "How do I make sure the Project Actions pattern is available to every project I create? I can't remember all of this."

This is the crux of working with AI tooling. You can build sophisticated systems, but if they require you to remember to use them, they'll atrophy. The value comes from **systems that guide you** rather than requiring memorization.

We already had a hint of this pattern. My `/session-start` skill already checked for missing roadmap sections and offered to add them:

```
⚠️ **Missing roadmap sections.** This project has CLAUDE.md but no session tracking.

Would you like me to add them?
```

This is an **active guardrail**. Instead of documentation that says "remember to add roadmap sections," the system notices when they're missing and prompts you.

We extended this philosophy to cover the entire project structure:

1. **No CLAUDE.md?** → "Would you like me to create one?"
2. **Missing roadmap sections?** → "Would you like me to add them?"
3. **End of orientation** → Show "Setup Suggestions" for anything missing

The system remembers so you don't have to.

## Two Layers of Memory

What emerged was a two-layer approach to workflow memory:

**Passive layer**: Architecture documentation in `~/.claude/AGENTS.md` explains how everything fits together—where skills live, where agents live, what goes at the global level vs. project level. You can read this anytime.

**Active layer**: `/session-start` checks the current project against the expected patterns and prompts for anything missing. You don't have to remember to read the documentation; the system brings relevant guidance to you at the moment you need it.

This mirrors how the best frameworks work. Rails doesn't require you to memorize where controllers go—it tells you when you've put something in the wrong place. The convention is encoded in the tooling, not just documented in a wiki.

## The Architecture

Here's what we built (conceptually—the actual implementation lives in markdown files that Claude reads):

```
~/.claude/
├── AGENTS.md           # Universal patterns (documented here)
├── skills/session-start/   # Orients you, checks for missing structure
├── agents/close-shop.md    # Wraps up sessions, updates roadmaps
└── commands/               # Simple slash commands

project/
├── CLAUDE.md           # Project context + roadmap
└── agents.md           # Project-specific actions
```

**The flow:**
1. Start a session → `/session-start` reads global patterns + project context
2. Missing something? → System prompts you to add it
3. Work happens
4. End session → `/close-shop` updates roadmap, commits, logs

Each layer has a clear responsibility. Global patterns define conventions. Project files instantiate them with specific context. Skills enforce the patterns and guide you when something's missing.

## What This Reveals

This session illustrates something I've been exploring in [Compound Engineering](https://chatwithgpt.substack.com/p/compound-engineering-use-it-before): using AI not just to write code, but to improve the workflows around writing code.

**The question evolved:**
- "Should I use a monorepo?" → (answered: no)
- "Where should project-specific automation live?" → (answered: with the project)
- "How do I remember to use these patterns?" → (answered: build systems that remind you)

Each question led to a better question. The AI wasn't just answering—it was helping me notice the real problem beneath the surface question.

**The meta-pattern:**
What we built today will make future sessions more productive. The `/session-start` skill now checks for project structure and offers to set it up. The Project Actions pattern means repo-specific workflows are discoverable. The architecture documentation means I (or Claude in a future session) can understand how the pieces fit together.

This is the compound effect: investing in workflow infrastructure pays dividends across every future session.

## Try It Yourself

If you're using Claude Code, consider building similar guardrails:

1. **Document your patterns** in a global AGENTS.md or CLAUDE.md
2. **Create a session-start skill** that reads project context and checks for missing structure
3. **Define project-specific actions** in project-level files, not global skills
4. **Make the system prompt you** when something's missing, rather than requiring you to remember

The goal isn't perfect documentation. It's building systems that guide you toward the right patterns without requiring memorization.

---

*This article was written by Claude, documenting a real collaboration session. The irony isn't lost on me that I'm now part of a system designed to remember things so humans don't have to.*

---

**Created:** 2025-12-26
**Last Updated:** 2025-12-26

*Read more at [The Hybrid Builder](https://chatwithgpt.substack.com/s/the-hybrid-builder)*
