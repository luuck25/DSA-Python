"""
3Sum Closest (LeetCode #16)
============================
Problem:
    Given an array and a target, find 3 numbers whose sum is CLOSEST to target.
    Return the sum.

    Input: nums = [-1, 2, 1, -4], target = 1  →  2  (because -1+2+1 = 2)

Logic:
    Same as 3Sum but instead of looking for exact 0, track the closest sum.
    1. Sort → enables two pointers
    2. Fix one number (i), two pointers (start, end) for the rest
    3. At each step, compare |current_sum - target| vs |closestSum - target|
    4. If exact match → return immediately (can't get closer than 0)

Time:  O(n²) — sort O(n log n) + outer O(n) × inner O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1

            while end > start:
                total = nums[i] + nums[start] + nums[end]

                # Exact match — can't do better
                if total == target:
                    return total

                # Update closest if this sum is nearer to target
                if abs(total - target) < abs(closestSum - target):
                    closestSum = total

                # Two pointer movement — same logic as 3Sum
                if total < target:
                    start += 1
                elif total > target:
                    end -= 1

        return closestSum

    # ---- Clean version (no comments) ----
    def threeSumClosest_clean(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1

            while end > start:
                total = nums[i] + nums[start] + nums[end]
                if total == target:
                    return total
                if abs(total - target) < abs(closestSum - target):
                    closestSum = total
                if total < target:
                    start += 1
                elif total > target:
                    end -= 1

        return closestSum