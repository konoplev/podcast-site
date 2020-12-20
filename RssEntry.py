class RssEntry:
    def __init__(self, title, published, summary, link, file):
        self.title = title
        self.published = published
        self.summary = summary
        self.link = link[link.rfind('/') + 1:]
        self.file = file


class PodcastFile:
    def __init__(self, href, file_type):
        self.href = href
        self.type = file_type
