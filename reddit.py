import praw

reddit = praw.Reddit(client_id='8lqDe9bsPlCVtg',
                     client_secret='RI8qqrHOy2lz6rF7MNnbdgZdZ6Q',
                     user_agent='python:8lqDe9bsPlCVtg:1.0.0 (by /u/learningdnd)')

print(reddit.read_only)

for submission in reddit.subreddit(reddit.random_subreddit(nsfw=False).display_name).hot(limit=10):
    print(submission.title)