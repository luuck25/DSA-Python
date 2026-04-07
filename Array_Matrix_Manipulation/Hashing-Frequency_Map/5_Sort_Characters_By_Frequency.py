"""
Sort Characters By Frequency (LeetCode #451)
==============================================
Problem:
    Sort a string by character frequency (most frequent first).

    Input:  "tree"   →  "eert" or "eetr"
    Input:  "cccaaa" →  "aaaccc" or "cccaaa"

Logic:
    1. Count frequency of each char → Counter
    2. Bucket sort: group chars by their count → mp[count] = [chars...]
    3. Walk buckets from highest count down → build result

    Why bucket sort? Avoids O(n log n) sort. Max bucket = len(s), so O(n).

Time:  O(n)
Space: O(n)
"""

from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)                  # step 1: count each char

        mp = defaultdict(list)
        for ch, count in counter.items():
            mp[count].append(ch)              # step 2: bucket by frequency

        result = []
        for count in range(len(s), 0, -1):   # step 3: walk from highest count down
            for ch in mp[count]:
                result.append(ch * count)     # repeat char 'count' times

        return "".join(result)

    # ---- Clean version (no comments) ----
    def frequencySort_clean(self, s: str) -> str:
        counter = Counter(s)
        mp = defaultdict(list)
        for ch, count in counter.items():
            mp[count].append(ch)
        result = []
        for count in range(len(s), 0, -1):
            for ch in mp[count]:
                result.append(ch * count)
        return "".join(result)