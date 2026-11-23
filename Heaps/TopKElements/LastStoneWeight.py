"""
Last Stone Weight

Description:
Given stones with positive integer weights, repeatedly smash the two heaviest
stones. If their weights differ, keep a stone with the difference in weight;
if they are equal, both are destroyed. Return the last remaining stone's
weight, or 0 if no stones remain.

Approach:
1. Python's `heapq` is a min-heap, so negate each weight to simulate a max-heap.
2. Heapify the weights so the heaviest stone can be removed efficiently.
3. While at least two stones remain, remove the two heaviest stones.
4. If their weights differ, push their positive difference back into the heap
   as a negative value. If they are equal, both are gone.
5. When zero or one stone remains, return its weight, or 0 if the heap is empty.

Time Complexity: O(n log n), where n is the number of stones. Heapifying takes
    O(n), and up to n smash operations each perform heap operations in O(log n).
Space Complexity: O(n), for the heap of negated stone weights.
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        
        stones = [-stone for stone in stones] # simulate max heap

        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x!=y:
                heapq.heappush(stones,-(x - y))



        return -stones[-1] if stones else 0


"""
Pseudocode:
-----------
function lastStoneWeight(stones):
    convert every weight to its negative
    heapify stones  // Negative weights make the min-heap act like a max-heap

    while the heap contains at least two stones:
        heaviest = negative of pop(heap)
        second_heaviest = negative of pop(heap)

        if heaviest != second_heaviest:
            push -(heaviest - second_heaviest) into heap

    if heap is empty:
        return 0
    return negative of the remaining heap value
"""
    
        




