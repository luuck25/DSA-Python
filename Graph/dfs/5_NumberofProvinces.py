"""
Number of Provinces

Description:
Given an n x n connectivity matrix for n cities, return the number of
provinces. Cities belong to the same province if they are connected directly
or through other connected cities.

Approach:
1. Convert the connectivity matrix into an adjacency list. For each pair of
    different cities, add an edge when the matrix says they are connected.
2. Keep a `visited` array to track cities already explored.
3. Scan every city. Whenever an unvisited city is found, it starts a new
    province; increment the count and run DFS to visit all cities reachable
    from it.
4. Return the number of DFS starts.

Let `n` be the number of cities.

Time Complexity:
1. Scan all n x n matrix entries to build the adjacency list: O(n^2).
2. DFS visits each city once and examines each adjacency-list edge at most
    once: O(V + E), where V = n and E <= n^2, so O(n^2) worst case.
3. The outer scan over cities takes O(n).
Overall: O(n^2).

Space Complexity:
- The adjacency list stores up to O(n^2) edges in a fully connected graph.
- The visited array and DFS recursion stack use O(n) space.
Overall auxiliary space: O(n^2), dominated by the adjacency list.
"""

from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        self.adj = [[] for _ in range(n)]

        # create adj list

        for i in range(n):
            for j in range(n):

                if isConnected[i][j] == 1 and i!=j:
                    self.adj[i].append(j)
        
        self.visited = [False] * n        
        count = 0
        for i in range(n):
            if not self.visited[i]:
                count += 1
                self.dfs(i)

                    
        return count            
                    
    def dfs(self,i:int):

        self.visited[i] = True

        for neighbour in self.adj[i]:

            if not self.visited[neighbour]:
                self.dfs(neighbour)


"""
Pseudocode:
-----------
function findCircleNum(isConnected):
    n = number of cities
    adjacency_list = n empty neighbor lists

    for each city i:
        for each city j:
            if i and j are different and connected:
                add j to adjacency_list[i]

    visited = n false values
    province_count = 0

    for each city:
        if city is not visited:
            province_count += 1
            dfs(city)

    return province_count

function dfs(city):
    mark city visited
    for each neighbor of city:
        if neighbor is not visited:
            dfs(neighbor)
"""

""
""
" Without buidling ADJ list"
""


"""
Second Solution: DFS Directly on the Connectivity Matrix

Approach:
1. Do not construct an adjacency list. Use each row of `isConnected` as the
    list of possible neighbors for that city.
2. Scan all cities. When an unvisited city is found, it starts a new province.
3. Run DFS from that city. For each city reached, scan its entire matrix row
    and recursively visit every connected, unvisited neighbor.
4. Return the number of DFS starts.

Let `n` be the number of cities.

Time Complexity:
1. The outer loop checks n cities: O(n).
2. Each city is visited at most once. Its DFS scans n entries in its matrix
    row, so the total DFS scanning work is O(n * n) = O(n^2).
Overall: O(n^2).

Space Complexity:
- The `visited` array stores n flags: O(n).
- The recursive DFS stack can contain up to n calls: O(n).
- No adjacency list or copied matrix is created.
Overall auxiliary space: O(n).
"""


from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(city):
            visited[city] = True

            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for city in range(n):
            if not visited[city]:
                count += 1
                dfs(city)

        return count


"""
Pseudocode for the second solution:
----------------------------------
function findCircleNum(isConnected):
    n = number of cities
    visited = n false values
    province_count = 0

    for each city:
        if city is not visited:
            province_count += 1
            dfs(city)

    return province_count

function dfs(city):
    mark city visited
    for neighbor from 0 to n - 1:
        if isConnected[city][neighbor] == 1 and neighbor is not visited:
            dfs(neighbor)
"""


class SolutionBFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = [False] * n
        qq = deque()

        def bfs():
            while qq:
                node = qq.popleft()

                for neighbour in range(n):
                    if not visited[neighbour] and isConnected[node][neighbour] != 0:
                        visited[neighbour] = True
                        qq.append(neighbour)

        for node in range(n):
            if not visited[node]:
                provinces += 1
                visited[node] = True
                qq.append(node)
                bfs()

        return provinces


"""
BFS directly on the connectivity matrix:
Mark cities visited before enqueueing so each city is queued only once.
The while loop processes all queued cities; no recursive bfs call is needed.

Time: O(n^2), since each of n cities scans its n possible neighbors once.
Auxiliary space: O(n) for the visited array and queue.

Pseudocode:
-----------
function findCircleNum(isConnected):
    visited = n false values
    provinces = 0
    queue = empty queue

    bfs():
        while queue is not empty:
            node = remove city from queue
            for each possible neighbor:
                if neighbor is connected and not visited:
                    mark neighbor visited
                    add neighbor to queue

    for each city:
        if city is not visited:
            provinces += 1
            mark city visited
            add city to queue
            bfs()

    return provinces
"""


