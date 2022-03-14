import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요>>>>")
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
print(links)

for link in links :
    title = link.text #태그 안의 텍스트 요소를 가져옴
    url = link.attrs['href'] #href의 속성값을 가져옴
    print(title, url)  