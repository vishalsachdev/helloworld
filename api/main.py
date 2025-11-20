"""
Gies Business School Agent-Friendly API
FastAPI demo server showcasing structured data access
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Dict, Any, Optional
import json
import os
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Gies Business School Agent API",
    description="LLM-friendly API providing structured access to Gies College of Business data. "
                "This demo showcases how website content can be made agent-accessible through "
                "clean APIs, structured data, and comprehensive documentation.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from JSON files
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "structured")


def load_json(filename: str) -> Any:
    """Load JSON data from file"""
    filepath = os.path.join(DATA_DIR, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# Load all data at startup
programs_data = load_json("programs.json")
faculty_data = load_json("faculty.json")
departments_data = load_json("departments.json")
news_data = load_json("news.json")


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """
    API root endpoint with service information and links
    """
    return {
        "service": "Gies Business School Agent API",
        "version": "1.0.0",
        "description": "Agent-friendly API for Gies College of Business",
        "documentation": {
            "interactive": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json"
        },
        "endpoints": {
            "programs": "/api/programs",
            "faculty": "/api/faculty",
            "departments": "/api/departments",
            "news": "/api/news",
            "search": "/api/search",
            "metadata": "/api/metadata"
        },
        "features": [
            "Structured JSON responses",
            "Advanced filtering",
            "Full-text search",
            "OpenAPI documentation",
            "CORS enabled"
        ],
        "timestamp": datetime.now().isoformat()
    }


# Metadata endpoint
@app.get("/api/metadata", tags=["Meta"])
async def get_metadata():
    """
    Get API metadata and capabilities
    """
    return {
        "name": "Gies Business Agent API",
        "version": "1.0.0",
        "description": "Proof-of-concept: Making Gies Business School agent-friendly",
        "baseUrl": "http://localhost:8000",
        "capabilities": [
            "program-search",
            "faculty-directory",
            "department-lookup",
            "news-feed",
            "cross-entity-search"
        ],
        "dataStats": {
            "programs": len(programs_data),
            "faculty": len(faculty_data),
            "departments": len(departments_data),
            "news": len(news_data)
        },
        "endpoints": {
            "rest": "/api/",
            "docs": "/docs",
            "schemas": "/schemas/"
        },
        "rateLimit": {
            "requests": 100,
            "window": "60s",
            "note": "Demo has no actual rate limiting"
        },
        "contact": {
            "description": "This is a demonstration API",
            "repository": "https://github.com/yourusername/gies-agent-api"
        }
    }


# Programs endpoints
@app.get("/api/programs", tags=["Programs"])
async def get_programs(
    type: Optional[str] = Query(None, description="Filter by program type (online, on-campus, hybrid)"),
    level: Optional[str] = Query(None, description="Filter by level (undergraduate, graduate, doctoral)"),
    department: Optional[str] = Query(None, description="Filter by department"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    offset: Optional[int] = Query(0, description="Offset for pagination")
):
    """
    Get all academic programs with optional filtering

    Example queries:
    - `/api/programs?type=online` - All online programs
    - `/api/programs?level=graduate` - All graduate programs
    - `/api/programs?department=finance` - All finance programs
    - `/api/programs?type=online&level=graduate` - Online graduate programs
    """
    results = programs_data.copy()

    # Apply filters
    if type:
        results = [p for p in results if p.get('type') == type]
    if level:
        results = [p for p in results if p.get('level') == level]
    if department:
        results = [p for p in results if p.get('department') == department]

    # Apply pagination
    total = len(results)
    if limit:
        results = results[offset:offset + limit]
    else:
        results = results[offset:]

    return {
        "count": len(results),
        "total": total,
        "offset": offset,
        "programs": results
    }


@app.get("/api/programs/{program_id}", tags=["Programs"])
async def get_program(program_id: str):
    """
    Get detailed information about a specific program

    Example: `/api/programs/imba`
    """
    program = next((p for p in programs_data if p['id'] == program_id), None)

    if not program:
        raise HTTPException(status_code=404, detail=f"Program '{program_id}' not found")

    return program


@app.get("/api/programs/{program_id}/faculty", tags=["Programs"])
async def get_program_faculty(program_id: str):
    """
    Get faculty associated with a specific program

    Links faculty members who teach in this program's department
    """
    program = next((p for p in programs_data if p['id'] == program_id), None)

    if not program:
        raise HTTPException(status_code=404, detail=f"Program '{program_id}' not found")

    # Find faculty in the same department
    program_dept = program.get('department')
    related_faculty = [f for f in faculty_data if f.get('department') == program_dept]

    return {
        "program": program_id,
        "department": program_dept,
        "facultyCount": len(related_faculty),
        "faculty": related_faculty
    }


# Faculty endpoints
@app.get("/api/faculty", tags=["Faculty"])
async def get_faculty(
    department: Optional[str] = Query(None, description="Filter by department"),
    research_area: Optional[str] = Query(None, description="Filter by research area (partial match)"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    offset: Optional[int] = Query(0, description="Offset for pagination")
):
    """
    Get faculty directory with optional filtering

    Example queries:
    - `/api/faculty?department=finance` - All finance faculty
    - `/api/faculty?research_area=sustainable` - Faculty researching sustainability
    """
    results = faculty_data.copy()

    # Apply filters
    if department:
        results = [f for f in results if f.get('department') == department]

    if research_area:
        results = [
            f for f in results
            if any(research_area.lower() in area.lower() for area in f.get('researchAreas', []))
        ]

    # Apply pagination
    total = len(results)
    if limit:
        results = results[offset:offset + limit]
    else:
        results = results[offset:]

    return {
        "count": len(results),
        "total": total,
        "offset": offset,
        "faculty": results
    }


@app.get("/api/faculty/{faculty_id}", tags=["Faculty"])
async def get_faculty_member(faculty_id: str):
    """
    Get detailed information about a specific faculty member

    Example: `/api/faculty/smith-john`
    """
    faculty = next((f for f in faculty_data if f['id'] == faculty_id), None)

    if not faculty:
        raise HTTPException(status_code=404, detail=f"Faculty member '{faculty_id}' not found")

    return faculty


@app.get("/api/faculty/{faculty_id}/publications", tags=["Faculty"])
async def get_faculty_publications(faculty_id: str):
    """
    Get publications for a specific faculty member
    """
    faculty = next((f for f in faculty_data if f['id'] == faculty_id), None)

    if not faculty:
        raise HTTPException(status_code=404, detail=f"Faculty member '{faculty_id}' not found")

    return {
        "facultyId": faculty_id,
        "name": faculty.get('name'),
        "publicationCount": len(faculty.get('publications', [])),
        "publications": faculty.get('publications', [])
    }


# Department endpoints
@app.get("/api/departments", tags=["Departments"])
async def get_departments():
    """
    Get all departments
    """
    return {
        "count": len(departments_data),
        "departments": departments_data
    }


@app.get("/api/departments/{department_id}", tags=["Departments"])
async def get_department(department_id: str):
    """
    Get detailed information about a specific department

    Example: `/api/departments/finance`
    """
    department = next((d for d in departments_data if d['id'] == department_id), None)

    if not department:
        raise HTTPException(status_code=404, detail=f"Department '{department_id}' not found")

    return department


@app.get("/api/departments/{department_id}/programs", tags=["Departments"])
async def get_department_programs(department_id: str):
    """
    Get all programs offered by a specific department
    """
    department = next((d for d in departments_data if d['id'] == department_id), None)

    if not department:
        raise HTTPException(status_code=404, detail=f"Department '{department_id}' not found")

    # Find programs in this department
    dept_programs = [p for p in programs_data if p.get('department') == department_id]

    return {
        "department": department_id,
        "programCount": len(dept_programs),
        "programs": dept_programs
    }


@app.get("/api/departments/{department_id}/faculty", tags=["Departments"])
async def get_department_faculty(department_id: str):
    """
    Get all faculty in a specific department
    """
    department = next((d for d in departments_data if d['id'] == department_id), None)

    if not department:
        raise HTTPException(status_code=404, detail=f"Department '{department_id}' not found")

    # Find faculty in this department
    dept_faculty = [f for f in faculty_data if f.get('department') == department_id]

    return {
        "department": department_id,
        "facultyCount": len(dept_faculty),
        "faculty": dept_faculty
    }


# News endpoints
@app.get("/api/news", tags=["News"])
async def get_news(
    category: Optional[str] = Query(None, description="Filter by category"),
    limit: Optional[int] = Query(10, description="Limit number of results"),
    offset: Optional[int] = Query(0, description="Offset for pagination")
):
    """
    Get recent news articles

    Example: `/api/news?category=Research&limit=5`
    """
    results = news_data.copy()

    # Apply filters
    if category:
        results = [n for n in results if n.get('category') == category]

    # Sort by date (most recent first)
    results.sort(key=lambda x: x.get('date', ''), reverse=True)

    # Apply pagination
    total = len(results)
    results = results[offset:offset + limit]

    return {
        "count": len(results),
        "total": total,
        "offset": offset,
        "news": results
    }


@app.get("/api/news/{news_id}", tags=["News"])
async def get_news_item(news_id: str):
    """
    Get a specific news article
    """
    article = next((n for n in news_data if n['id'] == news_id), None)

    if not article:
        raise HTTPException(status_code=404, detail=f"News article '{news_id}' not found")

    return article


# Search endpoint
@app.get("/api/search", tags=["Search"])
async def search(
    q: str = Query(..., description="Search query"),
    entity: Optional[str] = Query(None, description="Entity type to search (programs, faculty, departments, news)")
):
    """
    Universal search across all content

    Searches through programs, faculty, departments, and news for matching content.

    Example: `/api/search?q=finance`
    Example: `/api/search?q=online&entity=programs`
    """
    if not q or len(q) < 2:
        raise HTTPException(status_code=400, detail="Query must be at least 2 characters")

    q_lower = q.lower()
    results = {
        "query": q,
        "results": {}
    }

    # Search programs
    if not entity or entity == "programs":
        program_matches = []
        for p in programs_data:
            if (q_lower in p.get('name', '').lower() or
                q_lower in p.get('description', '').lower() or
                q_lower in p.get('department', '').lower()):
                program_matches.append(p)
        results["results"]["programs"] = {
            "count": len(program_matches),
            "items": program_matches
        }

    # Search faculty
    if not entity or entity == "faculty":
        faculty_matches = []
        for f in faculty_data:
            if (q_lower in f.get('name', '').lower() or
                q_lower in f.get('bio', '').lower() or
                any(q_lower in area.lower() for area in f.get('researchAreas', []))):
                faculty_matches.append(f)
        results["results"]["faculty"] = {
            "count": len(faculty_matches),
            "items": faculty_matches
        }

    # Search departments
    if not entity or entity == "departments":
        dept_matches = []
        for d in departments_data:
            if (q_lower in d.get('name', '').lower() or
                q_lower in d.get('description', '').lower()):
                dept_matches.append(d)
        results["results"]["departments"] = {
            "count": len(dept_matches),
            "items": dept_matches
        }

    # Search news
    if not entity or entity == "news":
        news_matches = []
        for n in news_data:
            if (q_lower in n.get('title', '').lower() or
                q_lower in n.get('summary', '').lower()):
                news_matches.append(n)
        results["results"]["news"] = {
            "count": len(news_matches),
            "items": news_matches
        }

    # Calculate total results
    total = sum(r["count"] for r in results["results"].values())
    results["totalResults"] = total

    return results


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint for monitoring
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "dataLoaded": {
            "programs": len(programs_data) > 0,
            "faculty": len(faculty_data) > 0,
            "departments": len(departments_data) > 0,
            "news": len(news_data) > 0
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
