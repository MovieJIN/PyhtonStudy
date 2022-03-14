import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요>>>>")
lastPage = pyautogui.prompt("크롤링 할 마지막 페이지를 입력해 주세요>>>>")
#여기서 입력받은 값은 문자열임
pageNum = 1
for i in range(1, 10*int(lastPage), 10):
    print(f"{pageNum}페이지 입니다.=======================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")
    print(links)

    for link in links :
        title = link.text #태그 안의 텍스트 요소를 가져옴
        url = link.attrs['href'] #href의 속성값을 가져옴
        print(title, url)  
    pageNum = pageNum + 1