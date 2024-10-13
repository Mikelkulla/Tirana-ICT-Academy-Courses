import math
class Trekendeshi:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def siperfaqja(self):
        if (self.a**2 + self.b**2) == self.c**2:
            return (self.a * self.b)/2
        elif (self.b**2 + self.c**2) == self.a**2:
            return (self.b * self.c)/2
        elif (self.c**2 + self.a**2) == self.b**2:
            return (self.c * self.a)/2
        else:
            s = (self.a + self.b + self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def trekendeshType(self):
        if (self.a**2 + self.b**2) == self.c**2 or (self.b**2 + self.c**2) == self.a**2 or (self.c**2 + self.a**2) == self.b**2:
            return "Trekendesh Kenddrejt"
        elif self.a == self.b == self.c:
            return "Trekendesh Barabrinjes"
        elif (self.a == self.b and self.b !=self.c) or (self.b == self.c and self.c != self.a) or (self.c == self.a and self.a != self.b):
            return "Trekendesh Dybrinjenjeshem"
        elif self.a != self.b and self.b != self.c and self.c != self.a:
            return "Trekendesh i cfardoshem"


a = float(input("A:"))
b= float(input("B:"))
c = float(input("C:"))
if (a + b <= c) or (b + c <= a) or (a + c <= b):
    print("Trekendeshi nuk ekziston!")
else:
    t1 = Trekendeshi(a, b, c)
    print("Siperfaqja:",t1.siperfaqja())
    print("Lloji:",t1.trekendeshType())
