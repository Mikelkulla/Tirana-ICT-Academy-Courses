workHouser=[
    [1, 4, 6, 7, 9, 2, 1],
    [2, 6, 6, 7, 9, 3, 4],
    [1, 4, 6, 2, 9, 2, 1],
    [2, 4, 1, 7, 1, 3, 3],
    [1, 5, 6, 1, 9, 2, 1],
    [1, 4, 8, 8, 9, 8, 1],
    [1, 5, 6, 5, 9, 5, 1],
    [2, 4, 6, 7, 4, 3, 2]
]
employees = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]

result = []

for row in range(len(workHouser)):
    tot_house = sum(workHouser[row])
    result.append([tot_house, employees[row]])

#result.sort(reverse=True)

print("*"*20)
for el in result:
    print(format(el[1], "10s") + " " + str(el[0]) + " ore")

print("*"*20)
avg_hours = 0
for row in result:
    avg_hours += row[0]
avg_hours /= len(employees)
print(avg_hours)

maxim = [0,""]
for el in result:
    if el[0] >= maxim[0]:
        maxim = el

print("Oret maksimale i ka "+ maxim[1] + ",",maxim[0], "ore")

#Gjejme oret totale per cdo jave
for col in range(len(workHouser[0])):
    tot_day_hours = 0
    for row in range(len(workHouser)):
        tot_day_hours += workHouser[row][col]
    result_per_day.append([tot_day_hours], col)