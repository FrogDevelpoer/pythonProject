import urllib.request

url = 'https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg'
savename = 'urldownload.png'

urllib.request.urlretrieve(url, savename)
print('웹에 있는 이미지 ' + url + '를', end='')
print(savename + ' 파일로 저장')