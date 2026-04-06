"""
Is Subsequence (LeetCode #392)
===============================
Problem:
    Check if s is a subsequence of t (characters appear in same order, not necessarily contiguous).

    Input:  s = "ace", t = "abcde"  →  True
    Input:  s = "aec", t = "abcde"  →  False

Logic:
    slow scans s, fast scans t.
    If match → advance both. No match → advance fast only.
    slow is always ≤ fast speed. If slow reaches end of s → all chars found.

Time:  O(n) — n = len(t)
Space: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = fast = 0

        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:  # match found → move slow
                slow += 1
            fast += 1              # fast always moves

        return slow == len(s)  # did we find all chars in s?

        """
        
        slow move conditionally if match is there

        fast moves if no match
        
        so speed of fast is more than slow 
        
        
        """

    # ---- Clean version (no comments) ----
    def isSubsequence_clean(self, s: str, t: str) -> bool:
        slow = fast = 0
        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        return slow == len(s)
