"""
Longest Mountain in Array (LeetCode #845)
==========================================
Problem:
    Find the length of the longest mountain subarray.
    A mountain has: strictly increasing → peak → strictly decreasing.
    Minimum length 3.

    Input:  [2, 1, 4, 7, 3, 2, 5]  →  5  (subarray [1, 4, 7, 3, 2])

Logic:
    Scan for peaks (arr[i-1] < arr[i] > arr[i+1]).
    From each peak, expand left (uphill) and right (downhill).
    Mountain length = right - left + 1.
    Skip i to right after each mountain (no overlap possible).

Time:  O(n) — each element visited at most twice (once by i, once by expansion)
Space: O(1)
"""

from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        i = 1
        n = len(arr)

        while i < n - 1:
            # Check if i is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # Expand left — climb uphill
                left = i
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                # Expand right — descend downhill
                right = i
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                longest = max(longest, right - left + 1)
                i = right  # skip ahead — no new mountain starts inside this one
            else:
                i += 1

        return longest

    # ---- Clean version (no comments) ----
    def longestMountain_clean(self, arr: List[int]) -> int:
        longest = 0
        i = 1
        n = len(arr)

        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                right = i
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                longest = max(longest, right - left + 1)
                i = right
            else:
                i += 1

        return longest