"""
Split breaks a string into parts and produces a list of strings. We think of these
as words. We can access a particular word or loop through all the words

When you do not specidy a delimiter, multiple spaces are treated like one delimiter

You can specify what delimiter character to use in the splitting
"""
abc = "With three words"
stuff = abc.split()

cde = ""
for w in stuff:
    if cde == "":
        cde = cde + w
    else:
        cde = cde + ", " + w
# using another delimiter to split the string with words devided by ","
stuff2 = cde.split(", ")

print(stuff)
print(stuff2)

print("Length of stuff: ", len(stuff))

print("First element of list is: ", stuff[0])

for w in stuff:
    print("Element is:", w)
for w in stuff2:
    print("Element2 is:", w)