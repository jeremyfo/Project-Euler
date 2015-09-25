# Project Euler
# Problem #16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
# Sum of numbers is: 1366
# [Finished in 0.1s]

sum = 0
strNum = str(2**1000)
length = len(strNum)

for i in range(0, length):
    sum += int(strNum[i])

print("Sum of numbers is:", sum)
