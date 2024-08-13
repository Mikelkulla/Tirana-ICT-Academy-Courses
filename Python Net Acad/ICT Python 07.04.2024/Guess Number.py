"""
Programi gjerenon nje numer rastesor midis 1 dhe 100,
me pas i kerkon perdoruesit te gjeje kete numer,
nese nuk e gjen perdoruesi, atehere i jepet nje ndihme
duke i treguar nese numri eshte me i madh ose me i vogel
se numri qe ai ka zgjedhur

Shembull: Kompjuteri gjeneron numrin 43

Gjej numrin tim? 87
Numri eshte me i vogel. Provo perseri? 77
Numri eshte me i vogel. Provo perseri? 67
Numri eshte me i vogel. Provo perseri? 57
Numri eshte me i vogel. Provo perseri? 47
Numri eshte me i vogel. Provo perseri? 37
Numri eshte me i madh. Provo perseri? 43
"""
import random

num = random.randint(1,100)
numri_userit = int(input("Gjej numrin tim?"))
hapa = 0
while numri_userit != num:
    if num < numri_userit:
        numri_userit = int(input("Numri eshte me i vogel. Provo perseri?"))
    elif num > numri_userit:
        numri_userit= int(input("Numri eshte me i madh. Provo perseri?"))
    hapa += 1
print("Success. Numri eshte ", num ," dhe ti gjete ", numri_userit, "me ", hapa, " hapa")