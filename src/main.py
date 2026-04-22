import os
import json
from config import RSS_FEEDS, DISCORD_WEBHOOK_URL
from rss_fetcher import fetch_latest_entries
from translator import clean_html, translate_text
from discord_sender import send_to_discord

HISTORY_FILE = "notified_articles.json"

def load_history():
    """過去に通知した記事URLの履歴を読み込む"""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except:
            return set()
    return set()

def save_history(history):
    """通知済みの記事URL履歴を保存する"""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(list(history), f)

def main():
    if not DISCORD_WEBHOOK_URL:
        print("⚠ DISCORD_WEBHOOK_URLが設定されていません。ログ出力と履歴更新のみ行います。")

    history = load_history()
    new_history = set(history)

    for category, url in RSS_FEEDS.items():
        print(f"[{category}] フィードを確認中: {url}")
        try:
            # 最新3件までチェック
            entries = fetch_latest_entries(url, limit=3)
        except Exception as e:
            print(f"[{category}] フィード取得エラー: {e}")
            continue

        for entry in reversed(entries): # 古い順に処理して通知を時系列に合わせる
            if entry["link"] in history:
                continue # 既に通知済み

            print(f"  新着記事: {entry['title']}")
            
            # HTMLタグのクリーニング
            clean_summary = clean_html(entry['summary'])
            
            # 翻訳 (タイトルと、要約冒頭500文字)
            translated_title = translate_text(entry['title'])
            translated_summary = translate_text(clean_summary[:500])
            if len(clean_summary) > 500:
                translated_summary += "..."
            
            print(f"  -> Discordに通知を送信中...")
            send_to_discord(
                DISCORD_WEBHOOK_URL, 
                category, 
                entry['title'], 
                translated_title, 
                translated_summary, 
                entry['link']
            )
            
            # 送信後に履歴に追加
            new_history.add(entry["link"])
    
    save_history(new_history)
    print("すべてのフィードの処理が完了しました。")

if __name__ == "__main__":
    main()
