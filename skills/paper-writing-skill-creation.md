# Paper Writing Skill Created

## Overview
Created a comprehensive academic paper writing skill for Claude Code.

**Location:** `~/.claude/skills/paper-writing/`

## Skill Structure

```
paper-writing/
├── SKILL.md                      # Main skill file with YAML frontmatter
├── LICENSE.txt                   # MIT License
├── references/                   # Detailed reference documentation
│   ├── REFERENCE.md             # Comprehensive writing guidelines
│   ├── STRUCTURE.md             # Paper structure templates
│   ├── STYLE.md                 # Academic writing style guide
│   └── ELITE-PAPERS.md          # Thatcher's 17 rules for elite IS papers
├── assets/                       # Ready-to-use templates
│   ├── README.md                # Template usage guide
│   ├── research-paper-template.md
│   └── conference-paper-template.md
└── scripts/                      # Helper utilities
    └── check_paper.py           # Paper quality checker script
```

## Features

### Main Skill (SKILL.md)
- Comprehensive workflow for all paper writing stages
- Section-specific guidance (Abstract, Introduction, Methods, etc.)
- Visualization best practices
- Common pitfalls to avoid
- Discipline-specific considerations
- Quality checklist

### Reference Materials

#### REFERENCE.md
- Argument construction techniques
- Evidence and citation best practices
- Writing style and clarity guidelines
- Common formatting standards (APA, IEEE, Chicago)
- Peer review and revision strategies
- Ethical considerations
- Advanced writing techniques

#### STRUCTURE.md
Complete templates for:
- Research Article (IMRAD format)
- Computer Science Conference Paper
- Literature Review / Survey Paper
- Position Paper / Perspective
- Technical Report
- Thesis Chapter
- Short Paper / Extended Abstract

#### STYLE.md
- Core principles of academic writing
- Sentence-level writing techniques
- Word choice and precision
- Common errors to avoid
- Discipline-specific styles
- Revision techniques

#### ELITE-PAPERS.md
Based on Jason Bennett Thatcher's "Rules for Writing Elite Information Systems Papers":
- 17 rules organized in 5 phases
- Detailed diagnostics and checklists
- Bonus principles from mentors (May Maxim, Pascoe Principle, George Law)
- Common Diagnostics Box workflow
- MISQ-style paper outline template

### Assets

Templates include:
- Complete section structure
- Placeholder guidance
- Example content
- Pre-submission checklists
- Inline comments for authors

### Scripts

**check_paper.py**: Automated quality checker
- Hedging detection
- Passive voice analysis
- Sentence length analysis
- Nominalization detection
- Wordy phrase identification
- Overall scoring (0-100)

## Usage

To use the paper-writing skill in Claude Code:

```markdown
When working on a paper, Claude Code will automatically detect and offer the
paper-writing skill when appropriate topics are discussed.
```

Or explicitly invoke with conversation context about academic writing.

## Key Capabilities

1. **Planning Phase**
   - Research question formulation
   - Outline creation
   - Structure selection

2. **Writing Phase**
   - Section-by-section guidance
   - Progressive writing strategies
   - Template usage

3. **Refinement Phase**
   - Multi-pass revision strategies
   - Style improvement
   - Quality assurance

4. **Elite Paper Standards**
   - Thatcher's 17 rules
   - Construct-centered approach
   - Mechanism-based theory
   - Rigorous empirics

## Sources

This skill synthesizes guidance from:
- APA Style (7th Edition) - [research.com](https://research.com/research/apa-format-for-academic-papers)
- Academic Writing Best Practices - [Ohio University](https://www.ohio.edu/cas/law-center/ma-law-justice-culture/requirements/writing-guide)
- Writing Research Papers - [UCSD Psychology](https://psychology.ucsd.edu/undergraduate-program/undergraduate-resources/academic-writing-resources/writing-research-papers/research-paper-structure.html)
- Academic Writing Style - [USC Research Guides](https://libguides.usc.edu/writingguide/academicwriting)
- Thatcher, J.B. (2025). "Rules for Writing Elite Information Systems Papers: Field Notes for my PhD Students"
- Agent Skills specification - [agentskills.io](https://agentskills.io/specification)
- Anthropic Skills Repository - [github.com/anthropics/skills](https://github.com/anthropics/skills)

## Installation

The skill is already installed at:
```
~/.claude/skills/paper-writing/
```

Claude Code will automatically discover and use this skill when appropriate.

## Testing

To test the paper quality checker:
```bash
cd ~/.claude/skills/paper-writing/scripts
python check_paper.py <your_paper.md>
```

## Next Steps

Potential enhancements:
- Additional templates for specific disciplines
- More automated checks
- Integration with reference managers
- LaTeX-specific templates
- Citation format validators

## Created

- Date: 2026-01-01
- Session: claude/paper-writing-skill-9VjqE
- Based on user request to create skill from SSRN paper and agentskills.io spec
