"""
Reverse Words in a String (LeetCode #151)
==========================================
Problem:
    Reverse the order of words. Strip leading/trailing/extra spaces.

    Input:  "  the sky  is blue  "  →  "blue is sky the"

Logic:
    1. Split + rejoin to clean extra spaces, convert to list
       s.split()        → ["the","sky","is","blue"]  (strips all extra spaces)
       " ".join(...)    → "the sky is blue"           (single space between words)
       list(...)        → ['t','h','e',' ','s','k','y',' ',...]  (spaces are elements too)
       Why list? Strings are immutable — need list for in-place swaps.
    2. Reverse the entire string in-place
    3. Reverse each individual word back to normal
       → whole-string reverse flips word order but scrambles letters,
         per-word reverse fixes the letters

Time:  O(n)
Space: O(n) — string to list conversion
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(" ".join(s.split()))

        def reverse(l, r):
            while r > l:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        # Step 1: reverse entire string
        reverse(0, len(s) - 1)

        # Step 2: reverse each word back
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                reverse(start, i - 1)
                start = i + 1

        return "".join(s)

    # ---- Clean version (no comments) ----
    def reverseWords_clean(self, s: str) -> str:
        s = list(" ".join(s.split()))

        def reverse(l, r):
            while r > l:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        reverse(0, len(s) - 1)

        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                reverse(start, i - 1)
                start = i + 1

        return "".join(s)
        