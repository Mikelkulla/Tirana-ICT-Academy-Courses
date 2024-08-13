import Ush6

def main():
    print("Feet    |" + " "*3 + "Meters","   |  ", "Meters" + "    |   " + "Feet    |")
    foot_list = list()
    foot_meter_list = list()
    meters_list = list()
    meter_foot_list = list()
    for i in range(1,11,1):
        foot_meter_list.append(i)
        foot_list.append(Ush6.footToMeter(i))

    for j in range(20,67,6):
        meter_foot_list.append(j)
        meters_list.append(Ush6.meterToFoot(j))

    for s in range(10):
        print(format(foot_list[s], "7.2f"), "   |", format(foot_meter_list[s], "12.1f"), "   | ",format(meters_list[s], "10.2f"), "   |   ", format(round(meter_foot_list[s], 1), "6.2f"), "   |")



if __name__ == '__main__':
    main()