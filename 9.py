# Project Euler
# Problem #9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which, a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#

def isPythagorean(a, b, c):
    return (a**2) + (b**2) == (c**2)

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - (a + b)
        if(isPythagorean(a, b, c)):
            if a + b + c == 1000:
                print(a * b * c)
                break
