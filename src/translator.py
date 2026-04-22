from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup

def clean_html(html_content):
    """HTMLタグを除去してプレーンテキストにする"""
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text(separator="\n").strip()

def translate_text(text, source='auto', target='ja'):
    """
    deep-translatorを使用してテキストを翻訳する。
    長すぎる場合は適度に切り詰める。
    """
    if not text:
        return ""
    try:
        # deep-translatorはデフォルトで1リクエスト5000文字の制限などがあるため、余裕を持たせる
        translated = GoogleTranslator(source=source, target=target).translate(text[:4000])
        return translated
    except Exception as e:
        print(f"[翻訳エラー] {e}")
        return text
