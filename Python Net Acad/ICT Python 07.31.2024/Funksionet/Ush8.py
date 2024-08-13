
# Kthen true nese nr i kartes eshte i sakte
def isValid(number: int) -> bool:
    if getSize(number) < 13 or getSize(number) > 17:
        return None
    if not prefixMatched(number, 4) and not prefixMatched(number,5) and not prefixMatched(number,6) and not prefixMatched(number,37):
        return None
    return (sumOfDoubleEvenPlaces(number) + sumOfOddPlaces(number)) % 10 == 0
#Hapi 2
def sumOfDoubleEvenPlaces(numri:int)->int:
    """numri = str(numri)
    numri = numri + " "
    double_even_places = list()
    for i in numri[::-2]:
        if i == " ":
            continue
        double_even_places.append(int(i)*2)
    return sum(double_even_places)"""
    s = str(numri)[::-1]
    return sum( [ getDigit(2* (int(s[i]) for i in range(len(s)) if i % 2 ==1)) ])
    # return sum([int(ch) for ch in str(numri)[::-1]][1::2])

#Kthen numer nese numri eshte nje shifror, perndryshe kthen shumen e dy shifrave
# DONE!!!!
def getDigit(number:int)->int:
    return sum([int(ch) for ch in str(getPrefix(number,2))])

# Kthen shumen e shifrave ne pozicionet teke te numrit
def sumOfOddPlaces(number:int)->int:
    s = str(number)[::-1]
    return sum([int(s[i]) for i in range(len(s)) if i % 2 == 0])

# Kthen True nese d eshte prefix i number ### DONE!!!!
def prefixMatched(number:int, d:int)->bool:
    return str(number).startswith(str(d))

# Kthen numrin e shifrave të d  ###Done!!!
def getSize(d:int)->int:
    return len(str(d))

# Kthen numrin e pare me k shifra nga number. Nëse numri ka me pak se k shifra, funksioni kthen të gjithe numrin number
# DONEE!!!
def getPrefix(number:int, k:int)->int:
    """if len(str(number)) < len(str(k)):
        return number
    else:
        return int(str(number)[:len(str(k))])"""
    return int(str(number)[:k])


def main():
    print("4388576018402626 is valid:", isValid(4388_5760_1840_2626))
    print("4388576018402627 is valid", isValid(4388576018402627))
    print("4388576018410707 is valid", isValid(4388576018410707))

main()