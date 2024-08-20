fhand = open("donald.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

print(sorted([(v, k) for k, v in counts.items()], reverse=True))
