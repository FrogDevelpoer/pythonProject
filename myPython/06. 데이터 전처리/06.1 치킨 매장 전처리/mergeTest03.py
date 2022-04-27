import pandas as pd

mystorefile = 'store.csv'
mystore = pd.read_csv(mystorefile, encoding='UTF-8', index_col=0, header=0)
print(mystore)
print('=' * 30)

districtfile = 'districtmini.csv'
district = pd.read_csv(districtfile, encoding='UTF-8', header=0)
print(district)
print('=' * 30)

# merge 메소드는 DB의 조인과 유사한 개념
result = pd.merge(mystore, district, on=['sido', 'gungu'], how='outer', suffixes=['', '_'], indicator=True)
print(result)
print('=' * 30)
'''
mystore는 left, district는 right
indicator=True에서 left_only는 mystore에만 있는 행
'''
m_result = result.query('_merge == "left_only"')
print('왼쪽에만 존재하는 행')
print(m_result)
print('=' * 30)

gungufile = open('gungufile.txt', encoding='UTF-8')
gungu_list = gungufile.readlines()
print(gungu_list)
print('=' * 30)

gungu_dict = {}
for onegu in gungu_list:
    mydata = onegu.replace('\n', '').split(':')
    gungu_dict[mydata[0]] = mydata[1]

print(gungu_dict)
print('=' * 30)

mystore.gungu = mystore.gungu.apply(lambda data : gungu_dict.get(data, data))
print('최종 결과')
print(mystore)
print('=' * 30)