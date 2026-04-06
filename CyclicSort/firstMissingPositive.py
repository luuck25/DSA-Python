def firstMissingPositive(nums):
    n = len(nums)
    
    # Phase 1: Move numbers to their "home" indices
    for i in range(n):
        # While the current number belongs in the array range 
        # AND it is not already at its correct home index...
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap it to its home index
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            
    # Phase 2: Find the first index that doesn't match
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
            
    # If all positions are correct, the missing number is n + 1
    return n + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        i =0
        n = len(nums)
        while i < n:

            correct = nums[i] - 1

            if  1<= nums[i] <=n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        print(nums)

        for i in range(n):
            if nums[i]!= i+1:
                return i+1   
        return n+1          