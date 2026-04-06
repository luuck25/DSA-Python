"""
Insert Interval — Plain English Walkthrough
=============================================
Problem: Given a sorted list of non-overlapping intervals and a new interval,
         insert the new interval and merge if necessary.

Example:
    intervals = [[1,2], [3,5], [6,7], [8,10]], newInterval = [4,8]

    Step 1: [1,2] ends before [4,8] starts → no overlap → add [1,2] to result
    Step 2: [3,5] overlaps with [4,8] → merge → newInterval becomes [3,8]
    Step 3: [6,7] overlaps with [3,8] → merge → newInterval becomes [3,8]
    Step 4: [8,10] overlaps with [3,8] → merge → newInterval becomes [3,10]
    Final:  append leftover newInterval [3,10]

    Result: [[1,2], [3,10]]

Approach:
    Loop through each existing interval. Only 3 things can happen:
      1. New interval comes AFTER current one → no overlap, just add current to result.
      2. New interval comes BEFORE current one → no overlap, add newInterval to result,
         then swap so current becomes the new "carry-forward" interval.
      3. They OVERLAP → merge by taking min of starts and max of ends.
    After the loop, append whatever newInterval is left (it's always valid).

Time:  O(n) — single pass through the list
Space: O(n) — for the result list
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:

            # Case 1: newInterval starts after current interval ends → no overlap
            # e.g., current = [1,3], new = [5,7] → just keep [1,3], carry [5,7] forward
            if newInterval[0] > interval[1]:
                result.append(interval)

            # Case 2: newInterval ends before current interval starts → no overlap
            # e.g., current = [5,7], new = [1,3] → add [1,3] to result,
            # then swap: newInterval = [5,7] so it gets carried forward
            # (all remaining intervals are after this, so they'll hit Case 1)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval

            # Case 3: overlap exists → merge them
            # Take the earlier start and the later end
            # Keep the merged result as newInterval so it can merge with next intervals too
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        # After the loop, newInterval holds either:
        # - the original new interval (if it came after everything)
        # - a swapped interval (from Case 2)
        # - a merged interval (from Case 3)
        # It's always valid and needs to be added to the result
        result.append(newInterval)

        return result

    # ---- Clean version (no comments) ----
    def insert_clean(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            if newInterval[0] > interval[1]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        result.append(newInterval)

        return result             




        