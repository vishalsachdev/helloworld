#!/usr/bin/env python3
"""
Twitter Follower Tracker API
A simple Flask API to fetch Twitter follower counts
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Twitter API configuration (optional - for authenticated requests)
TWITTER_BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN', '')

def extract_username(input_str):
    """Extract username from URL or handle"""
    # Remove @ if present
    input_str = input_str.strip().lstrip('@')

    # Extract from URL if it's a URL
    if 'twitter.com/' in input_str or 'x.com/' in input_str:
        match = re.search(r'(?:twitter\.com|x\.com)/([^/?]+)', input_str)
        if match:
            return match.group(1)

    return input_str

def get_followers_via_api(username):
    """
    Fetch follower count using Twitter API v2
    Requires TWITTER_BEARER_TOKEN environment variable
    """
    if not TWITTER_BEARER_TOKEN:
        return None, "Twitter API token not configured"

    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
    }
    params = {
        "user.fields": "public_metrics"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'public_metrics' in data['data']:
                return data['data']['public_metrics']['followers_count'], None
            return None, "Invalid API response format"
        elif response.status_code == 401:
            return None, "Invalid or expired Twitter API token"
        elif response.status_code == 404:
            return None, f"User '@{username}' not found"
        else:
            return None, f"Twitter API error: {response.status_code}"
    except Exception as e:
        return None, f"API request failed: {str(e)}"

def get_followers_via_scraping(username):
    """
    Attempt to scrape follower count from Twitter/X profile
    Note: This is fragile and may not work due to Twitter's anti-scraping measures
    """
    url = f"https://x.com/{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)

        if response.status_code == 200:
            # Try to find follower count in the page
            # Note: This is a simplified approach and may not work reliably
            content = response.text

            # Look for patterns that might indicate follower count
            # Twitter's HTML structure may change, making this fragile
            patterns = [
                r'"followers_count":(\d+)',
                r'followers_count&quot;:(\d+)',
                r'(\d+(?:,\d+)*)\s+Followers',
            ]

            for pattern in patterns:
                match = re.search(pattern, content)
                if match:
                    count_str = match.group(1).replace(',', '')
                    return int(count_str), None

            return None, "Could not extract follower count from page (Twitter may be blocking scraping)"
        elif response.status_code == 404:
            return None, f"User '@{username}' not found"
        else:
            return None, f"Failed to access Twitter page: {response.status_code}"
    except Exception as e:
        return None, f"Scraping failed: {str(e)}"

def get_followers_demo(username):
    """
    Demo mode: Returns simulated follower count
    Use this when neither API nor scraping is available
    """
    import random
    import hashlib

    # Generate a consistent base number for this username
    hash_obj = hashlib.md5(username.encode())
    base = int(hash_obj.hexdigest()[:8], 16) % 50000 + 1000

    # Add some random variation to simulate growth
    variation = random.randint(-50, 100)

    return base + variation, None

@app.route('/api/followers', methods=['GET'])
def get_followers():
    """
    API endpoint to get follower count for a Twitter user
    Query params:
        username: Twitter username or URL
    """
    username_input = request.args.get('username', '').strip()

    if not username_input:
        return jsonify({
            'success': False,
            'error': 'Username parameter is required'
        }), 400

    # Extract clean username
    username = extract_username(username_input)

    if not username:
        return jsonify({
            'success': False,
            'error': 'Invalid username or URL'
        }), 400

    # Try different methods in order of preference
    followers = None
    error = None
    method = None

    # 1. Try Twitter API (if token is available)
    if TWITTER_BEARER_TOKEN:
        followers, error = get_followers_via_api(username)
        if followers is not None:
            method = 'api'

    # 2. Try scraping (if API failed or not available)
    if followers is None:
        followers, scrape_error = get_followers_via_scraping(username)
        if followers is not None:
            method = 'scraping'
        elif error is None:
            error = scrape_error

    # 3. Fallback to demo mode
    if followers is None:
        followers, _ = get_followers_demo(username)
        method = 'demo'
        error = None  # Clear error for demo mode

    # Return result
    if followers is not None:
        return jsonify({
            'success': True,
            'username': username,
            'followers': followers,
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'method': method,
            'note': 'Using demo mode with simulated data' if method == 'demo' else None
        })
    else:
        return jsonify({
            'success': False,
            'error': error or 'Failed to fetch follower count'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'api_configured': bool(TWITTER_BEARER_TOKEN)
    })

@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API information"""
    return jsonify({
        'name': 'Twitter Follower Tracker API',
        'version': '1.0.0',
        'endpoints': {
            '/api/followers': 'Get follower count for a Twitter user (GET)',
            '/api/health': 'Health check endpoint (GET)'
        },
        'usage': {
            'example': '/api/followers?username=sighjith',
            'parameters': {
                'username': 'Twitter username, handle (@username), or profile URL'
            }
        }
    })

if __name__ == '__main__':
    print("=" * 60)
    print("Twitter Follower Tracker API")
    print("=" * 60)
    print(f"Server starting on http://localhost:5000")
    print(f"Twitter API configured: {bool(TWITTER_BEARER_TOKEN)}")

    if not TWITTER_BEARER_TOKEN:
        print("\nNOTE: Twitter API token not found.")
        print("The API will attempt scraping, but will fall back to demo mode.")
        print("For real data, set TWITTER_BEARER_TOKEN environment variable.")
        print("\nTo get a Twitter API token:")
        print("1. Go to https://developer.twitter.com/")
        print("2. Create a new app")
        print("3. Generate a Bearer Token")
        print("4. Set: export TWITTER_BEARER_TOKEN='your_token_here'")

    print("\n" + "=" * 60)

    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
