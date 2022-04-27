import folium

latitude = 37.55    # 위도
longitude = 126.98  # 경도

map_osm = folium.Map(location=[latitude, longitude])
print(type(map_osm))
map_osm.save('map1.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=16)
map_osm.save('map2.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17, tiles='Stamen Terrain')
map_osm.save('map3.html')

map_osm = folium.Map(location=[latitude, longitude])
folium.Marker([latitude, longitude], popup='서울역어딘가').add_to(map_osm)
map_osm.save('map4.html')

map_osm = folium.Map(location=[latitude, longitude], zoom_start=17)
folium.Marker([latitude, longitude], popup='서울역어딘가',
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
folium.CircleMarker([latitude, longitude], radius=150, color='blue', fill_color='red', popup='어디야').add_to(map_osm)
map_osm.save('map5.html')

print('fin')