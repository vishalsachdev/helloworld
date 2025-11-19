# API Reference

Complete reference for the Gies Business School Agent-Friendly API.

## Base URL

```
http://localhost:8000
```

## Response Format

All API responses follow this structure:

```json
{
  "count": 10,
  "total": 50,
  "offset": 0,
  "results": [ ... ]
}
```

Or for single resources:

```json
{
  "id": "...",
  "name": "...",
  ...
}
```

## Authentication

Currently, this demo API does not require authentication. In production, consider implementing:
- API keys
- OAuth 2.0
- JWT tokens

## Rate Limiting

Demo has no rate limiting. Production should implement:
- 100 requests per minute per IP
- 1000 requests per hour per API key

---

## Endpoints

### Root

#### `GET /`

Get API service information and available endpoints.

**Response:**
```json
{
  "service": "Gies Business School Agent API",
  "version": "1.0.0",
  "documentation": {
    "interactive": "/docs",
    "redoc": "/redoc"
  },
  "endpoints": { ... }
}
```

---

### Programs

#### `GET /api/programs`

Get all academic programs with optional filtering.

**Query Parameters:**
- `type` (string, optional): Filter by program type (`online`, `on-campus`, `hybrid`)
- `level` (string, optional): Filter by level (`undergraduate`, `graduate`, `doctoral`)
- `department` (string, optional): Filter by department
- `limit` (integer, optional): Limit number of results
- `offset` (integer, optional): Pagination offset (default: 0)

**Examples:**
```bash
# Get all programs
GET /api/programs

# Get online programs only
GET /api/programs?type=online

# Get graduate programs in finance
GET /api/programs?level=graduate&department=finance

# Pagination
GET /api/programs?limit=5&offset=10
```

**Response:**
```json
{
  "count": 3,
  "total": 7,
  "offset": 0,
  "programs": [
    {
      "id": "imba",
      "name": "iMBA (Online Master of Business Administration)",
      "type": "online",
      "level": "graduate",
      "department": "business-administration",
      "description": "...",
      "admissions": { ... },
      "rankings": [ ... ]
    }
  ]
}
```

#### `GET /api/programs/{program_id}`

Get detailed information about a specific program.

**Path Parameters:**
- `program_id` (string, required): Program identifier (e.g., `imba`, `accountancy-bs`)

**Example:**
```bash
GET /api/programs/imba
```

**Response:**
```json
{
  "id": "imba",
  "name": "iMBA (Online Master of Business Administration)",
  "type": "online",
  "level": "graduate",
  "department": "business-administration",
  "description": "The iMBA program...",
  "url": "https://giesbusiness.illinois.edu/imba",
  "admissions": {
    "requirements": [
      "Bachelor's degree from accredited institution",
      "GMAT or GRE score",
      "Professional experience recommended"
    ],
    "applicationDeadlines": {
      "fall": "April 15",
      "spring": "October 15"
    },
    "applicationUrl": "..."
  },
  "tuition": "$22,000-28,000 total program cost",
  "duration": "24-36 months",
  "rankings": ["#1 Online MBA (U.S. News & World Report)"],
  "highlights": [ ... ]
}
```

**Error Response (404):**
```json
{
  "detail": "Program 'xyz' not found"
}
```

#### `GET /api/programs/{program_id}/faculty`

Get faculty associated with a specific program.

**Example:**
```bash
GET /api/programs/imba/faculty
```

**Response:**
```json
{
  "program": "imba",
  "department": "business-administration",
  "facultyCount": 2,
  "faculty": [ ... ]
}
```

---

### Faculty

#### `GET /api/faculty`

Get faculty directory with optional filtering.

**Query Parameters:**
- `department` (string, optional): Filter by department
- `research_area` (string, optional): Filter by research area (partial match)
- `limit` (integer, optional): Limit number of results
- `offset` (integer, optional): Pagination offset

**Examples:**
```bash
# Get all faculty
GET /api/faculty

# Get finance faculty
GET /api/faculty?department=finance

# Search by research area
GET /api/faculty?research_area=sustainable
```

**Response:**
```json
{
  "count": 2,
  "total": 5,
  "offset": 0,
  "faculty": [
    {
      "id": "patel-raj",
      "name": "Dr. Raj Patel",
      "title": "Professor of Finance",
      "department": "finance",
      "email": "rpatel@illinois.edu",
      "researchAreas": [
        "Sustainable Finance",
        "ESG Investing"
      ],
      "publications": [ ... ]
    }
  ]
}
```

#### `GET /api/faculty/{faculty_id}`

Get detailed information about a specific faculty member.

**Example:**
```bash
GET /api/faculty/smith-john
```

**Response:**
```json
{
  "id": "smith-john",
  "name": "Dr. John Smith",
  "title": "Professor of Finance",
  "department": "finance",
  "email": "jsmith@illinois.edu",
  "phone": "217-333-0001",
  "office": "BIF 4025",
  "researchAreas": [
    "Corporate Finance",
    "Mergers & Acquisitions"
  ],
  "education": [
    {
      "degree": "PhD",
      "field": "Finance",
      "institution": "University of Chicago",
      "year": 2005
    }
  ],
  "publications": [ ... ],
  "courses": ["FIN 300", "FIN 450"],
  "bio": "..."
}
```

#### `GET /api/faculty/{faculty_id}/publications`

Get publications for a specific faculty member.

**Example:**
```bash
GET /api/faculty/smith-john/publications
```

**Response:**
```json
{
  "facultyId": "smith-john",
  "name": "Dr. John Smith",
  "publicationCount": 2,
  "publications": [
    {
      "title": "The Impact of M&A on Firm Value",
      "journal": "Journal of Finance",
      "year": 2023,
      "citations": 150
    }
  ]
}
```

---

### Departments

#### `GET /api/departments`

Get all departments.

**Example:**
```bash
GET /api/departments
```

**Response:**
```json
{
  "count": 3,
  "departments": [
    {
      "id": "accountancy",
      "name": "Department of Accountancy",
      "description": "...",
      "head": "Dr. Mary Williams",
      "facultyCount": 25,
      "programs": ["accountancy-bs", "imsa"],
      "rankings": ["#1 Accounting Faculty"]
    }
  ]
}
```

#### `GET /api/departments/{department_id}`

Get detailed information about a specific department.

**Example:**
```bash
GET /api/departments/finance
```

#### `GET /api/departments/{department_id}/programs`

Get all programs offered by a department.

**Example:**
```bash
GET /api/departments/finance/programs
```

**Response:**
```json
{
  "department": "finance",
  "programCount": 2,
  "programs": [ ... ]
}
```

#### `GET /api/departments/{department_id}/faculty`

Get all faculty in a department.

**Example:**
```bash
GET /api/departments/finance/faculty
```

---

### News

#### `GET /api/news`

Get recent news articles.

**Query Parameters:**
- `category` (string, optional): Filter by category
- `limit` (integer, optional): Limit results (default: 10)
- `offset` (integer, optional): Pagination offset

**Example:**
```bash
GET /api/news?category=Research&limit=5
```

**Response:**
```json
{
  "count": 2,
  "total": 3,
  "offset": 0,
  "news": [
    {
      "id": "news-001",
      "title": "Gies iMBA Program Ranked #1 Online MBA",
      "date": "2024-01-15",
      "category": "Rankings",
      "summary": "...",
      "url": "...",
      "tags": ["rankings", "imba"]
    }
  ]
}
```

#### `GET /api/news/{news_id}`

Get a specific news article.

**Example:**
```bash
GET /api/news/news-001
```

---

### Search

#### `GET /api/search`

Universal search across all content.

**Query Parameters:**
- `q` (string, required): Search query (minimum 2 characters)
- `entity` (string, optional): Limit search to specific entity type (`programs`, `faculty`, `departments`, `news`)

**Examples:**
```bash
# Search everything
GET /api/search?q=finance

# Search only programs
GET /api/search?q=online&entity=programs

# Search faculty
GET /api/search?q=sustainable&entity=faculty
```

**Response:**
```json
{
  "query": "finance",
  "totalResults": 8,
  "results": {
    "programs": {
      "count": 3,
      "items": [ ... ]
    },
    "faculty": {
      "count": 4,
      "items": [ ... ]
    },
    "departments": {
      "count": 1,
      "items": [ ... ]
    },
    "news": {
      "count": 0,
      "items": []
    }
  }
}
```

**Error Response (400):**
```json
{
  "detail": "Query must be at least 2 characters"
}
```

---

### Metadata

#### `GET /api/metadata`

Get API metadata and capabilities.

**Example:**
```bash
GET /api/metadata
```

**Response:**
```json
{
  "name": "Gies Business Agent API",
  "version": "1.0.0",
  "description": "...",
  "capabilities": [
    "program-search",
    "faculty-directory",
    "cross-entity-search"
  ],
  "dataStats": {
    "programs": 7,
    "faculty": 5,
    "departments": 3,
    "news": 3
  }
}
```

---

### Health

#### `GET /health`

Health check endpoint for monitoring.

**Example:**
```bash
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-19T10:30:00Z",
  "dataLoaded": {
    "programs": true,
    "faculty": true,
    "departments": true,
    "news": true
  }
}
```

---

## Error Handling

### HTTP Status Codes

- `200 OK` - Success
- `400 Bad Request` - Invalid parameters
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

### Error Response Format

```json
{
  "detail": "Error message here"
}
```

---

## Best Practices

### For Agents

1. **Use specific endpoints** when you know what you need
   - `/api/programs/imba` vs `/api/search?q=imba`

2. **Apply filters** to reduce response size
   - `/api/programs?type=online&level=graduate`

3. **Implement pagination** for large result sets
   - Use `limit` and `offset` parameters

4. **Cache responses** when appropriate
   - Program data changes infrequently

5. **Handle errors gracefully**
   - Check for 404 on specific resource requests
   - Validate query parameters before sending

### Example Agent Flow

```
User: "What are the admission requirements for the iMBA program?"

Agent:
1. GET /api/programs/imba
2. Extract data.admissions.requirements
3. Format response for user
```

---

## Interactive Documentation

For interactive API exploration, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Spec**: http://localhost:8000/openapi.json
