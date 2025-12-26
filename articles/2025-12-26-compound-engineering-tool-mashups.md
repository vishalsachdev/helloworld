# Compound Engineering: When Two Tools Are Better Than One

*How Claude helped me evaluate, compare, and combine two CLI tools without reading a single line of source code*

---

## The Setup

It's late evening, and I'm deep in a familiar pattern: testing new tools that promise to improve my Claude Code workflow. Tonight's candidates are two independent projects from different developers:

1. **pchalasani/claude-code-tools** — A session management toolkit with search, resume, and context preservation
2. **simonw/claude-code-transcripts** — A session export tool that converts JSONL transcripts to shareable HTML

Both tools operate on the same data (Claude Code session files), which immediately raised a question: *Are these redundant? Competing? Or complementary?*

This is the kind of evaluation that used to take hours of documentation reading, trial-and-error, and sometimes diving into source code. Tonight, it took about 20 minutes — and I never opened a single source file.

## The Compound Engineering Problem

Modern development increasingly involves **compound engineering** — combining existing tools, libraries, and services rather than building from scratch. The value isn't in any single tool; it's in how they compose.

But composition creates complexity:
- Which tools overlap?
- Where do they conflict?
- How do their mental models align (or clash)?
- What's the integration surface?

Traditional approaches to answering these questions:
1. **Read all documentation** — Time-consuming, often incomplete
2. **Read source code** — Even more time-consuming, requires understanding two codebases
3. **Trial and error** — Install both, break things, figure out why

There's a fourth approach that AI collaboration enables: **semantic evaluation** — understanding tools by their *purpose* and *behavior* rather than their implementation.

## Testing the First Tool: aichat

I started with claude-code-tools, specifically its `aichat` command. Installation was straightforward:

```bash
uv tool install claude-code-tools
brew install pchalasani/tap/aichat-search
```

The first impressive moment came when I built the search index:

```
Building search index...
Total: 20,639 session files to check
Indexed 3,119 new/modified sessions
```

Twenty thousand sessions. I've been using Claude Code for months, and this tool just made all that accumulated knowledge searchable. A quick test:

```bash
aichat search --json "helloworld worktree"
```

Returned rich JSON with session metadata, snippets, timestamps. The search uses Tantivy (a Rust-based search engine), so it's genuinely fast full-text search — not just filename matching.

## The Overlap Question

Here's where it got interesting. I mentioned to Claude that I was also testing `claude-code-transcripts` in another window. The natural question: *Do these tools step on each other?*

Rather than reading documentation or source code for both tools, I asked Claude to analyze them based on what we'd observed:

```
can you look at the other experiment im working on in another window,
and check if the two tools can work together or if they are redundant
```

Claude examined both tools — not their code, but their *purpose*:

| Aspect | `aichat` | `claude-code-transcripts` |
|--------|----------|---------------------------|
| Purpose | Session **management** | Session **export/sharing** |
| Primary use | Internal workflow | External communication |
| Output | Search index | Beautiful HTML |
| Who benefits | Me (finding past work) | Others (sharing work) |

The key insight emerged: **one finds, one shares**.

## The Grep vs Cat Analogy

Claude offered an analogy that crystallized the relationship:

> They're like `grep` vs `cat` — one finds things, one displays them.

This is the kind of insight that's hard to extract from documentation. Documentation tells you *what* a tool does. It rarely tells you *where it fits* in a broader workflow alongside other tools.

The compound engineering insight:

```
aichat search "canvas rendering bug"  →  finds session abc123
claude-code-transcripts abc123 --gist  →  shares that session
```

They're not just non-redundant — they're **complementary stages** in a workflow:
1. **Find** (aichat): "What sessions exist about X?"
2. **Share** (transcripts): "Let me export this one for my article"

## Personalized Recommendations Without Code Review

Here's where the AI collaboration became particularly valuable. I asked whether I should even use these tools given my specific patterns:

```
do you recommend this tool for me? given my usage patterns?
```

Claude examined my actual session statistics:

```
Top 5 cwds:
  1495 | /Users/vishal/code/tldraw
   768 | /Users/vishal/code/helloworld
   284 | .../venturebot-v1/athens
```

1,495 sessions in tldraw alone. That's institutional knowledge I'd accumulated without realizing it. The recommendation became contextual:

> Your 1,495 tldraw sessions are a goldmine of context. Next time you're debugging something in tldraw, try: `aichat search --json "canvas rendering bug"`. You might find you solved a similar problem 6 months ago.

This is compound engineering at the meta-level — not just "do these tools work together?" but "do these tools work together *for me*?"

## Managing Complexity Without Implementation Details

What struck me about this evaluation process was what we *didn't* do:

- **Didn't read source code** for either tool
- **Didn't trace data flows** through implementations
- **Didn't debug integration issues** at the code level
- **Didn't compare API signatures** or internal architectures

Instead, we evaluated at the level of:
- **Purpose**: What problem does each solve?
- **Workflow fit**: Where does each belong in my process?
- **Complementarity**: Do they compete or compose?
- **Personal relevance**: Given *my* usage, which pieces matter?

This is semantic evaluation — understanding tools by meaning rather than mechanism.

## The Documentation Decision

At the end of the session, I faced a familiar problem: I'd learned something valuable, but learnings evaporate if not documented. I asked:

```
how do i document what i learn from this experiment.
Your recommendations above need to be saved.
```

We ended up with a layered documentation approach:

| Location | Content | Purpose |
|----------|---------|---------|
| `CLAUDE.md` | Quick reference table | Immediate reminder |
| `docs/experiments/*.md` | Full analysis | Detailed reasoning |

The quick reference in CLAUDE.md means every future session starts with this knowledge visible:

```markdown
## Recommended Tools

| Tool | Purpose | Command |
|------|---------|---------|
| `aichat search` | Find past sessions | `aichat search "topic"` |
| `transcripts` | Export to HTML | `uvx claude-code-transcripts local --gist` |

**Key insight:** `aichat` finds sessions (for you), `transcripts` shares them (for others).
```

## The Meta-Pattern

This session revealed a pattern for compound engineering evaluation:

1. **Test tools independently** — Understand what each does in isolation
2. **Ask the overlap question** — Do they compete or compose?
3. **Seek analogies** — What established patterns do they follow?
4. **Personalize the evaluation** — Given *your* context, what matters?
5. **Document the synthesis** — Capture the combination, not just the components

The AI's role in each step:
1. Automate installation and testing
2. Compare purposes semantically (not just features)
3. Generate clarifying analogies
4. Analyze personal usage data
5. Structure documentation appropriately

## Why This Matters

We're entering an era where the value increasingly comes from **composition** rather than creation. The tools exist. The challenge is:
- Discovering what's available
- Understanding how pieces fit
- Avoiding redundancy
- Maximizing synergy

AI collaboration changes the economics of this evaluation. What used to require hours of documentation review or code reading can now happen through conversation — testing, comparing, synthesizing — in minutes.

The specific tools don't matter (though `aichat` and `claude-code-transcripts` are both excellent). What matters is the pattern: **compound engineering through semantic evaluation**.

---

## Quick Reference

**Install (persistent):**
```bash
uv tool install claude-code-tools
brew install pchalasani/tap/aichat-search
```

**Use (ephemeral):**
```bash
uvx claude-code-transcripts local --gist
```

**The workflow:**
```
aichat search "topic"  →  find relevant session
transcripts --gist     →  share it with others
```

**The insight:**
> `aichat` = "What sessions exist about X?" (for you)
> `transcripts` = "How can I share this session?" (for others)

---

*This article was written collaboratively with Claude, documenting a real evaluation session. The tools mentioned are [pchalasani/claude-code-tools](https://github.com/pchalasani/claude-code-tools) and [simonw/claude-code-transcripts](https://github.com/simonw/claude-code-transcripts).*
