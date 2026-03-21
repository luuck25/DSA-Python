from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if  t == "" : 
            return ""
        
        left = 0
        res, resLen = [-1,-1], float('inf')
        window, target = {} , {}

        target = Counter(t)
        have , need = 0, len(target)

        for right in  range(len(s)):
            curr_char  = s[right]
            window[curr_char] = window.get(curr_char,0) +1

            if curr_char in target and window[curr_char] == target[curr_char]:
                have += 1

            while need == have:

                if  (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1

                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right+1] if resLen != float('inf') else ""