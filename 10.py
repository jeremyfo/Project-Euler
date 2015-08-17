# Project Euler
# Problem #10
#
# jeremyfo@gmail.com
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# First Iteration
# 142913828922
# [Finished in 14747.4s] (4 hours)
#
# Second Interation, removing check on even numbers.

def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

num = 1
sum = 2  # 2 is prime but we wont count it

while(num < 2000000):
    num += 2
    if(is_prime(num)):
        # print("Sum is ", sum, "Prime # is ", num)
        sum = sum + num

print("Sum of all primes under 2 million is ", sum)
