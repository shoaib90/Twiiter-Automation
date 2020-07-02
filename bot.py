import tweepy
import time

CONSUMER_KEY = 'rUiHdjCb3KSeKIlQIrSH4tyg2'
CONSUMER_SECRET = 'lgzQHb9Zb7YbCEm3k96lNFGGBzLpNl5o4w1koWhmJwkDGzJ7Gd'
ACCESS_TOKEN = '1273963908059938816-DwcICxxLoQ7TNJnJf4Mx56TpxHhaMU'
ACCESS_TOKEN_SECRET = 'TjyMhXUxRGT6FqG9TG3v6ba1O8fcCy9YNeV1WBet3FIkb'

# * Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# * Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
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
