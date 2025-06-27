import pandas as pd
from random import random, randint, shuffle
import telebot
from telebot import types

TOKEN='your_token'
bot = telebot.TeleBot(TOKEN)

df = pd.DataFrame()
df['name'] = []
df['hobby'] = []
df['specialty'] = []
df['user_id'] = []
df['username'] = []
df.to_csv('users_random_coffee.csv')

name = ''
specialty = ''
hobby = ''
i = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это бот для поиска интересного собеседника в Якутске :) Он берет идею с Random Coffee. Тут люди обмениваются опытом, находят единомышленников и приятно проводят время.")
    bot.send_message(message.from_user.id, "Напиши свое имя")
    bot.register_next_step_handler(message, get_name)
    

def get_name(message): #получаем фамилию
    global name;
    global i;
    name = message.text;
    df.loc[0, 'name'] = name
    df.loc[0, 'user_id'] = message.from_user.id
    df.loc[0, 'username'] = message.from_user.username
    bot.send_message(message.from_user.id, 'Твоя специальность')
    bot.register_next_step_handler(message, get_specialty)
    

def get_specialty(message):
    global specialty, i
    specialty = message.text
    df.loc[i, 'specialty'] = specialty
    bot.send_message(message.from_user.id, 'Расскажи о своих интересах')
    bot.register_next_step_handler(message, get_hobbies)
    

def get_hobbies(message):
    global hobby, i
    hobby = message.text
    df.loc[i, 'hobby'] = hobby
    bot.send_message(message.from_user.id, 'Отлично! Теперь ты участник встреч RandomCoffeeYkt. Имя собеседника ты будешь узнавать каждый понедельник, сообщение придет в этот чат. Спишитесь по контактам в Telegram, чтобы договориться о встрече (онлайн или офлайн, день и время вы устанавливаете самостоятельно). Уважайте других участников и приходите, если договорились, также не бойтесь проявлять инициативу. Приятного общения :) ')
    i+=1



if now == datetime(2022, 11, 5, 3, 45, 0, 0):
    bot.send_message(message.from_user.id, "Напиши свое имя")

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
#         bot.send_message(call.message.chat.id, 'Запомню : )')
#     elif call.data == "no":
#         bot.send_message(call.message.chat.id, 'Bad : )')



__________________________________separate file__________________________________

import pandas as pd
import telebot
from telebot import types
from random import random, randint, shuffle, randrange
from datetime import datetime
import os
import numpy as np

df = pd.read_csv('users_random_coffee.csv')
TOKEN=os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)



def pop_random(lst):
    idx = randrange(0, len(lst))
    return lst.pop(idx)
while 1:
    if datetime.now().second%10 == 0:
        df = pd.read_csv('users_random_coffee.csv')
        df = df.drop_duplicates()
        pairs = {}
        lst = df['user_id'].to_list()
        shuffle(lst)
        j = 0 
        tmp = df.set_index('user_id')
        while j < len(lst) // 2: 
            bot.send_message(lst[j*2], "Привет, а вот и твой собеседник на эту неделю! \n@{} \nБио участника: {}-{}. {}".format(tmp.loc[lst[j*2] 'username'], tmp.loc[lst[j*2] 'name'], tmp.loc[lst[j*2] 'specialty'], tmp.loc[lst[j*2] 'hobby']))
            bot.send_message(lst[j*2+1], "Привет, а вот и твой собеседник на эту неделю! \n@{} \nБио участника: {}-{}. {}".format(tmp.loc[let[j*2+1] 'username'], tmp.loc[let[j*2+1] 'name'], tmp.loc[let[j*2+1] 'specialty'], tmp.loc[let[j*2+1] 'hobby']))
            print('have paired {} and {}', tmp.loc[lst[j*2] 'username'], tmp.loc[let[j*2+1] 'username'])
            j += 1
        if len(lst) % 2==1:
            bot.send_message(860496719, "Привет, а вот и твой собеседник на эту неделю! \n@{} \nБио участника: {}-{}. {}".format(tmp.loc[860496719, 'username'], tmp.loc[860496719, 'name'], tmp.loc[860496719, 'specialty'], tmp.loc[860496719, 'hobby']))
            bot.send_message(lst[j*2+1], "Привет, а вот и твой собеседник на эту неделю! \n@{} \nБио участника: {}-{}. {}".format(tmp.loc[let[j*2+1] 'username'], tmp.loc[let[j*2+1] 'name'], tmp.loc[let[j*2+1] 'specialty'], tmp.loc[let[j*2+1] 'hobby']))
            print('have paired {} and {}', tmp.loc[let[j*2+1] 'username'], tmp.loc[860496719, 'username'])
            
            
