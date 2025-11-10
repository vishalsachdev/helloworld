# Twitter Follower Tracker 📈

A simple, elegant web application to track the follower count of any Twitter/X account at 15-minute intervals. Features real-time visualization, historical data tracking, and automatic updates.

![Twitter Follower Tracker](https://img.shields.io/badge/Twitter-Follower%20Tracker-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)

## Features

✨ **Real-time Tracking**: Automatically fetches follower count every 15 minutes
📊 **Beautiful Visualization**: Interactive Chart.js graphs showing follower growth
💾 **Persistent Storage**: All data saved locally in your browser
⚡ **Instant Updates**: Manual refresh button for immediate data fetching
📱 **Responsive Design**: Works perfectly on desktop and mobile
🎨 **Modern UI**: Clean, gradient-based design with smooth animations

## Quick Start

### Prerequisites

- Python 3.7 or higher
- A modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Start the API server:**
```bash
python twitter-tracker-api.py
```

The server will start on `http://localhost:5000`

3. **Open the web app:**
Simply open `twitter-follower-tracker.html` in your web browser, or serve it:
```bash
# Option 1: Direct file access
open twitter-follower-tracker.html

# Option 2: Use a simple HTTP server
python -m http.server 8080
# Then visit http://localhost:8080/twitter-follower-tracker.html
```

## Usage

1. **Enter a Twitter username** (e.g., `sighjith` or `@sighjith` or full URL)
2. **Click "Start Tracking"** to begin automatic 15-minute interval checks
3. **View real-time stats:**
   - Current follower count
   - Change since last check
   - Total number of checks
   - Countdown to next check
4. **Use "Fetch Now"** for immediate updates without waiting
5. **Monitor the chart** to see follower growth trends over time

## Configuration

### Using Real Twitter API Data

By default, the app runs in **demo mode** with simulated data. To fetch real Twitter data:

1. **Get Twitter API Access:**
   - Go to [Twitter Developer Portal](https://developer.twitter.com/)
   - Create a new app (Free tier available)
   - Generate a Bearer Token

2. **Set the environment variable:**
```bash
export TWITTER_BEARER_TOKEN='your_bearer_token_here'
python twitter-tracker-api.py
```

### API Endpoints

The backend provides these endpoints:

- `GET /api/followers?username=<username>` - Get follower count
- `GET /api/health` - Health check
- `GET /` - API documentation

## Architecture

```
┌─────────────────────────┐
│  Browser (Frontend)     │
│  - HTML/CSS/JavaScript  │
│  - Chart.js for graphs  │
│  - localStorage for data│
└───────────┬─────────────┘
            │
            │ HTTP Requests
            │ (every 15 min)
            │
┌───────────▼─────────────┐
│  Flask API (Backend)    │
│  - Python 3.7+          │
│  - CORS enabled         │
│  - Multiple fetch modes │
└───────────┬─────────────┘
            │
            │ Fetch data
            │
┌───────────▼─────────────┐
│  Data Sources           │
│  1. Twitter API v2      │
│  2. Web scraping        │
│  3. Demo/simulation     │
└─────────────────────────┘
```

## Data Modes

The application intelligently falls back through multiple data fetching methods:

1. **Twitter API** (most reliable) - Requires Bearer Token
2. **Web Scraping** (may be blocked) - No authentication needed
3. **Demo Mode** (always works) - Generates realistic simulated data

## Features in Detail

### Frontend (`twitter-follower-tracker.html`)
- Single-page application with no external dependencies except Chart.js
- Stores all tracking data in browser localStorage
- Real-time countdown timer until next check
- Historical data table showing recent checks
- Responsive grid layout for statistics
- Color-coded positive/negative changes

### Backend (`twitter-tracker-api.py`)
- RESTful Flask API
- CORS enabled for local development
- Username extraction from URLs or handles
- Multiple fallback methods for data fetching
- Error handling and detailed error messages
- Health check endpoint

## Troubleshooting

### "Failed to fetch data" Error
- Make sure the Flask API server is running on port 5000
- Check that no firewall is blocking localhost connections
- Try opening http://localhost:5000/api/health in your browser

### "User not found" Error
- Verify the username is correct and the account exists
- Try using just the username without @ or URL

### No Real Data / Demo Mode Active
- The app is using simulated data
- To get real data, configure `TWITTER_BEARER_TOKEN`
- Web scraping may be blocked by Twitter

### CORS Errors
- Make sure flask-cors is installed: `pip install flask-cors`
- Check that the API server is running
- Try accessing the HTML file via a web server instead of `file://`

## Example Use Cases

- **Content Creators**: Track growth after campaigns
- **Social Media Managers**: Monitor multiple accounts
- **Research**: Study follower growth patterns
- **Personal**: Track your own account's progress

## Technical Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Visualization**: Chart.js
- **Backend**: Python Flask
- **HTTP Client**: Requests library
- **Storage**: Browser localStorage

## Limitations

- Checking interval is 15 minutes (can be modified in code)
- Data is stored locally (cleared if you clear browser data)
- Web scraping method may not work due to Twitter's anti-bot measures
- Demo mode generates simulated data when real access isn't available

## Customization

### Change Check Interval
Edit line in `twitter-follower-tracker.html`:
```javascript
trackingInterval = setInterval(fetchNow, 15 * 60 * 1000); // 15 minutes
```

### Change Chart Colors
Modify the Chart.js configuration in the `initChart()` function.

### Add More Statistics
Extend the stats grid in the HTML and calculate additional metrics in JavaScript.

## Privacy & Data

- All follower tracking data is stored **locally** in your browser
- No data is sent to any third-party servers (except Twitter for fetching)
- The backend API doesn't log or store any user data
- You can clear all data anytime using the "Clear Data" button

## License

This project is open source and available for personal and commercial use.

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the browser console for error messages
- Ensure all dependencies are installed correctly

## Example Screenshot Description

The app features:
- Gradient purple header with Twitter blue accents
- Four stat cards showing key metrics
- Interactive line chart with follower trends
- Data table with recent checks
- Clean, modern interface

---

Built with ❤️ for tracking Twitter growth

**Note**: This tool is for educational and personal use. Please respect Twitter's Terms of Service and rate limits when using the API.
