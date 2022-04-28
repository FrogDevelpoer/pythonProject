filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='UTF-8')
text = myfile.read()
print(type(text))
print('-'*30)

from wordcloud import WordCloud

wordcloud = WordCloud()
wordcloud = wordcloud.generate(text)    # 워드 클라우드를 위한 데이터 준비 완료
print(type(wordcloud))
print('-'*30)

bindo = wordcloud.words_
print(type(bindo))
print('-'*30)

# print(bindo)
# print('-'*30)

# 사전이므로 정렬이 필요
sorteddata = sorted(bindo.items(), key=lambda x: x[1], reverse=True)
chartdata = sorteddata[0:10]
print('-'*30)

xtick = []  # x축에 놓이는 문자열
chart = []  # 그래프에 그려질 데이터

for item in chartdata:
    xtick.append(item[0])
    chart.append(item[1])

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

plt.bar(xtick, chart)
plt.title('상위 빈도 top 10')
filename = 'wordCloudEx01_01.png'
plt.savefig(filename)
print(filename + ' 저장 완료')

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud)   # image show
plt.axis('off')     # 축 없애기
filename = 'wordCloudEx01_02.png'
plt.savefig(filename)
print(filename + ' 저장 완료')
