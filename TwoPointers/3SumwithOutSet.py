from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        if len(nums) < 3:
            return result

        nums.sort()

        for i in range(len(nums)):


            if i>0 and nums[i] == nums[i-1]:  # skip duplicates
                continue

            start = i + 1
            end = len(nums) - 1

            while end > start:
                sum = nums[i] + nums[start] + nums[end]

                if sum == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while end > start and nums[start] == nums[start -1]: # skip duplicates
                        start += 1  
                    while end > start and nums[end] == nums[end + 1]: # skip duplicates
                        end -= 1       

                elif sum > 0:
                    end -= 1
                else:
                    start += 1        


        return result
        