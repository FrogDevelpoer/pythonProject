import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class ChickenStore:
    def getWebDriver(self, cmdJavaScript):
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        time.sleep(wait)
        mypage = self.driver.page_source

        return BeautifulSoup(mypage, 'html.parser')

    def getSoup(self):  # BeautifulSoup 객체를 반환해주는 함수
        if self.soup is None:
            return None
        else:
            return BeautifulSoup(self.soup, 'html.parser')

    def get_request_url(self):  # urlopen 함수를 사용하여 url 객체를 반환하는 함수
        request = urllib.request.Request(self.url)
        try:
            response = urllib.request.urlopen(request)
            if response.getcode() == 200:  # http 응답 코드가 정상
                if self.brandName != 'pelicana':
                    return response.read().decode(self.myencoding)
                else:
                    return response
        except Exception as err:
            print(err)
            return None

    def __init__(self, brandName, url):
        self.myencoding = 'UTF-8'
        self.brandName = brandName
        self.url = url

        # csv 파일에 들어갈 컬럼 헤더
        self.mycolumns = ['brand', 'store', 'sido', 'gungu', 'address', 'phone']

        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            self.driver = None
        else:
            self.soup = None
            filepath = 'D:/chromedriver_win32/chromedriver.exe'
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(self.url)
        # print('생성자 호출됨')

        # 해당 리스트를 사용하여 csv 파일을 생성
    def save2Csv(self, saveData):
        data = pd.DataFrame(saveData, columns=self.mycolumns)
        data.to_csv(self.brandName + '.csv', encoding=self.myencoding, index=True)
# end class ChickenStore