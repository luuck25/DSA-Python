"""
Largest Unique Number — Plain English Walkthrough
===================================================
Problem:
    Given an array of integers, return the largest number that appears EXACTLY once.
    If no such number exists, return -1.

    Input:  [5, 7, 3, 9, 4, 9, 8, 3, 1]  →  8
    Input:  [9, 9, 8, 8]                  →  -1

Visual Example:
    Input: [5, 7, 3, 9, 4, 9, 8, 3, 1]

    Step 1: Build frequency map:
            {5:1, 7:1, 3:2, 9:2, 4:1, 8:1, 1:1}

    Step 2: Walk through array, track largest with count == 1:
            5 → count=1, unique → largest = 5
            7 → count=1, unique → largest = 7
            3 → count=2, skip
            9 → count=2, skip
            4 → count=1, unique → largest = max(7, 4) = 7
            8 → count=1, unique → largest = max(7, 8) = 8
            1 → count=1, unique → largest = max(8, 1) = 8

    Result: 8 ✅

Approach:
    1. Build a frequency map {num: count}
    2. Loop through the array — for each num with count == 1, track the max
    3. If no unique number found → return -1

Time:  O(n) — two passes through the array
Space: O(n) — frequency map
"""


def largest_uni_num(nums):

    # Pass 1: Count frequency of every number
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Start with -infinity so any real number beats it
    largest_num = float('-inf')

    # Pass 2: Find the largest number that appears exactly once
    for num in nums:

        if freq[num] == 1:
            largest_num = max(largest_num, num)

    # If largest_num is still -inf, no unique number was found
    return -1 if largest_num == float('-inf') else largest_num


# ---- Clean version (no comments) ----
def largest_uni_num_clean(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    largest_num = float('-inf')

    for num in nums:
        if freq[num] == 1:
            largest_num = max(largest_num, num)

    return -1 if largest_num == float('-inf') else largest_num
