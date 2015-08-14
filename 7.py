# Project Euler
# Problem #7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?
#

def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

flag = isPrime = True
primeNum = 0
num = 1

while(flag):
    num += 1
    isPrime = is_prime(num)
    if(isPrime):
        primeNum += 1
        print("Prime Number ", num)

    if(primeNum == 10001):
        flag = False

print("10001st Prime # is ", num)
