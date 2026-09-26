"""
PROBLEM: Minimum Swaps to Balance a String
Given a string containing only '[' and ']', find the minimum number of swaps to
make the string balanced.

APPROACH (Stack-based):
Use a stack to match bracket pairs.
1. Iterate through the string.
2. If we see '[', push it.
3. If we see ']':
   - if stack top is '[', pop it (a matched pair).
   - otherwise, push the ']'.
4. After processing, the stack contains only unmatched brackets (all ']' at the
   start and all '[' at the end).
5. The minimum swaps needed is (stack_size + 1) // 2.

Why (n+1)//2?
- Suppose we have n unmatched brackets left, all in pattern: ] ] ... ] [ [ ... [
- To balance, we pair them from outside: swap first ] with last [ (makes both balanced).
- Repeating, we need ceil(n/2) = (n+1)//2 swaps.

PSEUDOCODE:
1. stack = empty
2. for each character ch in s:
   - if stack is not empty, stack top is '[', and ch is ']':
       pop (matched pair)
   - else if ch is '[':
       push ch
3. return (len(stack) + 1) // 2

TIME COMPLEXITY: O(n)
- We scan the string once.

SPACE COMPLEXITY: O(n)
- In the worst case, stack stores O(n) characters.
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        # Stack stores unmatched opening brackets
        st = []

        for ch in s:
            if st and st[-1] == '[' and ch == ']':
                # Matched pair — remove it
                st.pop()
            elif ch == '[':
                # Unmatched opening bracket
                st.append(ch)
            # Note: unmatched ']' is neither pushed nor processed further
            # The stack effectively stores ] characters that couldn't be matched

        n = len(st)
        # Ceiling division: minimum swaps = ceil(n/2)
        return (n + 1) // 2


class Solution2:
    def minSwaps(self, s: str) -> int:
        """
        Optimized counter approach (no stack, single counter).
        Track only unmatched opening brackets.
        
        Key insight: After all matching, remaining unmatched brackets have pattern:
        ] ] ] ... ] [ [ [ ... [
        (all closing on left, all opening on right)
        
        So we only need to count unmatched '[' at the end.
        """
        size = 0

        for ch in s:
            if ch == '[':
                # Unmatched opening bracket
                size += 1
            else:  # ch == ']'
                if size > 0:
                    # Match with most recent unmatched opening bracket
                    size -= 1
                # else: unmatched closing bracket (implicitly counted in final formula)

        # Minimum swaps = ceil(size / 2) = (size + 1) // 2
        return (size + 1) // 2
