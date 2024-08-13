# we can read the whole file (newlines and all) into a single string

f_hand = open("mbox.txt")
inp = f_hand.read()
print(len(inp))

print(inp[0:19])