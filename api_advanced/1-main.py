#!/usr/bin/python3
""" 1-top_ten.py """
import praw

def top_ten(subreddit):
    reddit = praw.Reddit(
        client_id="your_client_id",
        client_secret="your_client_secret",
        user_agent="your_user_agent",
    )

    try:
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.hot(limit=10):
            print(submission.title)
    except:
        print(None)
