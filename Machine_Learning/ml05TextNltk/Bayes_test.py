import sys, math
from PyKomoran import *

class BayesianFilter:
    def __init__(self):
        self.words = set()
        self.words_dict = dict()
        self.category_dict = {}
    # end def __init__

    def mysplit(self, text):
        komoran = Komoran('STABLE')
        result = komoran.get_nouns(text)
        return result
    # end def mysplit

    def add(self, text, category):  # bf.add("text", "category")
        word_list = self.mysplit(text)
        # print('이메일 제목 : ', text)
        # print('단어 리스트 : ', word_list)

        for word in word_list:
            self.insert_word(word, category)
        self.insert_category(category)
    # end def add

    def insert_word(self, word, category):
        # print(word + ' / ' + category)
        self.words.add(word)

        if not category in self.words_dict:
            self.words_dict[category] = {}

        if not word in self.words_dict[category]:
            self.words_dict[category][word] = 0
        self.words_dict[category][word] += 1

    # end def insert_word

    def insert_category(self, category):
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1
    # end def insert_category

    def showInfo(self):
        print('self.words')
        print(self.words)

        print('self.words_dict')
        print(self.words_dict)

        print('self.category_dict')
        print(self.category_dict)
    # end def showInfo

    def score(self, words, category):
        # 카테고리 점수
        bunmo = sum(self.category_dict.values())
        bunja = self.category_dict[category]
        score = math.log(bunja/bunmo)

        for word in words:
            if word in self.words_dict[category]:
                bunja = self.words_dict[category][word]
            else:
                bunja = 0
            bunja += 1

            bunmo = sum(self.words_dict[category].values()) + len(self.words)
            score += math.log(bunja/bunmo)

        return score
    # end def score

    def predict(self, checkmail):
        best_category = None    # 어떤 메일인가(광고/일반)
        max_score = -sys.maxsize  # 가장 적은 수를 최대라고 가정
        words = self.mysplit(checkmail)

        # print(words)

        score_list = []     # 카테고리별 점수를 저장할 리스트

        for category in self.category_dict.keys():
            score = self.score(words, category)
            score_list.append((category, score))

            print('현 카테고리 : %s' % category)
            print('점수 : %f' % score)
            print('최고 점수 : %f' % max_score)

            if score > max_score :
                max_score = score
                best_category = category

        return best_category, score_list
    # end def predict
# end class

bf = BayesianFilter()   # 객체 생성

# 다음 데이터를 이용하여 텍스트 학습을 진행 합니다.
bf.add("파격 세일", "광고 메일")
bf.add("오늘 일정 확인", "일반 메일")
bf.add("파격 세일 - 오늘까지만 30% 할인", "광고 메일")
bf.add("쿠폰 선물 & 무료 배송", "광고 메일")
bf.add("신세계 백화점 세일", "광고 메일")
bf.add("봄과 함께 찾아온 따뜻한 신제품 소식", "광고 메일")
bf.add("인기 제품 기간 한정 세일", "광고 메일")
bf.add("프로젝트 진행 상황 보고", "일반 메일")
bf.add("계약 잘 부탁드립니다", "일반 메일")
bf.add("회의 일정이 등록되었습니다.", "일반 메일")
bf.add("오늘 일정이 없습니다.", "일반 메일")

# bf.showInfo()

# email = '재고 정리 할인 무료 배송'
emaillist = ['재고 정리 할인 무료 배송', '내일 일정']
for email in emaillist:
    best_category, scorelist = bf.predict(email)
    print("메일 제목이 '%s'인 메일은 '%s'입니다." % (email, best_category))
    print(scorelist)
    print('-' * 30)

print('fin')