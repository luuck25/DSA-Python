


"""
Problem: Dutch National Flag Algorithm (3-Way Partitioning)
------------------------------------------------------------
Given an array containing only 0s, 1s, and 2s, sort it in-place
so that all 0s come first, followed by all 1s, then all 2s.

Also known as: Sort Colors (LeetCode #75)

Example:
    Input:  [1, 0, 2, 1, 0]
    Output: [0, 0, 1, 1, 2]
"""


def sort(arr: list[int]) -> list[int]:
    """
    Sort an array of 0s, 1s, and 2s using Dutch National Flag algorithm.
    
    Algorithm (Three Pointers):
    ---------------------------
    We use THREE pointers to partition the array into four regions:
    
    1. [0 ... low-1]     -> Contains all 0s (sorted)
    2. [low ... mid-1]   -> Contains all 1s (sorted)
    3. [mid ... high]    -> Unknown/unsorted (to be processed)
    4. [high+1 ... n-1]  -> Contains all 2s (sorted)
    
    Three Cases:
    ------------
    Case 1: arr[mid] == 0 -> Swap with low, increment both
    Case 2: arr[mid] == 1 -> Just increment mid
    Case 3: arr[mid] == 2 -> Swap with high, decrement high only
    
    Time Complexity: O(n) - Single pass through array
    Space Complexity: O(1) - Only three pointer variables
    """
    low = 0
    mid = 0
    high = len(arr) - 1
    

    # Process until mid crosses high
    while mid <= high:
        if arr[mid] == 0:
            # Case 1: Found 0 -> swap to left region
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # Case 2: Found 1 -> already in correct place
            mid += 1
        else:
            # Case 3: Found 2 -> swap to right region
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# Test the function
print(sort([1, 0, 2, 1, 0]))
# Output: [0, 0, 1, 1, 2]

print(sort([2, 0, 1, 2, 1, 0]))
# Output: [0, 0, 1, 1, 2, 2]