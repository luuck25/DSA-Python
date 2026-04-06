"""
Minimum Meeting Rooms — Plain English Walkthrough
===================================================
Problem:
    Given a list of meeting time intervals, find the MINIMUM number of
    conference rooms required so that all meetings can take place.

    Input:  [(0,30), (5,10), (15,20)]  →  2 rooms needed
    Input:  [(7,10), (2,4)]            →  1 room needed

Visual Example:
    Input: [(0,30), (5,10), (15,20)]

    Step 1: Sort by START time → [(0,30), (5,10), (15,20)]

    Step 2: Use a min-heap to track END times of ongoing meetings.
            The heap tells us: "What's the earliest a room becomes free?"

    Step 3: Process each meeting:

    Meeting (0,30):
        heap is empty → no free room → assign a new room
        heap = [30]  (room 1 busy until 30)

    Meeting (5,10):
        heap top = 30 → earliest free room is at 30
        5 < 30 → meeting starts before any room is free → need a NEW room
        heap = [10, 30]  (room 1 busy till 30, room 2 busy till 10)

    Meeting (15,20):
        heap top = 10 → earliest free room is at 10
        15 >= 10 → a room is free! → REUSE it (pop 10, push 20)
        heap = [20, 30]  (room 1 busy till 30, room 2 now busy till 20)

    Result: len(heap) = 2 rooms needed ✅

Why a Min-Heap?
    The heap always gives us the room that frees up the EARLIEST.
    - If the earliest-freeing room is still busy → we definitely need a new room
    - If it's free → reuse it (pop old end time, push new end time)
    Think of it like checking: "Is the room that finishes soonest available?"

Why sort by START time (not end time)?
    We process meetings in the order they begin. For each meeting we ask:
    "Is any room free right now?" The heap answers that instantly.

Approach:
    1. Sort meetings by START time
    2. Use a min-heap to track end times of rooms in use
    3. For each meeting:
       - If the earliest-ending room is free → reuse it (pop + push)
       - Otherwise → allocate a new room (just push)
    4. Heap size at the end = number of rooms needed

Time:  O(n log n) — sorting + heap operations
Space: O(n) — heap can hold up to n end times

Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Base case: no meetings → no rooms needed
        if not intervals:
            return 0

        # Sort meetings by START time so we process them in chronological order
        intervals.sort(key=lambda x: x.start)

        # Min-heap stores END times of meetings currently using rooms
        # The smallest value (heap top) = the room that frees up earliest
        min_heap = []

        for interval in intervals:

            # Is the earliest-freeing room available?
            # heap[0] = the earliest end time among all rooms in use
            # If that end time <= current meeting's start → room is free → REUSE it
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)  # Free up this room (remove its old end time)

            # Assign this meeting to a room (push its end time)
            # Either we're reusing a freed room (popped above) or allocating a new one
            heapq.heappush(min_heap, interval.end)

        # Each entry in the heap = one room still in use
        # So the heap size = total rooms needed
        return len(min_heap)

    # ---- Clean version (no comments) ----
    def minMeetingRooms_clean(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
                




       