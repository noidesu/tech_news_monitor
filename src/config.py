import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Define target RSS feeds
# これらのフィードはテストしやすく、情報が豊富なものをデフォルトとして設定しています。
RSS_FEEDS = {
    "Space": "https://spacenews.com/feed/",
    "Defense Tech": "https://www.defensenews.com/arc/outboundfeeds/rss/?sort=display_date:desc",
    "AI Infrastructure": "https://techcrunch.com/category/artificial-intelligence/feed/"
}

# 翻訳後のDiscordメッセージの最大文字数
MAX_MESSAGE_LENGTH = 2000
