class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        next_unique = 2

        for i in range(2,len(nums)):
            if nums[i] != nums[next_unique - 2]:
                nums[next_unique] = nums[i]
                next_unique += 1
        return next_unique        

        