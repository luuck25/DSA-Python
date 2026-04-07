"""
Longest Palindrome from String — Plain English Walkthrough
===========================================================
Problem:
    Given a string of mixed-case letters, find the length of the LONGEST
    palindrome you can build using those characters.

    Input:  "abccccdd"  →  7  ("dccaccd")
    Input:  "a"         →  1

Visual Example:
    Input: "abccccdd"

    Step 1: Build frequency map:
            {'a':1, 'b':1, 'c':4, 'd':2}

    Step 2: Palindromes use characters in PAIRS (mirror both sides).
            c=4 → all 4 can be used (even)        → length += 4
            d=2 → both can be used (even)          → length += 2
            a=1 → can't pair it, but take count-1=0 → length += 0, odd_found = True
            b=1 → same deal                        → length += 0, odd_found = True

    Step 3: If ANY odd count existed, we can place 1 character in the CENTER.
            odd_found = True → length += 1

    Result: 4 + 2 + 0 + 0 + 1 = 7 ✅

Key Insight:
    A palindrome reads the same forwards and backwards:
    - Characters with EVEN counts → use all of them (pair on both sides)
    - Characters with ODD counts → use count-1 (the even part), save 1 for center
    - You can place at most ONE odd character in the center

Approach:
    1. Count frequency of each character
    2. For each count:
       - Even → add full count
       - Odd  → add count-1 (use the pairs), mark odd_found
    3. If any odd was found → add 1 for the center character

Time:  O(n) — one pass to count, one pass over freq values
Space: O(1) — at most 52 letters (bounded alphabet)
"""


def longestPalindrome(s):
    # Count frequency of each character
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    length = 0
    odd_found = False

    for count in freq.values():
        if count % 2 == 0:
            # Even count → all characters can be paired
            # e.g., 'c' appears 4 times → "cc...cc" (2 on each side)
            length += count
        else:
            # Odd count → use count-1 (the even portion)
            # e.g., 'a' appears 3 times → use 2 (pair them), 1 left over
            length += count - 1
            odd_found = True  # Remember we have a leftover for the center

    # A palindrome can have ONE character in the middle
    # e.g., "abcba" — 'c' is the center
    if odd_found:
        length += 1

    return length


# ---- Clean version (no comments) ----
def longestPalindrome_clean(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    length = 0
    odd_found = False

    for count in freq.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    if odd_found:
        length += 1

    return length
