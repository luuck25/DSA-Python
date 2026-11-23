import heapq

"""Find the minimum cost to connect all points using Prim's algorithm.

Approach:
Model each point as a vertex in a complete, undirected graph. The weight
between two points is their Manhattan distance: |x1 - x2| + |y1 - y2|.
Build the adjacency list for every pair, then run Prim's algorithm starting
from vertex 0. The min-heap selects the cheapest edge that can add a new
vertex to the growing minimum spanning tree (MST). `inMst` ignores stale
heap entries whose vertices were already added.

Pseudocode:
1. For every pair of distinct points (i, j):
    a. Compute their Manhattan distance.
    b. Add a weighted edge between i and j to the adjacency list.
2. Initialize a min-heap with (cost 0, vertex 0), all vertices outside the
    MST, and total cost zero.
3. While the heap is not empty:
    a. Pop the lowest-cost (edge cost, vertex).
    b. If the vertex is already in the MST, skip this stale entry.
    c. Otherwise, add the vertex and edge cost to the MST and total.
    d. Push each edge from it to a vertex not yet in the MST.
4. Return the total MST cost.

Complexity for this implementation:
Let V be the number of points. The complete graph has E = O(V^2) edges.
Time: O(V^2 log V), dominated by heap pushes and pops for the edges.
Space: O(V^2) for the adjacency list and up to O(V^2) heap entries.
"""


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        vertices = len(points)
        adj = [[] for _ in range(vertices)]

        # Build the adjacency list
        for i in range(vertices):
            for j in range(i+1,vertices):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    adj[i].append((j, distance))
                    adj[j].append((i,distance)) 

        def primsalgo(adj, v):
            pq = []
            heapq.heappush(pq, (0, 0))

            inMst = [False] * v
            total_cost = 0

            while pq:
                wt, node = heapq.heappop(pq)

                if inMst[node]:
                    continue

                inMst[node] = True
                total_cost += wt

                for neighbour_node, neighbour_wt in adj[node]:
                    if not inMst[neighbour_node]:
                        heapq.heappush(pq, (neighbour_wt, neighbour_node))

            return total_cost

        return primsalgo(adj, vertices)