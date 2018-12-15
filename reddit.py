import praw
import yaml

f = open('config.yml')
params = yaml.load(f)
f.close()

cid = params['auth']['client_id']
csecret = params['auth']['client_secret']
uagent = params['auth']['user_agent']

reddit = praw.Reddit(client_id=cid,
                     client_secret=csecret,
                     user_agent=uagent)

subr = reddit.random_subreddit(nsfw=False).display_name
print('Subreddit: {}'.format(subr))
for submission in reddit.subreddit(subr).hot(limit=10):
    print('* {}'.format(submission.title))