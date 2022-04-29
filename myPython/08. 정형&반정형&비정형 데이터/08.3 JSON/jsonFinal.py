import json

filename = '김주혁_naver_news.json'
myfile = open(filename, 'rt', encoding='UTF-8')
myfile = myfile.read()

jsondata = json.loads(myfile)

for oneitem in jsondata:
    print('타이틀 : ', oneitem['title'])
    print('설명 : ', oneitem['description'])
    print(' ')