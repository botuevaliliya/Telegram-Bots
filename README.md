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

<img width="758" alt="Screenshot 2025-06-27 at 6 36 49 PM" src="https://github.com/user-attachments/assets/b621b5c0-3f16-497f-a1bc-d8819cfcbda7" />


# GRE_prep
A Telegram bot that helps you memorize GRE-level vocabulary through fast-paced quizzes.
It was built to turn frustrating C2 English prep into an interactive, low-effort game you can play anywhere.

### Features
Quiz-based vocabulary learning (word → definition or definition → word)  
4-answer multiple-choice format  
Randomized options with feedback  
Designed for repeat, low-friction study sessions  

### Tech
Python + Telegram Bot API  
Excel vocabulary dataset (GRE prep.xlsx)  
Uses telebot and pandas  

### Why
GRE prep is boring. This bot makes it quick, repeatable, and a bit more fun — right from your phone.

<img width="758" alt="Screenshot 2025-06-27 at 6 34 55 PM" src="https://github.com/user-attachments/assets/f4fd6bbf-9160-4716-9801-c498e6602c38" />


# Random Coffee Chat Bot
A Telegram bot that powers serendipitous weekly meetups by randomly matching users for one-on-one chats.  
Built for a hackathon (in 1 hour!), it aims to make community networking feel organic and light.

### How It Works
Users register with name, interests, and specialty  
Each Monday, the bot matches them randomly  
Both users get each other's Telegram + bio to arrange a chat  

### Tech
Python + telebot  
CSV-based user storage (pandas)  
Simple pairing logic, 100% automated  
Can be extended to include timezone logic or group matching  

### Why
Random Coffee is a proven way to spark ideas, friendships, and surprising connections.  
This bot makes it easy for any local community to adopt the concept.

<img width="758" alt="Screenshot 2025-06-27 at 6 35 48 PM" src="https://github.com/user-attachments/assets/dec8823d-4868-49bc-a046-9b15cfbb2571" />

