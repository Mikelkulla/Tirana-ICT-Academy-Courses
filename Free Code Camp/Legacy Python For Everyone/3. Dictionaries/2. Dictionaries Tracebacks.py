"""
It is an error to reference a key that doesnt exists in the dictionary

We can use the in operator to check if a key is in the dictionary
"""

ccc = dict()

#print(ccc["csev"])
"""
Traceback (most recent call last):
  File "C:...
    print(ccc["csev"])
          ~~~^^^^^^^^
KeyError: 'csev'
"""
print("csev" in ccc)