from pandas import DataFrame
import pandas as pd
myencoding = 'UTF-8'
chickenList = ['cheogajip', 'goobne', 'nene', 'pelicana']

# 데이터 프레임을 만들고 각각의 파일을 불러와서 concat으로 합치기
newframe = DataFrame()
print(newframe)
print('-' * 30)

for onestore in chickenList:
    filename = './data/' + onestore + '.csv'
    print(filename)
    myframe = pd.read_csv(filename, index_col=0, encoding=myencoding)
    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=True)
    print(myframe.head())
    print('-' * 30)
# end for
print(newframe.info())
print('-' * 30)

totalfile = 'allstore.csv'
newframe.to_csv(totalfile, encoding=myencoding)
print(totalfile + ' 저장 완료')