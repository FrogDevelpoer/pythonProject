import urllib.request

url = 'https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg'
savename = 'urldownload02.png'

result = urllib.request.urlopen(url)
print(type(result))

data = result.read()
print(type(data))
print(data)

# with 구문을 파일 입출력에 사용하면 close() 메소드를 암시적으로
# wb: write binary
with open(savename, 'wb') as f:     # f는 open된 파일 객체의 별칭
    f.write(data)
    print(savename + ' 파일로 저장')