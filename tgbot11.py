from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube
import subprocess
import telebot

#logging.basicConfig(level=logging.INFO)
#bot = Bot('2048039746:AAFG_-yLOfI3puCWIuJe8VbpwSVRHSJDpAQ')
#dp = Dispatcher(bot)
bot = telebot.TeleBot('2048039746:AAFG_-yLOfI3puCWIuJe8VbpwSVRHSJDpAQ')

@bot.message_handler(commands = ['start'])
def start(message):
    id = message.from_user.id
    bot.send_message(id, 'Отправь ссылку на видео с ютуба!') 
'''
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    id = message.from_user.id
    await message.answer('Отправь ссылку на видео с ютуба!') 

@dp.message_handler(content_types=['text'])
async def step2(message: types.Message):
  ''' 
@bot.message_handler(content_types=['text'])
def step2(message):         
    try:
        yt = YouTube(message.text)
        bot.send_message(message.from_user.id, 'Выполняется обработка...\nЭто может занять некоторое время')
        yt.streams.filter(res = '720p', file_extension = 'mp4').first().download(output_path=f"./video", filename= 'video.mp4', skip_existing=False)
        print('video complited')
        subprocess.run(f"ffmpeg -i ./video/video.mp4 -b 500k ./video/edited.mp4 -y")
        print('DONE')
        bot.send_video(message.chat.id, open('./video/edited.mp4', 'rb'))
        #await bot.send_video(message.from_user.id, "https://www.youtube.com/watch?v=3HrSVXP99kQ")        
        print('message sent')
    except Exception as ex:
        print(ex)
        bot.send_message(message.from_user.id, 'Такой ссылки нет! Попробуй ввести другую.')
        #await message.answer('Такой ссылки нет! Попробуй ввести другую.')

bot.polling()
#executor.start_polling(dp, skip_updates=True)
