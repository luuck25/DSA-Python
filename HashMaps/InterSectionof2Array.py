class Solution:
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        result = set()

        for num in nums2:
            if num in s1:
                result.add(num)
        
        return list(result)