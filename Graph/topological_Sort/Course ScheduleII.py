"""Return a valid course order using Kahn's topological-sort algorithm.

Approach:
Treat each prerequisite as a directed edge from the prerequisite course to
the course that depends on it. Compute each course's in-degree. Courses with
in-degree zero have no remaining prerequisites, so add them to both the
result and a queue. Repeatedly process queued courses, reducing the in-degree
of their dependents and adding newly available courses. If every course is
included, the result is a valid order; if a cycle exists, return an empty list.

Pseudocode:
1. Initialize an adjacency list and an in-degree count for every course.
2. For each prerequisite pair, add the prerequisite-to-dependent edge and
    increment the dependent course's in-degree.
3. Enqueue all courses with in-degree zero and append them to the result.
4. While the queue is not empty:
    a. Dequeue a course.
    b. Decrement the in-degree of each dependent course.
    c. When a dependent course reaches zero, enqueue it and append it to result.
5. Return the result if it contains all courses; otherwise return an empty list.

Complexity:
Time: O(V + E), where V is the number of courses and E is the number of
prerequisite pairs.
Space: O(V + E) for the adjacency list, in-degree array, queue, and result.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses  # O(V) space

        adj = [[] for _ in range(numCourses)]  # O(V) space

        # Build the graph and in-degree counts - O(E) total across every pair
        for prerequisite in prerequisites:
            u = prerequisite[1]
            v = prerequisite[0]

            adj[u].append(v)  # O(1) each

            in_degree[v] += 1  # O(1) each


        qq = deque()  # O(V) worst case - holds every vertex at most once

        result = []  # O(V) - at most one entry per course
        # Seed the queue with every in-degree-0 course - O(V)
        for i in range(len(in_degree)):

            if  in_degree[i] == 0:
                result.append(i)
                qq.append(i)

                

        # Each vertex is popped at most once -> O(V) pops total
        while qq:

          node = qq.popleft()  # O(1) each

          # Summed across every pop over the whole run, touches each edge once -> O(E) total
          for neighbour in adj[node]:
            in_degree[neighbour] -= 1

            if in_degree[neighbour] == 0:
                qq.append(neighbour)
                result.append(neighbour)
         
                    

        return result if len(result) == numCourses else []    
        