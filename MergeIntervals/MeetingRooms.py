"""
Meeting Rooms — Plain English Walkthrough
==========================================
Problem:
    Given a list of meeting time intervals (start, end),
    determine if a person can attend ALL meetings.
    i.e., do any meetings overlap?

    Input:  [(0,30), (5,10), (15,20)]  →  False (can't attend all)
    Input:  [(7,10), (2,4)]            →  True  (no overlap)

Visual Example:
    Input: [(0,30), (5,10), (15,20)]

    Step 1: Sort by end time → [(5,10), (15,20), (0,30)]
    Step 2: prev_end = 10 (end of first meeting)
    Step 3: (15,20) → start=15, prev_end=10 → 15 < 10? No → no overlap → prev_end = 20
    Step 4: (0,30)  → start=0,  prev_end=20 → 0 < 20?  Yes → OVERLAP → return False ❌

    Result: False — can't attend all meetings

    Input: [(7,10), (2,4)]

    Step 1: Sort by end time → [(2,4), (7,10)]
    Step 2: prev_end = 4
    Step 3: (7,10) → start=7, prev_end=4 → 7 < 4? No → no overlap → prev_end = 10

    Result: True — can attend all meetings ✅

Approach:
    1. Sort meetings by end time
    2. Walk through each meeting:
       - If any meeting STARTS before the previous one ENDS → overlap → return False
       - Otherwise update prev_end and keep going
    3. If we finish the loop with no overlaps → return True

Time:  O(n log n) — because of sorting
Space: O(1) — only a few variables

Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Base case: no meetings or empty list → you can "attend" them all trivially
        if not intervals:
            return True

        # Sort meetings by END time
        # Same greedy idea as NonOverlapping — process meetings that finish earliest first
        intervals.sort(key=lambda x: x.end)

        # Track the end time of the last meeting we checked
        prev_end = intervals[0].end

        for i in range(1, len(intervals)):

            start, end = intervals[i].start, intervals[i].end

            # Does this meeting start BEFORE the previous one ends?
            # e.g., prev meeting ends at 30, this one starts at 5 → 5 < 30 → CONFLICT!
            if start < prev_end:
                return False  # Overlap found — can't attend all meetings
            else:
                # No conflict — move on, update prev_end to this meeting's end
                prev_end = end

        # Made it through all meetings with no conflicts
        return True

    # ---- Clean version (no comments) ----
    def canAttendMeetings_clean(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.end)
        prev_end = intervals[0].end

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start < prev_end:
                return False
            else:
                prev_end = end

        return True

