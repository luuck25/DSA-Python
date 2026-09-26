"""
PROBLEM: Minimum Add to Make Parentheses Valid
We need to add the minimum number of parentheses so that the string becomes
valid and balanced.

APPROACH:
Use a stack to track unmatched opening parentheses.
- If we see '(', push it onto the stack.
- If we see ')':
  - if the stack top is '(', it is a valid pair, so pop it.
  - otherwise, this ')' cannot match anything, so it must be added later,
    so push it to the stack.
At the end, the remaining stack contains all unmatched parentheses, and the
answer is simply the size of the stack.

PSEUDOCODE:
1. create empty stack
2. for each character ch in s:
   - if ch == '(':
       push ch onto stack
   - else:
       if stack is not empty and top is '(':
           pop top
       else:
           push ch onto stack
3. return length of stack

TIME COMPLEXITY: O(n)
- We process each character once.

SPACE COMPLEXITY: O(n)
- In the worst case, the stack stores all unmatched opening parentheses.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Stack stores unmatched opening parentheses and unmatched closing parentheses
        st = []

        for ele in s:
            if ele == '(':
                # Opening parenthesis must wait for a closing one
                st.append(ele)
            else:
                # If we can match with the latest opening bracket, cancel it
                if st and st[-1] == '(':
                    st.pop()
                else:
                    # This closing bracket cannot be matched, so it must be added
                    st.append(ele)

        # Remaining entries are the minimum parentheses needed to fix the string
        return len(st)


class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        # Counter approach: keep track of unmatched open brackets
        open = 0
        additions = 0

        for c in s:
            if c == '(':
                open += 1
            else:  # c == ')'
                if open > 0:
                    open -= 1
                else:
                    additions += 1

        # Any remaining open brackets also need closing ones
        return additions + open
