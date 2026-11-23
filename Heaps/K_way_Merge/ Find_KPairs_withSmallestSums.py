"""
Find K Pairs with the Smallest Sums

Description:
Given two sorted integer arrays, return up to `k` pairs (one value from each
array) with the smallest sums.

Approach:
1. Treat each possible pair as a cell `(i, j)` in a grid. Because both input
    arrays are sorted, moving right or down in this grid cannot decrease the
    pair sum.
2. Start with pair `(0, 0)` in a min-heap. Store its sum and indices so the
    smallest-sum pair is always removed first.
3. Repeatedly pop the smallest pair and append its values to the result.
4. After popping `(i, j)`, add its unvisited neighbors `(i + 1, j)` and
    `(i, j + 1)` when they are within the arrays. The `visited` set prevents
    adding the same index pair more than once.
5. Stop after returning `k` pairs or when no pairs remain.

Let:
- `m = len(nums1)`
- `n = len(nums2)`
- `r = min(k, m * n)`, the maximum number of pairs returned

Time Complexity:
1. Initialize the heap and visited set with `(0, 0)`: O(1).
2. Pop at most r pairs. Each heap pop costs O(log(r + 1)): O(r log(r + 1)).
3. Each popped pair checks at most two neighbors. There are at most 2r neighbor
    checks and insertions; each insertion costs O(log(r + 1)). This is
    O(r log(r + 1)) total. Set membership and insertion are O(1) on average.
4. Appending the r output pairs costs O(r).
Overall: O(r log(r + 1)), where r = min(k, m * n).

Space Complexity:
- The heap stores O(r) pending index pairs.
- `visited` stores O(r) index pairs, since at most two neighbors are added per
  popped pair.
- The result stores O(r) output pairs.
Total auxiliary and output space: O(r). The input arrays are not counted as
extra space.

https://www.youtube.com/watch?v=gJZfC9umfXg
"""

import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

        m = len(nums1)
        n = len(nums2)

        heap = []
        i, j= 0,0
        heapq.heappush(heap,(nums1[i]+nums2[j],(i,j)))
        visited = set()
        visited.add((i,j))
        result = []
        while k > 0 and heap:

            val,(i,j) = heapq.heappop(heap)
            result.append([nums1[i],nums2[j]])

            if i+1 < m and (i+1,j) not in visited:
                heapq.heappush(heap,(nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j))
            if j+1 < n and (i,j+1) not in visited:
                heapq.heappush(heap,(nums1[i]+nums2[j+1],(i,j+1)))
                visited.add((i,j+1))

            k -= 1

        return result


"""
Pseudocode:
-----------
function kSmallestPairs(nums1, nums2, k):
    m = length(nums1)
    n = length(nums2)
    if either array is empty or k <= 0:
        return empty list

    heap = [(nums1[0] + nums2[0], 0, 0)]
    visited = {(0, 0)}
    result = empty list

    while fewer than k pairs are in result and heap is not empty:
        sum, i, j = pop smallest entry from heap
        append [nums1[i], nums2[j]] to result

        for each neighbor (i + 1, j) and (i, j + 1):
            if neighbor is in bounds and not in visited:
                add neighbor to visited
                push (sum of neighbor, neighbor indices) into heap

    return result
"""
        




