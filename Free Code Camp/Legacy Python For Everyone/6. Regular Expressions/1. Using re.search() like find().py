import re
# using re.search() like find()
fhand = open("text.txt")
for line in fhand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)
print("*"*20)
fhand = open("text.txt")
# using re.search() like startswith()
for line in fhand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)
