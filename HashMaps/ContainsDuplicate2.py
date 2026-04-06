"""
Contains Duplicate II — Plain English Walkthrough
===================================================
Problem:
    Given an array nums and an integer k, return True if there are
    two DISTINCT indices i and j such that nums[i] == nums[j]
    and abs(i - j) <= k.

    i.e., find a duplicate where the two occurrences are at most k positions apart.

    Input:  nums = [1,2,3,1], k = 3      →  True  (index 0 and 3, distance = 3)
    Input:  nums = [1,0,1,1], k = 1      →  True  (index 2 and 3, distance = 1)
    Input:  nums = [1,2,3,1,2,3], k = 2  →  False (closest duplicates are 3 apart)

Visual Example:
    Input: nums = [1, 2, 3, 1], k = 3

    Step 1: Walk through array, store {value: last_seen_index}

    i=0, num=1 → not in map          → store {1: 0}
    i=1, num=2 → not in map          → store {1:0, 2:1}
    i=2, num=3 → not in map          → store {1:0, 2:1, 3:2}
    i=3, num=1 → 1 IS in map at index 0
                  abs(3 - 0) = 3 ≤ 3 → ✅ return True!

    Result: True ✅

Why store the LAST seen index (not first)?
    We only care about the CLOSEST pair of duplicates.
    If we saw num at index 2 and again at index 8 (too far),
    we update to index 8. Now if it appears at index 9,
    abs(9 - 8) = 1 which might satisfy the condition.
    Keeping the old index 2 would miss this!

Approach:
    1. Use a HashMap {value: last_seen_index}
    2. For each element:
       - If it's in the map AND distance ≤ k → return True
       - Update the map with the current index (always keep latest)
    3. If we finish the loop → no nearby duplicate → return False

Time:  O(n) — single pass
Space: O(n) — hashmap stores at most n entries
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Map to store {value: last_seen_index}
        freq = {}

        for i in range(len(nums)):

            num = nums[i]

            # Have we seen this number before?
            if num in freq:
                # Is the previous occurrence close enough (within k distance)?
                if abs(i - freq[num]) <= k:
                    return True

            # Store/update with the CURRENT index (always keep the latest)
            # This ensures we check the closest pair of duplicates
            freq[num] = i

        # No nearby duplicates found
        return False

    # ---- Clean version (no comments) ----
    def containsNearbyDuplicate_clean(self, nums: List[int], k: int) -> bool:
        freq = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in freq:
                if abs(i - freq[num]) <= k:
                    return True
            freq[num] = i

        return False
    
    # another approach using Window
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(0, len(nums)):

            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])        

        return False
    
            