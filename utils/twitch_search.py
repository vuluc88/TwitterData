import urllib,urllib2
import json
import re
import time
import cookielib
from models import Tweet, TwitterAccount

from pyquery import PyQuery

class TweetManager:

    def __init__(self):
        pass

    @staticmethod
    def getTweets(criteria):
        refreshCursor = ''

        results = []
        resultsAux = []
        cookieJar = cookielib.CookieJar()

        active = True

        while active:
            json = TweetManager.getJsonReponse(criteria, refreshCursor, cookieJar)
            if len(json['items_html'].strip()) == 0:
                break

            refreshCursor = json['min_position']
            scrapedTweets = PyQuery(json['items_html'])
            #Remove incomplete tweets withheld by Twitter Guidelines
            scrapedTweets.remove('div.withheld-tweet')
            tweets = scrapedTweets('div.js-stream-tweet')

            if len(tweets) == 0:
                break

            for tweetHTML in tweets:
                tweetPQ = PyQuery(tweetHTML)

                accountId   = int(tweetPQ.attr("data-user-id"))
                accountFullname = tweetPQ.attr("data-name")
                accountHref = "/" + tweetPQ.attr("data-screen-name")
                account = TwitterAccount(accountId, accountFullname, accountHref)

                epoch   = int(tweetPQ("small.time span.js-short-timestamp").attr("data-time"))
                date    = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))
                likes   = int(tweetPQ("span.ProfileTweet-action--favorite span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""))
                replies = int(tweetPQ("span.ProfileTweet-action--reply span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""))
                retweets = int(tweetPQ("span.ProfileTweet-action--retweet span.ProfileTweet-actionCount").attr("data-tweet-stat-count").replace(",", ""))
                txt = re.sub(r"\s+", " ", tweetPQ("p.js-tweet-text").text().replace('# ', '#').replace('@ ', '@'))

                tweet = Tweet(account, date, likes, replies, retweets, txt)

                results.append(tweet)

                if criteria['limit'] > 0 and len(results) >= criteria['limit']:
                    active = False
                    break

        return results

    @staticmethod
    def getJsonReponse(criteria, refreshCursor, cookieJar):
        url = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&max_position=%s"

        urlGetData = ''

        if 'username' in criteria:
            urlGetData += ' from:' + criteria['username']

        if 'hashtag' in criteria:
            urlGetData += ' #' + criteria['hashtag']


        url = url % (urllib.quote(urlGetData), refreshCursor)
        print url

        headers = [
            ('Host', "twitter.com"),
            ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"),
            ('Accept', "application/json, text/javascript, */*; q=0.01"),
            ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
            ('X-Requested-With', "XMLHttpRequest"),
            ('Referer', url),
            ('Connection', "keep-alive")
        ]

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        opener.addheaders = headers

        try:
            response = opener.open(url)
            jsonResponse = response.read()
        except:
            print "Twitter weird response. Try to see on browser: https://twitter.com/search?q=%s&src=typd" % urllib.quote(urlGetData)
            return

        dataJson = json.loads(jsonResponse)

        return dataJson 