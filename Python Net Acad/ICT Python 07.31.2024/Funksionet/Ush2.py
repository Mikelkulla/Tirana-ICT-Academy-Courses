def convertMillis(ms:int)->tuple:
    sekondat = ms // 1000
    minutat = sekondat // 60
    oret = minutat //60
    return sekondat % 60, minutat % 60, oret

def main():
    ms = int(input("Numri i ms:"))
    sekondat, minutat, oret = convertMillis(ms)
    print(oret, ":", minutat, ":", sekondat)

if __name__ == '__main__':
    main()