import sympy

inputNums = [int(char) for char in open("input.txt").readline().split(',')]

maxPrime = 0

for i in range(len(inputNums)):
    head, tail = i, i
    palinSum = inputNums[i]
    while(tail > 0 and head < len(inputNums) - 1):
        if(palinSum > maxPrime):
            if(sympy.isprime(palinSum)):
                maxPrime = max(maxPrime, palinSum)
        head += 1
        tail -= 1
        if(inputNums[head] == inputNums[tail]):
            palinSum += (2*inputNums[head])
        else:
            break

print(maxPrime)
