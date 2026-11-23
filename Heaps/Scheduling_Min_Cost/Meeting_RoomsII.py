"""
Meeting Rooms II

Description:
Given meeting intervals, return the minimum number of rooms required so that
all meetings can take place without overlap. A meeting ending at time t frees
its room for another meeting starting at time t.

Approach:
1. Sort the meetings by start time so they are considered chronologically.
2. Keep meeting end times in a min-heap. The smallest end time is the room
    that becomes available first.
3. Before assigning the current meeting, remove every end time <= its start;
    those meetings have finished and their rooms can be reused.
4. Push the current meeting's end time into the heap.
5. The largest heap size reached is the number of rooms needed. Since this
    implementation returns the final heap size after processing all meetings,
    ended meetings must be removed before each new meeting is added.

Let `n = len(intervals)`.

Time Complexity:
1. Sorting the n meetings takes O(n log n).
2. Each meeting end time is pushed once and popped at most once. Each heap
    operation costs O(log n), so all heap operations take O(n log n).
3. The loop over meetings and comparisons take O(n), which is covered by the
    sorting and heap costs.
Overall: O(n log n).

Space Complexity:
- The heap can hold up to n end times: O(n) worst case.
- Sorting may use implementation-dependent auxiliary space; the heap is the
  dominant explicit extra data structure.
Overall auxiliary space: O(n).
"""

import heapq
from typing import List


# Definition of Interval is provided by the judge.

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        minheap = []
       

        intervals.sort(key = lambda x : x.start)    

        for interval in intervals:

            while minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)

            heapq.heappush(minheap,interval.end) 
            

        return len(minheap)

"""
Pseudocode:
-----------
function minMeetingRooms(intervals):
    if intervals is empty:
        return 0

    sort intervals by start time
    end_times = empty min-heap
    max_rooms = 0

    for each interval in intervals:
        while end_times is not empty and smallest end time <= interval.start:
            remove smallest end time  // Reuse that room

        push interval.end into end_times
        max_rooms = max(max_rooms, size of end_times)

    return max_rooms
"""



       



