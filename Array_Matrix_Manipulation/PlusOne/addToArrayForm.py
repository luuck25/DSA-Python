from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        
        for i in range(n-1, -1, -1):
            k += num[i]          # add current digit
            num[i] = k % 10      # update digit
            k //= 10             # carry
            
        # handle remaining k
        while k > 0:
            num.insert(0, k % 10)
            k //= 10
            
        return num