"""
Longest Repeating Character Replacement (LeetCode #424)
========================================================
Problem:
    Given a string s and an integer k, you can replace at most k characters.
    Return the length of the longest substring with all the same character.

    Input:  s = "AABABBA", k = 1  →  4  ("AABA" → replace B → "AAAA")

Logic:
    Sliding window + frequency map.
    Track the most frequent character in the window (max_freq).
    Replacements needed = window_size − max_freq.
    If replacements > k → shrink left.
    max_freq never needs to decrease — we only care about beating
    the current best, so a stale max_freq still gives correct results.

Time:  O(n)
Space: O(1) — at most 26 keys in the map
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}                                    # char frequency in window
        left = 0
        max_freq = 0                               # highest single-char count in window
        mx_len = 0

        for end in range(len(s)):
            mp[s[end]] = mp.get(s[end], 0) + 1    # add right char
            max_freq = max(max_freq, mp[s[end]])   # update most frequent

            if (end - left + 1) - max_freq > k:   # replacements needed > k → shrink once
                mp[s[left]] -= 1
                left += 1

            mx_len = max(mx_len, end - left + 1)  # record longest valid window

        return mx_len

    # ---- Clean version (no comments) ----
    def characterReplacement_clean(self, s: str, k: int) -> int:
        mp = {}
        left = 0
        max_freq = 0
        mx_len = 0

        for end in range(len(s)):
            mp[s[end]] = mp.get(s[end], 0) + 1
            max_freq = max(max_freq, mp[s[end]])

            if (end - left + 1) - max_freq > k:
                mp[s[left]] -= 1
                left += 1

            mx_len = max(mx_len, end - left + 1)

        return mx_len