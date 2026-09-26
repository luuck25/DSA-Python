"""
Next Greater Element I — Plain English Walkthrough
====================================================
Problem:
    Given two arrays nums1 (subset of nums2) and nums2 (no duplicates),
    for each element in nums1, find its NEXT GREATER element in nums2.
    If no greater element exists, return -1 for that position.

    Input:  nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
    Output: [-1, 3, -1]

    Explanation:
        4 → in nums2: [1, 3, 4, 2] → after 4 comes 2, which is NOT greater → -1
        1 → in nums2: [1, 3, 4, 2] → after 1 comes 3, which IS greater → 3
        2 → in nums2: [1, 3, 4, 2] → nothing after 2 → -1

Visual Example — How Monotonic Stack works on nums2:
    nums2 = [1, 3, 4, 2]

    num=1:  stack=[]       → nothing to pop → push 1       stack=[1]
    num=3:  stack=[1]      → 3 > 1 → pop 1, map {1: 3}    stack=[]
                           → push 3                        stack=[3]
    num=4:  stack=[3]      → 4 > 3 → pop 3, map {1:3, 3:4} stack=[]
                           → push 4                        stack=[4]
    num=2:  stack=[4]      → 2 < 4 → can't pop → push 2   stack=[4, 2]

    Remaining stack [4, 2] → no next greater element for these

    Final map: {1: 3, 3: 4}

    Now look up nums1 = [4, 1, 2]:
        4 → not in map → -1
        1 → map[1] = 3  → 3
        2 → not in map → -1

    Result: [-1, 3, -1] ✅

Why a Monotonic Stack?
    Brute force: for each element, scan right → O(n²)
    Monotonic stack: process nums2 once, build a "next greater" map → O(n)

    The stack stays in DECREASING order (monotonic decreasing).
    When a new element is BIGGER than the top, it's the "next greater"
    for everything it can pop off.

    Think of it like a line of people:
    - Short person stands behind tall person → can't see past them
    - When a TALLER person arrives, all shorter people in front "see" them
      as their next greater → they leave the line (get popped)

Approach:
    1. Walk through nums2 with a monotonic stack
    2. When current num > stack top → pop and record: map[popped] = current num
    3. After processing nums2, the map has {value: next_greater_value}
    4. Look up each nums1 element in the map (default -1 if not found)

Time:  O(n + m) — n = len(nums2), m = len(nums1). Each element pushed/popped at most once.
Space: O(n) — stack + hashmap for nums2
"""

from typing import List


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Edge case
        if not nums2:
            return []

        # Map to store {value: its next greater element in nums2}
        frq = {}

        # Monotonic decreasing stack
        # Elements stay here until something BIGGER comes along
        stack = []

        for num in nums2:

            # Current num is GREATER than stack top → it's the "next greater"
            # for everything smaller sitting on the stack
            # Pop all smaller elements and record the answer
            while stack and num > stack[-1]:
                frq[stack.pop()] = num

            # Push current element — waiting for ITS next greater
            stack.append(num)

        # Anything left on stack has no next greater element (stays as -1)

        # Look up each nums1 element in the map
        for i in range(len(nums1)):

            if nums1[i] in frq:
                nums1[i] = frq[nums1[i]]  # found next greater
            else:
                nums1[i] = -1             # no next greater exists

        return nums1

    # ---- Clean version (no comments) ----

    # https://www.youtube.com/watch?v=3yI79Pujcf4

    
    def nextGreaterElement_clean(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return []

        frq = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                frq[stack.pop()] = num
            stack.append(num)

         #####   

        for i in range(len(nums1)):
            if nums1[i] in frq:
                nums1[i] = frq[nums1[i]]
            else:
                nums1[i] = -1

        return nums1
    
    #### or return [frq.get(num,-1) for num in nums1] 