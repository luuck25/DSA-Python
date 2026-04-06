class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(" ".join(s.split()))

        def reverse(l,r):
            while r>l:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        reverse(0, len(s)-1) # reverse strng

        #reverse words
        start = 0
        for i in range(len(s)+1):
            if i == len(s) or s[i] == ' ':
                reverse(start,i-1)
                start = i + 1

        return "".join(s)
        