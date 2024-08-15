
# open the file here and using fhand as the variable
fhand = open("mbox.txt")
# we iterate for each line of the file
for line in fhand:
    # use the rstrip() method to exclude the \n at the end of each line so we dont print empty lines between
    line = line.rstrip()
    # check if line doesn't start with "From"
    if not line.startswith("From"):
        # In this case we continue this iteration imediately
        continue
    # now we have only the lines that we want filtered
    # we split the lines whith .split(). We leave it epmty beacause the space is default delimiter
    # and store them in the words variable which is a list of strings now (all words)
    words = line.split()
    # for loop to print
    for i in range(len(words)):
        print("Word at index", i, "is", words[i])
    print("*" * 25)