"""Solution 2: Dijkstra's algorithm using a min-heap.

Approach:
Keep the best known distance from the source to each vertex. A min-heap
always processes the currently closest vertex first. When a shorter route
to a neighbor is found, update its distance and push the new candidate into
the heap. Ignore popped entries that are no longer the best known distance.
This algorithm requires non-negative edge weights.

Pseudocode:
1. Set every distance to infinity, then set the source distance to zero.
2. Push (0, source) into a min-heap.
3. While the heap is not empty:
    a. Pop the smallest (distance, vertex).
    b. Skip it if its distance is stale.
    c. For each neighbor, relax the edge and push any improved distance.
4. Return the distance array.

Complexity:
Time: 

In normal graph heap contain edges equal to V vertices.

In dual connected graph, heap can contain edges being added multiple times in heap so heap can contain 
E edges.


so push would be E log(E) and pop would be E log(E) -> Elog(E)

in normal graph it would be E Log(V)


-- O(V log V) + O(E log V) = O((V + E) log V)


Space: O(V + E) auxiliary space in the worst case, including the distance
         array and heap entries (the input adjacency list is not counted).

         https://www.youtube.com/watch?v=l4cxEQnuH-U&list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY&index=27
"""

import heapq


class Solution:
    def dijkstra(self, adj: list[list[list[int]]], src: int) -> list[int]:
        # Start with every vertex unreachable; the source is distance zero.
        result = [float('inf')] * len(adj) # <- piece 1: O(V)
        min_heap = [] # <- piece 2: O(E), worst case
        result[src] = 0

        # Heap entries are (distance, vertex), so the nearest is popped first.
        heapq.heappush(min_heap, (0, src))

        while min_heap:
            distance, vertex = heapq.heappop(min_heap)  # <- happens up to V times, O(log V) each

            # A better route may have been found since this entry was pushed.
            if distance > result[vertex]:
                continue

            # Relax each outgoing edge and enqueue any improved route.
            for neighbor, weight in adj[vertex]:
                new_distance = distance + weight
                if new_distance < result[neighbor]:
                    result[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor)) # <- happens up to E times, O(log V) each

        return result