# Gies Agent-Friendly API Demo

## Repo Type
type: code

## What This Is
A proof-of-concept transforming the Gies Business School website into an LLM agent-friendly platform with structured JSON data and REST APIs.

## Parent Repo
- **Framework:** `/Users/vishal/code/helloworld` (experiment sandbox)
- **Branch:** `exp/gies-agent-demo-vishal`
- **This is a git worktree** - commits go to the experiment branch

## Key Files
| File | Purpose |
|------|---------|
| `api/main.py` | FastAPI server with 20+ endpoints |
| `data/structured/` | Clean JSON data (programs, faculty, departments, news) |
| `data/schemas/` | JSON schemas for validation |
| `scrapers/scrape_gies.py` | Web scraper for giesbusiness.illinois.edu |
| `docs/API.md` | API reference documentation |
| `docs/EXAMPLES.md` | Usage examples |

## Quick Start
```bash
pip install -r api/requirements.txt
cd api && python main.py
# API at http://localhost:8000/docs
```

## Current Focus
- Expand coverage to all programs and courses
- Add authentication and rate limiting
- Consider GraphQL endpoint

## Git Workflow
```bash
# This is a worktree - commits go to experiment branch
git add . && git commit -m "exp: gies-demo - <what you did>"
git push origin exp/gies-agent-demo-vishal
```

## To Graduate to Own Repo
```bash
# Copy folder, update remote, push as new repo
cp -r /Users/vishal/code/gies-agent-demo /path/to/new-location
cd /path/to/new-location
git remote set-url origin git@github.com:vishalsachdev/gies-agent-demo.git
git push -u origin main
```
