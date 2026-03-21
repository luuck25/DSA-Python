


# Trailing zeroes = number of times 5 appears as a factor
#  in numbers from 1 to n

"""
Docstring for recursion.leadingZeroInFactorial


Step 1: Count numbers divisible by 5
   5, 10, 15, 20, ...

   
   contributes one 5

Count = n // 5

Step 2: Count extra 5s from numbers like 25, 125... 

Some numbers have more than one 5.

Examples:

25 = 5 × 5 → contributes two 5s

125 = 5 × 5 × 5 → contributes three 5s

So we also count:

n // 25
n // 125
n // 625

Final Formula

Add them all:

Trailing Zeroes =
n//5 + n//25 + n//125 + n//625 + ...
"""


def trailingZinFac(n):
    count =0
    divisor = 5
    while divisor <=n:
        count += n// divisor
        divisor = divisor *5
    return count     


