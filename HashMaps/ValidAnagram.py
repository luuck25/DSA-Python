"""
Valid Anagram — Plain English Walkthrough
==========================================
Problem:
    Given two strings s and t, return True if t is an anagram of s.
    An anagram uses the exact same characters, same number of times.

    Input:  s = "anagram", t = "nagaram"  →  True
    Input:  s = "rat",     t = "car"      →  False

Visual Example:
    Input: s = "anagram", t = "nagaram"

    Step 1: Length check → both are 7 → ✅ proceed

    Step 2: Build frequency map from s:
            {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}

    Step 3: Walk through t, subtract from map:
            'n' → count['n'] = 1→0   ✅
            'a' → count['a'] = 3→2   ✅
            'g' → count['g'] = 1→0   ✅
            'a' → count['a'] = 2→1   ✅
            'r' → count['r'] = 1→0   ✅
            'a' → count['a'] = 1→0   ✅
            'm' → count['m'] = 1→0   ✅

    Step 4: Never went negative, never hit a missing char → True ✅

    Counter-example: s = "rat", t = "car"
            Map from s: {'r':1, 'a':1, 't':1}
            Walk t: 'c' → NOT in map → immediately return False ❌

Why not just sort both strings?
    - sorted(s) == sorted(t) works but is O(n log n)
    - HashMap approach is O(n) — one pass to build, one pass to verify

Why check count < 0?
    - If t has MORE of a character than s, the count goes negative
    - e.g., s = "ab", t = "aa" → count['a'] starts at 1, goes to 0, then -1 → False

Approach:
    1. Quick check: if lengths differ → can't be anagrams → False
    2. Build frequency map from s (count each character)
    3. Walk through t, decrement counts:
       - Character not in map → False
       - Count goes below 0 → False (t has more of this char than s)
    4. Survived the loop → True

Time:  O(n) — one pass through each string
Space: O(1) — at most 26 lowercase letters (bounded alphabet)
"""


def isAnagram(s, t):
    # Quick length check — different lengths can never be anagrams
    if len(s) != len(t):
        return False

    # Build frequency map from the first string
    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # Verify against the second string
    for ch in t:
        # Character in t doesn't exist in s at all → not an anagram
        if ch not in count:
            return False
        # Decrement: "use up" one occurrence of this character
        count[ch] -= 1
        # t has MORE of this character than s → not an anagram
        if count[ch] < 0:
            return False

    # Every character matched perfectly → valid anagram
    return True


# ---- Clean version (no comments) ----
def isAnagram_clean(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True