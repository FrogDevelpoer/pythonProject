import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image

plt.rc('font', family='Malgun Gothic')

class Visualization:
    def __init__(self, wordList):
        self.wordList = wordList
        self.wordDict = dict(wordList)  # list를 사전으로 변경
        # print(wordDict)

    def makeWordCloud(self): # 워드 클라우드
        alice_color_file = 'alice_color.png'
        # alice_color_file = 'slice_pizza.jpg'
        alice_coloring = np.array(Image.open(alice_color_file))

        fontpath = 'malgun.ttf'
        wordcloud = WordCloud(font_path=fontpath, mask=alice_coloring, \
                              relative_scaling=0.2, background_color='lightyellow')
        print(self.wordDict)
        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)

        image_colors = ImageColorGenerator(alice_coloring)

        # newwc = wordcloud.recolor(color_func=image_colors, random_state=42)

        plt.imshow(wordcloud)
        plt.axis('off')

        filename = 'myWordCloud.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' 파일이 저장되었습니다.')
        plt.figure(figsize=(16, 8))
        # plt.show()
    # end def makeWordCloud(wordlist)

    def makeBarChart(self): # 막대 그래프 그리기
        barcount = 10  # 막대 갯수 : 10개만 그리겠다.
        xlow, xhigh = - 0.5, barcount - 0.5

        result = self.wordList[:barcount]
        chartdata = []  # 차트 수치
        xdata = []  # 글씨
        mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFF0F0', '#CCFFBB', '#05CCFF', '#11CCFF']

        for idx in range(len(result)):
            chartdata.append(result[idx][1])
            xdata.append(result[idx][0])

            value = str(chartdata[idx]) + '건'  # 예시 : 60건
            # 그래프의 위에 "건수" 표시
            plt.text(x=idx, y=chartdata[idx] - 5, s=value, fontsize=8, horizontalalignment='center')

        plt.xticks(range(barcount), xdata, rotation=45)
        plt.bar(range(barcount), chartdata, align='center', color=mycolor)

        plt.title('상위 ' + str(barcount) + '빈도수')
        plt.xlim([xlow, xhigh])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도수')

        filename = 'myBarChart.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' 파일이 저장되었습니다.')
        # plt.show()
    # end def makeBarChart(wordlist):
# end class Visualization
filename = '문재인대통령신년사.txt'
ko_con_text = open(filename, encoding='UTF-8').read()

from konlpy.tag import Komoran
komo = Komoran(userdic='user_dic.txt')
tokens_ko = komo.nouns(ko_con_text)     # 명사만 추출

stop_word_file = 'stopword.txt'
stop_file = open(stop_word_file, encoding='UTF-8')
stop_words = [word.strip() for word in stop_file.readlines()]
# print(stop_words)
# print('-' * 30)

tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_words]
# print(tokens_ko)
# print('-' * 30)

import nltk
ko = nltk.Text(tokens=tokens_ko)
# print(ko.vocab().most_common(10))   # 단어 사용 빈도수가 가장 많은 10가지 출력

data = ko.vocab().most_common(500)
# print(data)
# print('-' * 30)

wordlist = list()
for word, count in data:
    if count >= 2 and len(word) >= 2:
        wordlist.append((word, count))
# print(wordlist)

visual = Visualization(wordlist)
visual.makeWordCloud()
visual.makeBarChart()
print('fin')
