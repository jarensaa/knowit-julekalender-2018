import math

numbers = dict()

for line in open("input-rain.txt", "r"):

    coordinates = line.strip().replace("(", "").replace(")", "").split(";")
    firstPoint = coordinates[0].split(",")
    secondPoint = coordinates[1].split(",")

    changeX = int(firstPoint[0]) - int(secondPoint[0])
    changeY = int(firstPoint[1]) - int(secondPoint[1])

    derivative = changeX/changeY

    if(derivative not in numbers):
        numbers[derivative] = 1
    else:
        numbers[derivative] += 1

print(max(numbers.values()))
