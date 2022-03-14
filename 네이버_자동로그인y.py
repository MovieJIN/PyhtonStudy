from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

#웹페이지 주소로 이동(로그인 화면)
driver.implicitly_wait(5) #웹페이지 로딩을 위해 5초정도 기다림
driver.maximize_window() #화면 최대화

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

#id입력창
id = driver.find_element(By.CSS_SELECTOR, '#id')
id.click()
#id.send_keys('moviejin90') 이렇게 쓰면 자동입력 방지 문자뜨기 때문에 직접 쓰는거 처럼..
pyperclip.copy('moviejin90') #클립보드에 해당 글자 복사
pyautogui.hotkey('ctrl', 'v') #ctrl이랑 v 동시에 눌러서 붙여넣기
time.sleep(2) #2초 기다림

#PW입력
pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.click()
#pw.send_keys('MovieJin521!')
pyperclip.copy('MovieJin521!')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

#로그인 버튼 클릭
login = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login.click()
