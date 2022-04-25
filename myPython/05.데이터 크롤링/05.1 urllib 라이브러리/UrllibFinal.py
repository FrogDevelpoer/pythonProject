import urllib.request

url = 'https://shared-comic.pstatic.net/thumb/webtoon/648419/thumbnail/thumbnail_IMAG10_1421195d-13be-4cde-bcf9-0c78d51c5ea3.jpg'
savename = input('파일 이름을 입력해주세요: ')

result = urllib.request.urlopen(url)

data = result.read()

with open(savename, 'wb') as f:
    f.write(data)
    print(savename + ' 파일로 저장')