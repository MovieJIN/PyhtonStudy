import requests
from bs4 import BeautifulSoup

url = '/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220314'
html = requests.get(url)
# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
# soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong')
title_list = soup.select('div.info-movie')
for i in title_list:
    print(i.select_one('a > strong').text.strip())