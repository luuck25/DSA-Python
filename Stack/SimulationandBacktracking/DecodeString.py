"""
PROBLEM: Decode String
Given a string with encoded characters where:
- digits represent how many times to repeat the pattern that follows in brackets
- brackets denote the start and end of a pattern to repeat

Example: "3[a2[c]]" → "accaccacc"
- 2[c] → cc
- 3[a{cc}] → accaccacc

APPROACH:
Use a stack to handle nested encoding.
1. Iterate through each character.
2. If it's not ']', push the character onto the stack.
3. If it's ']':
   - Pop characters back to '[' to form the substring.
   - Pop the '[' itself.
   - Pop all digits before the '[' to get the repetition count k.
   - Push k * substring back onto the stack.
4. At the end, join all characters in the stack to get the decoded string.

Why this works:
- Stack naturally handles nested brackets.
- When we encounter ']', we know the pattern to repeat is on top of the stack.
- The digit(s) before '[' represent the repetition count for that specific pattern.
- By pushing the repeated string back, nested patterns are handled correctly.

PSEUDOCODE:
1. stack = empty
2. for each character char in s:
   - if char != ']':
       push char onto stack
   - else:
       substr = ''
       while stack[-1] != '[':
           substr = pop() + substr
       pop()  // pop '['
       k = ''
       while stack not empty and stack[-1].isdigit():
           k = pop() + k
       push(int(k) * substr)
3. return join all elements in stack

TIME COMPLEXITY: O(n * m)
- n = length of input string
- m = maximum length of decoded string
- We may need to process each character multiple times if nested deeply.
- In worst case with nested brackets, can reach O(n * m).

SPACE COMPLEXITY: O(n + decoded_length)
- Stack stores all characters and intermediate results.
- Could be up to O(n) for the input and O(decoded_length) for the output.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # Stack stores characters, digits, brackets, and decoded substrings
        st = []
      
        for char in s:
            if char == ']':
                # Closing bracket: process the encoded pattern
                substr = ''
                
                # Pop all characters until we hit '['
                while st[-1] != '[':
                    substr = st.pop() + substr

                # Pop the opening bracket
                st.pop()

                # Extract the repetition count (all digits before '[')
                k = ''
                while st and st[-1].isdigit():
                    k = st.pop() + k

                # Push the repeated substring back
                st.append(int(k) * substr)
                
            else:
                # Not a closing bracket: push digit, letter, or opening bracket
                st.append(char)

        # Join all decoded strings
        return "".join(st)


        