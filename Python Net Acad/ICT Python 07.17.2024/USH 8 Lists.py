"""
Te ndertojme nje program i cili gjeneron nje matrice random 10*10 dhe afishon
shumen e elemnteve te diagonales kryesore
"""

import random
 # gjeneron nje numer ne intervalin
print(random.randint(1,1000))

m = [[random.randint(1,1000) for i in range(10)] for j in range(10)]
for row in range(10):
    for col in range(10):
        print(format(m[row][col], "5d"), end=" ") # f float, d decimal, s string
    print("")
print("*"*10)
m1 = [rreshta[1:3] for rreshta in m[0:2]] # bejme slice kolonat 
j = len(m1[0])
i = len(m1)
for row in range(i):
    for col in range(j):
        print(format(m1[row][col], "5d"), end=" ") # f float, d decimal, s string
    print("")