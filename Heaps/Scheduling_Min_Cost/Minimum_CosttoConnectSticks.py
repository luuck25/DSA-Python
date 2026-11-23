"""
Minimum Cost to Connect Sticks

Description:
Given stick lengths, connect them into one stick. Connecting two sticks costs
the sum of their lengths. Return the minimum total cost.

Approach:
1. Turn the stick lengths into a min-heap so the two shortest sticks are
    available at the root.
2. Repeatedly remove the two shortest sticks and connect them. Add their sum
    to the total cost, then push the combined stick back into the heap.
3. Continue until at most one stick remains. The accumulated cost is the
    minimum total connection cost.
4. The implementation heapifies `sticks` directly, so it modifies the input
    list rather than making a separate heap copy.

Let `n = len(sticks)`.

Time Complexity:
1. `heapify` builds the min-heap in O(n).
2. Each iteration combines two sticks and pushes one combined stick back.
    There are at most n - 1 iterations, and each iteration uses two heap pops
    and one push, each costing O(log n). Total: O(n log n).
3. Accumulating the cost takes O(1) per iteration, or O(n) overall, which is
    covered by the heap operations.
Overall: O(n log n).

Space Complexity:
- The heap reuses the input list and stores at most n lengths: O(n) heap
  storage, but no separate list is allocated.
- Excluding the input list, the algorithm uses O(1) auxiliary space.
Note: `sticks` is modified by `heapify` and subsequent heap operations.
"""

import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        heapq.heapify(min_heap)
        total_cost = 0

        while len(min_heap) > 1:
            new_stick = heapq.heappop(min_heap) + heapq.heappop(min_heap)
            total_cost += new_stick
            heapq.heappush(min_heap, new_stick)

        return total_cost


"""
Pseudocode:
-----------
function connectSticks(sticks):
    min_heap = sticks
    heapify(min_heap)
    total_cost = 0

    while heap contains more than one stick:
        first = pop smallest stick
        second = pop next-smallest stick
        combined = first + second
        total_cost += combined
        push combined into heap

    return total_cost
"""