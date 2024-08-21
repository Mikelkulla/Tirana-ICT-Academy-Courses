import re

line = "From: mikel.kulla84@gmail.com Sat Jan  5 09:14:16 2008"
y = re.findall('^From: .*@([^ ]*)', line)
# "^From: "- start with From: followed by a space
# .*@ - any number of characters until we see an @ sign
# [^ ] - a set of characters that are anything but not blanks
# * - 0 or more times
print(y)