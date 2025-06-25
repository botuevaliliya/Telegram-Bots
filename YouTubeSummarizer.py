import telebot
import re
import ollama
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled
from langdetect import detect

TOKEN='your_token' #get it from @BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Greetings. Send me a YouTube URL and I’ll reply with insights from video.")

@bot.message_handler(func=lambda message: True)
def handle_youtube_url(message):
    url = message.text.strip()
    print('url')
    bot.reply_to(message, "Processing...")

    try:
        video_id = url.split("v=")[1].split("&")[0] if "v=" in url else url.split("/")[-1] if "youtu.be" in url else None
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            transcript = transcript_list.find_transcript(['ru', 'en']).fetch()
        except NoTranscriptFound:
            transcript = transcript_list.find_generated_transcript(['ru', 'en']).fetch()

        max_seconds=1200
        chunks, current_text, chunk_start = [], "", 0
        if hasattr(transcript, "snippets"):
            entries = transcript.snippets
        else:
            entries = transcript
        
        for entry in entries:
            start = entry.start if hasattr(entry, "start") else entry['start']
            text = entry.text if hasattr(entry, "text") else entry['text']
            
            if start - chunk_start >= max_seconds:
                chunks.append(current_text.strip())
                current_text, chunk_start = "", start
            current_text += " " + text
        
        if current_text:
            chunks.append(current_text.strip())


        all_insights = ""
        for i, chunk in enumerate(chunks):
            cleaned = re.sub(r'\[.*?\]', '', chunk)
            cleaned = re.sub(r'(subscribe|like|channel|click).*?\.', '', cleaned, flags=re.I)
            cleaned = re.sub(r'\s+', ' ', cleaned)
            lang = detect(cleaned)

            prompt = f"""
                This transcript is in {lang}. 
                Please summarize the following 20-minute spoken segment into 3–4 bullet points of meaningful insights.
                Write your response in {lang}. 
                Transcript:{cleaned}"""
            response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
            insight_block = response['message']['content'].strip()
            all_insights += f"\n{insight_block}"
            
        final_prompt = f"""Here are insight blocks from a long video: {all_insights}. Write your response in {lang}. 
            Please consolidate them into 7 high-level takeaways that summarize the big ideas.
            Please begin your response with one short sentence that introduces who is speaking or what the video is about."""
        summary_response = ollama.chat(model='mistral', messages=[{"role": "user", "content": final_prompt}])
        final_summary = summary_response['message']['content'].strip()

        if len(final_summary) <= 4000:
            bot.send_message(message.chat.id, final_summary)
        else:
            for part in [final_summary[i:i+4000] for i in range(0, len(final_summary), 4000)]:
                bot.send_message(message.chat.id, part)

    except Exception as e:
        print("Error:", e)
        bot.send_message(message.chat.id, "Sorry, error occurred.")

print("Bot is running...")
bot.polling()
