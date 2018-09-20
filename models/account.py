
class TwitterAccount:
    fullname    = ''
    href        = ''
    id          = 0

    def __init__(self, id, fullname, href):
        self.id = id
        self.fullname = fullname
        self.href = href

    def json(self):
        return {
            'fullname': self.fullname,
            'href': self.href,
            'id': self.id
        }