# YouTube-video-summary-maker-Telegram-bot


### YouTube Insight Bot
A Telegram bot that gives **7 key insights** from any YouTube video using transcripts + a local LLM (via Ollama). Designed for fast, private summarization of podcasts, lectures, and long-form content.

### How It Works
1. Send a YouTube link to the bot
2. It fetches the transcript (English or Russian)
3. Splits it into \~20-minute chunks
4. Uses a local LLM (`mistral`) via Ollama to summarize
5. Returns a final 7-point summary in Telegram

### Tech
* Python, Telegram Bot API (`telebot`)
* `youtube-transcript-api`, `langdetect`, `ollama`
* Runs entirely **locally** (no OpenAI API needed)

### Setup
1. Install dependencies:

   ```bash
   pip install pyTelegramBotAPI youtube-transcript-api langdetect
   ```
2. Run Ollama with `mistral`:

   ```bash
   ollama run mistral
   ```
3. Add your Telegram bot token in the script
4. Launch:

   ```bash
   python main.py
   ```

---

### Why

I watch long videos and want **fast, high-level summaries** without token limits or cost. This bot solves that by automating insight extraction locally — all stored in one place (Telegram).

