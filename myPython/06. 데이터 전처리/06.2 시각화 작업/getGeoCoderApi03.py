import folium, requests

address = '서울 특별시 금천구 독산동 가산로 94'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

api_key = 'b9900bdc06119144d3b02ae63fd650ff'
header = {'Authorization': 'KakaoAK ' + api_key}

def getGoocoder(address):
    result = ""
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

address_latlng = getGoocoder(address)
latitude = address_latlng[0]
longitude = address_latlng[1]

print('주소지 :', address)
print('위도 :', latitude)
print('경도 :', longitude)

homeadd = '우리집'
foli_map = folium.Map(location=[latitude, longitude], zoom_start=17)
myicon = folium.Icon(color='red', icon='info-sign')
folium.Marker([latitude, longitude], popup=homeadd, \
              icon=myicon).add_to(foli_map)

folium.CircleMarker([latitude, longitude], radius=300, color='blue', \
            fill_color='red', fill=False, popup=homeadd).add_to(foli_map)

foli_map.save('my_map_graph.html')
print('파일 저장 완료')