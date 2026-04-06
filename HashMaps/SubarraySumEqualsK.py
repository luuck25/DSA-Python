"""
Subarray Sum Equals K — Plain English Walkthrough
===================================================
Problem:
    Given an array of integers and an integer k, return the TOTAL NUMBER
    of contiguous subarrays whose sum equals k.

    Input:  nums = [1, 1, 1], k = 2  →  2  (subarrays [1,1] at index 0-1 and 1-2)
    Input:  nums = [1, 2, 3], k = 3  →  2  (subarrays [1,2] and [3])

Visual Example:
    Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7

    What is a prefix sum?
        prefix_sum[i] = sum of all elements from index 0 to i

        Index:       0   1    2    3    4    5    6    7
        Array:       3   4    7    2   -3    1    4    2
        Prefix sum:  3   7   14   16   13   14   18   20

    Key Insight:
        If prefix_sum at index j = 14 and prefix_sum at index i = 7,
        then the subarray from i+1 to j sums to 14 - 7 = 7 = k ✅

        In other words: prefix_sum[j] - prefix_sum[i] = k
        Rearranged:     prefix_sum[j] - k = prefix_sum[i]

        So for each j, we ask: "Have I seen a prefix sum equal to curr_sum - k before?"

    Step-by-step trace (k = 7):
        Start: prefix_map = {0: 1}, curr_sum = 0, count = 0

        num=3:  curr_sum=3,  check 3-7=-4 in map? NO           map={0:1, 3:1}
        num=4:  curr_sum=7,  check 7-7=0  in map? YES (1 time) → count=1
                                                                 map={0:1, 3:1, 7:1}
        num=7:  curr_sum=14, check 14-7=7 in map? YES (1 time) → count=2
                                                                 map={0:1, 3:1, 7:1, 14:1}
        num=2:  curr_sum=16, check 16-7=9 in map? NO           map={..., 16:1}
        num=-3: curr_sum=13, check 13-7=6 in map? NO           map={..., 13:1}
        num=1:  curr_sum=14, check 14-7=7 in map? YES (1 time) → count=3
                                                                 map={..., 14:2}
        num=4:  curr_sum=18, check 18-7=11 in map? NO          map={..., 18:1}
        num=2:  curr_sum=20, check 20-7=13 in map? YES (1 time)→ count=4
                                                                 map={..., 20:1}

        Result: 4 ✅

    Why {0: 1} at the start?
        If curr_sum itself equals k, then curr_sum - k = 0.
        We need 0 to be in the map so we count subarrays starting from index 0.
        Example: nums = [7], k = 7 → curr_sum = 7, check 7-7 = 0 → found!
        Without {0: 1}, we'd miss this case entirely.

    Why store COUNT (not just True/False)?
        The same prefix sum can appear multiple times.
        Example: nums = [1, -1, 1, -1, 1], k = 0
        Prefix sums: 1, 0, 1, 0, 1 — the sum "1" appears 3 times!
        Each occurrence represents a DIFFERENT subarray that sums to k.

Approach:
    1. Initialize prefix_map = {0: 1} (handles subarrays starting at index 0)
    2. Walk through array, building running prefix sum
    3. At each step, check if (curr_sum - k) exists in the map
       - If yes → that many subarrays ending HERE sum to k → add to count
    4. Record current prefix sum in the map
    5. Return count

Time:  O(n) — single pass through the array
Space: O(n) — prefix sum map can have up to n entries
"""

from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    # {prefix_sum: how many times we've seen it}
    # Start with {0: 1} — an empty subarray has sum 0, seen once
    # This lets us count subarrays that start from index 0
    prefix_map = {0: 1}

    # Running sum from index 0 to current position
    curr_sum = 0

    # Total count of subarrays that sum to k
    count = 0

    for num in nums:
        # Extend the prefix sum by adding current element
        curr_sum += num

        # Have we seen a prefix sum equal to (curr_sum - k)?
        # If yes, that means there's a subarray ending HERE that sums to k
        # Why? Because: curr_sum - earlier_prefix_sum = k
        if curr_sum - k in prefix_map:
            # Add the NUMBER of times we've seen it
            # (each occurrence = a different valid subarray)
            count += prefix_map[curr_sum - k]

        # Record this prefix sum (increment count if already seen)
        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

    return count


# ---- Clean version (no comments) ----
def subarraySum_clean(nums: List[int], k: int) -> int:
    prefix_map = {0: 1}
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num

        if curr_sum - k in prefix_map:
            count += prefix_map[curr_sum - k]

        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

    return count