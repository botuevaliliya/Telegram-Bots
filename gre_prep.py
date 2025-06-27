import pandas as pd
from random import random, randint, shuffle
import telebot
from telebot import types


TOKEN='your_token'
bot = telebot.TeleBot(TOKEN)

df = pd.read_excel('GRE prep.xlsx')
df = df.iloc[1:, :]
df.reset_index(drop=True, inplace=True)
df.columns = ['word', 'form', 'desc']

def get_new_question(f):
    question_i = randint(0, len(df) - 1)
    answer_i = [randint(0, len(df) - 1) for i in range(3)]
    answer_i.append(question_i)
    shuffle(answer_i)
    if f == 1:
        return {'question': df['word'][question_i], 
                'variants': [df['desc'][i][:50] for i in answer_i], 
                'answer': df['desc'][question_i][:50]}
    else:
        return {'question': df['desc'][question_i],
                'variants': [df['word'][i] for i in answer_i], 
                'answer': df['word'][question_i]}
quiz = {}

rem_message = 1

def quiz_mode(message):
    return True

@bot.message_handler(func=quiz_mode)#(commands=['More'])
def quiz(message): 
    global rem_message 
    rem_message = message
#     if message.text == 'Study':
#         learn_words(message)
#     else:
    quiz_continue(message)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global rem_message 
    if call.data == quiz['answer']: 
        bot.send_message(call.message.chat.id, 'Correct!')
        quiz_continue(rem_message)
    else:
        bot.send_message(call.message.chat.id, 'Incorrect')
    
def quiz_continue(message):
    global quiz
    f = randint(0, 1)
    quiz = get_new_question(f)
    keyboard = types.InlineKeyboardMarkup() 
    key_1 = types.InlineKeyboardButton(text=quiz['variants'][0], callback_data=quiz['variants'][0]) 
    keyboard.add(key_1) 
    key_2= types.InlineKeyboardButton(text=quiz['variants'][1], callback_data=quiz['variants'][1])
    keyboard.add(key_2)
    key_3 = types.InlineKeyboardButton(text=quiz['variants'][2], callback_data=quiz['variants'][2]) 
    keyboard.add(key_3) 
    key_4= types.InlineKeyboardButton(text=quiz['variants'][3], callback_data=quiz['variants'][3])
    keyboard.add(key_4)
    question = quiz['question']
    CORRECT_ANSWER=0
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


      
bot.polling()
