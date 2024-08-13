"""
Sipas CNNMoney.com facebook kishte 500 milion perdorues ne korrik te 2010
Dhe perdoruesit e tij riteshin me 5% cdo muaj. Sa muaj i duhen facebook per
te arritur vleren e 1 miliarde perdoruesve? Po 2 miliarde?
"""

p = 500_000 # user ne korrik 2010
m = 0 # counter per muajt
while p < 1_000_000:
    p += p*0.05 # shtojme me 0.05 numrin e userave
    m +=1 # cdo iterim shtojme muajin me 1
print("Facebook i duhen ", m," muaj per te arritur ", round(p,0)," perdorues")
while p < 2_000_000:
    p += p*0.05
    m +=1
print("Facebook i duhen ", m," muaj per te arritur ", round(p,0)," perdorues")