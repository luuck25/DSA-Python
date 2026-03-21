class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp ={}
        left =  0
        max_freq = 0
        mx_len = 0

        for end  in range(len(s)):
            mp[s[end]] = mp.get(s[end],0) + 1
            max_freq = max(max_freq, mp[s[end]])

            while (end - left + 1) - max_freq > k:
                mp[s[left]] -= 1
                left += 1


            mx_len = max(mx_len, end- left +1 )
        return mx_len    



        