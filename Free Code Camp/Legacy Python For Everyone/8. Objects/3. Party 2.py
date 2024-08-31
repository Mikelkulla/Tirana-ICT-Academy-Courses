class partyAnimnal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = partyAnimnal("Ice")
s.party()

j = partyAnimnal("Xhorxhi")
j.party()
s.party()