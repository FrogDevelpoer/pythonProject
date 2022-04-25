# +연산자를 사용하여 리스트를 합친 뒤, 요소의 값을 3으로 나누었을 때 1인 요소만 출력
listA = ('김의찬', '유만식', '이영철')
listB = listA + ('심수련', '윤기석', '노윤희', )


somelist = listA + listB

length = len(somelist)
print(somelist[1:length:3])
