import requests

def send_to_discord(webhook_url, category, original_title, translated_title, translated_summary, link):
    """
    DiscordのWebhookに記事情報を送信する
    """
    if not webhook_url:
        print("⚠ Webhook URLが設定されていません。ターミナルへの出力に留めます。")
        return

    # Embedの設定
    embed = {
        "title": translated_title,
        "url": link,
        "description": f"**元のタイトル:**\n{original_title}\n\n**要約:**\n{translated_summary}",
        "color": 3447003, # 青色
        "footer": {
            "text": f"Category: {category}"
        }
    }

    payload = {
        "embeds": [embed]
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"[Discord送信エラー] {e}")
