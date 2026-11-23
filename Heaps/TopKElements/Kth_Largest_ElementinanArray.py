"""
Kth Largest Element in an Array

Description:
Given an integer array `nums` and an integer `k`, return the kth largest
element. The kth largest element is based on sorted order, not the kth distinct
value.

Approach:
1. Maintain a min-heap containing at most `k` elements.
2. Push each number into the heap.
3. If the heap grows larger than `k`, remove its smallest element. That number
    cannot be among the `k` largest values processed so far.
4. After processing all numbers, the heap contains the `k` largest values.
    Its root, the smallest of those values, is the kth largest overall.

Time Complexity: O(n * log k), where n is the number of values. Each value is
     pushed into a heap of size at most k, with at most one removal per value.
Space Complexity: O(k), for the heap containing at most k values.
"""

import heapq

def findKthLargest(nums, k):
    heap = []

    for num in nums:                  # Runs n times
        heapq.heappush(heap, num)      # Insert
        if len(heap) > k:
            heapq.heappop(heap)        # Remove smallest

    return heap[0]


"""
Pseudocode:
-----------
function findKthLargest(nums, k):
    heap = empty min-heap

    for each num in nums:
        push num into heap
        if size of heap > k:
            remove the smallest value from heap

    return the smallest value in heap
"""