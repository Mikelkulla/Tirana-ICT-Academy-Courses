data = "From: mikel.kulla84@gmail.com Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ", atpos)
print(sppos)

# now we slice the string from the @ position +1 not including the at
# and we and at sppos but not including space position
host = data[atpos+1 : sppos]
print(host)