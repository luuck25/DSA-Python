class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        start = 0
        n  = len(s)
        end = n - 1

        while end > start:
            s[start] , s[end] = s[end], s[start]
            start += 1
            end -= 1
        