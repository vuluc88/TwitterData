from account import TwitterAccount

class Tweet:
    account     = None
    date        = None
    likes       = 0
    replies     = 0
    retweets    = 0
    text        = ''

    def __init__(self, account, date, likes, replies, retweets, text):
        self.account    = account
        self.date       = date
        self.likes      = likes
        self.replies    = replies
        self.retweets   = retweets
        self.text       = text

    def json(self):
        account = {}
        if self.account:
            account = self.account.json()
        return {
            'account': account,
            'date': self.date,
            'likes': self.likes,
            'replies': self.replies,
            'retweets': self.retweets,
            'text': self.text
        }