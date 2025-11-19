# Running the Demo

Quick guide to running the Gies Business School Agent-Friendly API demo.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

### 1. Install Dependencies

```bash
# From the project root directory
pip install -r api/requirements.txt
```

This will install:
- FastAPI (web framework)
- Uvicorn (ASGI server)
- Pydantic (data validation)

### 2. Verify Data Files

Make sure the data files exist:

```bash
ls -la data/structured/
```

You should see:
- `programs.json`
- `faculty.json`
- `departments.json`
- `news.json`
- `complete.json`

If these files don't exist, regenerate them:

```bash
python scrapers/scrape_gies.py
```

## Running the API

### Method 1: Direct Python

```bash
cd api
python main.py
```

### Method 2: Using Uvicorn

```bash
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The `--reload` flag auto-restarts on code changes (useful for development).

### Expected Output

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## Accessing the API

### Interactive Documentation (Swagger UI)

Open your browser to:
```
http://localhost:8000/docs
```

Here you can:
- See all available endpoints
- Try queries interactively
- View request/response schemas
- Test with different parameters

### Alternative Documentation (ReDoc)

```
http://localhost:8000/redoc
```

Cleaner, read-only documentation format.

### API Root

```
http://localhost:8000/
```

Returns service information and available endpoints.

## Testing Endpoints

### Using cURL

#### Get all programs
```bash
curl http://localhost:8000/api/programs
```

#### Get online programs only
```bash
curl "http://localhost:8000/api/programs?type=online"
```

#### Get a specific program
```bash
curl http://localhost:8000/api/programs/imba
```

#### Search for faculty
```bash
curl "http://localhost:8000/api/faculty?research_area=sustainable"
```

#### Universal search
```bash
curl "http://localhost:8000/api/search?q=finance"
```

#### Get departments
```bash
curl http://localhost:8000/api/departments
```

#### Get news
```bash
curl http://localhost:8000/api/news
```

#### Health check
```bash
curl http://localhost:8000/health
```

### Using Python

```python
import requests

# Get all programs
response = requests.get("http://localhost:8000/api/programs")
programs = response.json()
print(f"Found {programs['count']} programs")

# Search
response = requests.get(
    "http://localhost:8000/api/search",
    params={"q": "finance"}
)
results = response.json()
print(f"Total results: {results['totalResults']}")

# Get specific program
response = requests.get("http://localhost:8000/api/programs/imba")
program = response.json()
print(f"Program: {program['name']}")
print(f"Rankings: {program['rankings']}")
```

### Using JavaScript (Node.js)

```javascript
const fetch = require('node-fetch');

// Get all programs
fetch('http://localhost:8000/api/programs')
  .then(res => res.json())
  .then(data => {
    console.log(`Found ${data.count} programs`);
  });

// Search
fetch('http://localhost:8000/api/search?q=finance')
  .then(res => res.json())
  .then(data => {
    console.log(`Total results: ${data.totalResults}`);
  });
```

## Demo Scenarios

### Scenario 1: Prospective Student

**Goal:** Find information about online MBA programs

**Steps:**
1. Open http://localhost:8000/docs
2. Find `GET /api/programs`
3. Click "Try it out"
4. Set `type` parameter to `online`
5. Set `level` parameter to `graduate`
6. Click "Execute"
7. Review structured response

**What to show:**
- Fast response time
- Structured JSON data
- Complete information in one call
- Easy to filter and query

### Scenario 2: Research Discovery

**Goal:** Find faculty researching sustainable finance

**Steps:**
1. Open http://localhost:8000/docs
2. Find `GET /api/faculty`
3. Click "Try it out"
4. Set `research_area` to `sustainable`
5. Click "Execute"
6. Review faculty profiles with publications

**What to show:**
- Targeted search
- Research areas clearly listed
- Publications included
- Contact information available

### Scenario 3: Comparative Analysis

**Goal:** Compare two programs

**Steps:**
1. Get program 1: `GET /api/programs/imba`
2. Get program 2: `GET /api/programs/mba`
3. Compare structured fields side-by-side

**What to show:**
- Consistent data structure
- Easy comparison
- All relevant information
- Linked entities (department, faculty)

### Scenario 4: Universal Search

**Goal:** Find all finance-related content

**Steps:**
1. Open http://localhost:8000/docs
2. Find `GET /api/search`
3. Enter `finance` as query
4. Execute
5. Review results across all entity types

**What to show:**
- Single query searches everything
- Results organized by type
- Comprehensive coverage
- Relevance ranking

## Presentation Tips

### Before Starting
1. Have browser tabs ready:
   - http://localhost:8000/docs
   - http://localhost:8000/redoc
   - https://giesbusiness.illinois.edu (for comparison)

2. Have code examples ready in editor

3. Test all endpoints beforehand

### During Presentation

**Opening (2 min):**
- Show traditional website
- Demonstrate navigation challenges
- Explain agent difficulties

**Demo (5 min):**
- Show API docs (auto-generated!)
- Execute 2-3 example queries
- Highlight response speed
- Show structured data

**Comparison (3 min):**
- Side-by-side: web scraping code vs API call
- Emphasize simplicity
- Show reliability difference

**Business Case (5 min):**
- Explain benefits
- Show metrics (speed, reliability)
- Discuss implementation path

**Q&A (5 min):**
- Address concerns
- Discuss next steps

### Key Points to Emphasize

1. **Speed**: <200ms vs 5-10 seconds
2. **Reliability**: 99%+ vs ~70%
3. **Simplicity**: Single API call vs complex scraping
4. **Structured Data**: JSON vs HTML parsing
5. **Auto-Documentation**: Built-in, always current
6. **Feasibility**: Built in hours without backend access

## Troubleshooting

### Port Already in Use

```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn main:app --port 8001
```

### Module Not Found

```bash
# Reinstall dependencies
pip install -r api/requirements.txt

# Or install individually
pip install fastapi uvicorn pydantic
```

### Data Files Not Found

```bash
# Regenerate data files
python scrapers/scrape_gies.py

# Verify they exist
ls -la data/structured/
```

### CORS Issues (Browser)

CORS is already enabled in the API. If you still have issues:
1. Use the interactive docs at /docs
2. Or add credentials to your request
3. Or use a tool like Postman instead of browser

## Next Steps After Demo

1. **Gather Feedback**
   - What content areas are most important?
   - What queries would be most valuable?
   - Who are the key stakeholders?

2. **Plan Pilot**
   - Scope: Which entities first?
   - Timeline: 4-6 weeks realistic?
   - Resources: Who will build/maintain?

3. **Technical Decisions**
   - CMS integration approach
   - Hosting infrastructure
   - Authentication requirements
   - Analytics tracking

4. **Launch Strategy**
   - Internal testing phase
   - Soft launch to select users
   - Promotion to AI platforms
   - Full public launch

## Additional Resources

- **API Documentation**: See `docs/API.md`
- **Examples**: See `docs/EXAMPLES.md`
- **Schemas**: See `docs/SCHEMAS.md`
- **Presentation**: See `PRESENTATION.md`
- **Agent Queries**: See `examples/agent-queries.md`

## Questions?

For technical questions about this demo:
- Review the code in `api/main.py`
- Check the documentation in `docs/`
- Examine the data in `data/structured/`

For business questions:
- See `PRESENTATION.md` for the full business case
- Review success metrics and ROI estimates
- Consider the competitive landscape

---

**Ready to Transform Gies Business School?**

This demo proves it's possible, valuable, and straightforward. Let's make it happen!
