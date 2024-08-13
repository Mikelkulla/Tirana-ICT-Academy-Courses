"""
Te shkruajme nje funksion qe mer si parameter nje numer
te plote qe perfaqson nje vit kalendarik dhe kthen true
nese viti eshte i brishte dhe false perndryshe. Funksioni
eleminon ato argumente qe nuk bejne sens (para 1582)
"""

def leap_year(viti:int)->bool:
    if viti < 1582:
        return None
    if viti % 4 == 0 and viti % 100 != 0 or viti % 400 == 0:
        return True
    else:
        return False

def main():
    test_data = [1900, 2000, 2016, 1987, 100, 2024, 2025, 2100]
    test_results = [False, True, True, False, None, True, False, False]
    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr, "->", end="")
        result = leap_year(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")
# parandalon qe rezultatet te shfaqen tek filet qe e therasin kete file
# main therritet vetem kur bejm run nga ky file.
if __name__ == "__main__": main()