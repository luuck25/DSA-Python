class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start= mid = 0
        end = len(nums) - 1

        while  mid <= end:

            if nums[mid] == 2:
                nums[end] , nums[mid] = nums[mid], nums[end]
                end -= 1
            elif nums[mid] == 1:
                 mid += 1
            elif nums[mid] == 0:
                 nums[start] , nums[mid] = nums[mid], nums[start]
                 start += 1
                 mid += 1         
        

        """
        Idea is -

        start and mid start at 0 and end is last index

        start tells pos where 0 has to be placed


        Logic is  we move mid pointer from left to right so iterate until
        mid does not cross end

        if mid is 2, put it at end , move end
        if mid is 1 , move mid, 1 is at right place
        if mid is 0, its where low should be there, hence swap
        
        
        """