"""
First Non-Repeating Character — Plain English Walkthrough
==========================================================
Problem:
    Given a string, find the first character that does NOT repeat.
    Return -1 if every character repeats.

    Input:  "aabbcdd"  →  'c'
    Input:  "aabb"     →  -1

Visual Example:
    Input: "leetcode"

    Step 1: Build frequency map:
            {'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}

    Step 2: Walk through the STRING again (not the map — order matters!):
            'l' → freq = 1 → ✅ FIRST non-repeating → return 'l'

    Result: 'l' ✅

Why two passes?
    Pass 1: Count every character (we need full picture before deciding)
    Pass 2: Walk the ORIGINAL string in order so we find the FIRST one with count == 1

    Why not use the map for pass 2?
    → Dicts in Python 3.7+ maintain insertion order, so it would work,
      but iterating the original string makes the intent crystal clear.

Approach:
    1. Build a frequency map {char: count}
    2. Loop through the string again — return the first char with count == 1
    3. If none found → return -1

Time:  O(n) — two passes through the string
Space: O(1) — at most 26 lowercase letters (bounded alphabet)
"""


def first_non_repeat_char(s):
    # Pass 1: Count frequency of every character
    freq = {}

    for ch in s:
        # .get(ch, 0) returns 0 if ch not in dict yet, avoids KeyError
        freq[ch] = freq.get(ch, 0) + 1

    # Pass 2: Walk the original string in order
    # Return the FIRST character whose count is exactly 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    # Every character repeats → no unique character found
    return -1


# ---- Clean version (no comments) ----
def first_non_repeat_char_clean(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return -1