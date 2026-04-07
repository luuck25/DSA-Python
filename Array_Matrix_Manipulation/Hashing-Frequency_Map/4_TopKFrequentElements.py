"""
Top K Frequent Elements — Plain English Walkthrough
=====================================================
Problem:
    Given an integer array and an integer k, return the k most frequent elements.
    You may return the answer in any order.

    Input:  nums = [1,1,1,2,2,3], k = 2  →  [1, 2]
    Input:  nums = [1], k = 1             →  [1]

Visual Example:
    Input: nums = [1,1,1,2,2,3], k = 2

    Step 1: Count frequencies using Counter:
            {1: 3, 2: 2, 3: 1}

    Step 2: Create BUCKET array where index = frequency.
            Size = len(nums) + 1 = 7 (frequency can be at most n)

            Index:  0    1    2    3    4    5    6
            Bucket: []  [3]  [2]  [1]  []   []   []
                         ↑    ↑    ↑
                     freq=1 freq=2 freq=3

    Step 3: Walk buckets from RIGHT to LEFT (highest freq first):
            i=6 → []     → skip
            i=5 → []     → skip
            i=4 → []     → skip
            i=3 → [1]    → result = [1]
            i=2 → [2]    → result = [1, 2] → len == k → DONE!

    Result: [1, 2] ✅

Why Bucket Sort (not a Heap)?
    - A max-heap approach works but is O(n log k)
    - Bucket sort is O(n) — we use the FREQUENCY as the index
    - Max possible frequency = n (every element is the same)
    - So we create n+1 buckets and place each number into its frequency bucket
    - Walking from right to left gives us highest frequency first

Approach:
    1. Count frequency of each number → {num: count}
    2. Create buckets array of size n+1 (index = frequency)
    3. Place each number into its frequency bucket
    4. Walk from highest index down, collect numbers until we have k

Time:  O(n) — counting + bucket fill + bucket scan are all linear
Space: O(n) — for the frequency map and buckets array
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Edge case: empty input
        if not nums:
            return []

        # Step 1: Count how often each number appears
        # e.g., [1,1,1,2,2,3] → {1:3, 2:2, 3:1}
        count = Counter(nums)

        # Step 2: Create buckets where index = frequency
        # Size is len(nums)+1 because max frequency can be n
        # e.g., [1,1,1,1] has frequency 4 → need index 4 → size 5
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Place each number in the bucket matching its frequency
        # e.g., num=1, freq=3 → buckets[3] = [1]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Walk from highest frequency bucket down to lowest
        # Collect numbers until we have k results
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

    # ---- Clean version (no comments) ----
    def topKFrequent_clean(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result





        