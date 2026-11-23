"""Clone an undirected graph (two common solutions in this file).

Approach 1 (DFS + HashMap):
Use depth-first traversal and a map from original node -> cloned node.
When visiting a node:
- If it is already cloned, return the clone (prevents infinite loops).
- Otherwise create its clone, store it in the map, and recursively clone
  each neighbor.

Pseudocode (DFS):
1. If input node is null, return null.
2. Maintain oldToNew map.
3. dfs(x):
    a. If x in oldToNew, return oldToNew[x].
    b. Create clone of x and store in map.
    c. For each neighbor of x, append dfs(neighbor) to clone.neighbors.
    d. Return clone.
4. Return dfs(startNode).

Complexity (DFS):
Time: O(V + E), each node and edge is processed once.
Space: O(V) for the map and recursion stack (worst case).

Approach 2 (BFS + HashMap):
Use a queue to traverse level by level. Create clone nodes lazily when first
seen, and connect cloned neighbors as edges are explored.

Pseudocode (BFS):
1. If input node is null, return null.
2. Create oldToNew map with the start node clone.
3. Push start node into queue.
4. While queue not empty:
    a. Pop current node.
    b. For each neighbor:
        - If neighbor not cloned, clone it and enqueue neighbor.
        - Append cloned neighbor to cloned current node's neighbors.
5. Return clone of start node.

Complexity (BFS):
Time: O(V + E), each vertex and edge is visited once.
Space: O(V) for the map and queue.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])

        return oldToNew[node]