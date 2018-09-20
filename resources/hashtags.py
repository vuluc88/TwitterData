from flask import Flask, request
from flask_restful import Resource
from models import TwitterAccount
from models import Tweet


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
        #TODO: using Twitter's API to get tweets by hashtag

        #Fetch account data
        account = TwitterAccount(1, 'Vu Luc', '/vuluc88')

        #Fetch Tweet data
        #Tweet(account, date, likes, replies, retweets, text)
        tweet   = Tweet(account, '12:57 PM 7 Mar 2018', 169, 13, 27, "Historically, bash filename pattern matching was known")

        lst_tweets.append(tweet.json())
        return lst_tweets


