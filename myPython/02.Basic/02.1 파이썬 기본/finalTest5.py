# 리스트를 이용하여 딕셔너리 만들기
fruits = {('바나나', 10), ('수박', 20), ('오렌지', 15)}

mydict = dict()

for key, value in fruits:
    mydict[key] = value

print(mydict)
