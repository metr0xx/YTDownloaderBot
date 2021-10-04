from moviepy.editor import *
import telebot
import os
from pytube import YouTube

bot = telebot.TeleBot('2048039746:AAFG_-yLOfI3puCWIuJe8VbpwSVRHSJDpAQ')
@bot.message_handler(commands = ['start'])
def start(message):
    id = message.from_user.id
    bot.send_message(id, 'Отправь ссылку на видео с ютуба!') 

@bot.message_handler(content_types=['text'])
def step2(message):
        
        
    try:
        yt = YouTube(message.text)
        yt.streams.filter(res = '720p', file_extension = 'mp4').first().download(r'C:/Users/mafr/Videos/tgvideos')
        print('video complited')
        video = open(r'C:/Users/mafr/Videos/tgvideos/' + yt.title + '.mp4', 'rb')
        print('file opened')
        bot.send_video(message.chat.id, video)
        print('message sent')
    except Exception as ex:
        print(ex)
        bot.send_message(message.from_user.id, 'Такой ссылки нет! Попробуй ввести другую.')

bot.polling()
