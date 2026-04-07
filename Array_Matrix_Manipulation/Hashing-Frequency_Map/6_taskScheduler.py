"""
Task Scheduler (LeetCode #621)
================================
Problem:
    Given tasks and cooldown n, find minimum time to finish all tasks.
    Same task must wait n intervals before repeating.

    Input:  tasks = ["A","A","A","B","B","B"], n = 2  →  8
    Output: A B _ A B _ A B  (8 intervals)

Logic:
    Greedy with max-heap + cooldown queue.
    1. Count frequencies, push into max-heap (negate for max behavior).
    2. Each tick: pop most frequent task, decrement count, push to cooldown queue with ready time.
    3. If heap is empty but queue has tasks → fast-forward time to next ready task.
    4. If front of queue is ready (time >= ready_time) → push back to heap.

Time:  O(n × m) — n = total intervals, m = distinct tasks (heap ops)
Space: O(m) — heap + queue

https://www.youtube.com/watch?v=s8p8ukTyA2I
"""

from collections import Counter, deque
from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        maxHeap = [-cnt for cnt in counter.values()]  # negate for max-heap
        heapq.heapify(maxHeap)

        q = deque()  # [remaining_count, ready_at_time]
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # +1 because negated (e.g. -3 → -2)
                if cnt:                             # still has remaining tasks
                    q.append([cnt, time + n])       # can be reused after cooldown
            elif q:
                time = q[0][1]                      # idle → fast-forward to next ready task

            if q and q[0][1] <= time:               # front of queue is ready
                heapq.heappush(maxHeap, q.popleft()[0])  # push back to heap

        return time

    # ---- Clean version (no comments) ----
    def leastInterval_clean(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            elif q:
                time = q[0][1]
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time