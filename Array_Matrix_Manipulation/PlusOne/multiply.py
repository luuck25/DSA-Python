"""
Multiply Strings (LeetCode #43)
================================
Problem:
    Multiply two numbers represented as strings. Return result as string.
    Cannot use built-in BigInteger or convert inputs directly to int.

    Input:  "123" × "45"  →  "5535"

Logic:
    Simulate grade-school multiplication.
    Result has at most n1 + n2 digits. Use a result array of that size.
    For each digit pair (i, j):
      - product lands at positions [i+j] (tens) and [i+j+1] (ones)
      - add carry from previous products at that position

    "123" × "45":
       i=2,j=1 → 3×5=15 → res[4]=5, res[3]+=1
       i=2,j=0 → 3×4=12+carry → ...
       ... and so on right to left

Time:  O(n1 × n2)
Space: O(n1 + n2) — result array

https://www.youtube.com/watch?v=1Hftrgb30BQ
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n1 = len(num1)
        n2 = len(num2)
        res = [0] * (n1 + n2)  # max possible digits in result

        for i in range(n1 - 1, -1, -1):        # right to left in num1
            for j in range(n2 - 1, -1, -1):    # right to left in num2
                multi = int(num1[i]) * int(num2[j])

                pos1 = i + j + 1  # ones position
                pos2 = i + j      # tens position

                total = multi + res[pos1]  # add existing value (carry from earlier)

                res[pos1] = total % 10     # keep ones digit
                res[pos2] += total // 10   # carry tens to left

        return "".join(map(str, res)).lstrip('0')  # strip leading zeros

    # ---- Clean version (no comments) ----
    def multiply_clean(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                multi = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j + 1, i + j
                total = multi + res[pos1]
                res[pos1] = total % 10
                res[pos2] += total // 10

        return "".join(map(str, res)).lstrip('0')