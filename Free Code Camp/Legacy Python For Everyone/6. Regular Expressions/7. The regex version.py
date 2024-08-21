import re

line = "From: mikel.kulla84@gmail.com Sat Jan  5 09:14:16 2008"
y = re.findall("@([^ ]*)", line)
# @ - look through a string until it find the "@ sign"
# [^ ] - a set of characters that are anything but not blanks
# * - 0 or more times
print(y)