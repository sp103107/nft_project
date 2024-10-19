import praw
from config import (
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
)

def fetch_reddit_posts(subreddit_name="all", limit=5):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    subreddit = reddit.subreddit(subreddit_name)
    return [post.title for post in subreddit.hot(limit=limit)]

if __name__ == "__main__":
    titles = fetch_reddit_posts("cryptocurrency", limit=3)
    print("Top Posts:")
    for title in titles:
        print(f"- {title}")