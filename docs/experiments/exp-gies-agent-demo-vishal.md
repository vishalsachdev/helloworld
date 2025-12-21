# Experiment: exp/gies-agent-demo-vishal
- Owner: vishal
- Date: 2025-11-13
- Goal: Transform Gies Business School website into an LLM agent-friendly platform

## Plan
- Scrape public data from giesbusiness.illinois.edu
- Structure data as clean JSON with schemas
- Build REST API with FastAPI (20+ endpoints)
- Create comprehensive documentation and examples

## Changes
- `api/main.py` - FastAPI server implementation
- `api/requirements.txt` - Python dependencies
- `scrapers/scrape_gies.py` - Web scraping script
- `data/structured/` - Clean JSON data (programs, faculty, departments, news)
- `data/schemas/` - JSON schemas for validation
- `docs/API.md` - API reference documentation
- `docs/EXAMPLES.md` - Usage examples
- `examples/agent-queries.md` - Sample agent interactions
- `DEMO.md`, `PRESENTATION.md`, `QUICKSTART.md` - Demo materials

## Results
- Functional API with 20+ endpoints
- Coverage: 7 programs, 5 faculty, 3 departments, 3 news articles
- Response time: <50ms average
- Auto-generated OpenAPI documentation

## Follow-ups
- Expand coverage to all programs and courses
- Add authentication and rate limiting
- Consider GraphQL endpoint
- Deploy to production
