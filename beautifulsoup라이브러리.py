import requests
from bs4 import BeautifulSoup

#네이버 서버에 대화 시도
response = requests.get("http://www.naver.com")

#네이버에서 html을 줌
html = response.text

#html 번역을 이용함
soup = BeautifulSoup(html, 'html.parser')

#id를 이용하여 해당 태그 찾아서 출력
word = soup.select_one('#NM_set_home_btn')
print(word.text)