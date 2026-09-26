"""
PROBLEM: Minimum Remove to Make Valid Parentheses
Remove the minimum number of characters so the remaining parentheses string is
balanced and valid.

APPROACH:
Use a stack to find unmatched parentheses.
1. Scan the string from left to right.
2. Push index of every '(' onto the stack.
3. For every ')':
   - if there is an opening '(' available to match, pop it.
   - otherwise, mark this index as invalid and remove it.
4. After the first pass, any leftover '(' in the stack are unmatched and must be
   removed as well.
5. Build the final valid string using only the indices not marked for removal.

PSEUDOCODE:
1. stack = empty list
2. remove = empty set
3. for each index i and character ch in s:
   - if ch == '(':
       push i onto stack
   - else if ch == ')':
       if stack is not empty:
           pop from stack
       else:
           add i to remove
4. add all remaining stack indices to remove
5. build result by skipping indices in remove
6. return result string

TIME COMPLEXITY: O(n)
- We scan the string a constant number of times.

SPACE COMPLEXITY: O(n)
- The stack and set can each hold up to O(n) indices in the worst case.
"""


def minRemoveToMakeValid(s):
    # Stack stores indices of unmatched opening parentheses
    stack = []
    # remove stores indices that must be deleted
    remove = set()

    # Step 1: Identify invalid indices
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                remove.add(i)

    # Step 2: Add leftover '(' indices
    remove.update(stack)

    # Step 3: Build result
    result = []
    for i, ch in enumerate(s):
        if i not in remove:
            result.append(ch)

    return ''.join(result)