# Twitter Follower Tracker

## Repo Type
type: code

## What This Is
A web application to track Twitter/X follower counts at 15-minute intervals with real-time visualization and historical data tracking.

## Parent Repo
- **Framework:** `/Users/vishal/code/helloworld` (experiment sandbox)
- **Branch:** `claude/twitter-follower-tracker-*` (detached HEAD from remote)
- **This is a git worktree**

## Key Files
| File | Purpose |
|------|---------|
| `twitter-tracker-api.py` | Python backend API server |
| `twitter-follower-tracker.html` | Frontend web application |
| `requirements.txt` | Python dependencies |
| `TWITTER_TRACKER_README.md` | Documentation |

## Quick Start
```bash
pip install -r requirements.txt
python twitter-tracker-api.py
# Server at http://localhost:5000
# Open twitter-follower-tracker.html in browser
```

## Status
Reference implementation - functional but not actively developed.

## Session Log
### 2025-12-27
- Initial roadmap sections added

## Git Workflow
```bash
# Note: This is a detached HEAD worktree
# Create a proper branch if making changes:
git checkout -b exp/twitter-tracker-updates
git add . && git commit -m "exp: twitter-tracker - <what you did>"
git push -u origin exp/twitter-tracker-updates
```
