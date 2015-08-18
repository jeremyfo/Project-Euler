# Project Euler
# Problem #12
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The
# first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred
# divisors?
#
# 500 divisors is 76576500.0
# [Finished in 15.2s]

def get_factor(num):
    table = []
    for i in range(1, int(num**0.5) + 1):
        if(num % i == 0):
            if i not in table:
                table.append(i)
                if(num / i) not in table:
                    table.append(num / i)
    return table

table = []
num = x = 0
flag = True

while(flag):
    x += 1
    num = ((x * (x + 1)) / 2)
    table = get_factor(num)
    #print(num,":",len(table), ":", table)
    if(len(table) > 500):
            flag = False
            print("500 divisors is", num)
