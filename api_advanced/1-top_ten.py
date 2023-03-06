import praw

def top_ten(subreddit):
    try:
        reddit = praw.Reddit(client_id='your_client_id',
                             client_secret='your_client_secret',
                             user_agent='your_user_agent')
        hot_posts = reddit.subreddit(subreddit).hot(limit=10)
        for post in hot_posts:
            print(post.title)
    except:
        print(None)
