"""
Take the file name as an input from the user
"""

fname = input("Enter the file name: ")
# we use try and except because if the file name does not exist it will give an error
try:
    f_hand = open(fname)
except:
    print("File can not be opened:", fname)
    # after that we quite because the rest of the code will give an error because
    # ,f_hand is not assigned
    quit()
count = 0
for line in f_hand:
    if line.startswith("Name: "):
        count = count + 1

print("There were", count,"name lines in", fname)
