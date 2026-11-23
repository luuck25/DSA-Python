"""Determine whether all courses can be completed using Kahn's algorithm.

Approach:

Represent each prerequisite as a directed edge from the prerequisite course
to the course that depends on it. Compute each course's in-degree, then
process courses with in-degree zero using a queue. Processing a course
reduces the in-degree of its dependent courses. If all courses are
processed, the dependency graph has no cycle and all courses can be finished.

Pseudocode:

1. Create an adjacency list and initialize every course's in-degree to zero.
2. For each prerequisite pair, add an edge from prerequisite to dependent
    course and increment the dependent course's in-degree.
3. Enqueue all courses whose in-degree is zero; count them as processed.
4. While the queue is not empty:
    a. Remove one course from the queue.
    b. Decrement the in-degree of each course that depends on it.
    c. When a dependent course reaches in-degree zero, enqueue and count it.
5. Return true if the processed count equals the number of courses;
    otherwise, a cycle prevents completing all courses.

Complexity:
Time: O(V + E), where V is the number of courses and E is the number of
prerequisite pairs.
Space: O(V + E) for the adjacency list, in-degree array, and queue.

https://www.youtube.com/watch?v=lqjlGGMjSMU&list=PLpIkg8OmuX-LZB9jYzbbZchk277H5CbdY&index=12
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        in_degree = [0] * numCourses  # O(V) space

        adj = [[] for _ in range(numCourses)]  # O(V) space

        # Build the graph and in-degree counts - O(E) total across every pair

        for prerequisite in prerequisites:
            u = prerequisite[1]
            v = prerequisite[0]

            adj[u].append(v)  # O(1) each

            in_degree[v] += 1  # O(1) each


        qq = deque()  # O(V) worst case - holds every vertex at most once

        count = 0  # O(1) - just a counter, not a per-vertex structure

        # Seed the queue with every in-degree-0 course - O(V)

        for i in range(len(in_degree)):

            if  in_degree[i] == 0:
                qq.append(i)

        # Each vertex is popped at most once -> O(V) pops total
        
        while qq:

          node = qq.popleft()  # O(1) each
          count += 1  # O(1) each

          # Summed across every pop over the whole run, touches each edge once -> O(E) total
          for neighbour in adj[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                qq.append(neighbour)
                
        return True if count == numCourses else False            





        