#!/usr/bin/python3
"""This module holds a function to that queries
    the Reddit API and returns the number of subscribers
    for a given subreddit
    """
import requests


def number_of_subscribers(subreddit):
    """If an invalid subreddit is given"""
    headers = {
        'User-agent': 'Holberton'
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=headers)

    try:
        return req.json().get("data").get("subscribers")
    except Exception:
        return 0
