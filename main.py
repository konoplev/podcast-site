from PagesGenerator import PagesGenerator
from RssEntriesProducer import RssEntriesProducer


def generate(url):
    PagesGenerator('./docs', RssEntriesProducer().get_entries(url)).generate()


if __name__ == '__main__':
    generate('https://anchor.fm/s/1c9e8da8/podcast/rss')
