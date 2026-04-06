

"""
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['b', 'b', 'b', 'a', 'l', 'l', 'o', 'o'],
    ['b', 'a', 'c', 'c', 'e', 's', 'c', 'n'],
    ['a', 'l', 't', 'e', 'w', 'c', 'e', 'w'],
    ['a', 'l', 'o', 's', 's', 'e', 'c', 'c'],
    ['w', 'o', 'o', 'w', 'a', 'c', 'a', 'w'],
    ['i', 'b', 'w', 'o', 'w', 'w', 'o', 'w']     
    
    
    
]
word1_1 = "access"      # [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
word1_2 = "balloon"     # [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]"""

def dfs(r, c, index, path):
    # Base case
    if index == len(word):
        return True

    # Invalid
    if r >= rows or c >= cols or grid[r][c] != word[index]:
        return False

    # Choose
    path.append((r, c))

    # Explore
    if dfs(r, c+1, index+1, path) or dfs(r+1, c, index+1, path):
        return True

    # Backtrack
    path.pop()

    return False

for r in range(rows):
    for c in range(cols):
        if dfs(r, c, 0, path):
            return path