from konlpy.tag import Komoran

sentence = '코로나 바이러스 태블릿 PC, 뽕뺭, 가나다라'
print('사전 사용 전')
komo = Komoran()
print(komo.pos(sentence))
print('-' * 30)

print('사전 사용 후')
komo = Komoran(userdic='user_dic.txt')
print(komo.pos(sentence))
print('-' * 30)

print('komo.nouns')
print(komo.nouns(sentence))
print('-' * 30)

print('komo.morphs')
print(komo.morphs(sentence))
print('-' * 30)