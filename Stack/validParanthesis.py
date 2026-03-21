class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
        ')':'(',
        ']':'[',
        '}':'{'
        }

        st = []

        for ch in s:
            if ch in mapping:
                if not st or st[-1] != mapping[ch]:
                    return False
                st.pop()
            else:
                st.append(ch)        

        return len(st) ==0