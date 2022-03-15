import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot('5258330220:AAHnMgzY-NbnBYNfKws7yCRgJzBGDaTpegM')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220315'

def do_function() :
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.select_one('span.imax'))
    imax = soup.select_one('span.imax')
    # imax상영 여부 확인 후 imax대상 영화 제목 가져오기
    if(imax):
        imax = imax.find_parent('div', class_='col-times')
        imax_title = imax.select_one('div.info-movie > a > strong').text.strip()
        # print(imax_title + ' imax 예매가 열렸습니다.')
        bot.sendMessage(chat_id=5211769165, text= imax_title + ' imax 예매가 열렸습니다.')
        #스케쥴러 멈추기(작성 안하면 30초마다 계속 메세지 옴)
        sched.pause()
    
    #안열리면 메세지 굳이 필요없으니 주석처리해도 됨
    # else: 
    #     # print('imax 예매가 아직 열리지 않았습니다.')
    #     bot.sendMessage(chat_id=5211769165, text = 'imax 예매가 아직 열리지 않았습니다.')
 
sched = BlockingScheduler()
sched.add_job(do_function, 'interval', seconds=30)
sched.start()

