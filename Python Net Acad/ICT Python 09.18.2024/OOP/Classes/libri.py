class Libri:
    def __init__(self, isbn,titulli, nr_faqeve, zhaneri, viti, autori= "John Smith") -> None:
        self.isbn = isbn
        self.titulli = titulli
        self. zhaneri = zhaneri
        self.nr_faqeve = nr_faqeve
        self.autori = autori
        self.viti = viti
    
libri1 = Libri(
    "123",
    "Katedralja e Parisit", 
    500, 
    "I lodhshem",  
    2000,
    "Viktor")

class Animal:
    pass

class Dog(Animal):
    pass

class Dalmat(Dog):
    pass