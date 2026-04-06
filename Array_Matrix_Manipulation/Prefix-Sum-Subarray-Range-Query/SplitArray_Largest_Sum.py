class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def countSubarray(nums, elementSum):
            num_subarray = 1
            curr_sum = 0

            for i in range(len(nums)):
                if curr_sum + nums[i] <= elementSum:
                    curr_sum += nums[i]
                else:
                    curr_sum = nums[i]
                    num_subarray += 1    
            
            return num_subarray       

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low) // 2

            subarray = countSubarray(nums, mid)

            if subarray > k:
                low = mid + 1
            else:
                high = mid - 1

        return low
    

    # https://www.youtube.com/watch?v=Z0hwjftStI4