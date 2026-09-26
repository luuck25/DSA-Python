# Stack — Deep Dive: Patterns & Problem Types

---

## 🧠 Core Concept

A **stack** is a **Last-In, First-Out (LIFO)** data structure. Think of a stack of plates — you can only add/remove from the **top**.

| Operation | Python | Time |
|---|---|---|
| Push (add to top) | `stack.append(x)` | O(1) |
| Pop (remove from top) | `stack.pop()` | O(1) |
| Peek (look at top) | `stack[-1]` | O(1) |
| Is empty? | `not stack` or `len(stack) == 0` | O(1) |

> **When to think "Stack":** Whenever you see **matching**, **nesting**, **"most recent"**, or **"undo the last thing"**.

---

## 📌 PATTERN 1: Matching / Valid Parentheses

**Recognize when:** "valid brackets", "matching pairs", "balanced", "nesting"

**How it works:** Push opening brackets, pop when you see the matching closing bracket. If anything mismatches or stack isn't empty at the end → invalid.

```python
# Template
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:           # closing bracket
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)        # opening bracket

    return not stack  # stack must be empty
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Valid Parentheses | push open, pop on matching close |
| Minimum Remove to Make Valid | track indices of invalid brackets |
| Longest Valid Parentheses | stack of indices, calculate lengths |
| Generate Parentheses | backtracking (conceptually stack-based) |
| Valid Parenthesis String (with `*`) | two stacks: one for `(`, one for `*` |

**🔍 Recognition cues:** "parentheses", "brackets", "valid", "balanced", "matching"

---

## 📌 PATTERN 2: Monotonic Stack (Next Greater / Smaller Element)

**Recognize when:** "next greater element", "next smaller", "previous greater", "stock span", "temperatures"

**This is the MOST IMPORTANT stack pattern for interviews.**

**How it works:** Maintain a stack where elements are always in increasing (or decreasing) order. When a new element breaks the order, pop and process.

```python
# Template — Next Greater Element (right to left)
def nextGreater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n - 1, -1, -1):
        # Pop elements smaller than current (they can't be "next greater" for anyone)
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        # If stack not empty, top is the next greater element
        if stack:
            result[i] = nums[stack[-1]]

        stack.append(i)

    return result
```

```python
# Template — Next Greater Element (left to right, more common)
def nextGreater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        # Current element is the "next greater" for everything smaller on the stack
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result
```

**Visual Example:**

```
nums = [2, 1, 2, 4, 3]

i=0: num=2, stack=[]       → push 0         stack=[0]
i=1: num=1, stack=[0]      → 1 < 2, push 1  stack=[0,1]
i=2: num=2, stack=[0,1]    → 2 > 1, pop 1 → result[1]=2
                            → 2 >= 2, pop 0 → result[0]=2 (or not if strictly >)
                            → push 2         stack=[2]
i=3: num=4, stack=[2]      → 4 > 2, pop 2 → result[2]=4
                            → push 3         stack=[3]
i=4: num=3, stack=[3]      → 3 < 4, push 4  stack=[3,4]

Remaining stack: result[3]=-1, result[4]=-1

result = [2, 2, 4, -1, -1]  (or variation based on strict >)
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Next Greater Element I & II | monotonic decreasing stack |
| Daily Temperatures | "how many days until warmer?" = next greater index |
| Stock Span Problem | count consecutive days with price ≤ today |
| Largest Rectangle in Histogram | monotonic increasing stack, pop to calc area |
| Trapping Rain Water | monotonic stack (or two pointers) |
| Remove K Digits | monotonic increasing stack, pop larger digits |
| 132 Pattern | monotonic stack from right, track "2" |

**🔍 Recognition cues:** "next greater", "next smaller", "span", "temperatures", "histogram", "rectangle area"

---

## 📌 PATTERN 3: Expression Evaluation / Calculator

**Recognize when:** "evaluate expression", "calculator", "reverse polish notation", "postfix"

**How it works:** Use stack to hold numbers and intermediate results. Process operators based on precedence.

```python
# Template — Basic Calculator (handles +, -, with parentheses)
def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in '+-':
            result += sign * num
            sign = 1 if ch == '+' else -1
            num = 0
        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ')':
            result += sign * num
            result *= stack.pop()   # sign before parenthesis
            result += stack.pop()   # result before parenthesis
            num = 0

    return result + sign * num
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Evaluate Reverse Polish Notation | push numbers, pop two on operator |
| Basic Calculator I | stack for signs, handle `(` `)` |
| Basic Calculator II | stack for `*` `/` priority |
| Decode String `3[a2[c]]` | stack of (string, count) pairs |
| Mini Parser (nested integers) | stack of NestedInteger objects |

**🔍 Recognition cues:** "evaluate", "calculator", "expression", "postfix", "RPN", "decode"

---

## 📌 PATTERN 4: Stack for Undo / History / Backtracking

**Recognize when:** "undo", "backspace", "browser history", "simplify path"

**How it works:** Push actions/states onto stack. Pop to undo or backtrack.

```python
# Template — Backspace String Compare
def processString(s):
    stack = []
    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()    # backspace = undo last character
        else:
            stack.append(ch)
    return ''.join(stack)
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Backspace String Compare | `#` = pop from stack |
| Simplify Unix Path | split by `/`, push dirs, pop on `..` |
| Browser History | two stacks: back and forward |
| Baseball Game | push scores, pop/peek for operations |
| Remove All Adjacent Duplicates | pop if top == current |

**🔍 Recognition cues:** "backspace", "undo", "remove adjacent", "simplify", "history"

---

## 📌 PATTERN 5: Stack for String Manipulation / Reversal

**Recognize when:** "reverse", "remove duplicates", "decode", "build smallest string"

**How it works:** Build result character by character on a stack. Pop conditionally.

```python
# Template — Remove All Adjacent Duplicates in String
def removeDuplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()         # adjacent duplicate → remove both
        else:
            stack.append(ch)
    return ''.join(stack)
```

```python
# Template — Remove K Adjacent Duplicates
def removeDuplicates(s, k):
    stack = []  # [(char, count)]
    for ch in s:
        if stack and stack[-1][0] == ch:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([ch, 1])
    return ''.join(ch * count for ch, count in stack)
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Remove All Adjacent Duplicates | pop if top matches current |
| Remove All Adjacent Duplicates II (k) | stack of (char, count) pairs |
| Decode String `3[abc]` | stack of (prev_string, repeat_count) |
| Reverse a String | push all, pop all |
| Remove Outermost Parentheses | depth counter as conceptual stack |

**🔍 Recognition cues:** "remove duplicates", "decode", "reverse", "adjacent"

---

## 📌 PATTERN 6: Min Stack / Stack with Extra State

**Recognize when:** "get minimum in O(1)", "max stack", "track additional info"

**How it works:** Maintain a parallel stack (or store tuples) to track extra state alongside normal values.

```python
# Template — Min Stack
class MinStack:
    def __init__(self):
        self.stack = []      # (value, current_min)

    def push(self, val):
        curr_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, curr_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Min Stack | store (val, current_min) pairs |
| Max Stack | store (val, current_max) pairs |
| Max Frequency Stack | map freq→stack, track max freq |
| Stock Span | stack of (price, span) pairs |

**🔍 Recognition cues:** "O(1) min/max", "design stack", "frequency stack"

---

## 📌 PATTERN 7: Recursive / DFS Simulation with Stack

**Recognize when:** "convert recursion to iteration", "DFS iteratively", "tree traversal without recursion"

**How it works:** Replace the call stack with an explicit stack.

```python
# Template — Iterative DFS (tree inorder)
def inorder(root):
    stack = []
    result = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Binary Tree Inorder Traversal | stack replaces recursion |
| Binary Tree Preorder Traversal | push right first, then left |
| Flatten Nested List Iterator | stack of iterators |
| Decode String (nested) | stack simulates recursive calls |
| Asteroid Collision | stack simulates chain reactions |

**🔍 Recognition cues:** "iterative traversal", "without recursion", "flatten nested", "simulate"

---

## 🎯 Quick Decision Flowchart

```
See a stack-like problem?
│
├── Matching/nesting? ──────────────► PATTERN 1: Valid Parentheses
│   "brackets", "balanced"
│
├── "Next greater/smaller"? ────────► PATTERN 2: Monotonic Stack ⭐
│   "temperatures", "histogram"       (most common in interviews!)
│
├── "Evaluate expression"? ─────────► PATTERN 3: Calculator
│   "calculator", "postfix"
│
├── "Undo / backtrack"? ───────────► PATTERN 4: History Stack
│   "backspace", "simplify path"
│
├── "Remove adjacent / decode"? ───► PATTERN 5: String Manipulation
│   "duplicates", "decode string"
│
├── "O(1) min/max retrieval"? ─────► PATTERN 6: Min/Max Stack
│   "design", "getMin"
│
└── "Iterative DFS / recursion"? ──► PATTERN 7: DFS Simulation
    "without recursion", "flatten"
```

---

## ⚠️ Common Pitfalls

| Pitfall | Fix |
|---|---|
| Popping from empty stack | Always check `if stack` before `stack.pop()` or `stack[-1]` |
| Forgetting leftover items | After the loop, process remaining items on the stack |
| Monotonic stack direction | Decide: increasing or decreasing? Left-to-right or right-to-left? |
| Using stack when deque is better | If you need both ends → use `collections.deque` |
| Not storing indices | Store **indices** (not values) when you need positions later |

---

## 🔑 When Stack vs Other Data Structures?

| Situation | Use |
|---|---|
| Need LIFO (last in, first out) | **Stack** |
| Need FIFO (first in, first out) | **Queue** (`deque`) |
| Need both ends | **Deque** |
| Need min/max efficiently | **Heap** (or Min Stack for O(1)) |
| Need "next greater" | **Monotonic Stack** ⭐ |
| Need matching pairs | **Stack** |
| Need frequency | **HashMap** |

---

These 7 patterns cover **~95%** of all stack problems in interviews. The **monotonic stack** (Pattern 2) is by far the most frequently tested and the hardest to recognize at first — practice it the most!

---

---

## Folder-to-Pattern Map

### Valid Parentheses
- `Stack/ValidParentheses/1_validParanthesis.py` — matching brackets
- `Stack/ValidParentheses/2_MinimumAddtoMakeParenthesesValid.py` — minimum insertions
- `Stack/ValidParentheses/3_minRemoveToMakeValid.py` — remove invalid parentheses
- `Stack/ValidParentheses/4_min_swap_balance_string.py` — minimum bracket swaps
- `Stack/ValidParentheses/5_longestValidParentheses.py` — longest valid substring

### Monotonic Stack
- `Stack/Monotonic_Stack/1_nextGreaterElement.py`
- `Stack/Monotonic_Stack/2_nextGreaterElements2.py`
- `Stack/Monotonic_Stack/3_DailyTemperatures.py`
- `Stack/Monotonic_Stack/4_RemoveKDigits.py`
- `Stack/Monotonic_Stack/5_CarFleet.py`
- `Stack/LargestRectange_Histogram/largestRectangleArea.py`
- `Stack/LargestRectange_Histogram/maxRectangle.py`

### Expression and Simulation
- `Stack/Expression_evaluation/EvaluateReversePolishNotation.py`
- `Stack/SimulationandBacktracking/DecodeString.py`
- `Stack/SimulationandBacktracking/asteroidCollision.py`

### Stack Design
- `Stack/Min_Stack_Design/minstack.py`
- `Stack/Min_Stack_Design/OnlineStockSpan.py`

---

## Quick Reference: Stack Problems

This table follows the same format as the Linked List guide: problem name, LeetCode number, complexity, approach, and special attention.

### Parentheses and Brackets

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Valid Parentheses** | [#20](https://leetcode.com/problems/valid-parentheses/) | O(n) | O(n) | Push opening brackets; pop only when the closing bracket matches the stack top. | Check both mismatch and leftover opening brackets. |
| 2 | **Minimum Add to Make Parentheses Valid** | [#921](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | O(n) | O(1) | Track unmatched opening brackets and count closing brackets that need an inserted opener. | Do not let the opening count become negative. |
| 3 | **Minimum Remove to Make Valid Parentheses** | [#1249](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | O(n) | O(n) | Store indices of unmatched parentheses, then rebuild the string without those indices. | Store indices, not just characters, to remove the correct duplicates. |
| 4 | **Minimum Number of Swaps to Make the String Balanced** | [#1963](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) | O(n) | O(1) | Track bracket balance and greedily fix each invalid prefix with one swap. | The input must have equal counts of `[` and `]`. |
| 5 | **Longest Valid Parentheses** | [#32](https://leetcode.com/problems/longest-valid-parentheses/) | O(n) | O(n) | Store indices of unmatched boundaries; calculate length when a closing bracket finds a match. | Initialize the stack with `-1` as the boundary before the current segment. |

### Monotonic Stack

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Next Greater Element I** | [#496](https://leetcode.com/problems/next-greater-element-i/) | O(n + m) | O(n) | Scan the reference array with a decreasing stack and map each popped value to its next greater value. | Resolve answers from `nums2` before looking up values from `nums1`. |
| 2 | **Next Greater Element II** | [#503](https://leetcode.com/problems/next-greater-element-ii/) | O(n) | O(n) | Simulate two passes with `i % n` to handle circular wraparound. | Push indices only during the first pass. |
| 3 | **Daily Temperatures** | [#739](https://leetcode.com/problems/daily-temperatures/) | O(n) | O(n) | Keep unresolved day indices in a decreasing stack and assign distances when a warmer day appears. | Store indices because the answer is a number of days. |
| 4 | **Remove K Digits** | [#402](https://leetcode.com/problems/remove-k-digits/) | O(n) | O(n) | Maintain increasing digits; remove larger preceding digits while removals remain. | Remove trailing digits when the number is already increasing, then strip leading zeroes. |
| 5 | **Car Fleet** | [#853](https://leetcode.com/problems/car-fleet/) | O(n log n) | O(n) | Sort cars from nearest to farthest target and keep arrival times for fleets ahead. | A car behind joins the fleet ahead when its arrival time is less than or equal to that fleet's time. |
| 6 | **Largest Rectangle in Histogram** | [#84](https://leetcode.com/problems/largest-rectangle-in-histogram/) | O(n) | O(n) | Use an increasing stack; when a shorter bar appears, pop and calculate the rectangle's width. | Add a zero-height sentinel to flush the remaining bars. |
| 7 | **Maximal Rectangle** | [#85](https://leetcode.com/problems/maximal-rectangle/) | O(mn) | O(n) | Convert each matrix row into histogram heights and solve a histogram rectangle for every row. | Reset a column's height to zero whenever the current cell is `0`. |

### Expression Evaluation and Simulation

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Evaluate Reverse Polish Notation** | [#150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | O(n) | O(n) | Push operands; for each operator pop the right operand first, then the left operand. | Operand order matters for subtraction and division; truncate division toward zero. |
| 2 | **Decode String** | [#394](https://leetcode.com/problems/decode-string/) | O(L) | O(L) | Push the outer string and repeat count at `[`, then restore and repeat the nested string at `]`. | Build multi-digit repeat counts before processing `[`. `L` is the decoded output length. |
| 3 | **Asteroid Collision** | [#735](https://leetcode.com/problems/asteroid-collision/) | O(n) | O(n) | Keep surviving asteroids in a stack and repeatedly resolve collisions with a positive top and negative incoming asteroid. | One asteroid can destroy several previous asteroids, so collision handling needs a `while` loop. |

### Stack Design

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Min Stack** | [#155](https://leetcode.com/problems/min-stack/) | O(1) per operation | O(n) | Store each value with the minimum value seen up to that point. | Popping a pair automatically restores the previous minimum. |
| 2 | **Online Stock Span** | [#901](https://leetcode.com/problems/online-stock-span/) | Amortized O(1) per call | O(n) | Store `(price, span)` pairs in a decreasing stack and merge spans while previous prices are less than or equal to today’s price. | Aggregate stored spans instead of counting previous days one by one. |
