import random
startn = 1 # numri i fillimit te intervalit
endn = 100 # numri i fundit te intervalit
num = random.randint(startn,endn) # gjenerojm nje numer random
print(num)
hapa = 1
kompjuteri = random.randint(startn, endn) # ky eshte numri qe kerkon te gjeje numrin e meparshem random
while kompjuteri != num:

    if num < kompjuteri: # nese numri i gjetur eshte me i vogel, ndryshojme intervalin e siperm me numrin,
        endn = kompjuteri   # pasi ai eshte numri max qe mund te shkojme
        kompjuteri = random.randint(startn, endn)

    if num > kompjuteri:
        startn = kompjuteri
        kompjuteri = random.randint(startn, endn)

    hapa += 1
print("Success. Numri eshte ", num ," dhe ti gjete ", kompjuteri, "me ", hapa, " hapa")