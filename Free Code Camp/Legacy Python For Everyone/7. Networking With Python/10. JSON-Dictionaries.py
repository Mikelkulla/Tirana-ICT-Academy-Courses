"""
JSON represents data as nested "lists" and "dictionaries"
"""

import json
data = """{
    "name": "Mikel",
    "phone": {
        "type": "intl",
        "number": "+355 67 75 41 945"
    },
    "email": {
        "hide": "yes"
    }
}"""
# parse the data and returns a dictionary
info = json.loads(data)
for k,v in info.items():
    print(k,v)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])