# Project Euler
# Problem #10
#
# jeremyfo@gmail.com
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# This is second attempt with a much faster get_prime() function.
#
# 142913828922
# [Finished in 1.3s]

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

total = sum(get_primes(2000000))

print(total)
