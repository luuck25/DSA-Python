class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)

        start = 0
        end = n - 1
        vow = {'a','e','i','o','u'}
        while end > start:

            while end > start and s[start].lower() not in vow:
                    start += 1
            while end > start and s[end].lower() not in vow:
                    end -= 1  

            
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1 

                


        return "".join(s)          
        