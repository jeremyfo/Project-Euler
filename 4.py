# Project Euler
# Problem #4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
def palindrome(num):
    return str(num) == str(num)[::-1]

max = 0
sum = 0

for x in range(100, 999):
    for y in range(100, 999):
        sum = x * y
        if palindrome(sum):
            if(sum > max):
                max = sum

print("Max Palindrome is ", max)
