"""
Sometimes we spit a line one way, and then grab one of the pieces of the line
and split that piece again
"""

line = "From: mikel.kulla84@gmail.com Sat Jan  5 09:14:16 2008"
# split the line into list of strings words
words = line.split()
# assign the second element of the list in the eamil variable (index 1)
email = words[1]
# we split the email in pieces at the @,
pieces = email.split("@")
# print the second element of the split
print(pieces[1])
