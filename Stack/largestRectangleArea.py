"""
Largest Rectangle in Histogram — Plain English Walkthrough
===========================================================
Problem:
    Given an array of bar heights, find the area of the largest rectangle
    that can be formed within the histogram.

    Input:  [2, 1, 5, 6, 2, 3]
    Output: 10

    Visual:
             ___
            |   |
         ___|   |
        |   |   |       ___
        |   |   |  ___ |   |
   ___  |   |   | |   ||   |
  |   | |   |   | |   ||   |
  |___|_|___|___|_|___|_|___|
    2   1   5   6   2   3

    Largest rectangle = 5 × 2 = 10 (using bars at index 2 and 3)

Core Idea:
    For each bar, the biggest rectangle using THAT bar's height depends on:
        - How far LEFT it can extend (until a shorter bar)
        - How far RIGHT it can extend (until a shorter bar)
        - Area = height × (right_boundary - left_boundary - 1)

    Brute force: for each bar, scan left and right → O(n²)
    Monotonic stack: track boundaries as we go → O(n)

The Sentinel Trick — heights.append(0):
    Adding 0 at the end guarantees EVERY bar gets popped from the stack.
    Height 0 is shorter than everything, so it forces cleanup.
    Without it, bars still on the stack at the end would be missed.

The Width Formula:
    When you pop a bar:
        - Right boundary = i (current bar, which is shorter)
        - Left boundary = stack[-1] (new stack top, which is also shorter)
        - Width = i - stack[-1] - 1

    If stack is empty after popping:
        - No left boundary → bar extends all the way to index 0
        - Width = i

    Visual:
                 popped bar (height h)
                 ←───── width ─────→
        ___      ___________________      ___
       |   |    |                   |    |   |
       |   |    |    h × width      |    |   |
       |___|____|___________________|____|___|
      stack[-1]                           i
              ↑                          ↑
         left boundary             right boundary

Step-by-step with [2, 1, 5, 6, 2, 3]:
---------------------------------------
    After append: [2, 1, 5, 6, 2, 3, 0]
    stack=[], max_area=0

    i=0: h=2, stack empty → push 0              stack=[0]
    i=1: h=1 < 2 → pop 0: h=2, w=1, area=2     max_area=2
         push 1                                  stack=[1]
    i=2: h=5 > 1 → push 2                       stack=[1,2]
    i=3: h=6 > 5 → push 3                       stack=[1,2,3]
    i=4: h=2 < 6 → pop 3: h=6, w=4-2-1=1, area=6   max_area=6
         h=2 < 5 → pop 2: h=5, w=4-1-1=2, area=10  max_area=10 ✅
         h=2 ≥ 1 → stop, push 4                 stack=[1,4]
    i=5: h=3 > 2 → push 5                       stack=[1,4,5]
    i=6: h=0 (sentinel!) pops everything:
         pop 5: h=3, w=6-4-1=1, area=3          max_area=10
         pop 4: h=2, w=6-1-1=4, area=8          max_area=10
         pop 1: h=1, stack empty, w=6, area=6   max_area=10

    Result: 10 ✅

Time:  O(n) — each bar pushed once, popped once
Space: O(n) — stack holds at most n indices
"""

from typing import List


def largestRectangleArea(heights: List[int]) -> int:

    # Monotonic increasing stack — stores indices of bars
    # Bars stay here until a SHORTER bar arrives (their right boundary)
    stack = []

    max_area = 0

    # Sentinel trick: append 0 so every bar eventually gets popped
    # Height 0 is shorter than everything → forces cleanup
    heights.append(0)

    for i in range(len(heights)):

        # Current bar is shorter than stack top → stack top has found
        # its RIGHT boundary (current bar) → pop and calculate area
        while stack and heights[i] < heights[stack[-1]]:

            # The popped bar's height IS the rectangle height
            h = heights[stack.pop()]

            # Width depends on whether anything is left on the stack
            if not stack:
                # Nothing on stack → no left boundary → extends to index 0
                width = i
            else:
                # Left boundary is the new stack top (first shorter bar to the left)
                # Right boundary is i (first shorter bar to the right)
                # Width = right - left - 1
                width = i - stack[-1] - 1

            max_area = max(max_area, h * width)

        # Push current index — this bar is waiting for its right boundary
        stack.append(i)

    return max_area


# ---- Clean version (no comments) ----
def largestRectangleArea_clean(heights: List[int]) -> int:
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area