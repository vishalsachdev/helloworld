# Quick Start Guide

Get the Gies Business School Agent-Friendly API demo running in 5 minutes.

## TL;DR

```bash
# 1. Install dependencies
pip install -r api/requirements.txt

# 2. Start API server
cd api && python main.py

# 3. Open browser
# Visit: http://localhost:8000/docs
```

## What You'll See

### Interactive API Documentation
Navigate to http://localhost:8000/docs for:
- Complete API reference
- Try-it-out functionality
- Request/response examples
- Schema documentation

### Available Endpoints

**Programs:**
- `GET /api/programs` - List all programs (filterable)
- `GET /api/programs/{id}` - Get program details
- `GET /api/programs/{id}/faculty` - Get program faculty

**Faculty:**
- `GET /api/faculty` - List all faculty (filterable)
- `GET /api/faculty/{id}` - Get faculty details
- `GET /api/faculty/{id}/publications` - Get publications

**Departments:**
- `GET /api/departments` - List all departments
- `GET /api/departments/{id}` - Get department details
- `GET /api/departments/{id}/programs` - Get department programs
- `GET /api/departments/{id}/faculty` - Get department faculty

**Search:**
- `GET /api/search?q={query}` - Universal search

**Other:**
- `GET /api/news` - Get recent news
- `GET /api/metadata` - Get API metadata
- `GET /health` - Health check

## Example Queries

### Find Online Programs
```bash
curl "http://localhost:8000/api/programs?type=online"
```

### Get iMBA Details
```bash
curl "http://localhost:8000/api/programs/imba"
```

### Search for Sustainable Finance Faculty
```bash
curl "http://localhost:8000/api/faculty?research_area=sustainable"
```

### Universal Search
```bash
curl "http://localhost:8000/api/search?q=finance"
```

## Sample Data Included

- **7 Programs** (Undergraduate, Graduate, Online)
- **5 Faculty Members** (With publications and research areas)
- **3 Departments** (Accountancy, Finance, Business Admin)
- **3 News Articles** (Recent announcements)

## Project Structure

```
/
├── api/                    # FastAPI server
│   ├── main.py            # Main application
│   └── requirements.txt   # Dependencies
├── data/
│   ├── structured/        # JSON data files
│   └── schemas/          # JSON schemas
├── scrapers/              # Data extraction
├── docs/                  # Documentation
├── examples/              # Usage examples
├── README.md              # Main documentation
├── PRESENTATION.md        # Business pitch
└── DEMO.md               # Demo guide
```

## Key Features Demonstrated

1. **Structured Data** - Clean JSON vs messy HTML
2. **Fast Responses** - <200ms vs 5-10 seconds
3. **Auto-Documentation** - Swagger UI built-in
4. **Filtering** - Query exactly what you need
5. **Search** - Universal search across all content
6. **Linked Entities** - Programs ↔ Faculty ↔ Departments

## What This Proves

1. **Feasible** - Built without backend access
2. **Fast** - Ready in hours, not months
3. **Valuable** - Dramatically better agent experience
4. **Strategic** - Future-proof for AI era

## Next Steps

1. **Explore** - Try the interactive docs
2. **Review** - Read PRESENTATION.md for business case
3. **Discuss** - Share with stakeholders
4. **Plan** - Consider implementation path

## Questions?

- **Technical**: See `docs/API.md`
- **Examples**: See `docs/EXAMPLES.md`
- **Business Case**: See `PRESENTATION.md`
- **Full Demo**: See `DEMO.md`

---

**Ready to make Gies Business School agent-friendly?**

This demo proves it's possible. Let's make it happen!
