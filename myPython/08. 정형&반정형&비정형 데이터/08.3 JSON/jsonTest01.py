import json

data = {'age': 30, 'name': '홍길동', 'address': '금천 독산동', 'broadcast': {'sbs': 5, 'kbs': 9, 'mbc': 11}}
json_str = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)
print(type(json_str))
print(json_str)

json_data = json.loads(json_str)
print(type(json_data))
print('-' * 30)
print(json_data['name'])
print(json_data['age'])
print(json_data['broadcast']['kbs'])