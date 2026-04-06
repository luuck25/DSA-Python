class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_window = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_window = min(min_window,right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_window == float('inf') else  min_window       




        