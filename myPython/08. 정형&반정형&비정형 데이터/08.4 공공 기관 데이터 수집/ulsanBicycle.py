import urllib.request, math

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            return response.read().decode('UTF-8')
    except Exception as err :
        print(err)
        return None
# end def getRequestUrl

def getBicycleData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6310000/ulsanbicyclepath/getUlsanbicyclepathList'

    access_key = 'vbActpiUEDfK7G%2BT4AUaypDlZyjlk2AYnp6OVn42%2FFj7o0GciljiCbOofZu%2Btu8uMbKZ6fPVhNOTe0rB6ir9BQ%3D%3D'

    parameters = '?'
    parameters += 'serviceKey=' + access_key
    parameters += '&pageNo=' + str(pageNo)
    parameters += '&numOfRows=' + str(numOfRows)

    url = end_point + parameters

    result = getRequestUrl(url)
    if result == None :
        return None
    else :
        return result

# end def GetBicycleData

pageNo = 1
numOfRows = 2
nPage = 0

import xml.etree.ElementTree as ET

dataList = []

while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    xmldata = getBicycleData(pageNo, numOfRows)
    # print(xmldata)
    xmlTree = ET.fromstring(xmldata)

    if (xmlTree.find('header').find('resultMsg').text == 'success') :
        totalCount = int(xmlTree.find('body').find('totalCount').text)
        # print('총개수 : %d' % totalCount)

        if totalCount == 0 :
            break

        listTree = xmlTree.find('body').find('data').findall('list')

        for node in listTree:
            bikeFirstLanes = node.find("bikeFirstLanes").text
            bikeFirstLanesRatio = node.find("bikeFirstLanesRatio").text
            bikeLanesRatio = node.find("bikeLanesRatio").text
            bikeOnlyLanes = node.find("bikeOnlyLanes")
            if bikeOnlyLanes == None :
                bikeOnlyLanes = ""
            else :
                bikeOnlyLanes = bikeOnlyLanes.text
            bikeOnlyLanesRatio = node.find("bikeOnlyLanesRatio").text
            cycleRoute = node.find("cycleRoute").text
            entId = node.find("entId").text
            gugun = node.find("gugun").text
            pedestrianBikeLanes = node.find("pedestrianBikeLanes").text
            pedestrianBikeLanesRatio = node.find("pedestrianBikeLanesRatio").text

            onedict = {'자전거우선도로':bikeFirstLanes, \
                       '자전거우선도로비율':bikeFirstLanesRatio, '자전거전용도로비율':bikeLanesRatio, \
                       '자전거전용차로':bikeOnlyLanes, '자전거전용차로비율':bikeOnlyLanesRatio, \
                       '자전거전용도로':cycleRoute, '고유번호':entId, '군구':gugun, \
                       '자전거보행자겸용도로':pedestrianBikeLanes, '자전거보행자겸용도로비율':pedestrianBikeLanesRatio}
            dataList.append(onedict)

        nPage = math.ceil(totalCount/numOfRows)
        if pageNo == nPage :
            break

        pageNo += 1
    else :
        break
# end while

import pandas as pd
savedFilename = 'ulsanByke.csv'
myfrmae = pd.DataFrame(dataList)
myfrmae.to_csv(savedFilename)
print(savedFilename +  ' 파일 저장 완료')
















