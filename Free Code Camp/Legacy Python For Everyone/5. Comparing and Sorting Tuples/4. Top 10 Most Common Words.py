
fhand = open("donald.txt")
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
print(counts)
templist = []
for k, v in counts.items():
    newtup = (v,k)
    templist.append(newtup)

templist = sorted(templist, reverse=True)
i = 1
for v,k in templist[:10]:
    print(i,"-", v,k)
    i +=1