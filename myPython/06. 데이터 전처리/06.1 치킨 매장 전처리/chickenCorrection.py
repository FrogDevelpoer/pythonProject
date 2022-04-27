import pandas as pd
import numpy as np

pd.options.display.max_columns = 1000
pd.options.display.max_rows = 100

class ChickenCorrection:
    myencoding = 'UTF-8'

    def __init__(self, workfile):
        self.workfile = workfile
        self.myframe = pd.read_csv(self.workfile, index_col=0, encoding=self.myencoding)
        # print(self.myframe.info())

        self.correctionSido()
        self.correctionGungu()
        self.showMergeResult()
        self.correctionAddress()

        self.myframe.to_csv('allStoreModified.csv', encoding=self.myencoding)

    def correctionSido(self):   # 시/도 보정
        # 행 데이터 제거
        self.myframe = self.myframe[self.myframe['store'] != 'CNTTEST']     # pelicana
        self.myframe = self.myframe[self.myframe['sido'] != '테스트']     # pelicana

        # print('before sido')
        # print(self.myframe['sido'].unique())
        # print('-' * 30)

        sidofile = open('sido_correction.txt', 'r', encoding=self.myencoding)
        linelist = sidofile.readlines()

        sido_dict = {}
        for oneline in linelist:
            mydata = oneline.replace('\n', '').split(':')
            sido_dict[mydata[0]] = mydata[1]

        # print(sido_dict)
        # print('-' * 30)

        self.myframe.sido = self.myframe.sido.apply(lambda data : sido_dict.get(data, data))

        # print('after sido')
        # print(self.myframe['sido'].unique())

    def correctionGungu(self):  # 군/구 보정
        # self.myframe = self.myframe[self.myframe['gungu'] != '테스트']
        # print('before gungu')
        # print(self.myframe['gungu'].unique())
        # print('-' * 30)

        gungufile = open('gungu_correction.txt', 'rt', encoding=self.myencoding)
        linelist = gungufile.readlines()

        gungu_dict = {}
        for oneline in linelist:
            mydata = oneline.replace('\n', '').split(':')
            gungu_dict[mydata[0]] = mydata[1]

        self.myframe.gungu = self.myframe.gungu.apply(lambda data: gungu_dict.get(data, data))

        # print('after gungu')
        # print(self.myframe['gungu'].unique())
        # print('-' * 30)

    def showMergeResult(self):
        district = pd.read_csv('district.csv', encoding=self.myencoding)

        mergedData = pd.merge(self.myframe, district, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)

        result = mergedData.query('_merge == "left_only"')
        # print('좌측에만 있는 데이터')
        # print(result[['sido', 'gungu', 'address']])

    def correctionAddress(self):    # 주소 보정
        try:
            for idx in range(len(self.myframe)):
                imsiseries = self.myframe.iloc[idx]
                addrSplit = imsiseries['address'].split(' ')[2:]
                imsiAddress = [imsiseries['sido'], imsiseries['gungu']]
                imsiAddress = imsiAddress + addrSplit
                self.myframe.iloc[idx]['address'] = ' '.join(imsiAddress)
        except TypeError as err:
            pass
# end class

filename = 'allstore.csv'
chknStore = ChickenCorrection(filename)