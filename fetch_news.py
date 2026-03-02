# fetch_news.py

import feedparser
import json
import os
from datetime import datetime, timedelta
from config import RSS_FEEDS, NEWS_STORAGE_FILE


FOUR_HOURS_AGO = datetime.utcnow() - timedelta(hours=4)


def is_recent(entry):
    try:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published_time = datetime(*entry.published_parsed[:6])
            return published_time >= FOUR_HOURS_AGO
        else:
            return True  # If no timestamp, keep it
    except:
        return True


def fetch_rss():
    articles = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            if not is_recent(entry):
                continue

            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary if "summary" in entry else "",
                "published": entry.published if "published" in entry else "",
                "source": feed.feed.title if "title" in feed.feed else "Unknown",
                "fetched_at": datetime.utcnow().isoformat()
            })

    return articles


def save_articles(new_articles):
    if os.path.exists(NEWS_STORAGE_FILE):
        with open(NEWS_STORAGE_FILE, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    # Remove articles older than 24 hours (optional cleanup)
    cutoff = datetime.utcnow() - timedelta(hours=24)
    cleaned_existing = []

    for article in existing:
        try:
            fetched_time = datetime.fromisoformat(article["fetched_at"])
            if fetched_time >= cutoff:
                cleaned_existing.append(article)
        except:
            continue

    # Deduplicate by link
    existing_links = {article["link"] for article in cleaned_existing}

    unique_new_articles = [
        article for article in new_articles
        if article["link"] not in existing_links
    ]

    final_articles = cleaned_existing + unique_new_articles

    with open(NEWS_STORAGE_FILE, "w") as f:
        json.dump(final_articles, f, indent=2)


if __name__ == "__main__":
    articles = fetch_rss()
    save_articles(articles)