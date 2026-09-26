"""
Next Greater Element II (Circular Array) — Plain English Walkthrough
=====================================================================
Problem:
    Given a CIRCULAR array, find the next greater element for each element.
    The array wraps around — after the last element, you continue from the first.
    If no greater element exists, return -1.

    Input:  [1, 2, 1]
    Output: [2, -1, 2]

    Explanation (circular):
        1 → look right: 2 is greater → 2 ✅
        2 → look right: 1, then wrap to 1 → nothing greater → -1
        1 → wrap around: 1 (not greater), 2 is greater → 2 ✅

How is this different from Next Greater Element I?
    In NGE I, the array is linear — you stop at the end.
    Here, the array is CIRCULAR — after the last element you wrap to the start.

Key Trick — Loop through the array TWICE using modulo:
-------------------------------------------------------
    Instead of duplicating the array [1,2,1,1,2,1], we loop from
    0 to 2n-1 and use i % n to wrap around.

    For [1, 2, 1], n=3, we iterate i = 0,1,2,3,4,5:
        i=0 → i%3=0 → nums[0]=1   ← first pass
        i=1 → i%3=1 → nums[1]=2   ← first pass
        i=2 → i%3=2 → nums[2]=1   ← first pass
        i=3 → i%3=0 → nums[0]=1   ← second pass (wrapping!)
        i=4 → i%3=1 → nums[1]=2   ← second pass
        i=5 → i%3=2 → nums[2]=1   ← second pass

    We only PUSH indices during the FIRST pass (i < n).
    The second pass is just for POPPING — finding next greater elements
    that need to wrap around.

Step-by-step with [1, 2, 1]:
------------------------------
    result = [-1, -1, -1], stack = []

    --- First pass (i=0 to 2): push indices AND pop ---

    i=0: curr=1, stack=[]
         nothing to pop → push 0                stack=[0]

    i=1: curr=2, stack=[0]
         2 > nums[0]=1 → pop 0, result[0]=2     stack=[]
         i<3 → push 1                           stack=[1]

    i=2: curr=1, stack=[1]
         1 < nums[1]=2 → can't pop
         i<3 → push 2                           stack=[1, 2]

    --- Second pass (i=3 to 5): only pop, NO pushing ---

    i=3: curr=nums[0]=1, stack=[1, 2]
         1 < nums[2]=1 → can't pop
         i≥3 → don't push

    i=4: curr=nums[1]=2, stack=[1, 2]
         2 > nums[2]=1 → pop 2, result[2]=2     stack=[1]
         2 ≥ nums[1]=2 → can't pop (not strictly greater)
         i≥3 → don't push

    i=5: curr=nums[2]=1, stack=[1]
         1 < nums[1]=2 → can't pop
         i≥3 → don't push

    Remaining stack [1] → stays -1 (no next greater for index 1)

    Result: [2, -1, 2] ✅

Why only push in the first pass?
    Each index should appear on the stack ONCE. The second pass exists
    solely to find "wraparound" next-greater matches for elements that
    didn't find one in the first pass.

Approach:
    1. Initialize result with -1s (default: no next greater)
    2. Loop i from 0 to 2n-1 (simulates two passes around the circle)
    3. Use i % n to get the actual index (handles wrapping)
    4. Monotonic stack logic: pop smaller elements, record next greater
    5. Only push indices during the first pass (i < n)

Time:  O(n) — we loop 2n times, each element pushed once and popped at most once
Space: O(n) — stack + result array
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # Edge case
        if not nums:
            return []

        len_nums = len(nums)
        # Initialize result with -1 (default: no next greater element)
        result = len_nums * [-1]

        # Monotonic decreasing stack (stores indices)
        stack = []

        

        # Loop 2n times to simulate circular array
        # First pass (i=0 to n-1): push and pop
        # Second pass (i=n to 2n-1): only pop (handle wraparound matches)
        for i in range(2 * len_nums):

            # Use modulo to wrap around: index 5 in a size-3 array → 5%3 = 2
            curr_num = nums[i % len_nums]

            # Pop all elements smaller than current — current IS their next greater
            while stack and curr_num > nums[stack[-1]]:
                index = stack.pop()
                result[index] = curr_num

            # Only push during the first pass — each index appears on stack once
            if i < len_nums:
                stack.append(i)

        return result

    # ---- Clean version (no comments) ----
    def nextGreaterElements_clean(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        result = len(nums) * [-1]
        stack = []
        len_nums = len(nums)

        for i in range(2 * len_nums):
            curr_num = nums[i % len_nums]
            while stack and curr_num > nums[stack[-1]]:
                index = stack.pop()
                result[index] = curr_num
            if i < len_nums:
                stack.append(i)

        return result
