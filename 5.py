# Project Euler
# Problem #5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#

flag = True
notDiv = True
num = 0

while(flag):
    num += 1
    for x in range(1, 21):
        if(num % x > 0):
            notDiv = False
    if(notDiv):
        flag = False
    notDiv = True

print("Smallest positive multiple divisible by all numbers 1 - 20 is ", num)
