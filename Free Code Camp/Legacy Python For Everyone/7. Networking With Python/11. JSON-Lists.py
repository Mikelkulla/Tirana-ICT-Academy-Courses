import json
data = """[
    {
        "id": "001",
        "x": "2",
        "name": "Mikel"
    },
    {
        "id": "002",
        "x": "7",
        "name": "Chuck"
    }
]"""
info = json.loads(data)
print("User count:", len(info))
for item in info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('Attribute:', item['x'])

