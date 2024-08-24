import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
countslist = list()
for k, v in counts.items():
    countslist.append((v,k))
countslist = sorted(countslist, reverse=True)[:10]
print(countslist)