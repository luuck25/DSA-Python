"""
Merge Overlapping Intervals — Plain English Walkthrough
========================================================
Problem:
    Given a list of intervals like [[1,3], [2,6], [8,10], [15,18]],
    merge all overlapping intervals and return the result.
    Expected output: [[1,6], [8,10], [15,18]]

Visual Example:
    Input:  [1,3]  [2,6]  [8,10]  [15,18]

    Step 1: Sort by start time (already sorted here)
    Step 2: [1,3] → merged is empty, so just add it → merged = [[1,3]]
    Step 3: [2,6] → 2 <= 3 (overlaps!) → merge → merged = [[1,6]]
    Step 4: [8,10] → 8 > 6 (no overlap) → just add → merged = [[1,6], [8,10]]
    Step 5: [15,18] → 15 > 10 (no overlap) → just add → merged = [[1,6], [8,10], [15,18]]

    Result: [[1,6], [8,10], [15,18]] ✅

Approach:
    1. Sort intervals by start time so overlapping ones sit next to each other
    2. Walk through each interval:
       - If it doesn't overlap with the last merged one → add it
       - If it overlaps → extend the last merged one's end time

Time:  O(n log n) — because of sorting
Space: O(n) — for the merged list
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Base case: if intervals is empty [] or None → nothing to merge
        if not intervals:
            return []

        # Sort all intervals by their START time
        # Why? So overlapping intervals are guaranteed to be next to each other
        # Example: [[3,5], [1,4]] → [[1,4], [3,5]]
        intervals.sort(key=lambda x: x[0])

        # This will hold our final merged intervals
        merged = []

        for interval in intervals:

            # Case 1: Just add this interval as-is
            # Two reasons:
            #   a) merged is empty (first interval, nothing to compare)
            #   b) current interval's START is AFTER last merged interval's END
            #      → no overlap, e.g. last = [1,3], current = [8,10] → 8 > 3
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)

            # Case 2: They overlap — merge them!
            # Current interval's START is <= last merged interval's END
            # → extend the end to whichever ends later
            # e.g. last = [1,3], current = [2,6] → 2 <= 3 → merged = [1, max(3,6)] = [1,6]
            # no need to check start for max as intervals are already sorted
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged         

        