import heapq
from typing import List


"""
Minimum Interval to Include Each Query

Description:
Given intervals and query points, return for each query the length of the
smallest interval containing it, or -1 if no interval contains the query.
Interval endpoints are inclusive, so an interval's length is `right-left+1`.

Approach:
1. Sort intervals by start, and sort queries while keeping each query's
    original index so answers can later be restored to input order.
2. Process queries in ascending order. Before answering query `q`, add every
    interval whose start is <= q to a min-heap ordered by interval length.
3. Remove heap entries whose right endpoint is less than q; those intervals
    do not contain the current query.
4. If the heap is nonempty, its root is the shortest interval that contains
    q. Store its length at the query's original index. Otherwise leave -1.

Let:
- `N = len(intervals)`
- `Q = len(queries)`

Time Complexity:
1. Sort the intervals: O(N log N).
2. Sort the indexed queries: O(Q log Q).
3. Each interval is pushed into the heap once and popped at most once. Each
    heap operation costs O(log N), for O(N log N) total heap work.
4. Each query is processed once, with O(1) work apart from heap operations:
    O(Q).
Overall: O(N log N + Q log Q + N log N + Q), commonly simplified to
O(N log N + Q log Q).

Space Complexity:
- The indexed sorted-query list stores Q entries: O(Q).
- The result stores Q answers: O(Q).
- The heap can hold up to N intervals: O(N).
Total auxiliary and output space: O(N + Q). Sorting may also use
implementation-dependent auxiliary space.
"""


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        result = [-1] * len(queries)
        min_heap = []
        j = 0

        for q, idx in sorted_queries:
            while j < len(intervals) and intervals[j][0] <= q:
                left, right = intervals[j]
                length = right - left + 1

                heapq.heappush(min_heap, (length, right))
                j += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                result[idx] = min_heap[0][0]

        return result


"""
Pseudocode:
-----------
function minInterval(intervals, queries):
    sort intervals by start
    sorted_queries = queries paired with original indices, sorted by value
    result = array of -1 values, one per query
    min_heap = empty heap ordered by (interval length, right endpoint)
    interval_index = 0

    for each (query, original_index) in sorted_queries:
        while there are unprocessed intervals with start <= query:
            compute inclusive interval length
            push (length, right endpoint) into min_heap
            advance interval_index

        while heap is not empty and its shortest interval ends before query:
            pop heap root

        if heap is not empty:
            result[original_index] = heap root's length

    return result
"""