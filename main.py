from flask import Flask, request
from flask_restful import Resource, Api
from resources import HashtagTweetApi
from resources import UserTweetApi

app = Flask(__name__)
api = Api(app)


api.add_resource(HashtagTweetApi, '/hashtags/<string:hashtag_str>')
api.add_resource(UserTweetApi, '/users/<string:user_str>')

if __name__ == '__main__':
    app.run(debug=False, port=5000)


