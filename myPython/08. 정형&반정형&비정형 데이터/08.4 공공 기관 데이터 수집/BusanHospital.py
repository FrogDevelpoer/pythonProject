import json, urllib.request, math

def getRequestUrl(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('UTF-8')
    except Exception as err:
        return None
# end def getRquestUrl

def getHospitalData(pageNo, numOfRows):
    # 엔드 포인트
    end_point = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'

    # 일반 인증키
    access_key = 'O8HB5ghnh2d3I5RkSWdTfjbzex4iuOUPnuqA5rBMs4E6dUej3clePMiWy%2BFuEl0jL8KfzzK%2F35bxQpFKdmZuNA%3D%3D'

    parameters = ''
    parameters += '?resultType=json'
    parameters += '&serviceKey=' + access_key
    parameters += '&pageNo=' + str(pageNo)
    parameters += '&numOfRows' + str(numOfRows)

    url = end_point + parameters

    # print(url)

    result = getRequestUrl(url)

    if result == None:
        return None
    else:
        return json.loads(result)
# end def getHospitalData

pageNo = 1
numOfRows = 100
npage = 0

jsonResult = []

while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, npage))
    jsondata = getHospitalData(pageNo, numOfRows)
    # print(jsondata)

    if jsondata['MedicalInstitInfo']['header']['code'] == '00':
        totalCount = jsondata['MedicalInstitInfo']['totalCount']
        print('데이터 총 개수 : %d' % totalCount)

        if totalCount == 0:
            break

        print(len(jsondata['MedicalInstitInfo']['item']))

        for item in jsondata['MedicalInstitInfo']['item']:
            jsonResult.append(item)

        npage = math.ceil(totalCount / numOfRows)

        if pageNo == npage:     # 끝 페이지이면
            break

        pageNo += 1
    else:
        break

# end while
savedFilename = '부산시 의료 기관, 약국 운영시간 정보.json'
with open(savedFilename, 'wt', encoding='UTF-8') as outfile:
    retJson = json.dumps(jsonResult, indent=8, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)

print(savedFilename + ' 파일 저장')