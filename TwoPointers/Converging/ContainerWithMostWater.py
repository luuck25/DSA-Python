"""
Container With Most Water (LeetCode #11)
=========================
Logic:
    - Two pointers at both ends, converge inward.
    - Area = min(left_height, right_height) × distance between them.
    - Always move the SHORTER side inward — keeping the short side
      can never help (width shrinks, height stays bottlenecked).
    - Moving the taller side only makes things worse or the same.

Time: O(n)  Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0

        while end > start:
            min_value = min(heights[end], heights[start])
            max_area = max(max_area, min_value * (end - start))

            # Move the shorter side — it's the bottleneck
            if heights[end] > heights[start]:
                start += 1
            else:
                end -= 1

        return max_area

    # ---- Clean version ----
    def maxArea_clean(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        max_area = 0

        while end > start:
            max_area = max(max_area, min(heights[start], heights[end]) * (end - start))
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_area