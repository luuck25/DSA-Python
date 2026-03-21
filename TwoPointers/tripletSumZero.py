"""
Problem: 3Sum - Find All Triplets with Zero Sum
------------------------------------------------
Given an array of unsorted numbers, find all unique triplets in it
that add up to zero.

This is a classic interview problem (LeetCode #15) that combines
sorting with the Two Pointer technique.

Example:
    Input:  [-3, 0, 1, 2, -1, 1, -2]
    Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    
    Input:  [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
"""


def sumTriplets(arr: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in the array that sum to zero.
    
    Algorithm (Sort + Two Pointer):
    -------------------------------
    1. SORT the array first (enables two pointer technique)
    2. Fix one element (arr[i]) and find pairs that sum to -arr[i]
    3. Use Two Pointers (start, end) to find the pairs in remaining array
    4. Use a SET to automatically handle duplicate triplets
    
    Visual Example:
    ---------------
    arr = [-3, 0, 1, 2, -1, 1, -2]
    
    After sorting: [-3, -2, -1, 0, 1, 1, 2]
    
    i=0, arr[i]=-3, need pair that sums to 3:
         [-3, -2, -1, 0, 1, 1, 2]
           ^   ^               ^
           i  start           end
         
         -2 + 2 = 0 < 3 → move start right
         -1 + 2 = 1 < 3 → move start right
         0 + 2 = 2 < 3  → move start right
         1 + 2 = 3 = 3  → FOUND! (-3, 1, 2), move both pointers
         1 + 1 = 2 < 3  → move start right
         start >= end   → done with i=0
    
    i=1, arr[i]=-2, need pair that sums to 2:
         Found: (-2, 0, 2) and (-2, 1, 1)
    
    ... continue for remaining elements
    
    Why sorting works:
    ------------------
    - If curr_sum < 0: sum is too small → increase it by moving start RIGHT
    - If curr_sum > 0: sum is too large → decrease it by moving end LEFT
    - If curr_sum == 0: FOUND! Record triplet, move both pointers
    
    Args:
        arr: A list of integers (can be unsorted, can have duplicates)
        
    Returns:
        A list of unique triplets [a, b, c] where a + b + c = 0
        
    Time Complexity: O(n²)
        - Sorting: O(n log n)
        - Outer loop: O(n)
        - Inner two-pointer loop: O(n)
        - Total: O(n log n) + O(n²) = O(n²)
        
    Space Complexity: O(n)
        - Sorting may use O(n) space (depending on implementation)
        - Set to store results: O(n) in worst case
        - Result list: O(n) for storing triplets
    """
    # Edge case: need at least 3 elements
    if len(arr) < 3:
        return []

    # STEP 1: Sort the array - REQUIRED for two pointer technique
    arr.sort()
    
    # Use set to automatically handle duplicate triplets
    # Tuples are hashable, so we store triplets as tuples
    result = set()

    # STEP 2: Fix one element and find pairs for remaining
    # Only go up to len(arr)-2 because we need at least 2 more elements
    for i in range(len(arr) - 2):
        # Two pointers for the remaining subarray
        start = i + 1
        end = len(arr) - 1

        # STEP 3: Two pointer search for pair that sums to -arr[i]
        while start < end:
            curr_sum = arr[i] + arr[start] + arr[end]

            if curr_sum == 0:
                # Found a valid triplet!
                result.add((arr[i], arr[start], arr[end]))
                # Move both pointers to find other possible pairs
                start += 1
                end -= 1
            elif curr_sum < 0:
                # Sum is too small, need larger values → move start right
                start += 1
            else:
                # Sum is too large, need smaller values → move end left
                end -= 1

    # STEP 4: Convert set of tuples to list of lists (required output format)
    return [list(triplet) for triplet in result]


# Test the function
print(sumTriplets([-3, 0, 1, 2, -1, 1, -2]))
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

print(sumTriplets([-5, 2, -1, -2, 3]))
# Output: [[-5, 2, 3], [-2, -1, 3]]

print(sumTriplets([0, 0, 0, 0]))
# Output: [[0, 0, 0]]

