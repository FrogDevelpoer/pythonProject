import json

def get_Json_data():
    filename = 'jumsu.json'
    myfile = open(filename, 'rt', encoding='UTF-8')
    myfile = myfile.read()

    jsondata = json.loads(myfile)
    # print(type(jsondata))
    # print(jsondata)

    for oneitem in jsondata:
        print('이름 : ', oneitem['name'])
        kor = float(oneitem['kor'])
        math = float(oneitem['math'])
        eng = float(oneitem['eng'])

        total = kor + eng + math
        print('국어', kor)
        print('영어', eng)
        print('수학', math)
        print('총점', total)

        if 'hello' in oneitem.keys():
            hello = oneitem['hello']
            print('메세지 : ', hello)

        _gender = oneitem['gender'].upper()
        if _gender == 'M':
            gender = '남자'
        elif _gender == 'F':
            gender = '여자'
        print('성별 : ', gender)
        print('-' * 30)

get_Json_data()