readings = "  18,27,35,20  "

total = 0

average = 0

readings = readings.strip().split(",")

for i in readings:
    total += int(i)

average = float(total/4)

print("total:", total)
print("average:", average)
