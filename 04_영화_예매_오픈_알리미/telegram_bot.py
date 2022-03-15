import telegram

bot = telegram.Bot('5258330220:AAHnMgzY-NbnBYNfKws7yCRgJzBGDaTpegM')

#보낸 메세지 불러오기
# for i in bot.getUpdates():
#     print(i.message)

#메세지 보내기
bot.sendMessage(chat_id=5211769165, text='~테스트중~')