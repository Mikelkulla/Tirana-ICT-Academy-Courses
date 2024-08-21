"""
re.search() - returns True/False depending on whether the string matches the regulart expression

if we actually want the matching string to be extracted, we use re.findall()
"""
import re
x = "My 2 favourite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
#[0-9] gjen nje karakter nga 0 ne 9, + kerkon per disa numra resht
print(y)