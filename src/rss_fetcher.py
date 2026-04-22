import feedparser

def fetch_latest_entries(feed_url, limit=5):
    """
    指定されたURLのRSSフィードから最新記事を取得します。
    """
    feed = feedparser.parse(feed_url, agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    if hasattr(feed, 'status') and feed.status != 200:
        print(f"      -> HTTP Status: {feed.status}")
    if feed.bozo and hasattr(feed, 'bozo_exception'):
        print(f"      -> Parse Error: {feed.bozo_exception}")
        
    entries = []
    
    for entry in feed.entries[:limit]:
        entries.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "summary": entry.get("summary", "")
        })
        
    return entries
