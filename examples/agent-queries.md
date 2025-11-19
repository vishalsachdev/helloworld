# Agent Query Examples

Real-world examples of how AI agents can interact with the Gies Business School API.

---

## Query 1: Program Discovery

**User:** "What online graduate programs does Gies offer?"

**Agent Code:**
```python
import requests

response = requests.get(
    "http://localhost:8000/api/programs",
    params={"type": "online", "level": "graduate"}
)

programs = response.json()['programs']

for program in programs:
    print(f"• {program['name']}")
    print(f"  Duration: {program['duration']}")
    print(f"  Cost: {program['tuition']}")
    if program['rankings']:
        print(f"  Ranking: {program['rankings'][0]}")
    print()
```

**Agent Response:**
> "Gies offers three online graduate programs:
>
> 1. **iMBA (Online MBA)** - 24-36 months, $22,000-28,000
>    - Ranked #1 Online MBA by U.S. News
>
> 2. **iMSA (Master of Science in Accountancy)** - 18-24 months, $19,000-23,000
>    - From the #1 ranked Accounting program
>
> 3. **iMSM (Master of Science in Management)** - 12-18 months, $18,000-22,000
>    - No prior business degree required
>
> All three are fully online and asynchronous."

---

## Query 2: Faculty Research

**User:** "Find professors studying sustainable finance"

**Agent Code:**
```python
response = requests.get(
    "http://localhost:8000/api/faculty",
    params={"research_area": "sustainable"}
)

faculty = response.json()['faculty']

for member in faculty:
    print(f"{member['name']} - {member['title']}")
    print(f"Research: {', '.join(member['researchAreas'])}")

    if member.get('publications'):
        recent = member['publications'][0]
        print(f"Recent: '{recent['title']}' ({recent['year']})")
    print()
```

**Agent Response:**
> "I found Dr. Raj Patel, a Professor of Finance specializing in:
> - Sustainable Finance
> - ESG Investing
> - Impact Investing
>
> His recent publication 'ESG Factors and Stock Returns' (2024) in the Journal of Financial Economics has 120 citations.
>
> Contact: rpatel@illinois.edu"

---

## Query 3: Admission Requirements

**User:** "What do I need to apply to the iMBA program?"

**Agent Code:**
```python
response = requests.get("http://localhost:8000/api/programs/imba")
program = response.json()

print(f"{program['name']}\n")
print("Admission Requirements:")
for req in program['admissions']['requirements']:
    print(f"  ✓ {req}")

print("\nApplication Deadlines:")
for term, deadline in program['admissions']['applicationDeadlines'].items():
    print(f"  • {term.capitalize()}: {deadline}")

print(f"\nApply at: {program['admissions']['applicationUrl']}")
```

**Agent Response:**
> "To apply to the iMBA (Online MBA) program, you need:
>
> ✓ Bachelor's degree from an accredited institution
> ✓ GMAT or GRE score
> ✓ Professional experience (recommended)
> ✓ English proficiency (TOEFL/IELTS for international students)
>
> Application Deadlines:
> • Fall: April 15
> • Spring: October 15
>
> Apply at: https://giesbusiness.illinois.edu/imba/admissions"

---

## Query 4: Department Information

**User:** "Tell me about the Finance department at Gies"

**Agent Code:**
```python
# Get department info
dept = requests.get(
    "http://localhost:8000/api/departments/finance"
).json()

# Get department faculty
faculty = requests.get(
    "http://localhost:8000/api/departments/finance/faculty"
).json()

# Get department programs
programs = requests.get(
    "http://localhost:8000/api/departments/finance/programs"
).json()

print(f"{dept['name']}\n")
print(f"{dept['description']}\n")
print(f"Department Head: {dept['head']}")
print(f"Faculty: {faculty['facultyCount']} members")
print(f"Programs: {programs['programCount']}")
```

**Agent Response:**
> "The Department of Finance at Gies offers cutting-edge research and education in corporate finance, investments, and financial markets.
>
> Led by Dr. John Smith, the department has 20 faculty members and offers two programs:
> - Bachelor of Science in Finance (undergraduate)
> - Master of Science in Finance (graduate)
>
> The department is home to the Center for Financial Innovation."

---

## Query 5: Comparative Analysis

**User:** "Compare the undergraduate and graduate finance programs"

**Agent Code:**
```python
undergrad = requests.get(
    "http://localhost:8000/api/programs/finance-bs"
).json()

graduate = requests.get(
    "http://localhost:8000/api/programs/msf"
).json()

comparison = [
    ["Aspect", "Undergraduate", "Graduate"],
    ["Duration", undergrad['duration'], graduate['duration']],
    ["Format", undergrad['format'], graduate['format']],
    ["Cost", undergrad['tuition'], graduate['tuition']],
]

# Print as table
for row in comparison:
    print(f"{row[0]:15} | {row[1]:25} | {row[2]:25}")
```

**Agent Response:**
> "Here's a comparison of Gies Finance programs:
>
> | Aspect | Undergraduate | Graduate |
> |--------|--------------|----------|
> | Duration | 4 years | 12-18 months |
> | Format | On-campus, full-time | On-campus, full-time |
> | Cost | Varies by residency | $35,000-45,000 |
>
> Both offer Bloomberg Terminal access and trading simulations. The BS in Finance is ranked #12 nationally for undergraduate business. The MSF is aligned with the CFA curriculum and targets students with 0-2 years of experience."

---

## Query 6: Universal Search

**User:** "Find everything related to accounting"

**Agent Code:**
```python
response = requests.get(
    "http://localhost:8000/api/search",
    params={"q": "accounting"}
)

results = response.json()

print(f"Found {results['totalResults']} total results\n")

for entity_type, data in results['results'].items():
    if data['count'] > 0:
        print(f"{entity_type.upper()} ({data['count']} results):")
        for item in data['items'][:3]:  # Show first 3
            print(f"  • {item.get('name') or item.get('title')}")
        print()
```

**Agent Response:**
> "Found 5 results for 'accounting':
>
> PROGRAMS (2 results):
> • Bachelor of Science in Accountancy
> • iMSA (Master of Science in Accountancy)
>
> FACULTY (2 results):
> • Dr. Sarah Johnson - Associate Professor of Accountancy
> • Dr. Mary Williams - Clinical Professor of Accountancy
>
> DEPARTMENTS (1 result):
> • Department of Accountancy - Ranked #1 nationally"

---

## Query 7: Recent News

**User:** "What's new at Gies?"

**Agent Code:**
```python
response = requests.get(
    "http://localhost:8000/api/news",
    params={"limit": 3}
)

news = response.json()['news']

for article in news:
    print(f"📰 {article['title']}")
    print(f"   {article['date']} | {article['category']}")
    print(f"   {article['summary']}\n")
```

**Agent Response:**
> "Here's the latest from Gies Business School:
>
> 📰 New Research on E-Scooter Safety Published
>    2024-11-10 | Research
>    Gies faculty publish groundbreaking study on e-scooter rollout and urban safety implications.
>
> 📰 Finance Students Win National Trading Competition
>    2024-10-28 | Student Achievement
>    Gies Finance students take first place in the National Investment Banking Competition.
>
> 📰 Gies iMBA Program Ranked #1 Online MBA
>    2024-01-15 | Rankings
>    U.S. News & World Report has ranked the Gies iMBA program as the #1 online MBA."

---

## Query 8: Faculty Publications

**User:** "Show me Dr. John Smith's recent publications"

**Agent Code:**
```python
# Get publications
response = requests.get(
    "http://localhost:8000/api/faculty/smith-john/publications"
)

data = response.json()

print(f"{data['name']} has {data['publicationCount']} publications:\n")

for pub in data['publications']:
    print(f"'{pub['title']}'")
    print(f"{pub['journal']}, {pub['year']}")
    print(f"Citations: {pub['citations']}\n")
```

**Agent Response:**
> "Dr. John Smith has 2 publications:
>
> 'The Impact of M&A on Firm Value'
> Journal of Finance, 2023
> Citations: 150
>
> 'Capital Structure Decisions in Emerging Markets'
> Review of Financial Studies, 2022
> Citations: 95"

---

## Query 9: Multi-Hop Reasoning

**User:** "Which programs offer courses taught by Dr. Sarah Johnson?"

**Agent Code:**
```python
# Get faculty member
faculty = requests.get(
    "http://localhost:8000/api/faculty/johnson-sarah"
).json()

# Get programs in that department
programs = requests.get(
    "http://localhost:8000/api/programs",
    params={"department": faculty['department']}
).json()

print(f"Dr. {faculty['name']} teaches in the {faculty['department']} department.\n")
print("Programs that may include her courses:")
for program in programs['programs']:
    print(f"  • {program['name']} ({program['level']})")
```

**Agent Response:**
> "Dr. Sarah Johnson teaches in the accountancy department. She teaches ACCY 201, ACCY 405, and ACCY 570.
>
> Programs that include her courses:
> • Bachelor of Science in Accountancy (undergraduate)
> • iMSA - Master of Science in Accountancy (graduate/online)
>
> As an Associate Professor specializing in Financial Reporting and Audit Quality, she contributes to both undergraduate and graduate accounting education."

---

## Query 10: Complex Filtering

**User:** "Find all on-campus graduate programs"

**Agent Code:**
```python
response = requests.get(
    "http://localhost:8000/api/programs",
    params={
        "type": "on-campus",
        "level": "graduate"
    }
)

programs = response.json()['programs']

print(f"Found {len(programs)} on-campus graduate programs:\n")

for program in programs:
    print(f"{program['name']}")
    print(f"  Department: {program['department']}")
    print(f"  Duration: {program['duration']}")
    print(f"  Cost: {program['tuition']}\n")
```

**Agent Response:**
> "Found 2 on-campus graduate programs:
>
> MBA (Master of Business Administration)
>   Department: business-administration
>   Duration: 2 years
>   Cost: $30,000-40,000 per year
>
> MSF (Master of Science in Finance)
>   Department: finance
>   Duration: 12-18 months
>   Cost: $35,000-45,000 total program"

---

## Testing the API

### Health Check
```bash
curl http://localhost:8000/health
```

### Get All Programs
```bash
curl http://localhost:8000/api/programs
```

### Search
```bash
curl "http://localhost:8000/api/search?q=finance"
```

### Filter Faculty
```bash
curl "http://localhost:8000/api/faculty?department=finance"
```

---

## Python Helper Class

For easier agent integration:

```python
class GiesAPI:
    """Helper class for Gies Business School API"""

    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def get_programs(self, **filters):
        """Get programs with optional filters"""
        response = requests.get(f"{self.base_url}/api/programs", params=filters)
        return response.json()

    def get_program(self, program_id):
        """Get specific program"""
        response = requests.get(f"{self.base_url}/api/programs/{program_id}")
        return response.json()

    def get_faculty(self, **filters):
        """Get faculty with optional filters"""
        response = requests.get(f"{self.base_url}/api/faculty", params=filters)
        return response.json()

    def search(self, query, entity=None):
        """Search across all content"""
        params = {"q": query}
        if entity:
            params["entity"] = entity
        response = requests.get(f"{self.base_url}/api/search", params=params)
        return response.json()

# Usage
api = GiesAPI()
programs = api.get_programs(type="online")
results = api.search("sustainable finance")
```

---

## Conclusion

These examples demonstrate how AI agents can efficiently access Gies Business School data through the API, providing fast, accurate responses to user queries.

The API transforms what would be complex web scraping into simple, reliable function calls.
