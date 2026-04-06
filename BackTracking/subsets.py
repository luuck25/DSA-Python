class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = []

        def backtrack(index,path):

            if index == len(nums):
                result.append(path[:])
                return

            path.append(nums[index])
            # include element

            backtrack(index+1,path)
            path.pop()

            # exclude element

            backtrack(index+1,path) 

        backtrack(0,[])
        return result       

                
        