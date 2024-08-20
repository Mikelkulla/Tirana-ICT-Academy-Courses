"""
If we could construct a list of tuples of the form (value,key) we could sort by value

We do this with a for loop that creates a list of tuples
"""
d = {'a': 10, 'c': 22, 'b': 1}
temp = list()
for k,v in d.items():
    temp.append( (v, k) )
print(temp)

temp = sorted(temp, reverse=True)
print(temp)