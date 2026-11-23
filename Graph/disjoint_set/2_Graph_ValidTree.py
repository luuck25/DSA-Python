"""Check whether an undirected graph is a valid tree using Union-Find.

Approach:
A tree with n vertices must have exactly n - 1 edges. Reject the graph
immediately if this condition is not met. Then process every edge using a
disjoint-set structure. If an edge connects vertices that already share a
root, it creates a cycle, so the graph is not a tree. With n - 1 edges and
no cycle, the graph is connected and therefore is a valid tree. `find` uses
path compression and `union` uses rank.

Pseudocode:
1. If the number of edges is not n - 1, return false.
2. Initialize each vertex as its own parent and set each rank to one.
3. For each edge (u, v):
    a. Find the root of u and the root of v.
    b. If the roots are equal, return false because the edge creates a cycle.
    c. Otherwise, merge the two sets by rank.
4. Return true.

Complexity:
Time: O(E * alpha(n)) amortized for E edges and n vertices, where alpha is
the inverse Ackermann function. Since a valid candidate has E = n - 1, this
is also O(n * alpha(n)).
Space: O(n) for the parent and rank arrays.
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        par = [i for i in range(n)]
        rank = [1] * n


        def find(n):
            if n == par[n]:
                return n
            par[n] = find(par[n])

            return par[n]

        def union(x,y):

            parent_x = find(x)
            parent_y = find(y)

            if parent_x == parent_y:
                return False
            elif rank[parent_x]  >    rank[parent_y]:
                par[parent_y] = parent_x
            elif rank[parent_y]  >    rank[parent_x]:    
                par[parent_x] =  parent_y
            else:
                par[parent_y] =   parent_x
                rank[parent_x] += 1
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return False
        return True                         