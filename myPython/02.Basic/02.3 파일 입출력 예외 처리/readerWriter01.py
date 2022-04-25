print('파일을 읽기 모드로 오픈합니다.')

myfile01 = open('sample.txt', 'rt', encoding='UTF-8')

linelists = myfile01.readlines()     # readlines는 모든 내용을 읽어서 List 형태로 만들어줌
myfile01.close()

print(type(linelists))

total = 0  # 총합
for one in linelists:
    print(one)
    score = int(one)
    total += score

print('총점 : %d ' % total)

average = total / len(linelists)
print('평균 : %.2f ' % average)

print('파일에 기록')
myfile02 = open('result.txt', 'wt', encoding='UTF-8')

myfile02.write('총점 : ' + str(total) + '\n')
myfile02.write('평균 : ' + str(average))

myfile02.close()
print('파일 쓰기가 완료되었습니다.')
