"""
K Closest Points to Origin

Description:
Given points on a 2D plane and an integer `k`, return the `k` points closest
to the origin (0, 0). Distance is measured by Euclidean distance.

Approach:
1. Keep a heap containing at most `k` points.
2. For each point, calculate its distance from the origin and push the
    negative distance and point into Python's min-heap. Negative distances make
    the smallest heap entry represent the farthest point currently retained.
3. If the heap has more than `k` points, remove its root, discarding the
    farthest point among those seen so far.
4. After processing every point, the heap contains the `k` closest points.
    Pop them into the result and return it. Their output order is not specified.

- `n = len(points)`
- `k` is the number of points to return

Time Complexity:
For each of the `n` points:
- `heappush` takes O(log k); the heap grows to at most k + 1 before trimming.
- If the heap exceeds size k, `heappop` takes O(log k).

After processing all points, popping the remaining k points takes O(k log k).
Overall: O(n log k + k log k) = O(n log k), assuming k <= n.

Space Complexity:
The heap stores at most k points, and `result` stores k points: O(k).
The input `points` is not counted as extra space.
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap =[]
        for point in points:
            x = point[0]
            y = point[1]

            dist_origin = (x ** 2 + y ** 2) ** 0.5

            ## You do not need to calculate the square root. 
            # Comparing squared distances gives the same ordering and avoids unnecessary work:
            # dist_origin = (x ** 2 + y ** 2)

            heapq.heappush(heap,(-dist_origin,point))
          
            if len(heap) > k:
                
                heapq.heappop(heap)

        result = []
        while heap: 
            result.append(heapq.heappop(heap)[1])

        return result


"""
Pseudocode:
-----------
function kClosest(points, k):
    heap = empty min-heap

    for each point (x, y) in points:
        distance = square root of (x squared + y squared)
        push (-distance, point) into heap

        if heap size > k:
            pop the heap  // Remove the farthest retained point

    result = empty list
    while heap is not empty:
        append the point from the popped heap entry to result

    return result
"""
        



