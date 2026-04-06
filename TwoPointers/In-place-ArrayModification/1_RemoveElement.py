"""
Remove Element (LeetCode #27)
==============================
Problem:
    Remove all occurrences of val in-place. Return new length.
    Order can change.

    Input:  nums = [3,2,2,3], val = 3  →  2  (nums becomes [2,2,...])

Logic:
    Two pointers — i scans from left, n shrinks from right.
    If nums[i] == val → overwrite with last element, shrink n (don't move i — new value unchecked).
    Else → move i forward.

Time:  O(n)
Space: O(1)
"""


def removeElement(nums, val):
    i = 0
    n = len(nums)  # n = virtual end of array

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]  # overwrite with last element
            n -= 1                 # shrink array (don't move i — new value needs checking)
        else:
            i += 1  # safe, move forward

    return n  # everything before n is valid


# ---- Clean version (no comments) ----
def removeElement_clean(nums, val):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n