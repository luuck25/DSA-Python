from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        if len(nums) < 3:
            return result

        nums.sort()

        for i in range(len(nums)):


            if i>0 and nums[i] == nums[i-1]:  # skip duplicates
                continue

            start = i + 1
            end = len(nums) - 1

            while end > start:
                sum = nums[i] + nums[start] + nums[end]

                if sum == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while end > start and nums[start] == nums[start -1]: # skip duplicates
                        start += 1  
                    while end > start and nums[end] == nums[end + 1]: # skip duplicates
                        end -= 1       

                elif sum > 0:
                    end -= 1
                else:
                    start += 1        


        return result
        

        nums = [-1, -1, 0, 0, 1, 1]


"""

nums = [-1, -1, -1, 0, 1, 2]
        i=0  i=1  i=2

i=0: Captain is -1     → "OK, go find your team!"  ✅
i=1: Captain is -1     → "Wait, you're the SAME captain as before!"
                          "Your team will be the same. SIT DOWN." ❌ skip
i=2: Captain is -1     → "SAME captain again! SIT DOWN." ❌ skip
i=3: Captain is 0      → "New captain! Go find your team!" ✅

SKIP #1 — Before even searching:
"Is this captain (-1) the same as the last captain? Skip!"
  [-1, -1, ...]
   i=0  i=1 ← SKIP (same as i=0)

SKIP 2 and 3    - AFTER finding a match

Analogy: You're at a buffet. You picked rice for your plate. The next 3 containers also have rice. 
You skip past ALL of them to find something different.
"""



