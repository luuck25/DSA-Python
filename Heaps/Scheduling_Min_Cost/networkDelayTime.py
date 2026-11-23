"""
Network Delay Time

Description:
Given directed, weighted edges `times`, a source node `k`, and `n` nodes,
find the time it takes for the signal to reach every node. Return -1 if any
node is unreachable.

Approach:
1. Build an adjacency list mapping each node to its outgoing (neighbor, travel
    time) edges.
2. Start Dijkstra's algorithm from `k`, using a min-heap of (elapsed time,
    node) candidates. The heap always provides the candidate with the smallest
    elapsed time.
3. When a node is popped for the first time, its elapsed time is its shortest
    travel time. Mark it visited and add that time to each unvisited neighbor's
    travel time, pushing those candidates into the heap.
4. The last finalized time is the time the signal needs to reach the farthest
    node, provided all n nodes were reached. Otherwise return -1.

Let:
- `V = n` = number of nodes
- `E = len(times)` = number of directed edges

Time Complexity:
1. Build the adjacency list by scanning E edges: O(E).
2. Dijkstra pushes at most one candidate per edge, plus the source: O(E + 1)
    heap pushes. Each heap operation costs O(log(E + 1)) because the heap can
    contain O(E) candidate entries.
3. Each node is finalized once, and each outgoing edge of a finalized node is
    examined once: O(V + E) work apart from heap operations.
Overall:
        O(E) + O(V) + O(E)                         # build, finalize nodes, scan edges
    + O(log(E + 1))                             # push the source
    + E * O(log(E + 1))                         # up to E edge-candidate pushes
    + (E + 1) * O(log(E + 1))                   # up to E + 1 heap pops
    = O(E) + O(V) + O(E) + O(log(E + 1))
        + E * O(log(E + 1)) + (E + 1) * O(log(E + 1))
    = O(V + 2E + (2E + 2) log(E + 1))
    = O(V + (E + 1) log(E + 1))
    = O((V + E) log(E + 1))

The first terms are graph construction, node finalization, edge scanning, and
heap operations, respectively. For a simple graph, this is often written as
O((V + E) log V), since E is at most O(V^2).

Space Complexity:
- The adjacency list stores V nodes and E edges: O(V + E).
- The visited set stores at most V nodes: O(V).
- The heap can contain O(E) pending candidates, including stale entries: O(E).
Overall auxiliary space: O(V + E), including the adjacency list.

https://www.youtube.com/watch?v=EaphyqKU4PQ&t=46s
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)

        for u, v, w in times:  # O(E) total to build the adjacency list
            edges[u].append((v, w))  # O(1) amortized per edge

        minheap = []
        t = 0 

        heapq.heappush(minheap, (0, k))  # Heap has at most O(E + 1) entries

        visited = set()  # O(V)

        while minheap:

            w1, n1 = heapq.heappop(minheap)  # O(log(E + 1)); heap can hold O(E) entries

            if n1 in visited:
                continue
            visited.add(n1)

            t = w1

            for n2, w2 in edges[n1]:  # O(E) total across finalized nodes

                if n2 not in visited:

                    heapq.heappush(minheap, (w1 + w2, n2))  # O(log(E + 1))

        return t if len(visited) == n else -1


"""
Pseudocode:
-----------
function networkDelayTime(times, n, source):
    graph = adjacency list built from times
    min_heap = [(0, source)]
    visited = empty set
    last_time = 0

    while min_heap is not empty:
        time, node = pop smallest entry
        if node is already visited:
            continue

        mark node visited
        last_time = time

        for each (neighbor, travel_time) from node:
            if neighbor is not visited:
                push (time + travel_time, neighbor) into min_heap

    if every node was visited:
        return last_time
    return -1
"""

