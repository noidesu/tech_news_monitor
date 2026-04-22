# Tech News Monitor

海外の技術ニュース(宇宙、防衛、AI等)をRSSフィードから取得し、日本語に翻訳・要約してDiscordに通知するPythonスクリプトです。

## ローカルでの実行方法

1. **リポジトリのクローン・移動**
   ```bash
   cd tech_news_monitor
   ```

2. **依存関係のインストール**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linuxの場合
   pip install -r requirements.txt
   ```

3. **環境変数の設定**
   `.env.example` をコピーして `.env` を作成し、ご自身のDiscord Webhook URLを設定してください。
   ```bash
   cp .env.example .env
   # .env ファイルを開き、DISCORD_WEBHOOK_URLを編集
   ```

4. **実行**
   Pythonパスを通しつつ実行します：
   ```bash
   PYTHONPATH=./src python src/main.py
   ```

## GitHub Actionsでの自動実行

1. GitHubリポジトリの `Settings` > `Secrets and variables` > `Actions` に移動します。
2. `New repository secret` をクリックし、名前に `DISCORD_WEBHOOK_URL`、値にご自身のWebhook URLを貼り付けて保存します。
3. デフォルトで毎日日本時間午前9時と午後9時に自動実行されます。手動で実行したい場合は「Actions」タブから「Python Tech News Monitor」を選択して「Run workflow」ボタンを押してください。
