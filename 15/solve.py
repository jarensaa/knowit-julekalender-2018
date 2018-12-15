import math

numGoldenPeople = 0
goldenYears = set()

yearsInput = [int(line.split("f.")[1])
              for line in open("input-gullbursdag.txt").readlines()]

for age in range(0, 60):
    goldenYears.add(math.pow(age, 2) - age)

for year in yearsInput:
    if(year in goldenYears):
        numGoldenPeople += 1

print(numGoldenPeople)
