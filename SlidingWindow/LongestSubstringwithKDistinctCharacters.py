"""
Longest Substring with Exactly K Distinct Characters (GFG / LeetCode #340 variant)
===================================================================================

Problem:
    Given a string `s` and an integer `k`, find the length of the longest 
    substring that contains exactly K distinct characters.
    Return -1 if no such substring exists.

Algorithm: Variable-Size Sliding Window + HashMap
    1. Use a hashmap to track character frequencies in current window
    2. Expand window by adding characters (wind_end moves right)
    3. If distinct chars > k, SHRINK window from left until <= k
    4. Only update max when we have EXACTLY k distinct characters

Visual Example:
    s = "aabacbebebe", k = 3
    
    Window          | char_freq              | Distinct | Action
    ----------------|------------------------|----------|------------------
    [a]             | {a:1}                  | 1        | expand
    [a,a]           | {a:2}                  | 1        | expand
    [a,a,b]         | {a:2, b:1}             | 2        | expand
    [a,a,b,a]       | {a:3, b:1}             | 2        | expand
    [a,a,b,a,c]     | {a:3, b:1, c:1}        | 3 = k ✓  | length=5, expand
    [a,a,b,a,c,b]   | {a:3, b:2, c:1}        | 3 = k ✓  | length=6, expand
    [a,a,b,a,c,b,e] | {a:3, b:2, c:1, e:1}   | 4 > k    | SHRINK!
    [a,b,a,c,b,e]   | {a:2, b:2, c:1, e:1}   | 4 > k    | SHRINK!
    [b,a,c,b,e]     | {a:1, b:2, c:1, e:1}   | 4 > k    | SHRINK!
    [a,c,b,e]       | {a:1, b:1, c:1, e:1}   | 4 > k    | SHRINK!
    [c,b,e]         | {b:1, c:1, e:1}        | 3 = k ✓  | length=3 (not max)
    ... continue ...
    [c,b,e,b,e,b,e] | {c:1, b:3, e:3}        | 3 = k ✓  | length=7 ← maximum!
    
    Answer: 7 (substring "cbebebe")

Key Insight - "Exactly K" vs "At Most K":
    - len(char_freq) == k  → EXACTLY K distinct chars (this problem)
    - len(char_freq) <= k  → AT MOST K distinct chars (LeetCode #340)
    
    The only difference is the condition when updating max_length!

Why delete from hashmap when count reaches 0?
    - len(char_freq) represents number of DISTINCT characters
    - If we keep chars with count=0, our distinct count would be wrong
    - Example: {a:2, b:0} has len=2, but only 'a' is actually in window!

Time Complexity: O(n)
    - Each character is added once (wind_end) and removed at most once (wind_start)
    - HashMap operations (get, set, delete) are O(1) average

Space Complexity: O(k)
    - HashMap stores at most k+1 distinct characters at any time
    - We shrink when it exceeds k, so bounded by O(k)
"""


class Solution:
    def longestKSubstr(self, s, k):
        char_freq = {}              # HashMap: character → frequency in current window
        wind_start = 0              # Left boundary of sliding window
        length_max = float('-inf')  # Track maximum length (-inf = none found yet)

        # Expand window by moving right boundary
        for wind_end in range(len(s)):
            curr_char = s[wind_end]
            # Add current character to frequency map
            char_freq[curr_char] = char_freq.get(curr_char, 0) + 1

            # SHRINK window if we have more than k distinct characters
            while len(char_freq) > k:
                # Remove leftmost character from window
                char_freq[s[wind_start]] -= 1
                # If frequency becomes 0, remove from map (important!)
                if char_freq[s[wind_start]] == 0:
                    del char_freq[s[wind_start]]
                wind_start += 1

            # Update max only when we have EXACTLY k distinct characters
            if len(char_freq) == k:
                length_max = max(length_max, wind_end - wind_start + 1)
            # Note: Remove "== k" check for "At Most K" variant

        # Return -1 if no valid substring found, else return max length
        return -1 if length_max == float('-inf') else length_max