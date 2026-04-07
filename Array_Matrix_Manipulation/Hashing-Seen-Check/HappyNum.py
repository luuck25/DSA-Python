"""
Happy Number — Plain English Walkthrough
==========================================
Problem:
    A number is "happy" if you repeatedly replace it with the sum of the
    squares of its digits, and eventually reach 1.
    If it loops forever without reaching 1 → not happy.

    Input:  19  →  True
    Input:  2   →  False

Visual Example (Happy):
    Input: n = 19

    19 → 1² + 9² = 1 + 81 = 82
    82 → 8² + 2² = 64 + 4  = 68
    68 → 6² + 8² = 36 + 64 = 100
    100 → 1² + 0² + 0² = 1  →  ✅ Happy!

Visual Example (Not Happy):
    Input: n = 2

    2  → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4  ← LOOP!
                                                    ↑
                                            4 appeared again → cycle detected → ❌

Key Insight:
    There are only two outcomes:
    1. The sequence reaches 1 → happy number ✅
    2. The sequence enters a CYCLE (same number appears again) → not happy ❌

    It can NEVER grow to infinity because:
    - A 3-digit number (max 999) → max sum = 9²+9²+9² = 243
    - So the values stay bounded and must eventually repeat or hit 1.

Why HashSet?
    - We need to detect if we've seen a number before (cycle detection)
    - set lookup is O(1) → perfect for "have I seen this before?"

    Alternative: Floyd's fast/slow pointer (O(1) space, no set needed)

Approach:
    1. Use a HashSet to track every number we've computed
    2. While n != 1:
       - If n is in the set → we're in a loop → return False
       - Add n to the set
       - Replace n with the sum of squares of its digits
    3. Loop exited → n == 1 → return True

Time:  O(log n) per step × number of steps (bounded, typically small)
Space: O(log n) per entry × number of entries in the set
"""


def isHappy(n):
    # Track every number we've seen to detect cycles
    seen = set()

    while n != 1:
        # If we've seen this number before → infinite loop → not happy
        if n in seen:
            return False

        # Mark this number as visited
        seen.add(n)

        # Replace n with sum of squares of its digits
        # str(n) splits into individual digits: 19 → "19" → '1', '9'
        # int(digit)**2 squares each: 1² + 9² = 82
        n = sum(int(digit) ** 2 for digit in str(n))

    # Reached 1 → happy number!
    return True


# ---- Clean version (no comments) ----
def isHappy_clean(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return True