class Product:
    def __init__(self, cmimi, sasia, emri):
        self.cmimi = cmimi
        self.sasia = sasia
        self.emri = emri

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def shto(self, product):
        self.items.append(product)
    
    def hiq(self, product):
        for p in self.items:
            if p.emri == product.emri:
                self.items.remove(p)