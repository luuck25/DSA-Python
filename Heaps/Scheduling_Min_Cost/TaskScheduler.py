"""
Task Scheduler

Description:
Given tasks represented by uppercase letters and a cooldown `n`, return the
minimum number of time intervals needed to execute all tasks. The same task
must have at least `n` intervals between executions; idle intervals are
allowed.

Approach:
1. Count each task type with `Counter`.
2. Put the negative task counts in a min-heap to simulate a max-heap, so the
    next task chosen is one with the most remaining occurrences.
3. Keep tasks that were just executed in a queue with the time when they become
    available again (`current time + n`).
4. Advance time one interval at a time. If a task is available, execute it and
    put its remaining count in the cooldown queue. If the task's cooldown ends,
    return it to the heap.
5. Stop when both the heap and cooldown queue are empty. The elapsed time is
    the minimum schedule length produced by this greedy simulation.

Let:
- `N = len(tasks)` = total number of tasks
- `m` = number of distinct task types
- `L` = number of intervals in the schedule, including idle intervals

Time Complexity:
1. `Counter(tasks)` scans all N tasks: O(N).
2. Build and heapify the m task counts: O(m).
3. The simulation advances once per interval, including idle intervals: O(L).
    Across the schedule, each task is popped from the heap once and pushed
    back at most once. These heap operations cost O(N log m) total.
4. Queue operations take O(1) each and occur at most O(N) times.
Overall: O(N + L + N log m), simplified to O(L + N log m). Counting alone is
O(N), but cooldown idle intervals are simulated too, so total runtime can be
greater than O(N).

Space Complexity:
- The frequency map stores m task types: O(m).
- The heap and cooldown queue each hold at most O(m) task entries.
Total auxiliary space: O(m), which is at most O(N). If task types are limited
to the 26 uppercase English letters, m <= 26, so auxiliary space is O(1).
The input task list is not counted as extra space.
"""

import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        frq = Counter(tasks)

        heap = [ -count for count in frq.values()]

        heapq.heapify(heap)

        qq = deque()

        time = 0

        while heap or qq:
            time += 1

            if heap:

                cnt = 1 + heapq.heappop(heap)

                if cnt:

                    qq.append((cnt,time+n))
            if qq and qq[0][1] == time:

                heapq.heappush(heap,qq.popleft()[0])

        return time


"""
Pseudocode:
-----------
function leastInterval(tasks, n):
    frequencies = count occurrences of each task
    heap = max-heap of task frequencies
    cooldown_queue = empty queue of (remaining_count, available_time)
    time = 0

    while heap or cooldown_queue:
        time += 1

        if heap is not empty:
            remaining_count = pop task with highest remaining frequency
            decrement remaining_count
            if remaining_count > 0:
                enqueue (remaining_count, time + n)

        if the queue's first task is available at time:
            push its remaining count back into heap

    return time
"""


