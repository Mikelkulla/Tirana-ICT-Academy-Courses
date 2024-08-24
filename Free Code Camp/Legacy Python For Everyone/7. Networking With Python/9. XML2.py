
import xml.etree.ElementTree as ET
input = """<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Mikel</name>
        </user>
        <user x = "7">
            <id>002</id>
            <name>Chuck</name>
        </user>
    </users>
</stuff>"""
# creates the elemnt tree from the string we took
stuff = ET.fromstring(input)
# find all tags users/user and add them into a list
lst = stuff.findall("users/user")
print("User Count:", len(lst))
print("*"*20)
for item in lst:
    print("Name:", item.find("name").text)
    print("ID:", item.find("id").text)
    print("Attribute:", item.get("x"))
    print("_"*20)
print("*"*20)
for i in range(len(lst)):
    print(lst[i].find("name").text)
    print(lst[i].find("id").text)
    print(lst[i].get("x"))


