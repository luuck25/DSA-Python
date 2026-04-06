class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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
                result.append(i+1)            
        return result
    


    """
    Here nums[i] < n not needed as numbers from 1 to n

    where in missing it was 0 to n but size was n
    
    """