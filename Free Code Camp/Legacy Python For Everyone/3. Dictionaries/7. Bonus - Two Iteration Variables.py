"""
We loop through the key-value pairs in a dictionary using two iteration variables

Each iteration, the first variable is the key and second variable is the corresponding
value for the key.
"""

jjj = {'chuck': 1, 'fred': 40, 'jan': 100}
for aaa,bbb in jjj.items():
    print(aaa.capitalize(),bbb)