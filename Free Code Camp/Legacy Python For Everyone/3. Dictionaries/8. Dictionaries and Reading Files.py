name = input("Enter File Name:")
fhand = open(name)

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
bigcounts = None
bigword = None
for word, count in counts.items():
    if bigcounts is None or count > bigcounts:
        bigword = word
        bigcounts = count

print(bigword, bigcounts)
