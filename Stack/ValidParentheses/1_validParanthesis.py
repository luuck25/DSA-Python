"""
PROBLEM: Valid Parentheses
Given a string containing only parentheses characters, determine whether the
string is validly balanced.

APPROACH:
Use a stack to match each closing bracket with the most recent unmatched opening
bracket.
- If the current character is an opening bracket, push it onto the stack.
- If it is a closing bracket:
  - check whether the stack top matches the corresponding opening bracket.
  - if yes, pop it.
  - if no, the string is invalid immediately.
At the end, the string is valid only if the stack is empty.

PSEUDOCODE:
1. create empty stack
2. create map: ) -> (, ] -> [, } -> {
3. for each character c in s:
   - if c is a closing bracket:
       if stack is not empty and stack[-1] == matching opening bracket:
           pop stack
       else:
           return False
   - else:
       push c onto stack
4. return True if stack is empty else False

TIME COMPLEXITY: O(n)
- We scan the string once.

SPACE COMPLEXITY: O(n)
- In the worst case, the stack stores all opening brackets.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack stores opening brackets waiting to be matched
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                # Check if current closing bracket matches the most recent opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Opening bracket must be stored until it gets matched
                stack.append(c)

        # Valid only if all opening brackets were matched
        return True if not stack else False