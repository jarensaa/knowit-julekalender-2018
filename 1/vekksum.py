file = open("input-vekksort.txt")

sum = 0
prev = 0

for line in file:
    value = int(line)
    if(prev <= value):
        sum += value
        prev = value

print(sum)
