

# me germa te medha python kupton qe eshte CONSTANT
MILJE_TO_KM = 1.609344
GALLON_TO_LITRA = 3.785411784

def liters_100km_to_miles_gallon(liters:float)->float:
    """
    Funksioni konverton konsumin e karburantit nga europian ne amerikan
    parametrat - liters, konsumi europian litra/100km
    return - konsumi milje/gallon
    """
    return 1/(liters / 100 * MILJE_TO_KM / GALLON_TO_LITRA)

def miles_gallon_to_liters_100km(miles:float)->float:
    return 100/(miles * MILJE_TO_KM / GALLON_TO_LITRA)
def main():
    # kthejm lit/100km te mil/gall
    print(format(liters_100km_to_miles_gallon(3.9), ".2f") + " milje/gallon")
    print(format(liters_100km_to_miles_gallon(7.5), ".2f") + " milje/gallon")
    print(format(liters_100km_to_miles_gallon(10.), ".2f") + " milje/gallon")
    # ruajme vlerat ne variablat testuese
    test1 = liters_100km_to_miles_gallon(3.9)
    test2 = liters_100km_to_miles_gallon(7.5)
    test3 = liters_100km_to_miles_gallon(10.)

    # perdorim variablat testuese per te kontrolluar funksionin e anasjellte
    print(format(miles_gallon_to_liters_100km(test1),".2f") + " litra/100km")
    print(format(miles_gallon_to_liters_100km(test2),".2f") + " litra/100km")
    print(format(miles_gallon_to_liters_100km(test3),".2f") + " litra/100km")

if __name__ == '__main__':
    main()