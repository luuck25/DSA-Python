"""
Flood Fill

Description:
Starting from pixel `(sr, sc)`, recolor every pixel connected to it in the
four cardinal directions that has the same original color.

Approach:
1. Save the starting pixel's original color.
2. If the requested color is already the original color, return immediately;
    otherwise, recoloring would not mark visited pixels and DFS could loop.
3. Use DFS from the starting pixel. Stop when a coordinate is out of bounds
    or its color is not the original color.
4. Recolor a matching pixel before visiting its four neighbors. The changed
    color marks it as visited, so it will not be processed again.
5. Return the modified image.

Let `R` be the number of rows and `C` the number of columns.

Time Complexity:

each pixel visits 4 neighbours

so 4n, n here is r * c

1. Each pixel in the starting pixel's connected region is visited once.
2. Each visit checks four neighbors, which is constant work.
Worst case: O(R * C), if the whole image is in the connected region.

Space Complexity:
- The recursive DFS call stack can hold up to O(R * C) calls in the worst
  case, when the connected region contains the whole image.
- The image is recolored in place; no separate visited matrix is allocated.
Auxiliary space: O(R * C) worst case due to recursion.
"""

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        actual_color = image[sr][sc]

        if actual_color == color:
            return image

        row = len(image)
        col = len(image[0])

        def dfs(sr, sc):
            # No explicit return means each dfs call returns None by default.
            if 0 <= sr < row and 0 <= sc < col and image[sr][sc] == actual_color:
                image[sr][sc] = color

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = sr + dr
                    nc = sc + dc
                    dfs(nr, nc)

        dfs(sr, sc)
        return image


class SolutionDFSEarlyReturn:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        actual_color = image[sr][sc]

        if actual_color == color:
            return image

        row = len(image)
        col = len(image[0])

        def dfs(sr, sc):
            if sr < 0 or sr >= row or sc < 0 or sc >= col or image[sr][sc] != actual_color:
                return

            image[sr][sc] = color

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = sr + dr
                nc = sc + dc
                dfs(nr, nc)

        dfs(sr, sc)
        return image





"BFS Approach"

"""
BFS visited rule:
Mark a cell as visited before adding it to the queue. In this flood-fill
solution, changing the cell's color is the visited mark.

For example, if every cell has the same original color:

    A  B
    C  D

Starting at A, BFS adds B and C to the queue. When it processes B, it adds D.
If B only gets recolored when it is removed from the queue, then processing C
can still see D's original color and add D to the queue a second time. D is
then processed twice unnecessarily.

Recolor each matching neighbor before enqueueing it:

    image[nr][nc] = color
    qq.append((nr, nc))

Now another neighbor sees that D no longer has the original color and cannot
enqueue it again. The starting cell is also recolored before the BFS loop.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        actual_color = image[sr][sc]

        if actual_color == color:
            return image

        qq = deque([(sr,sc)])

        image[sr][sc] = color

        while qq:

            r,c = qq.popleft()

            for dr,dc in[(1,0),(-1,0),(0,1),(0,-1)]:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == actual_color:

                    image[nr][nc] = color

                    qq.append((nr,nc))
        return image            




            
