"""
PROBLEM: Maximal Rectangle
Find the largest rectangle containing only 1's in a binary matrix.

APPROACH:
1. Convert the 2D matrix problem into multiple 1D "largest rectangle in histogram" problems
2. For each row, treat heights of consecutive '1's as a histogram
3. Use a monotonic stack to efficiently find the largest rectangle in each histogram
4. Track the maximum area found across all rows

INTUITION:
- At each row, heights[j] represents the height of consecutive 1's above (including current row)
- If matrix[row][j] == '1': increase height, else reset to 0
- Use stack to maintain indices in increasing order of heights
- When a smaller height is encountered, pop from stack and calculate areas

PSEUDO CODE:
    heights = array of 0's with length = number of columns
    maxArea = 0
    
    FOR each row in matrix:
        FOR each column j:
            IF matrix[row][j] == '1':
                heights[j] += 1
            ELSE:
                heights[j] = 0
        
        # Find largest rectangle in histogram for current heights
        stack = empty
        FOR i in range(0 to columns):
            WHILE stack is not empty AND current height < heights[stack.top]:
                h = heights[stack.pop()]
                width = i if stack is empty ELSE (i - stack.top - 1)
                area = h * width
                maxArea = max(maxArea, area)
            stack.push(i)
    
    RETURN maxArea

TIME COMPLEXITY: O(m * n)
    - m = number of rows, n = number of columns
    - Outer loop: m iterations (for each row)
    - Inner height update: n operations
    - Stack processing: each element pushed/popped once = O(n)
    - Total: O(m * (n + n)) = O(m * n)

SPACE COMPLEXITY: O(n)
    - heights array: O(n)
    - stack: O(n) in worst case
    - Total: O(n)

EXAMPLE:
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    
    Row 0: heights = [1,0,1,0,0] -> maxArea = 1
    Row 1: heights = [2,0,2,1,1] -> maxArea = 2
    Row 2: heights = [3,1,3,2,2] -> maxArea = 6
    Row 3: heights = [4,0,0,3,0] -> maxArea = 6
    
    Output: 6
"""

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # Initialize variables
        cols = len(matrix[0])  # Number of columns
        heights = [0] * cols   # Height array representing histogram for each column
        maxArea = 0            # Track maximum rectangle area found

        # Process each row in the matrix
        for row in matrix:
            # Update heights array: build histogram for current row
            for j in range(cols):
                if row[j] == '1':
                    # If current cell is '1', increment the height (consecutive 1's count)
                    heights[j] += 1
                else:
                    # If current cell is '0', reset height to 0 (histogram breaks)
                    heights[j] = 0

            # ===== Find largest rectangle in histogram using monotonic stack =====
            st = []   # Monotonic stack stores indices in increasing order of heights

            # Iterate through heights (include len(heights) to process remaining stack)
            for i in range(len(heights) + 1):
                # Get current height (0 if we've processed all columns)
                current = 0 if i == cols else heights[i]

                # Pop from stack when current height is smaller than stack top
                # This means we found the right boundary for rectangle with height at stack top
                while st and current < heights[st[-1]]:
                    # Pop the index with greater height
                    h = heights[st.pop()]

                    # Calculate width of rectangle with height h
                    if not st:
                        # If stack is empty, width extends from start (0) to current position
                        width = i
                    else:
                        # Otherwise, width is between current position and new stack top
                        # (st[-1] is the left boundary, i is the right boundary)
                        width = i - st[-1] - 1

                    # Calculate area and update maximum
                    maxArea = max(maxArea, h * width) 

                # Push current index to stack for future processing
                st.append(i)    
        

        