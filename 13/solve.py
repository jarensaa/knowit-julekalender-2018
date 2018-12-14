import sympy
import sys

frequencies = dict()
output = [1, 3]
primesCount = 1
primesSum = 3

while(primesCount < 100):
    head = output[-1]
    for i in range(0, len(output) - 1):
        s = output[i] + head
        if(s not in frequencies):
            frequencies[s] = 1
        else:
            frequencies[s] += 1

    for i in range(head + 1, sys.maxsize):
        # Perf degrades quickly here, but it's fine for 100 primes.
        if(frequencies.get(i, 2) == 1):
            output.append(i)
            if(sympy.isprime(i)):
                primesCount += 1
                primesSum += i
            break

print(primesSum)
