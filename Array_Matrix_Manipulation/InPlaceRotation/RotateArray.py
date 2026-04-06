from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k = k % n   # handle large k  # if u rotate array of size n -> n times u would get same
        # so for k more than n, u would get correct value
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # Step 1: reverse whole array
        reverse(0, n - 1)
        
        # Step 2: reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: reverse rest
        reverse(k, n - 1)