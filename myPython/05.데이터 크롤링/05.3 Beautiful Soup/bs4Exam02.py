from bs4 import BeautifulSoup

html = open('fruits.html', 'r', encoding='UTF-8')
soup = BeautifulSoup(html, 'html.parser')

# select_one과 find는 비슷한 느낌. css에 접근하기 위해 find 사용
body = soup.select_one('body')  # 1개 찾기
print('-' * 30)
print(body)
print('-' * 30)

print(type(body))
print('-' * 30)

ptag = body.find('p')   # find는 1개 찾기
print(ptag)
print('-' * 30)

print(ptag['class'])    # 속성 읽기
print('-' * 30)

ptag['id'] = 'apple'    # 신규 속성 만들기
print(ptag['id'])

body_tag = soup.find('body')
idx = 0
for child in body_tag.children: # body 태그의 자식 요소들 반환
    idx += 1
    print(str(idx) + '번째 요소')
    print(child)
    print('-' * 30)

mydiv = soup.find('div')
print(mydiv)
print('-' * 30)

print('div의 부모는?')
print(mydiv.parent)
print('-' * 30)

mytag = soup.find('p', attrs={'class': 'hard'}) # find는 가장 첫번째 요소를 반환하지만 attrs를 이용하여 원하는 요소 반환이 가능.
print(mytag)
print('-' * 30)

print('mytag의 부모는?')
print(mytag.find_parent())
print('-' * 30)

parents = mytag.find_parents()
for p in parents:
    print(p.name)