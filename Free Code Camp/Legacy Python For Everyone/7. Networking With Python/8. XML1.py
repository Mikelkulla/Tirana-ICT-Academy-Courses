import xml.etree.ElementTree as ET

data1 = '''<person>
    <name>Mikel</name>
    <phone>+355 67 75 41 945</phone>
    <email hide = "Yes"/>
</person>'''
tree = ET.fromstring(data1)
print("Name:", tree.find('name').text)
print("Attr:", tree.find('email').get('hide'))