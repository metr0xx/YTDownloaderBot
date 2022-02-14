from pytube import YouTube
import subprocess
import telebot

with open("data.txt") as data:
    bot = telebot.TeleBot(data.readline())

@bot.message_handler(commands = ['start'])
def start(message):
    id = message.from_user.id
    bot.send_message(id, 'Send link to YouTube video') 
    
@bot.message_handler(content_types=['text'])
def send(message):           
    try:
        yt = YouTube(message.text)
        bot.send_message(message.from_user.id, 'Searching and downloading...')
        yt.streams.filter(res = '720p', file_extension = 'mp4').first().download(output_path=f"./video", filename= 'video.mp4', skip_existing=False)
        subprocess.run(f"ffmpeg -i ./video/video.mp4 -b 500k ./video/edited.mp4 -y")
        bot.send_video(message.chat.id, open('./video/edited.mp4', 'rb'))       
    except Exception as ex:
        print(ex)
        bot.send_message(message.from_user.id, 'Your link is incorrect, try to give an other one')
bot.polling()

