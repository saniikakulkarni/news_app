# config.py

import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

NEWS_STORAGE_FILE = "news_storage.json"

RSS_FEEDS = [
    # 🌍 Global Major
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://www.reutersagency.com/feed/?best-topics=top-news",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "http://rss.cnn.com/rss/edition.rss",
    "https://feeds.apnews.com/apnews/topnews",

    # 🇮🇳 India Major
    "https://www.thehindu.com/news/national/feeder/default.rss",
    "https://indianexpress.com/section/india/feed/",
    "https://feeds.feedburner.com/ndtvnews-india-news",
    "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    "https://economictimes.indiatimes.com/rssfeedsdefault.cms",

    # 🔎 Google News Topic Feeds (Dynamic & Powerful)
    "https://news.google.com/rss/search?q=india&hl=en-IN&gl=IN&ceid=IN:en",
    "https://news.google.com/rss/search?q=geopolitics&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=global+economy&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=technology&hl=en-US&gl=US&ceid=US:en",
    "https://news.google.com/rss/search?q=AI&hl=en-US&gl=US&ceid=US:en"
]