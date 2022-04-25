from pandas import Series

mylist = ['라일락', '코스모스', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '라일락']
myseries = Series(mylist)
print(myseries)

myunique = myseries.unique()    # unique 메소드는 리스트에 있는 요소 중 중복을 제외하고 어떠한 요소가 있는지 보여준다
print(myunique)
print(type(myunique))

print(myseries.value_counts())      # value_counts는 리스트에 원소별로 몇 개가 있는지 보여줌
print(type(myseries.value_counts()))

mask = myseries.isin(['들장미', '라일락'])    # isin 메소드는 리스트 순서대로 값이 같으면 True, 아니라면 False 반환
print(mask)

print(myseries[mask])   # isin 메소드에서 입력한 값에서 같은 요소만 반환