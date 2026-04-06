"""
3Sum (LeetCode #15) — Plain English Walkthrough
==================================
Problem:
    Find all UNIQUE triplets that sum to zero. No duplicate triplets allowed.

    Input:  [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Logic:
    1. Sort → enables two pointers + easy duplicate skipping
    2. Fix one number (i), use two pointers (start, end) to find pairs = -nums[i]
    3. Skip duplicates at 3 places to avoid repeated triplets

Time:  O(n²)
       nums.sort()              → O(n log n)
       for i (outer loop)       → O(n)
         while start<end (inner) → O(n) per i
       Total = O(n log n) + O(n × n) = O(n log n) + O(n²) = O(n²)
       n² is always > n log n, so drop the smaller term.
Space: O(1) extra — just pointers (result list not counted)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        if len(nums) < 3:
            return result

        # Sort — required for two pointers and duplicate skipping
        nums.sort()

        # Fix first number, find pairs in remaining
        for i in range(len(nums) - 2):

            # SKIP #1: same first number as previous → same results
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while end > start:
                total = nums[i] + nums[start] + nums[end]

                if total == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    # SKIP #2: skip duplicate left values after a match
                    while end > start and nums[start] == nums[start - 1]:
                        start += 1
                    # SKIP #3: skip duplicate right values after a match
                    while end > start and nums[end] == nums[end + 1]:
                        end -= 1

                elif total > 0:
                    end -= 1      # sum too big → need smaller → move end left
                else:
                    start += 1    # sum too small → need bigger → move start right

        return result

    # ---- Clean version (no comments) ----
    def threeSum_clean(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start, end = i + 1, len(nums) - 1

            while end > start:
                total = nums[i] + nums[start] + nums[end]

                if total == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while end > start and nums[start] == nums[start - 1]:
                        start += 1
                    while end > start and nums[end] == nums[end + 1]:
                        end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1

        return result



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



