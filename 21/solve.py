from math import sqrt, ceil


def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i > 0]


def is_abundant_number(n):
    s = 0
    for i in range(1, ceil(sqrt(n))):
        if (n % i == 0):
            s += i
            if (n / i != i):
                s += int(n/i)

        if(s-n > n):
            return True

    return False


primes = sieve_for_primes_to(10000000)
outputSum = 0

for i in range(len(primes) - 1):
    if(primes[i+1] == primes[i]+2):
        if(is_abundant_number(primes[i] + 1)):
            outputSum += primes[i] + 1

print(outputSum)
print(272839298286)
