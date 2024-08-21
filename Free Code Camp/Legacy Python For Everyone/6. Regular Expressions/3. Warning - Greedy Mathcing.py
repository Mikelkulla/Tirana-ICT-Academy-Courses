import re
x = "From: Using the:"
y = re.findall("^F.+:", x)
# in this case the exprasion is greedy and will return the largest
# that starts with "F" and has some characters and a :
# it will return the whole between
print(y)
z = re.findall("^F.+?:",x)
# "?" removes the greed and returns the short one
# "^F" starts with F, .+? - one or more character but not greedy
# : - last character in the match is
print(z)