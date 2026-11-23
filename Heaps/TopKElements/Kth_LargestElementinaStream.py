"""
Kth Largest Element in a Stream

Description:
Design a class that receives an integer `k` and an initial list of numbers.
As new values are added, return the kth-largest value seen so far.

Approach:
1. Keep a min-heap containing at most the k largest values seen so far.
2. The smallest value in this heap, at index 0, is the kth-largest value:
    the other heap values are at least as large.
3. During initialization, heapify the input list and remove the smallest
    values until only k remain.
4. When adding a value, push it onto the heap. If the heap now has more than k
    values, remove the smallest; this discards a value outside the k largest.
5. Return the heap root.

Time Complexity:
- Initialization: O(n + (n - k) log n), where n is the initial list length.
  Heapifying takes O(n), then removing values until the heap has k items takes
  O((n - k) log n) in the worst case.
- Each add: O(log k), since the heap contains at most k + 1 items during an
  insertion.
Space Complexity: O(k) retained heap elements after initialization. The input
list is heapified in place and becomes the heap.
"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap, self.k = nums, k

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]    
        

"""
Pseudocode:
-----------
class KthLargest(k, nums):
    heap = nums
    build a min-heap from heap

    while heap has more than k values:
        remove the smallest value

    return the object

add(value):
    push value onto heap

    if heap has more than k values:
        remove the smallest value

    return the smallest value in heap
"""

