"""
- We can strip the whitespaces from the right hand side of the string
  using rstrip(), from the string library
- The new line is considered 'white space' and is stripped
"""

f_hand = open("mbox.txt")
for line in f_hand:
    line = line.rstrip()
    if line.startswith("Name:"):
        print(line)