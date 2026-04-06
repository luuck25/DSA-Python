class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect cycle intersection
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]           # Move slow pointer 1 step
            fast = nums[nums[fast]]     # Move fast pointer 2 steps
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle
        slow = nums[0]                  # Reset slow to head
        while slow != fast:
            slow = nums[slow]           # Move both 1 step
            fast = nums[fast]
            
        return slow