import random


def printMatrix(n:int)->None:
    """Printon nje matrice n * n me 1 dhe 0 random"""
    m = [[random.randint(0,1) for j in range(n)] for i in range(n) ]
    for i in range(n):
        for j in range(n):
            print(format(m[i][j], "3d"), end="")
        print()

def main():
    n = int(input("Shkruaj nje numer te plote:"))
    printMatrix(n)

main()