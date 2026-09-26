class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []

        for char in num:
            while st and k > 0 and st[-1] > char:
                st.pop()
                k -= 1

            st.append(char)

        # If removals are still left, remove from the end
        while k > 0:
            st.pop()
            k -= 1

        result = ''.join(st).lstrip('0')

        return result if result else '0'