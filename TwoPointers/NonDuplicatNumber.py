"""
Problem: Remove Duplicates from Sorted Array (In-Place)
--------------------------------------------------------
Given a sorted array, remove the duplicates in-place such that each element
appears only once and return the new length.

This is a classic Two Pointer problem where we modify the array in-place
without using extra space.

Example:
    Input:  [2, 3, 3, 3, 6, 9, 9]
    Output: 4 (array becomes [2, 3, 6, 9, ...])
    
    Input:  [1, 1, 2, 2, 2, 3]
    Output: 3 (array becomes [1, 2, 3, ...])
"""


def nonDuplicateNumber(arr: list[int]) -> int:
    """
    Remove duplicates from a sorted array in-place and return count of unique elements.
    
    Algorithm (Two Pointer Technique):
    ----------------------------------
    1. Use 'next_unique' pointer to track where the next unique element should go
    2. Use 'i' pointer to scan through the array
    3. When we find a new unique element (different from last unique):
       - Place it at 'next_unique' position
       - Increment 'next_unique'
    
    Visual Example:
    ---------------
    arr = [2, 3, 3, 3, 6, 9, 9]
    
    Initial:    next_unique = 1
    
    i=1: arr[1]=3 != arr[0]=2 → place 3 at index 1, next_unique = 2
         [2, 3, 3, 3, 6, 9, 9]
              ^
    i=2: arr[2]=3 == arr[1]=3 → skip (duplicate)
    
    i=3: arr[3]=3 == arr[1]=3 → skip (duplicate)
    
    i=4: arr[4]=6 != arr[1]=3 → place 6 at index 2, next_unique = 3
         [2, 3, 6, 3, 6, 9, 9]
                 ^
    i=5: arr[5]=9 != arr[2]=6 → place 9 at index 3, next_unique = 4
         [2, 3, 6, 9, 6, 9, 9]
                    ^
    i=6: arr[6]=9 == arr[3]=9 → skip (duplicate)
    
    Result: 4 unique elements [2, 3, 6, 9]
    
    Args:
        arr: A sorted list of integers (ascending order)
        
    Returns:
        The count of unique elements (first 'n' elements are unique)
        
    Time Complexity: O(n) - Single pass through the array
    Space Complexity: O(1) - In-place modification, no extra space used
    """
    # Edge case: empty array
    if not arr:
        return 0
    
    # Pointer for the position where next unique element should be placed
    # Start at 1 because first element is always unique
    next_unique = 1
    
    # Scan through array starting from second element
    for i in range(1, len(arr)):
        # If current element is different from last unique element
        if arr[i] != arr[next_unique - 1]:
            # Place current element at next_unique position
            arr[next_unique] = arr[i]
            # Move pointer forward
            next_unique += 1
    
    # Return count of unique elements
    return next_unique


# Test the function
print(nonDuplicateNumber([2, 3, 3, 3, 6, 9, 9]))  # Output: 4
print(nonDuplicateNumber([1, 1, 2, 2, 2, 3]))     # Output: 3
print(nonDuplicateNumber([1, 2, 3, 4, 5]))        # Output: 5 (no duplicates)
