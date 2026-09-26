"""
Daily Temperatures — Plain English Walkthrough
================================================
Problem:
    Given an array of daily temperatures, return an array where result[i]
    is the number of days you have to wait after day i to get a WARMER
    temperature. If no warmer day exists, result[i] = 0.

    Input:  [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [1,  1,  4,  2,  1,  1,  0,  0]

    Explanation:
        Day 0 (73°) → Day 1 (74°) is warmer → wait 1 day
        Day 2 (75°) → Day 6 (76°) is warmer → wait 4 days
        Day 6 (76°) → nothing warmer → 0
        Day 7 (73°) → nothing warmer → 0

This is just "Next Greater Element" but you return the DISTANCE, not the value.

Visual Example:
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    result = [0,  0,  0,  0,  0,  0,  0,  0]  (initialized)
    stack = []  (stores indices of days waiting for a warmer day)

    i=0: temp=73, stack=[]
         nothing to pop → push 0                    stack=[0]

    i=1: temp=74, stack=[0]
         74 > 73 → pop 0, result[0] = 1-0 = 1       stack=[]
         push 1                                     stack=[1]

    i=2: temp=75, stack=[1]
         75 > 74 → pop 1, result[1] = 2-1 = 1       stack=[]
         push 2                                     stack=[2]

    i=3: temp=71, stack=[2]
         71 < 75 → can't pop → push 3               stack=[2, 3]

    i=4: temp=69, stack=[2, 3]
         69 < 71 → can't pop → push 4               stack=[2, 3, 4]

    i=5: temp=72, stack=[2, 3, 4]
         72 > 69 → pop 4, result[4] = 5-4 = 1       stack=[2, 3]
         72 > 71 → pop 3, result[3] = 5-3 = 2       stack=[2]
         72 < 75 → can't pop → push 5               stack=[2, 5]

    i=6: temp=76, stack=[2, 5]
         76 > 72 → pop 5, result[5] = 6-5 = 1       stack=[2]
         76 > 75 → pop 2, result[2] = 6-2 = 4       stack=[]
         push 6                                     stack=[6]

    i=7: temp=73, stack=[6]
         73 < 76 → can't pop → push 7               stack=[6, 7]

    Remaining stack [6, 7] → no warmer day → result stays 0

    Result: [1, 1, 4, 2, 1, 1, 0, 0] ✅

Why store INDICES (not temperatures)?
    We need to calculate the DISTANCE (i - stack[-1]).
    If we stored values, we'd know "74 is warmer than 73" but not
    HOW MANY DAYS apart they are.

Connection to Next Greater Element:
    - Next Greater Element: find the VALUE of the next greater element
    - Daily Temperatures: find the DISTANCE to the next greater element
    - Same monotonic stack pattern, just store i - index instead of the value

Approach:
    1. Initialize result with 0s (default: no warmer day)
    2. Monotonic decreasing stack stores indices of days "waiting" for warmth
    3. For each day:
       - Pop all days with lower temp → current day IS their warmer day
       - Distance = current index - popped index
       - Push current index onto stack
    4. Anything left on stack → never found a warmer day → stays 0

Time:  O(n) — each index pushed once, popped at most once
Space: O(n) — stack can hold up to n indices
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Monotonic decreasing stack — stores indices of days waiting for warmth
        stack = []

        # Default 0: if no warmer day found, answer is 0
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            # Is today WARMER than the days sitting on the stack?
            # If yes, those days have been "waiting" for this moment
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # Distance = today's index - that day's index
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            # Push today's index — now THIS day is waiting for a warmer day
            stack.append(i)

        # Anything left on stack never found a warmer day → result stays 0
        return result

    # Similar to Nge 1 and 2
    # ---- Clean version (no comments) ----
    def dailyTemperatures_clean(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return result