# 'key': value
dictionary = {'김유신': 50, '윤봉길': 40, '김구': 60}

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print('{}의 나이는 {}살입니다.'.format(key, value))

for key in dictionary.keys():
    print('{}의 나이는 {}살입니다.'.format(key, dictionary[key])) # dictionary[key]는 자바의 get 메소드와 유사한 느낌

findkey = '유관순'
if findkey in dictionary:
    print(findkey + '은(는) 존재함')
else:
    print(findkey + '은(는) 존재하지 않음')

result = dictionary.pop('김구')   # 김구의 값만 제외하고 출력
print(dictionary)
print(result)

dictionary.clear()  # 배열의 모든 값 비우기
print(dictionary)
