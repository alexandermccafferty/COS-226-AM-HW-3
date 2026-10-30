class Movie:
    def __init__(self, title = "", quote = ""):
        self.title = title
        self.quote = quote
        self.next = None
        self.status = 0