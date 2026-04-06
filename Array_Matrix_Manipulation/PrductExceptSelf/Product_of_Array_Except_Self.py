class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = 1
        for num in nums:
            res.append(prefix)

            prefix = prefix * num


        n = len(nums)
        posfix = 1
        for i in range(n-1,-1,-1):
            res[i] = res[i] * posfix
            posfix = nums[i] * posfix
            
        return res    
            





        