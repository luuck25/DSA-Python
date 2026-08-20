class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) //2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left] :
                # left array is sorted

                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1    
            else:
                # right arry is sorted
                
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1                     
        return -1              


"""
Pseudocode:
-----------
function search(nums, target):
    left = 0
    right = length(nums) - 1
    
    while left <= right:
        mid = (left + right) / 2
        
        if nums[mid] == target:
            return mid
        
        // Determine which half is sorted
        if nums[mid] >= nums[left]:  // Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  // Target in sorted left half
            else:
                left = mid + 1   // Target in unsorted right half
        else:  // Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   // Target in sorted right half
            else:
                right = mid - 1  // Target in unsorted left half
    
    return -1  // Target not found
"""