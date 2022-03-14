from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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