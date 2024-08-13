"""
We can conveniently skip a line by using continue statement
"""

f_hand = open("mbox.txt")
for line in f_hand:
    line = line.rstrip()
    if not line.startswith("Master Degree:"):
        continue
    print(line)