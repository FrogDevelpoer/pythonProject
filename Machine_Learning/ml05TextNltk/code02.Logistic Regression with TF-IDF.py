DATA_IN_PATH = './data_in/'
TRAIN_CLEAN_DATA = 'train_clean.csv'

import pandas as pd
train_data = pd.read_csv(DATA_IN_PATH + TRAIN_CLEAN_DATA)
print(train_data.head())

reviews = list(train_data['review'])
sentiments = list(train_data['sentiment'])

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=0.0, analyzer='char', sublinear_tf=True, max_features=5000, ngram_range=(1, 3))

x = vectorizer.fit_transform(reviews)

import numpy as np
y = np.array(sentiments)

features = vectorizer.get_feature_names_out()
print('토큰의 갯수 :', len(features))
print('토큰화된 단어 목록 :', features)

from sklearn.model_selection import train_test_split

RANDOM_SEED = 42
TEST_SPLIT = 0.2

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=TEST_SPLIT, random_state=RANDOM_SEED)

from sklearn.linear_model import LogisticRegression
lgs = LogisticRegression(class_weight='balanced')

lgs.fit(x_train, y_train)

predicted = lgs.predict(x_test)

print('정확도 : %.4f' % lgs.score(x_test, y_test))

TEST_CLEAN_DATA = 'test_clean.csv'
test_data = pd.read_csv(DATA_IN_PATH + TEST_CLEAN_DATA)

testDataVecs = vectorizer.transform(test_data['review'])
test_predicted = lgs.predict(testDataVecs)
print('test_predicted : ', test_predicted)










