"""
Reverse Vowels of a String (LeetCode #345)
============================================
Problem:
    Reverse only the vowels in a string. Consonants stay in place.

    Input:  "IceCreAm"  →  "AcesCreIm"
    Input:  "leetcode"  →  "leotcede"

Logic:
    Two pointers from both ends. Each pointer skips non-vowels.
    When both land on vowels → swap, move both inward.

Time:  O(n)
Space: O(n) — string converted to list for in-place swaps
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start = 0
        end = len(s) - 1
        vow = {'a', 'e', 'i', 'o', 'u'}

        while end > start:
            while end > start and s[start].lower() not in vow:
                start += 1
            while end > start and s[end].lower() not in vow:
                end -= 1

            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return "".join(s)

    # ---- Clean version (no comments) ----
    def reverseVowels_clean(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s) - 1
        vow = {'a', 'e', 'i', 'o', 'u'}

        while end > start:
            while end > start and s[start].lower() not in vow:
                start += 1
            while end > start and s[end].lower() not in vow:
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return "".join(s)          
        