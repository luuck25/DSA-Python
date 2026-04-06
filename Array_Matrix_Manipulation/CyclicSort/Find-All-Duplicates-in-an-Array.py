class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i =0
        n = len(nums)
        while i < n:

            correct = nums[i] - 1

            if  nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        print(nums)        
        result = []
        for i in range(n):
            if i+1 != nums[i]:
                print()
                result.append(nums[i])            
        return result
    

    """
    same solution as Disappeard num

    just retrun nums[i] instead of index i
    
    """