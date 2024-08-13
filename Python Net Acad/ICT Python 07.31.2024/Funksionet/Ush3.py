def kundert(numri:int)->int:
    if numri >=0:
        numri = str(numri)
        numri_kundert = numri[::-1]
        numri_kundert = int(numri_kundert)
    else:
        numri = str(abs(numri))
        numri_kundert = numri[::-1]
        numri_kundert = -1 * int(numri_kundert)
    return numri_kundert
def polindrome(numri:int)->bool:

    if numri == kundert(numri):
        return True
    else:
        return False
print(polindrome(123))
print(polindrome(101))
print(polindrome(0))
print(polindrome(-101))
print(polindrome(-123321))
