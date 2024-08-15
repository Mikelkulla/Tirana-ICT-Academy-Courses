"""
Now we will take the email from the file
"""
fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From"):
        continue

    email = line.split()
    name_mail = email[1].split("@")
    print("Name is:", name_mail[0])
    print("Email is:", name_mail[1])
    # now we are going to split the email with the index of 1 in the list
