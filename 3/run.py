from math import sqrt
import itertools


def factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


counter = 0

for i in range(6500 + 1):
    f = factors(i)

    if(len(f) == 8):
        print(f)
        counter += 1


print(counter)
