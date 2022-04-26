from itertools import count
from ChickenUtil import ChickenStore
############################################################################
brandName = 'pelicana'
base_url = 'https://www.pelicana.co.kr/store/stroe_search.html'
############################################################################
def getData():
    savedData = []  # 액셀로 저장될 중첩 리스트 구조
    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        # print( url )
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytable = soup.find('table', attrs={'class': 'table mt20'})
        mytbody = mytable.find('tbody')
        # print(len(mytbody.findAll('tr')))

        shopExists = False  # 매장 목록이 없다고 가정

        for mytr in mytbody.findAll('tr'):
            shopExists = True
            mylist = list(mytr.strings)
            # print(mylist)
            # print('*' * 30)

            store = mylist[1]
            address = mylist[3]
            # print('{' + address + '}')

            imsiphone = mytr.select_one('td:nth-of-type(3)').string
            if imsiphone is not None:
                phone = imsiphone.strip()
            else:
                phone = ""

            if len(address) >= 2:
                imsi = address.split()
                sido = imsi[0]      # 주소의 시/도
                gungu = imsi[1]     # 주소의 군/구

                mydata = [brandName, store, sido, gungu, address, phone]
                # print(mydata)
                savedData.append(mydata)

        # print('*' * 30)
        if shopExists == False:
            chknStore.save2Csv(savedData)
            break
        # if page_idx >= 2:
        #     chknstore.save2Csv(savedData)
        #     break
############################################################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')