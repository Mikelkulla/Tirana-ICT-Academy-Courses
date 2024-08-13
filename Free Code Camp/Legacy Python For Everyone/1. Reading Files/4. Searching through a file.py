""" We can put an if statement in our for loop to
    only print lines that meet some criteria
"""

f_hand = open("mbox.txt")
for line in f_hand:
    if line.startswith("Faculty"):
        print(line)