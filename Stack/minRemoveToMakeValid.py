def minRemoveToMakeValid(s):
    stack = []
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