class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        left = 0
        result = 0

        curr_sum = 0

        for right in range(len(nums)):
            target = nums[right]
            curr_sum += nums[right]

            window_sum = (right - left + 1) * target

            if window_sum - curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            result = max(result, right -left + 1) 

        return result       











        # https://www.youtube.com/watch?v=iOqH_JnXIOQ