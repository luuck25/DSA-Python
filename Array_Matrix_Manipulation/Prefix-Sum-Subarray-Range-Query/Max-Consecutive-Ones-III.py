class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0

        changed = 0

        max_subarray = float('-inf')

        for right in range(len(nums)):
            
            if nums[right] ==0:
                changed += 1
                
            while changed > k:

                if nums[left] == 0:
                    changed -= 1
                left += 1




            max_subarray = max(max_subarray, right - left + 1)

        return max_subarray        


        