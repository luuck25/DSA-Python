class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        window_start = 0
    
        max_len = 0
        char_set = set()

        for window_end in range(len(s)):
            current_char = s[window_end]
            
            while current_char in char_set:
                char_set.remove(s[window_start])
                window_start += 1
            
            char_set.add(current_char)
            max_len = max((window_end - window_start) + 1, max_len)

        return max_len