from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0

        mp = {}

      

        while end > start:
            min_value = min(heights[end],heights[start])

            max_area = max(max_area, min_value * (end-start))

            if heights[end] > heights[start]:
                start += 1
            else:
                end -= 1    
        return max_area
        