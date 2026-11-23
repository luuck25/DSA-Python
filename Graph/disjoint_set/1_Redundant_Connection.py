"""Find the edge that first creates a cycle using a disjoint-set structure.

Approach:
Initially, each vertex belongs to its own component. Process edges in order
and use union-find to check whether their endpoints are already connected.
If they are, the edge closes a cycle and is redundant. Otherwise, merge the
two components. `find` uses path compression, and `union` uses rank to keep
the component trees shallow.

Pseudocode:
1. Initialize each vertex as its own parent and set each rank to one.
2. For each edge (u, v):
    a. Find the root of u and the root of v.
    b. If the roots are equal, return (u, v): this edge creates a cycle.
    c. Otherwise, attach the lower-rank root below the higher-rank root.
        If ranks are equal, attach one root below the other and increase rank.
3. Return the first redundant edge.

Complexity:
Time: O(E * alpha(V)) amortized for E edges and V vertices, where alpha is
the inverse Ackermann function (effectively constant for practical inputs).
Space: O(V) for the parent and rank arrays.
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        par = [i for i in range(len(edges) + 1)]  # Each vertex starts in its own set.
        rank = [1] * (len(edges) + 1)  # Rank estimates tree height for efficient unions.

        def find(x):

            if x == par[x]:
                return x
            par[x] = find(par[x])  # Path compression points x directly to its root.
            return par[x]


        def union(x,y):
            parent_x = find(x)  # Find the set representative for each endpoint.
            parent_y = find(y)

            if parent_x == parent_y:
                return False  # Already connected: this edge would create a cycle.

            # Attach the shallower tree below the deeper tree.
            if rank[parent_x] > rank[parent_y]:
                par[parent_y] = parent_x
            elif rank[parent_y] > rank[parent_x]:
                par[parent_x] = parent_y
            else:
                par[parent_y] = parent_x
                rank[parent_x] += 1
            return True    

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]  # First edge whose endpoints are already connected.
