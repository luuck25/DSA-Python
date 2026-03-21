"""
Problem: Target Sum Pair in Sorted Array
-----------------------------------------
Given an array of numbers sorted in ascending order and a target sum,
find a pair in the array whose sum is equal to the given target.

Example:
    Input: arr = [1, 2, 3, 4, 6], target_sum = 6
    Output: (1, 3) -> indices of elements 2 and 4 (2 + 4 = 6)
"""


def search(arr: list[int], target_sum: int) -> tuple[int, int] | None:
    """
    Find two numbers in a sorted array that add up to the target sum.
    
    Uses the Two Pointer Technique:
    - Start with pointers at both ends of the array
    - If sum is too large, move the right pointer left (decrease sum)
    - If sum is too small, move the left pointer right (increase sum)
    - This works because the array is SORTED
    
    Args:
        arr: A sorted list of integers in ascending order
        target_sum: The target sum to find
        
    Returns:
        A tuple of (start_index, end_index) if pair found, None otherwise
        
    Time Complexity: O(n) - Single pass through the array
    Space Complexity: O(1) - Only using two pointer variables
    """
    # Initialize two pointers at opposite ends
    start, end = 0, len(arr) - 1
    
    # Loop until pointers meet
    while start < end:
        current_sum = arr[start] + arr[end]
        
        # Found the pair
        if current_sum == target_sum:
            return (start, end)
        # Sum too large -> need smaller values -> move end pointer left
        elif current_sum > target_sum:
            end -= 1
        # Sum too small -> need larger values -> move start pointer right
        else:
            start += 1
    
    # No pair found
    return None


# Test the function
print(search([1, 2, 3, 4, 6], 6))  # Output: (1, 3) -> arr[1]=2, arr[3]=4

   