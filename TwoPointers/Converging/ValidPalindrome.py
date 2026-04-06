"""
Valid Palindrome (LeetCode #125)
================================
Problem:
    Given a string, return True if it's a palindrome considering only
    alphanumeric characters and ignoring case.

    Input: "A man, a plan, a canal: Panama"  →  True
    Input: "race a car"                      →  False

Logic:
    Two pointers from both ends, skip non-alphanumeric chars,
    compare lowercase versions. If mismatch → False.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while end > start:
            # Skip non-alphanumeric from left
            if not s[start].isalnum():
                start += 1
                continue
            # Skip non-alphanumeric from right
            if not s[end].isalnum():
                end -= 1
                continue

            # Case-insensitive compare
            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True

    # ---- Clean version (no comments) ----
    def isPalindrome_clean(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while end > start:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True    