"""
When we encounter a new name, we need to add a new entry in the dictionary and if this
the second or later time we have seen the 'name', we simply add one to the count in the
dictionary under the 'name'
"""

counts = dict()
names = ['csev', 'swen', 'csev', 'zqian', 'cwen']

for name in names :
    # this whole thing is replaced by the .get method
    """if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1"""
    # returns the value of the key (name) in the dictionary if it exists or use the default (0)
    counts[name] = counts.get(name, 0) + 1

print(counts)