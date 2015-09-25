# Project Euler
# Problem #20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
#
# Sum of numbers is: 648
# [Finished in 0.1s]

def factorial(n):
    num = 1
    for i in range(n, 0, -1):
        num = num * i
    return num

length = sum = 0

strNum = str(factorial(100))
length = len(strNum)

for i in range(0, length):
    sum += int(strNum[i])

print("Sum of numbers is:", sum)
