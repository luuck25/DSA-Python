"""Count connected components in an undirected graph with Union-Find.

Approach:
Start with each of the n vertices in its own component. For every edge,
find the roots of its endpoints. If the roots differ, union the two sets
and decrement the component count; if they are the same, the edge does not
join two previously separate components. `find` uses path compression and
`union` uses rank to keep the sets' trees shallow.

Pseudocode:
1. Set components = n; initialize each vertex as its own parent with rank 1.
2. For each edge (u, v):
    a. Find root_u and root_v.
    b. If the roots differ, union their sets by rank and decrement components.
3. Return components.

Complexity:
Time: O(n + E * alpha(n)) amortized, where E is the number of edges and
alpha is the inverse Ackermann function.
Space: O(n) for the parent and rank arrays.
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        components = n
        par = list(range(n))
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

            # Equivalent union-by-rank form for these branches:
            #  Ensure parent_x has the larger rank.
            # If parent_x has a smaller rank, swap the two roots.
            # if rank[parent_x] < rank[parent_y]:
            #     parent_x, parent_y = parent_y, parent_x
            # par[parent_y] = parent_x
            # if rank[parent_x] == rank[parent_y]:
            #     rank[parent_x] += 1
            else:
                par[parent_y] =   parent_x
                rank[parent_x] += 1
            
            return True

        for n1,n2 in edges:
            if union(n1,n2):
                components -= 1    



        return components         
        