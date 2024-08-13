import Ush5

def main():
    fahrenheit_list = list()
    celcius_list = list()
    for i in range(30,41,1):
        fahrenheit_list.append(Ush5.celciu_to_fahrenheit(i))
    for j in range(30,131,10):
        celcius_list.append(Ush5.fahrenheit_to_celcius(j))
    celciusi = 30
    fahrenheiti = 30
    print("-"*62)
    print("Celcius    |" + " "*3 + "fahrenheit","   |  ", "fahreheit" + "    |   " + "celcius    |")
    print("-"*62)
    for y in range(len(fahrenheit_list)):
        print(format(celciusi, "7.2f"),"   |",format(fahrenheit_list[y],"12.1f"),"   | ",format( fahrenheiti, "10.2f"),"   |   ",format( round( celcius_list[y],1),"6.2f") , "   |" )
        celciusi +=1
        fahrenheiti +=10
    print("-" * 62)


main()