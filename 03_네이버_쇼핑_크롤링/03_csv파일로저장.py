from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

#브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

#웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) #로딩이 끝날 때 까지 10초 기다림
#만약 로딩이 완료되기 전에 쇼핑 메뉴 클릭이 되면 찾을 수 없어서 에러가 나기 때문에 기다리는 시간을 추가로 넣어줌

#쇼핑 메뉴 클릭하기
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2) #2초동안 기다리게 해줌

#검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

#검색어 입력
search.send_keys('아이폰13')

#enter입력
search.send_keys(Keys.ENTER)

#스크롤 전 높이 확인
#excute_script = 자바 명령어 수행
before_h = browser.execute_script("return window.scrollY")

#무한 스크롤 (반복문 이용)
while True :
    #맨 아래로 스크롤을 내려줌 : 키보드의 END키 눌러서 바디 태그의 제일 아래로 보내줌
    browser.find_element_by_css_selector('body').send_keys(Keys.END)

    #스크롤 사이 페이지 로딩 시간 부여
    time.sleep(1)

    #스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h


#파일 생성(경로, 쓰기모드, 인코딩, 윈도우에서 줄바꿈문자 추가되는거 없애줌)
f = open(r"D:\Crawling_Python\03_네이버_쇼핑_크롤링\date.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

#상품 정보 div
items = browser.find_elements_by_css_selector('.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
    try :
        price = item.find_element_by_css_selector('.price_num__2WUXn').text
    except :
        price = "판매중단"
    link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href')

    print(name, price, link)
    #데이터 쓰기
    csvWriter.writerow([name, price, link]) #한 행을 추가하는 명령어

#파일 닫아줌
f.close()
