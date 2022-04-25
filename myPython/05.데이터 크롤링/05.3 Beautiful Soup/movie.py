import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class': 'tit3'})
print(tags)
print('-' * 30)

for tag in tags:
    print(tag.a.string)     # 영화 제목만

print('-' * 30)

url_header = '://movie.naver.com'
for tag in tags:
    print(url_header + tag.a['href'])

mytrs = soup.find_all('tr')

no = 0
totallist = []

for one_tr in mytrs:
    title = ''
    up_down = ''
    mytd = one_tr.find('td', attrs={'class': 'title'})
    if mytd is not None:
        no += 1
        newno = str(no).zfill(2)

        mytag = mytd.find('div', attrs={'class': 'tit3'})
        title = mytag.a.string

        mytd = one_tr.select_one('td:nth-of-type(3)')
        myimg = mytd.find('img')
        if myimg.attrs['alt'] == 'up':
            up_down = '상승'
        elif myimg.attrs['alt'] == 'down':
            up_down = '강등'
        else:
            up_down = '불변'

        change = one_tr.find('td', attrs={'class': 'range ac'})
        if change is None:
            pass
        else:
            change = change.string
            totallist.append((newno, title, up_down, change))


mycolumn = ['순위', '제목', '변동', '변동값']

myframe = DataFrame(totallist, columns=mycolumn)
filename = 'naverMovie.csv'
myframe.to_csv(filename, encoding='UTF-8', index=False)
print(filename + '으로 저장완료')
print('fin')
