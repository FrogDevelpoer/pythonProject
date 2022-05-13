content = ['우리 아버지 이름은 홍길동', '홍길동 여자 친구 이름은 심순애 심순애', '여자 친구 있나요']

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=1, stop_words=['친구'])

print(type(vectorizer))
print('-' * 30)

print('단어 사전 만들기')
matrix = vectorizer.fit(content)
print(type(matrix))
print('-' * 30)

print("matrix.vocabulary_")
print(matrix.vocabulary_)
print('-' * 30)

print('단어 사전 정렬')
print(sorted(matrix.vocabulary_.items()))
print('-' * 30)

print('단어 목록 보기')
feature = vectorizer.get_feature_names_out()
print(type(feature))
print(feature)
print('-' * 30)

print('불용어 목록 보기')
print(vectorizer.get_stop_words())
print('-' * 30)

for data in content:
    myarray = vectorizer.transform([data]).toarray()
    print(data)
    print(type(myarray))
    print(myarray)
    print('-' * 30)

