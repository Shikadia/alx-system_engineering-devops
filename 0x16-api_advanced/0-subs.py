#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if response is successful
    if response.status_code == 200:
        # Try to access JSON data, handle if subreddit doesn't exist
        try:
            results = response.json().get("data")
            return results.get("subscribers")
        except AttributeError:
            # Subreddit doesn't exist or JSON response is malformed
            return 0
    else:
        # Subreddit doesn't exist or other error occurred
        return 0
