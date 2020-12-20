import feedparser

from RssEntry import RssEntry, PodcastFile


class RssEntriesProducer:

    def get_entries(self, podcast_feed):
        feed = feedparser.parse(podcast_feed)
        i = 0
        rss_entries = list()
        for entries in feed['entries']:
            rss_entries.append(RssEntry(
                feed['entries'][i]['title'],
                feed['entries'][i]['published'],
                feed['entries'][i]['summary'],
                feed['entries'][i]['link'],
                PodcastFile(
                    feed['entries'][i]['links'][1]['href'],
                    feed['entries'][i]['links'][1]['type']
                )
            ))
            i += 1
        return rss_entries
