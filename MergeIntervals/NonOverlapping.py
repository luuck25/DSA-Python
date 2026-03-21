"""
Non-Overlapping Intervals — Plain English Walkthrough
======================================================
Problem:
    Given a list of intervals like [[1,2], [2,3], [3,4], [1,3]],
    find the MINIMUM number of intervals you need to REMOVE
    so that the remaining intervals don't overlap.
    Expected output: 1 (remove [1,3] and the rest don't overlap)

Visual Example:
    Input:  [1,2]  [2,3]  [3,4]  [1,3]

    Step 1: Sort by END time → [1,2]  [2,3]  [1,3]  [3,4]
    Step 2: prev_end = 2 (end of first interval)
    Step 3: [2,3] → start=2, prev_end=2 → 2 > 2? No → no overlap → update prev_end = 3
    Step 4: [1,3] → start=1, prev_end=3 → 3 > 1? Yes → OVERLAP → count = 1 (remove this one)
    Step 5: [3,4] → start=3, prev_end=3 → 3 > 3? No → no overlap → update prev_end = 4

    Result: 1 interval removed ✅

Why sort by END time (not start time)?
    Sorting by end time is a GREEDY strategy — we always keep the interval
    that finishes earliest, leaving the most room for future intervals.
    This guarantees the minimum removals.

    Example why start-time sorting fails:
        [1,100]  [2,3]  [4,5]
        If we keep [1,100] (starts first), we'd remove 2 intervals.
        If we keep [2,3] and [4,5] (end earlier), we only remove 1. ✅

Approach:
    1. Sort intervals by END time (greedy — finish early, keep more)
    2. Track the end of the last kept interval (prev_end)
    3. For each interval:
       - If it overlaps with prev_end → remove it (count += 1)
       - If no overlap → keep it (update prev_end)

Time:  O(n log n) — because of sorting
Space: O(1) — only using a counter and a variable
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Base case: no intervals → nothing to remove
        if not intervals:
            return 0

        # Sort by END time (greedy: keep intervals that finish earliest)
        # This leaves the most room for upcoming intervals
        intervals.sort(key=lambda x: x[1])

        # Track the end of the last interval we decided to KEEP
        prev_end = intervals[0][1]

        # Count of intervals we need to REMOVE
        count = 0

        # Start from index 1 (we already "kept" the first interval)
        for i in range(1, len(intervals)):

            start, end = intervals[i]

            # Does this interval overlap with the last one we kept?
            # i.e., does the previous interval end AFTER this one starts?
            if prev_end > start:
                # Yes → overlap! Remove this interval (just count it, don't update prev_end)
                # Why not update? Because the previous interval ends earlier (we sorted by end),
                # so keeping IT leaves more room for future intervals
                count += 1
            else:
                # No overlap → keep this interval, update prev_end
                prev_end = end

        return count        


        