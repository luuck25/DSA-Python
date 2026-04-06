class Solution:
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        result = set()

        for num in nums2:
            if num in s1:
                result.add(num)
        
        return list(result)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        res = []
        for num in nums2:
            if counter[num] > 0:
                res.append(num)
                counter[num] -= 1

        return res
