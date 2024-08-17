"""
Even though dictionaries are not stored in order, we can write a for loop that
goes through all the entries in a dictionary - actually it goes through all the
keys in the dictionary and looks up the values.
"""

counts = {"chuck": 1, "fred": 42, "Jan": 100}
for key in counts:
    print(key, counts[key])