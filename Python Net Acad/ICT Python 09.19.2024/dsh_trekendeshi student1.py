"""
Krijoni klases trekendesh qe do te permbaje bazen, lartesine dhe 2 katetet.
Beni metodat per llogaritjen e siperfaqes dhe perimetrit.
Beni nje metode e cila kthen tipin e trekendeshit.
Ne konstruktor, mos e krijoni trekendeshin nese nuk eshte fizikisht e mundur.
"""


class Trekendesh():
    def _init_(self, baze, lartesi, k1, k2):        
        k1 = int(k1)
        k2 = int(k2)
        baze = int(baze)
        
        if (baze > (k1 + k2)):
            print("Eshte fizikisht e pamundur per te ndertuar trekendeshin!")
            # raise ArithmeticError("Eshte fizikisht e pamundur per te ndertuar trekendeshin!")
        else:
            self.baza = baze
            self.lartesia = lartesi
            self.kateti1 = k1
            self.kateti2 = k2

    def siperfaqja(self):
        sip = (self.baza * self.lartesia)/2
        return sip

    def perimetri(self):
        p = self.baza + self.kateti1 + self.kateti2
        return p

    def tipiTrekendeshit(self):
        if self.kateti1 == self.kateti2 == self.baza:
            print("Trekendeshi eshte barabrinjes!")
        elif self.kateti1 == self.kateti2 or self.kateti1 == self.baza or self.kateti2 == self.baza:
            print("Trekendeshi eshte dybrinjeshem!")
        elif (self.kateti1 * 2 + self.kateti2 * 2 == self.baza * 2) or (self.kateti1 * 2 + self.baza * 2 == self.kateti2 * 2) or (self.kateti2 * 2 + self.baza * 2 == self.kateti1 ** 2):
            print("Trekendeshi eshte kenddrejte!")
        else:
            print("Trekendeshi eshte i cfaredoshem!")


trekendeshi = Trekendesh(
    baze=5,
    lartesi=4,
    k1=4,
    k2=4,
)

if trekendeshi.baza:
    print(trekendeshi.siperfaqja())
    print(trekendeshi.perimetri())
    trekendeshi.tipiTrekendeshit()