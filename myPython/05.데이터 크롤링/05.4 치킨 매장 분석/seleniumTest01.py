from selenium import webdriver
from selenium.webdriver.common.by import By

filename = 'D:/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(filename)
print(type(driver))

print('구글로 이동하기')
url = 'http://www.google.com'
driver.get(url)

# search_textbox = driver.find_element_by_name('q')
search_textbox = driver.find_element(by=By.NAME, value='q')

word = '북미정상회담'
search_textbox.send_keys(word)

search_textbox.submit()

import time

# 3초 후 스크린샷 찍고 저장
wait = 3
print(str(wait) + '초 대기')
time.sleep(wait)

imageFile = 'capture.png'
driver.save_screenshot(imageFile)
print(imageFile + ' 파일로 저장')

wait = 3
print(str(wait) + '초 후 종료')
driver.implicitly_wait(wait)

driver.quit()