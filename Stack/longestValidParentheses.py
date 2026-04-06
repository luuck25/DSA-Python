"""
Longest Valid Parentheses — Plain English Walkthrough
======================================================
Problem:
    Given a string containing only '(' and ')', find the length of the
    longest valid (well-formed) parentheses substring.

    Input:  "(()"    →  2   (the valid part is "()")
    Input:  ")()())" →  4   (the valid part is "()()")
    Input:  ""       →  0

Visual Example:
    Input: ")()())"

    Index:  0  1  2  3  4  5
    Char:   )  (  )  (  )  )

    Stack stores INDICES (not characters). We start with [-1] as a "base marker".

    Start: stack = [-1], longest = 0

    i=0, ')':
        Pop → stack becomes []
        Stack is EMPTY → this ')' is unmatched → push its index as new base
        stack = [0]

    i=1, '(':
        Push index 1
        stack = [0, 1]

    i=2, ')':
        Pop → removes 1 → stack = [0]
        Stack NOT empty → valid length = i - stack[-1] = 2 - 0 = 2
        longest = 2

    i=3, '(':
        Push index 3
        stack = [0, 3]

    i=4, ')':
        Pop → removes 3 → stack = [0]
        Stack NOT empty → valid length = i - stack[-1] = 4 - 0 = 4
        longest = 4

    i=5, ')':
        Pop → removes 0 → stack = []
        Stack is EMPTY → push index 5 as new base
        stack = [5]

    Result: 4 ✅

Why start with [-1] in the stack?
    It acts as a "boundary marker" — the index just BEFORE the start
    of a potential valid substring. When we calculate length as
    i - stack[-1], we need something on the stack to subtract from.

    Without [-1]:
        s = "()" → i=1, pop '(' at 0 → stack empty → can't calculate length!

    With [-1]:
        s = "()" → i=1, pop '(' at 0 → stack = [-1] → length = 1 - (-1) = 2 ✅

Why push index when stack is empty after popping?
    An unmatched ')' becomes the new boundary. Everything valid
    after this point is measured from HERE.

    Example: ")()()" → the ')' at index 0 is the boundary.
    Valid substring "()()" starts at index 1, measured from boundary 0.

Approach:
    1. Initialize stack with [-1] (boundary marker)
    2. For each character:
       - '(' → push its index
       - ')' → pop from stack
         - If stack is empty → unmatched ')' → push current index as new boundary
         - If stack not empty → valid match → length = i - stack[-1]
    3. Track the maximum length

Time:  O(n) — single pass through the string
Space: O(n) — stack can hold up to n indices
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # Start with -1 as a boundary marker
        # It represents "the index just before any valid substring starts"
        stack = [-1]

        # Track longest valid substring found
        longest = 0

        for i, ch in enumerate(s):

            if ch == '(':
                # Push index of '(' — waiting for a matching ')'
                stack.append(i)

            if ch == ')':
                # Try to match with the most recent '('
                stack.pop()

                if not stack:
                    # Stack empty → this ')' is unmatched
                    # Push its index as the new boundary marker
                    # (everything valid after here is measured from this point)
                    stack.append(i)
                else:
                    # Stack not empty → we successfully matched a pair
                    # Length of current valid substring = current index - top of stack
                    # stack[-1] is the index just BEFORE this valid substring started
                    longest = max(longest, i - stack[-1])

        return longest

    # https://www.youtube.com/watch?v=gqQsbdTcey0
    # ---- Clean version (no comments) ----
    # The key to solving the Longest Valid Parentheses problem
    #  efficiently is recognizing the usefulness of a stack for tracking unmatched parentheses 
    # https://algomap.io/question-bank/longest-valid-parentheses
    def longestValidParentheses_clean(self, s: str) -> int:
        stack = [-1]
        longest = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            if ch == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest