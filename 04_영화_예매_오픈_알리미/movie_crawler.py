import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220318'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
# print(soup.select_one('span.imax'))
imax = soup.select_one('span.imax')
# imax상영 여부 확인
if(imax):
    imax = imax.find_parent('div', class_='col-times')
    imax_title = imax.select_one('div.info-movie > a > strong').text.strip()
    print(imax_title + ' imax 예매가 열렸습니다.')
else:
    print('imax 예매가 아직 열리지 않았습니다.')

# imax대상 영화 제목 가져오기