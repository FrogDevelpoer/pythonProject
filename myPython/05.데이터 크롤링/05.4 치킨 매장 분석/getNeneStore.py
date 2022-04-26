from itertools import count
from ChickenUtil import ChickenStore
import re

############################################################################
brandName = 'nene'
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'


############################################################################
def getData():
    savedData = []
    for page_idx in range(1, 45 + 1):
        url = base_url + '?page=%d' % page_idx
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        tablelist = soup.findAll('table', attrs={'class': 'shopTable'})
        # print(len(tablelist))
        # print(page_idx)
        for onetable in tablelist:
            store = onetable.select_one('.shopName').string
            temp = onetable.select_one('.shopAdd').string

            im_address = onetable.select_one('.shopMap')
            im_address = im_address.a['href']
            # print(im_address)

            if temp == None:    # shopAdd가 없는 항목
                apos = im_address.find("(")
                dpos = im_address.find(")")
                temp = im_address[apos+1:dpos].replace("'", "")
                address = temp
                sido = ''
                gungu = ''
            else:
                regex = '\d\S*'  # 숫자로 시작하고   # \s : white Character # \S : 눈에 보이는 모든 글자
                pattern = re.compile(regex)
                mymatch = pattern.search(im_address)
                # print(mymatch)

                addr_suffix = mymatch.group().replace("');", "")
                address = temp + ' ' + addr_suffix
                # print(address)

                imsi = temp.split(' ')
                sido = imsi[0]
                gungu = imsi[1]
            # end if
            # print(store + '/' + temp)

            phone = onetable.select_one('.tooltiptext').string

            mydata = [brandName, store, sido, gungu, address, phone]
            savedData.append(mydata)

            print('-' * 30)

            if page_idx == 3:
                break

    chknStore.save2Csv(savedData)


############################################################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')
