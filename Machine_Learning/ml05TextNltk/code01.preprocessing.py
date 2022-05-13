import zipfile

DATA_IN_PATH = './data_in/'

# file_list = ['labeledTrainData.tsv.zip', 'testData.tsv.zip', 'unlabeledTrainData.tsv.zip']
#
# for file in file_list:
#     onefile=zipfile.ZipFile(DATA_IN_PATH + file, mode='r')
#     onefile.extractall(DATA_IN_PATH)
#     onefile.close()
# end for

# import os
# print('파일 사이즈 확인')
# for file in os.listdir(DATA_IN_PATH):
#     if 'tsv' in file and 'zip' not in file:
#         filezie = round(os.path.getsize(DATA_IN_PATH + file) / 1000000, 2)
#         message = file.ljust(30) + str(filezie) + 'MB'
#         print(message)

import pandas as pd

train_data = pd.read_csv(DATA_IN_PATH + 'labeledTrainData.tsv.zip', header=0, delimiter='\t', quoting=3)
# print('train_data.head()')
# print(train_data.head())
# print('-' * 30)
#
# print('훈련 데이터 개수 : {}'.format(len(train_data)))
# print('-' * 30)
#
# print('reviews 컬럼의 문자열 길이 확인')
train_length = train_data['review'].apply(len)
# print('train_length')
# print(train_length.head())
# print('-' * 30)
#
# print(train_length.describe())
# print('-' * 30)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
#
# print('히스토그램 그리기')
# plt.figure(figsize=(12, 5))
# plt.hist(train_length, bins=200, alpha=0.5, color='r', label='word')
# plt.yscale('log', nonpositive='clip')
# plt.title('log-histogram of length of reviews')
# plt.xlabel('length of review')
# plt.ylabel('number of review')
# filename = 'code01.preprocessing_01.png'
# plt.savefig(filename)
# print(filename + ' 저장 완료')
#
import numpy as np
#
# print('reviews 컬럼의 문자열에 대한 통계 정보')
# print('리뷰 길이 최대 값 : {}'.format(np.max(train_length)))
# print('리뷰 길이 최소 값 : {}'.format(np.min(train_length)))
# print('리뷰 길이 평균 값 : {:.2f}'.format(np.mean(train_length)))
# print('리뷰 길이 표준 편차 : {}'.format(np.std(train_length)))
# print('리뷰 길이 중간 값 : {}'.format(np.median(train_length)))
#
# print('사분위수 정보')
# print('리뷰 길이 제 1사분위 값 : {}'.format(np.percentile(train_length, 25)))
# print('리뷰 길이 제 3사분위 값 : {}'.format(np.percentile(train_length, 25)))
#
# print('상자 수염(boxplot) 그리기')
# plt.figure(figsize=(12, 5))
# plt.boxplot(train_length, labels=['counts'], showmeans=True)
# plt.title('boxplot of length of reviews')
# filename = 'code01.preprocessing_02.png'
# plt.savefig(filename)
# print(filename + ' 저장 완료')

# 워드 클라우드
# from wordcloud import WordCloud
# clouddata = ' '.join(train_data['review'])
# cloud = WordCloud(width=800, height=600).generate(clouddata)
#
# plt.figure(figsize=(12, 5))
# plt.imshow(cloud)
# plt.axis('off')
# filename = 'code01.preprocessing_03.png'
# plt.savefig(filename)
# print(filename + ' 저장 완료')

#########################################

# print('긍정과 부정 데이터의 분포')
# bindo = train_data['sentiment'].value_counts()
# print(bindo)
# print('positive 리뷰 개수 : {}'.format(bindo[1]))
# print('negative 리뷰 개수 : {}'.format(bindo[0]))
#
# import seaborn as sns
# fig, axe = plt.subplots()
# sns.countplot(train_data['sentiment'])      # countplot : 빈도를 토대로 막대 그래프를 그려줌
# plt.title('긍정/부정 데이터의 분포')
# filename = 'code01.preprocessing_04.png'
# plt.savefig(filename)
# print(filename + ' 저장 완료')
#
# print('리뷰 단어들의 개수 데이터 확인하기')
split_lambda = lambda x : len(x.split(' '))
# train_word_counts = train_data['review'].apply(split_lambda)
# print('split_word_counts.head()')
# print(train_word_counts.head())
# print('-' * 30)
#
# print('히스토그램 그리기')
# plt.figure(figsize=(12, 5))
# plt.hist(train_word_counts, bins=50, color='r', label='train')
# plt.yscale('log', nonpositive='clip')
# plt.title('각 리뷰의 단어 개수 분포')
# plt.xlabel('length of word')
# plt.ylabel('number of review')
# filename = 'code01.preprocessing_05.png'
# plt.savefig(filename)
# print(filename + ' 저장 완료')
#
# # print('reviews 컬럼의 문자열에 대한 통계 정보')
# # print('리뷰 단어 개수 최대 값 : {}'.format(np.max(train_word_counts)))
# # print('리뷰 단어 개수 최소 값 : {}'.format(np.min(train_word_counts)))
# # print('리뷰 단어 개수 평균 값 : {:.2f}'.format(np.mean(train_word_counts)))
# # print('리뷰 단어 개수 표준 편차 : {}'.format(np.std(train_word_counts)))
# # print('리뷰 단어 개수 중간 값 : {}'.format(np.median(train_word_counts)))
# #
# # print('사분위수 정보')
# # print('리뷰 단어 개수 제 1사분위 값 : {}'.format(np.percentile(train_word_counts, 25)))
# # print('리뷰 단어 개수 제 3사분위 값 : {}'.format(np.percentile(train_word_counts, 75)))
#
# # 특수 문자, 대소문자, 마침표, 물음표, 숫자 등에 대한 비율
# review = train_data['review']
# question = np.mean(review.apply(lambda x: '?' in x))  # 물음표
# fullstop = np.mean(review.apply(lambda x: '.' in x))  # 마침표
# capital_first = np.mean(review.apply(lambda x: x[0].isupper()))  # 첫 글자가 대문자인가?
# capitals=np.mean(review.apply(lambda x: max([y.isupper() for y in x])))  # 대문자가 존재하는가?
# digit = np.mean(review.apply(lambda x: max([y.isdigit() for y in x])))  # 숫자가 존재하는가?
#
# # print('물음표가 있는 review : {:.2f}%'.format(question))
# # print('마침표가 있는 review : {:.2f}%'.format(fullstop))
# # print('첫 글자가 대문자인 review : {:.2f}%'.format(capital_first))
# # print('대문자가 있는 review : {:.2f}%'.format(capitals))
# # print('숫자가 있는 review : {:.2f}%'.format(digit))
#
# print('데이터 전처리를 수행')
# train_data = pd.read_csv(DATA_IN_PATH + 'labeledTrainData.tsv.zip', header=0, delimiter='\t', quoting=3)
#
# # 1번째 데이터
review = train_data['review'][0]
# print(review)

# pip install html5lib
from bs4 import BeautifulSoup
review_text = BeautifulSoup(review, 'html5lib').get_text()

import re
regEx = '[^a-zA-Z]'
review_text = re.sub(regEx, ' ', review_text)  # sub : substitude(치환)

review_text = review_text.lower()
print(review_text)
print('-' * 30)

# import nltk
# nltk.download('stopwords')

print('불용어 제거')
# nltk : National Language ToolKit
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
print('stop_words')
print(stop_words)
print('-' * 30)

words = review_text.split()
words = [w for w in words if w in stop_words]
print('불용어 제거 후 결과물')
print(words)
print('-' * 30)

clean_view = ' '.join(words)
print('전처리된 단어들을 하나로 다시 합치기')
print(clean_view)
print('-' * 30)

# 전처리를 수행해주는 범용 사용자 정의 함수
def preprocessing(review, remove_stopwords = False):
    review_text = BeautifulSoup(review, 'html5lib').get_text()
    review_text = re.sub(regEx, ' ', review_text)
    words = review_text.lower().split()

    if remove_stopwords :
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if w in stop_words]
    # end if

    clean_view = ' '.join(words)
    return clean_view
# end def preprocessing

print('모든 행에 대하여 전처리 중...')
clean_train_reviews = []    # 전처리가 완료된 데이터 셋

for review in train_data['review']:
    clean_train_reviews.append(preprocessing(review, remove_stopwords=True))

print('모든 행에 대하여 전처리 완료')

print('전처리된 데이터를 sentiment 컬럼과 함께 csv파일에 저장')
mydict = {'review':clean_train_reviews, 'sentiment': train_data['sentiment']}
clean_train_df = pd.DataFrame(mydict)

filename = DATA_IN_PATH + 'train_clean.csv'
clean_train_df.to_csv(filename, index=False)

from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()

tokenizer.fit_on_texts(clean_train_reviews)
text_sequence = tokenizer.texts_to_sequences(clean_train_reviews)
print('text_sequence[0]')
print(text_sequence[0])

word_vocab = tokenizer.word_index
print('전체 단어 개수 : ', len(word_vocab) + 1)
print('10개만 출력')
idx = 0
for key, value in word_vocab.items():
    idx += 1
    print(key + ':' + str(value))
    if idx == 10:
        break
# end for

# 단어 사전과 전체 단어 개수를 json으로 저장하기
data_config = {}
data_config['vocab'] = word_vocab   # 단어 사전
data_config['vocab_size'] = len(word_vocab)     # 전체 단어 개수

import json
json.dump(data_config, open(DATA_IN_PATH + 'data_config.json', 'w'), ensure_ascii=False)

from keras.preprocessing.sequence import pad_sequences

MAX_SEQUENCE_LENGTH = 174   # 단어 길이의 평균 값

# x_train
train_inputs = pad_sequences(text_sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post')
print('train_inputs.shape', train_inputs.shape)

# y_train
import numpy as np
train_labels = np.array(train_data['sentiment'])
print('train_label.shape', train_labels.shape)

# 전처리된 데이터를 넘파일 파일 형식으로 저장
np.save(open(DATA_IN_PATH + 'train_input.npy', 'wb'), train_inputs)
np.save(open(DATA_IN_PATH + 'train_labels.npy', 'wb'), train_labels)

# 테스트용 데이터도 동일하게 처리합니다.
test_data=pd.read_csv(DATA_IN_PATH + 'testData.tsv', header=0, delimiter='\t', quoting=3)

clean_test_reviews=[]
for review in test_data['review']:
    clean_test_reviews.append(preprocessing(review, True))

mydict={'review':clean_test_reviews, 'id':test_data['id']}
clean_test_df=pd.DataFrame(mydict)

filename = DATA_IN_PATH + 'test_clean.csv'
clean_test_df.to_csv(filename, index=False)
print(filename + ' 파일이 저장되었습니다.')

text_sequences=tokenizer.texts_to_sequences(clean_test_reviews)
test_inputs=pad_sequences(text_sequences, maxlen=MAX_SEQUENCE_LENGTH, padding='post')

np.save(open(DATA_IN_PATH + 'test_inputs.npy', 'wb'), test_inputs)

test_id=np.array(test_data['id'])
np.save(open(DATA_IN_PATH + 'test_id.npy', 'wb'), test_id)


print('fin')