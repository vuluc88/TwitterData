from flask import Flask, request
from flask_restful import Resource
from models import TwitterAccount
from models import Tweet
from utils import TweetManager


#get tweets by user APIs
class UserTweetApi(Resource):
    def get(self, user_str):
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
            'username': user_str,
            'limit': limit
        }
        results = manager.getTweets(criteria)

        for tweet in results:
            lst_tweets.append(tweet.json())

        return lst_tweets