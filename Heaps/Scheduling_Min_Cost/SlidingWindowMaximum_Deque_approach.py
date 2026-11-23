"""
Sliding Window Maximum - Monotonic Deque

Description:
Given an integer list `nums` and a window size `k`, return the maximum value
in each contiguous window of size k.

Approach:
1. Store indices in a deque so their corresponding values are in decreasing
    order from front to back. The front always points to the current maximum.
2. Before processing index `i`, remove the front index if it has fallen
    outside the current window.
3. Remove indices from the back while their values are smaller than `nums[i]`.
    They cannot be a future window maximum because the new value is larger and
    stays in the window at least as long.
4. Append `i` to the deque.
5. Once the first full window has been processed, append the front value to
    the result.

Let:
- `N = len(nums)`
- `k` = window size

Time Complexity:
1. The for-loop visits all N indices: O(N) iterations.
2. Each index is appended to the deque once: O(N) total appends.
3. Each index is removed from the front at most once and from the back at most
    once. Although there is a while-loop, all back removals across the entire
    algorithm total at most N: O(N).
4. Appending one maximum for each of the N - k + 1 windows costs O(N - k + 1),
    which is O(N).
Overall: O(N).

Space Complexity:
- The deque stores at most k indices: O(k).
- The result stores N - k + 1 maximum values: O(N - k + 1).
Total space including output: O(k + N - k + 1) = O(N). Auxiliary space,
excluding the returned result: O(k).

https://www.youtube.com/watch?v=WcTMo1SHV_s
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        qq = deque()

        result =[]

        for i in range(len(nums)):

            
            if qq and qq[0] == i -k:
                qq.popleft()
            
            while qq and nums[qq[-1]] < nums[i]:
                qq.pop()

            qq.append(i)

            if i>= k - 1:
                result.append(nums[qq[0]])

        return result


"""
Pseudocode:
-----------
function maxSlidingWindow(nums, k):
    deque = empty deque of indices
    result = empty list

    for each index i in nums:
        if deque front is outside the current window:
            remove front index

        while deque is not empty and value at back index < nums[i]:
            remove back index

        append i to deque

        if a full window has been processed:
            append value at deque front to result

    return result
"""

        


