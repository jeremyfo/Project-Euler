# Project Euler
# Problem #14
#
# The following iterative sequence is defined for the set of positive integers:
#   n → n/2 (n is even)
#   n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# The number that starts the longest chain is 837799 Sequence is 525 long
# [Finished in 37.4s]

flag = True
num = 13

def get_sequence(num):
    list = []
    while(num > 1):
        list.append(num)
        if(num % 2 == 0):
            num //= 2
        else:
            num = (3 * num) + 1
    list.append(num)
    return list

seq = []
maxLen = myNum = 0

for i in range(13, 1000000):
    seq = get_sequence(i)
    if(len(seq) > maxLen):
        maxLen = len(seq)
        myNum = i

print("The number that starts the longest chain is", myNum, "Sequence is", maxLen,"long")
