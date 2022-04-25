wordInfo = {'세탁기': 50, '선풍기': 30, '청소기': 40, '냉장고': 60}

myxticks = sorted(wordInfo, key=wordInfo.get, reverse=True)     # 그래프의 x축으로ㅓ 사용
# reverse : True면 내림차순 False면 오름차순
# key=dict.get : 딕셔너리의 key 값을 가져옴

print(myxticks)

reverse_key = sorted(wordInfo.keys(), reverse=True)     # 가나다 역순으로 출력
print(reverse_key)

chartdata = sorted(wordInfo.values(), reverse=True)     # 그래프의 눈금으로 사용
print(chartdata)
