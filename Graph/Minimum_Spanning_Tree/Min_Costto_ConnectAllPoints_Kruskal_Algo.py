"""Find the minimum cost to connect all points using Kruskal's algorithm.

Approach:
Treat each point as a vertex in a complete, undirected graph. The weight of
an edge is the Manhattan distance between its two points. Sort all edges by
weight, then use a disjoint-set union (DSU) structure to add an edge only
when it connects two previously separate components. Stop after selecting
V - 1 edges, which forms a minimum spanning tree (MST).

Pseudocode:
1. For every pair of points (i, j), where i < j:
    a. Compute their Manhattan distance.
    b. Add (distance, i, j) to the edge list.
2. Sort the edge list by distance.
3. Initialize a DSU with one component per point and total cost zero.
4. For each edge (weight, u, v) in sorted order:
    a. If u and v belong to different components, union them and add the
       weight to the total cost.
    b. Stop after accepting V - 1 edges.
5. Return the total cost.

Complexity for this implementation:
Let V be the number of points. The complete graph has E = O(V^2) edges.
Time: O(E log E), or O(V^2 log V), dominated by sorting; DSU operations
take O(E alpha(V)) amortized time, where alpha is the inverse Ackermann
function.
Space: O(E + V), or O(V^2), for the edge list and DSU arrays.
"""


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        vertices = len(points)
        edges = []

        # Build the edge list
        for i in range(vertices):
            for j in range(i + 1, vertices):
                x1, y1 = points[i]
                x2, y2 = points[j]

                distance = abs(x1 - x2) + abs(y1 - y2)

                edges.append((distance, i, j))

        # Sort edges by weight
        edges.sort()

        parent = list(range(vertices))
        rank = [0] * vertices

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        total_cost = 0
        edges_used = 0

        # Kruskal's algorithm
        for wt, u, v in edges:
            if union(u, v):
                total_cost += wt
                edges_used += 1

                if edges_used == vertices - 1:
                    break

        return total_cost