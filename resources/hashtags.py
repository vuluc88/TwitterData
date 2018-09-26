from flask import Flask, request
from flask_restful import Resource
from models import TwitterAccount
from models import Tweet
from utils import TweetManager


#get tweets by hashtag APIs
class HashtagTweetApi(Resource):
    def get(self, hashtag_str):
        args = request.args
        limit = 30 #set the limit to default = 30

        if 'limit' in args:
            try:
                limit = int(args['limit'])
            except ValueError:
                pass

        lst_tweets = []
        manager = TweetManager()
        criteria    = {
            'hashtag': hashtag_str,
            'limit': limit
        }
        results = manager.getTweets(criteria)

        for tweet in results:
            lst_tweets.append(tweet.json())

        return lst_tweets