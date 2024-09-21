class Dhoma():
    def __init__(self, s, p ,gjat, gjer, lart, ngj, kon):    
        self.siperfaqja = s
        self.perimetri = p
        self.gjatesia = gjat
        self.gjeresia = gjer
        self.lartesia = lart
        self.ngjyra_mureve = ngj
        self.kondicioner = kon

    def __str__(self) -> str:
        return f"Dhoma me siperfaqe: {self.siperfaqja}"
dhoma1 = Dhoma(100, 40, 10, 10 ,10, "bardhe", True)
dhoma2 = Dhoma(200, 60, 20, 10, 10, "Zeze", False)
for k,v in dhoma1.__dict__.items():
    print(k,": ",v, sep="")
print(dhoma2.ngjyra_mureve)