import tweepy
import time
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# MY_ENV_VAR = os.getenv('MY_ENV_VAR')

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


# * Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# * Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
# Write your hashtag that you want to search for in "search" variable.
search = 'GalwanKeBalwaan'
nrtweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrtweets):
    try:
        print('Tweet Liked')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
