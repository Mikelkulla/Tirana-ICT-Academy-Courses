# open a file read only
# use a for loop to read each line
# count the lines and print out the number of lines

f_hand = open('mbox.txt')

count = 0
for line in f_hand:
    count = count + 1
print("Line Count: ", count)
