"""
We can take advantage of the ability to sort a list of tuples to
get a sorted version of dictionary

First we sort the dictionary by the key using the items() method
and sorted() function
"""
d = {'a': 10, 'c': 22, 'b': 1}
print(d.items())
print(sorted(d.items()))
