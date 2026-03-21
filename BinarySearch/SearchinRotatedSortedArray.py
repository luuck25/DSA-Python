class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:

            mid = low + high -low //2

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[high] and target < nums[mid]:
                low = mid + 1
            else:

                high = mid - 1
        return -1                
        