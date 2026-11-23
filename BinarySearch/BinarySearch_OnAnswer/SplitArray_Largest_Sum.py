"""
Split Array Largest Sum

Description:
Given an array of non-negative integers `nums` and an integer `k`, split the
array into `k` non-empty contiguous subarrays. Return the smallest possible
value of the largest subarray sum.

Approach:
1. Binary search on the largest allowed subarray sum.
2. The minimum possible limit is max(nums), because every number must fit in
    some subarray. The maximum is sum(nums), which allows the whole array to be
    one subarray.
3. For a candidate limit `mid`, greedily scan the numbers in order. Start a
    new subarray whenever adding the next number would make the current sum
    exceed `mid`.
4. If this limit needs at most `k` subarrays, it is feasible. Keep it as a
    candidate and try a smaller limit by setting `right = mid`.
5. If it needs more than `k` subarrays, the limit is too small. Search larger
    limits by setting `left = mid + 1`.
6. Stop when `left == right`; this is the minimum feasible largest sum.

Time Complexity: O(n * log S), where n is the number of values and S is their
     sum. Each binary-search candidate is checked in O(n) time, and the search
     range has at most S possible values.
Space Complexity: O(1), using only a fixed number of variables.
"""

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left < right :

            mid = (left + right) // 2

            sub_arrays = 1

            curr_sum = 0

            
            for num in nums:
                if curr_sum + num > mid:
                    curr_sum = 0
                    sub_arrays += 1


                curr_sum += num


            if sub_arrays <=k:
                right = mid
            else:
                left = mid+1

        return left


"""
Pseudocode:
-----------
function splitArray(nums, k):
    left = maximum value in nums
    right = sum of nums

    while left < right:
        limit = floor((left + right) / 2)
        subarrays = 1
        current_sum = 0

        for each number in nums, in order:
            if current_sum + number > limit:
                subarrays += 1
                current_sum = 0
            current_sum += number

        if subarrays <= k:
            right = limit  // Limit works; try a smaller one
        else:
            left = limit + 1  // Limit is too small

    return left  // Minimum possible largest subarray sum
"""


        