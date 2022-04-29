import urllib.request

def getRequestUrl(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('UTF-8')
    except Exception as err:
        return None
# end def g etRequestUrl

def getCultureSchedule(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6480000/gyeongnamculture/'

    access_key = 'O8HB5ghnh2d3I5RkSWdTfjbzex4iuOUPnuqA5rBMs4E6dUej3clePMiWy%2BFuEl0jL8KfzzK%2F35bxQpFKdmZuNA%3D%3D'

    parameters = '?'
    parameters += 'serviceKey' + access_key
    parameters += '&pageNo' + str(pageNo)
    parameters += '&numOfRows=' + str(numOfRows)

    url = end_point + parameters
    # print(url)

    result = getRequestUrl(url)

    if result == None:
        return None
    else:
        return result
# end def getCultureSchedule

import xml.etree.ElementTree as ET

pageNo = 1
numOfRows = 4
nPage = 0

datalist = []

while(True):
    xmlData = getCultureSchedule(pageNo, numOfRows)
    print(xmlData)