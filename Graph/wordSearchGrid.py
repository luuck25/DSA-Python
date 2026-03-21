"""
Word Search in 2D Grid (Right and Down Movement Only)

Problem:
- Find a word in a 2D grid where consecutive letters can only be:
  - Immediately to the RIGHT, or
  - Immediately BELOW the previous letter
- Return the path as a list of (row, col) coordinates

Approach: DFS with Backtracking
- Time Complexity: O(rows * cols * 2^len(word)) - worst case
- Space Complexity: O(len(word)) - recursion stack depth
"""

def find_word_in_grid(grid, word):
    """
    Find word in grid moving only right or down.
    Returns list of (row, col) coordinates or empty list if not found.
    """
    if not grid or not grid[0] or not word:
        return []
    
    rows = len(grid)
    print(f'rows are {rows}')
    cols = len(grid[0])
    print(f'cols are {cols}')
    
    def dfs(row, col, index, path):
        """
        DFS helper function
        
        Args:
            row: current row position
            col: current column position
            index: current index in the word we're trying to match
            path: list of coordinates visited so far
        
        Returns:
            path if word is found, None otherwise
        """
        # Base case: if we've matched all characters, return the path
        if index == len(word):
            return path
        
        # Boundary check: out of grid bounds
        if row >= rows or col >= cols:
            return None
        
        # Check if current cell matches the current character in word
        if grid[row][col] != word[index]:
            return None
        
        # Current cell matches! Add to path and explore further
        current_path = path + [(row, col)]
        
        # If this was the last character, we found the word!
        if index == len(word) - 1:
            return current_path
        
        # Try moving RIGHT (same row, next column)
        result = dfs(row, col + 1, index + 1, current_path)
        if result:
            return result
        
        # Try moving DOWN (next row, same column)
        result = dfs(row + 1, col, index + 1, current_path)
        if result:
            return result
        
        # Neither direction worked - backtrack
        return None
    
    # Try starting from every cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Only start DFS if first character matches
            if grid[row][col] == word[0]:
                result = dfs(row, col, 0, [])
                if result:
                    return result
    
    return []


# ============== TEST CASES ==============

grid1 = [
    ['b', 'b', 'b', 'a', 'l', 'l', 'o', 'o'],
    ['b', 'a', 'c', 'c', 'e', 's', 'c', 'n'],
    ['a', 'l', 't', 'e', 'w', 'c', 'e', 'w'],
    ['a', 'l', 'o', 's', 's', 'e', 'c', 'c'],
    ['w', 'o', 'o', 'w', 'a', 'c', 'a', 'w'],
    ['i', 'b', 'w', 'o', 'w', 'w', 'o', 'w']
]

word1_1 = "access"

print("Grid:")
for row in grid1:
    print(row)
print()

print(f"Finding '{word1_1}':")
result = find_word_in_grid(grid1, word1_1)
print(f"Path: {result}")

# Visualize the path
if result:
    print("\nVisualization:")
    for i, (r, c) in enumerate(result):
        print(f"  Step {i+1}: grid[{r}][{c}] = '{grid1[r][c]}'")


# Additional test cases
print("\n" + "="*50)
print("Additional Tests:")

word2 = "balloon"
result2 = find_word_in_grid(grid1, word2)
print(f"\nFinding '{word2}': {result2}")

word3 = "ace"
result3 = find_word_in_grid(grid1, word3)
print(f"Finding '{word3}': {result3}")

word4 = "xyz"  # Not in grid
result4 = find_word_in_grid(grid1, word4)
print(f"Finding '{word4}': {result4}")
