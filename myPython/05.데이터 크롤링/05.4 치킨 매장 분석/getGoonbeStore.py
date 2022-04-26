from itertools import count
from ChickenUtil import ChickenStore
############################################################################
brandName = 'goobne'
base_url = 'http://www.goobne.co.kr/store/search_store.jsp'
############################################################################
def getData():
    savedData = []
    chknStore = ChickenStore(brandName, base_url)

    for page_idx in count():
        print('%s 페이지가 호출 되었습니다.' % str(page_idx + 1))
        bEndPage = False     # True 이면 마지막 페이지 도달

        cmdJavaScript = "javascript:store.getList('%s')" % str(page_idx + 1)
        soup = chknStore.getWebDriver(cmdJavaScript)
        # print(type(soup))

        store_list = soup.find('tbody', attrs={'id': 'store_list'})
        mytrlist = store_list.findAll('tr')

        for onestore in mytrlist:
            mytdlist = onestore.findAll('td')

            if len(mytdlist) > 1:
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True)
                phone = onestore.select_one('td:nth-of-type(2)').a.string
                address = onestore.select_one('td:nth-of-type(3)').a.string
                imsi = str(address).split(' ')
                sido = imsi[0]
                gungu = imsi[1]

                savedData.append([brandName, store, sido, gungu, address, phone])
            else:
                bEndPage = True
                break
        print('-' * 30)

        # if page_idx >= 1:
        #     break

        if bEndPage == True:
            break

        chknStore.save2Csv(savedData)
############################################################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')