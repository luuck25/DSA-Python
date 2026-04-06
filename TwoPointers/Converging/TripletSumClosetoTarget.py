class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')
        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            
            while(end> start):
                sum = nums[i] + nums[start] + nums[end]
                
                if sum == target: return sum
                if  abs(sum-target) < abs(closestSum - target):
                    closestSum = sum
                if sum < target: start+= 1
                elif sum > target: end-= 1

        return closestSum 