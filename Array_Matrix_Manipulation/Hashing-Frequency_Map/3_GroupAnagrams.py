"""
Group Anagrams — Plain English Walkthrough
============================================
Problem:
    Given an array of strings, group the anagrams together.
    An anagram uses the exact same letters in a different order.

    Input:  ["eat","tea","tan","ate","nat","bat"]
    Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Visual Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

    Step 1: For each word, build a character count array of size 26 (a-z).
            This becomes the KEY in our hashmap.

            "eat" → count a=1, e=1, t=1 → key = (1,0,0,0,1,...,1,...0)
            "tea" → count a=1, e=1, t=1 → key = (1,0,0,0,1,...,1,...0)  ← SAME key!
            "tan" → count a=1, n=1, t=1 → key = (1,0,0,...,1,...,1,...0)
            "ate" → count a=1, e=1, t=1 → key = (1,0,0,0,1,...,1,...0)  ← SAME as eat/tea!
            "nat" → count a=1, n=1, t=1 → key = (1,0,0,...,1,...,1,...0) ← SAME as tan!
            "bat" → count a=1, b=1, t=1 → key = (1,1,0,...,0,...,1,...0)

    Step 2: Group words that share the same key:
            key1 → ["eat", "tea", "ate"]
            key2 → ["tan", "nat"]
            key3 → ["bat"]

    Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]] ✅

Why character count instead of sorted()?
    - sorted("eat") → "aet" also works as a key, but costs O(k log k) per word
    - Character count is O(k) per word (just count 26 letters)
    - Both work; count array is slightly faster for long words

Why tuple?
    - Lists are NOT hashable → can't be used as dict keys
    - tuple(count) converts [1,0,0,...] → (1,0,0,...) which IS hashable

Approach:
    1. For each word, build a 26-element count array (frequency of each letter)
    2. Convert count array to a tuple → use as the hashmap key
    3. Append the word to the list under that key
    4. Return all the grouped lists

Time:  O(n * k) — n words, k = max word length (counting chars)
Space: O(n * k) — storing all words in the hashmap
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # defaultdict(list) auto-creates an empty list for any new key
        # So we never need to check "if key not in groups"
        groups = defaultdict(list)

        for str in strs:
            # Build a frequency count of each character (a=0, b=1, ..., z=25)
            count = [0] * 26
            # [0, 0, 0, ..., 0]  (26 zeros for a–z)
            for ch in str:
                # ord('a') - ord('a') = 0, ord('b') - ord('a') = 1, etc.
                count[ord(ch) - ord('a')] += 1


                # ord() gives the ASCII number of a character
                # ord('a') → 97 | ord('b') → 98
                # 97 - 97 index 0
                # 98 - 97 index 1


            # Convert to tuple so it can be used as a dict key
            # All anagrams produce the SAME tuple → they land in the same group
            key = tuple(count)

            groups[key].append(str)

        # Return just the grouped lists, not the keys
        return list(groups.values())

    # ---- Clean version (no comments) ----
    def groupAnagrams_clean(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for ch in str:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            groups[key].append(str)

        return list(groups.values())