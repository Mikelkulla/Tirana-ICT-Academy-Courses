class Drejtkendeshi:
    def __init__(self,gjatesi, gjeresi) -> None:
        self.gjat = gjatesi
        self.gjer = gjeresi

    def area(self):
        return self.gjat * self.gjer
    
    def perimeter(self):
        return 2 * (self.gjat + self.gjer)
    
d1 = Drejtkendeshi(10,20)

print("Perimetri: ", d1.perimeter())
print("Siperfaqja: ", d1.area())