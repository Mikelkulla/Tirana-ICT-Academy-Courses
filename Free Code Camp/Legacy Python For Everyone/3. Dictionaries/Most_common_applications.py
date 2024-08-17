import math

numri = math.factorial(1000)
num = 1
for i in range(1, 1001):
    num = num * i
print(num)
print(numri)
print(num==numri)