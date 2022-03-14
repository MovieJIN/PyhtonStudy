import requests 
from bs4 import BeautifulSoup

#종목 코드 리스트(여러 종목을 가져오기 위해)
codes = [
    '005930', #삼성전자
    '000660', #sk하이닉스
    '035720' #카카오
]

for code in codes :
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text 
    #그냥 출력하면 75,000처럼 ,가 있는 상태로 출력되고 문자열이기 때문에 아래처럼 대체해줌
    price = price.replace(',', '')

    print(price)