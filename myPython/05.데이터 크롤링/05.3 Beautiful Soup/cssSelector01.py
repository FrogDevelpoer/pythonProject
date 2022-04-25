from bs4 import BeautifulSoup

filename = 'css01.html'
myencoding = 'UTF-8'
myparser = 'html.parser'

html = open(filename, encoding=myencoding)
soup = BeautifulSoup(html, myparser)
print(type(soup))
print('-' * 30)

h1 = soup.select_one('div#cartoon > h1').string  # div의 아이디가 cartoon인 것중 h1 태그의 내용
print('h1 = ', h1)
print('-' * 30)

li_list = soup.select('div#cartoon > ul.elements > li')
for li in li_list:
    print('li = ', li.string)

print('-' * 30)
choice = lambda x: print(soup.select_one(x).string)
choice('#item5')
choice('li#item4')
choice('ul > li#item3')
choice('#itemlist #item2')
choice('#itemlist > #item3')
choice('ul#itemlist > li#item2')
choice('li[id="item1"]')
choice('li:nth-of-type(4)')
print('-' * 30)

# .string 차이
print(soup.select('li')[1].string)
print(soup.select('li')[1])
print('-' * 30)

print(soup.find_all('li')[4].string)
print('-' * 30)

mytag = soup.select_one('div#cartoon > ul.elements')
print(mytag)
print('-' * 30)

mystring = mytag.select_one('li:nth-of-type(3)').string
print(mystring)
print('-' * 30)

mytag = soup.select_one('ul#itemlist')
mystring = mytag.select_one('li:nth-of-type(4)').string
print(mystring)
print('-' * 30)

print(soup.select('#vegatables > li[class="us"]')[0].string)
print('-' * 30)

print(soup.select('#vegatables > li.us')[1].string)
print('-' * 30)

result = soup.select('a[href$=".com"]')
for item in result:
    print(item['href'])
print('-' * 30)

result = soup.select('a[href*="daum"]')
for item in result:
    print(item['href'])
print('-' * 30)

cond = {'id': 'ko', 'class': 'cn'}
print(soup.find('li', cond).string)
print('-' * 30)

print(soup.find(id='vegatables').find('li', cond).string)
print('-' * 30)

import re
li = soup.find_all(href=re.compile('^https://'))
for e in li:
    print(e.attrs['href'])

