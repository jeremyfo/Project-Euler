# Project Euler
# Problem #6
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

num1 = num2 = i = 0

for x in range(1, 101):
    num1 += x
num1 = num1 ** 2

print(num1)

for x in range(1, 101):
    i = x ** 2
    num2 += i

print(num2)

print("Difference is ", num1 - num2)
