# Agents Guide

This repo is meant for rapid experiments—every experiment runs on its own branch and should leave a short paper trail so others can pick it up.

## Workflow
- Pull the latest `main`, then create a branch: `git checkout -b exp/<topic>-<owner>` (e.g. `exp/search-tuning-vishal`).
- Record notes in `docs/experiments/<branch>.md` using the template in `docs/experiments/README.md`.
- Keep changes scoped to your experiment; do not modify `main` directly.
- When done, push your branch and open a PR into `main` (or keep it as a reference branch if it's a spike).

## Repo hints
- API server: `cd api && python main.py` or `uvicorn main:app --reload --host 0.0.0.0 --port 8000`.
- Scraper: `python scrapers/scrape_gies.py` updates the structured JSON files in `data/structured/`.
- Docs live in `docs/`; examples in `examples/agent-queries.md`; quick setup in `README.md`.

## Expectations for experiments
- Add a brief summary of what you changed, why, and how to rerun it in your experiment log file.
- Prefer small, clear commits with messages like `exp: <topic> - <action>`.
- Note any data or schema edits so downstream consumers can adjust.
- Run any relevant checks you introduce (tests, scripts) and note the commands you executed.
