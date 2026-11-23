import collections

"""Return a topological ordering using Kahn's algorithm.

Approach:
For each vertex, count how many incoming edges it has. Vertices with
in-degree zero have no prerequisites, so add them to a queue. Repeatedly
remove a ready vertex, add it to the ordering, and decrement the in-degree
of each of its neighbors. A neighbor becomes ready when its in-degree
reaches zero. This produces a topological order for a directed acyclic graph.
If the graph contains a cycle, this implementation returns only the vertices
it can process; a cycle is present when the result contains fewer than V nodes.

Pseudocode:
1. Initialize every vertex's in-degree to zero.
2. Scan all edges and count each destination's in-degree.
3. Enqueue all vertices with in-degree zero.
4. While the queue is not empty:
    a. Dequeue a vertex and append it to the result.
    b. For each outgoing neighbor, decrement its in-degree.
    c. Enqueue the neighbor if its in-degree becomes zero.
5. Return the result.

Complexity:
Time: O(V + E), since every vertex and edge is processed a constant number
of times.
Space: O(V) auxiliary space for the in-degree array, queue, and result.

https://www.youtube.com/watch?v=uVl4ftleTes
"""


class Solution:
    def topoSort(self, adj: list[list[int]]) -> list[int]:
        n = len(adj)
        in_degree = [0] * n

        # Calculate the in-degree of every vertex
        for neighbors in adj:
            for neighbor in neighbors:
                in_degree[neighbor] += 1

        # Add all vertices with in-degree 0
        qq = collections.deque()

        for i in range(n):
            if in_degree[i] == 0:
                qq.append(i)

        result = []

        while qq:
            node = qq.popleft()
            result.append(node)

            # Remove the outgoing edges from this node
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    qq.append(neighbor)

        return result