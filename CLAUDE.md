# Experiment: factorio-skills

A browser-based game inspired by Factorio, designed to build mental models that transfer to agentic coding.

## Goal

Create a simplified Factorio-like game where the core mechanics directly map to skills needed for working with AI agents:
- **Resource flow** → Token/context management
- **Factory blueprints** → Reusable agent compositions
- **Throughput optimization** → Parallelization & batching
- **Dependency chains** → Agent orchestration
- **Debugging bottlenecks** → Tracing agent failures

## Repo Type
type: code

## The Hypothesis

Expert Factorio players excel at:
1. Thinking in systems, not individual actions
2. Designing for scalability from the start
3. Debugging by tracing dependencies upstream
4. Balancing throughput across parallel processes
5. Building modular, reusable components

These are *exactly* the skills needed for effective agentic coding.

## Skill Mapping (Factorio → Agentic Coding)

| Factorio Concept | Agentic Coding Equivalent |
|------------------|---------------------------|
| Conveyor belts | Data pipelines between agents |
| Assemblers | Specialized agents (tools) |
| Inserters | Context injection / tool calls |
| Power grid | Token budget / rate limits |
| Blueprints | Saved agent compositions |
| Logistics network | Agent orchestration layer |
| Bottleneck (red inserter) | Rate-limited API / slow agent |
| Research tree | Capability unlocks |

## Tech Stack
- **Rendering**: HTML5 Canvas or Phaser.js
- **State**: Vanilla JS (start simple)
- **No backend**: All client-side for now

## Current Focus
- [ ] Define MVP game mechanics
- [ ] Create basic grid-based world
- [ ] Implement resource nodes (iron, copper)
- [ ] Add conveyor belt placement

## Session Log
### 2025-12-26
- Created experiment from helloworld framework
- Documented Factorio → Agentic Coding skill mapping
- Next: Design MVP mechanics and start prototyping
