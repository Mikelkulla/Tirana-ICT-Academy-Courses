"""
We can look for a string anywhere in a line as our selection criteria
"""

f_hand = open("mbox.txt")
for line in f_hand:
    line = line.rstrip()
    if not 'gmail.com' in line:
        continue
    print(line)