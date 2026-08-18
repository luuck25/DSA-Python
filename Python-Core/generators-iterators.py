"""
=============================================================================
  GENERATORS & ITERATORS — Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. ITERABLES vs ITERATORS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Iterable: anything you can loop over (has __iter__)
#       → list, tuple, str, dict, set, range, file
#
#   Iterator: object that produces next value (has __next__)
#       → created from iterable via iter()
#
#   Every iterator IS an iterable, but not every iterable is an iterator.

nums = [10, 20, 30]           # iterable
it = iter(nums)               # iterator
# next(it)  → 10
# next(it)  → 20
# next(it)  → 30
# next(it)  → StopIteration exception

# for loop does this internally:
# for x in nums:
#     internally calls iter(nums), then next() until StopIteration


# ═══════════════════════════════════════════════════════════════════════════
# 2. WRITING A CUSTOM ITERATOR (Java-style)
# ═══════════════════════════════════════════════════════════════════════════

class CountDown:
    """Counts down from n to 1."""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self              # iterator returns itself

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

# for x in CountDown(3): print(x)   → 3, 2, 1

# Java equivalent requires:
#   class CountDown implements Iterator<Integer> {
#       public boolean hasNext() { ... }
#       public Integer next() { ... }
#   }


# ═══════════════════════════════════════════════════════════════════════════
# 3. GENERATORS — THE PYTHON WAY (much simpler)
# ═══════════════════════════════════════════════════════════════════════════
#
#   A generator is a function that uses `yield` instead of `return`.
#   Each call to next() runs until the next yield, then PAUSES.

def countdown(n):
    while n > 0:
        yield n         # pause here, return n
        n -= 1          # resume here on next call

# gen = countdown(3)
# next(gen)  → 3
# next(gen)  → 2
# next(gen)  → 1
# next(gen)  → StopIteration

# Key insight: Function state (local vars) is PRESERVED between yields.
# Java has nothing this simple — need explicit Iterator class.


# ═══════════════════════════════════════════════════════════════════════════
# 4. WHY GENERATORS? — MEMORY EFFICIENCY
# ═══════════════════════════════════════════════════════════════════════════

# BAD: creates entire list in memory
def get_squares_list(n):
    return [x**2 for x in range(n)]    # O(n) memory

# GOOD: yields one at a time
def get_squares_gen(n):
    for x in range(n):
        yield x**2                     # O(1) memory

# For 10 million numbers:
# get_squares_list(10_000_000)  → ~80 MB in memory
# get_squares_gen(10_000_000)   → negligible memory (one value at a time)


# ═══════════════════════════════════════════════════════════════════════════
# 5. GENERATOR EXPRESSIONS (one-liner generators)
# ═══════════════════════════════════════════════════════════════════════════

# List comprehension → builds full list
squares_list = [x**2 for x in range(10)]     # [0, 1, 4, 9, ...]

# Generator expression → lazy, one at a time
squares_gen = (x**2 for x in range(10))      # <generator object>

# Use gen expressions when you only need to iterate ONCE:
total = sum(x**2 for x in range(1000))       # no intermediate list!

# Interview tip: sum(), min(), max(), any(), all() accept gen expressions
# directly — no need for a list.


# ═══════════════════════════════════════════════════════════════════════════
# 6. yield vs return
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Feature         | return                    | yield                        |
#   |-----------------|---------------------------|------------------------------|
#   | Terminates?     | Yes, function done        | No, function pauses          |
#   | Memory          | All results at once       | One at a time                |
#   | State           | Lost after return         | Preserved between yields     |
#   | Result type     | Single value / list       | Generator object             |
#   | Resumable?      | No                        | Yes (via next())             |


# ═══════════════════════════════════════════════════════════════════════════
# 7. COMMON PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

# --- Infinite sequence ---
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

# Can't do this with a list! Would be infinite memory.
# Usage: take first 5 → from itertools import islice
# list(islice(natural_numbers(), 5))  → [1, 2, 3, 4, 5]


# --- Reading large files line by line ---
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:          # file object is already an iterator
            yield line.strip()


# --- Flatten nested lists ---
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)    # yield from = delegate to sub-generator
        else:
            yield item

# list(flatten([1, [2, [3, 4]], 5]))  → [1, 2, 3, 4, 5]


# --- Fibonacci ---
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# ═══════════════════════════════════════════════════════════════════════════
# 8. yield from — DELEGATING TO SUB-GENERATORS
# ═══════════════════════════════════════════════════════════════════════════

def gen_1():
    yield 1
    yield 2

def gen_2():
    yield 3
    yield 4

def combined():
    yield from gen_1()      # delegates to gen_1
    yield from gen_2()      # then delegates to gen_2

# list(combined())  → [1, 2, 3, 4]

# Without yield from, you'd need:
# for x in gen_1(): yield x
# for x in gen_2(): yield x


# ═══════════════════════════════════════════════════════════════════════════
# 9. GENERATOR .send() — TWO-WAY COMMUNICATION
# ═══════════════════════════════════════════════════════════════════════════

def accumulator():
    total = 0
    while True:
        value = yield total     # yield current total, receive next value
        total += value

# acc = accumulator()
# next(acc)          → 0   (prime the generator)
# acc.send(10)       → 10
# acc.send(20)       → 30
# acc.send(5)        → 35

# Rarely used in interviews, but good to know.


# ═══════════════════════════════════════════════════════════════════════════
# 10. itertools — STANDARD LIBRARY FOR ITERATION
# ═══════════════════════════════════════════════════════════════════════════

from itertools import (
    count,          # count(10) → 10, 11, 12, ... (infinite)
    cycle,          # cycle([1,2,3]) → 1,2,3,1,2,3,... (infinite)
    repeat,         # repeat('x', 3) → 'x','x','x'
    chain,          # chain([1,2], [3,4]) → 1,2,3,4
    islice,         # islice(gen, 5) → first 5 items
    combinations,   # combinations('ABC', 2) → AB, AC, BC
    permutations,   # permutations('ABC', 2) → AB, AC, BA, BC, CA, CB
    product,        # product('AB', '12') → A1, A2, B1, B2
    groupby,        # group consecutive equal elements
    accumulate,     # running totals
    zip_longest,    # zip but fills missing with fillvalue
)

# Interview favorites:
# combinations('ABCD', 2) → all pairs without repetition
# permutations('ABC', 2)  → all ordered pairs
# product([0,1], repeat=3) → all 3-bit binary numbers


# ═══════════════════════════════════════════════════════════════════════════
# 11. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What's the difference between list and generator?
#   A: List stores all values in memory; generator produces one at a time (lazy).
#
#   Q: When would you use a generator?
#   A: Large datasets, infinite sequences, streaming data, when you only iterate once.
#
#   Q: Can you iterate a generator twice?
#   A: No! Once exhausted, it's done. Create a new one.
#
#   Q: What does yield do?
#   A: Pauses function, returns value. Next call resumes from that point.
#
#   Q: range() — list or generator?
#   A: Neither — it's a lazy sequence object. But it behaves like a generator
#      (O(1) memory) while also supporting indexing and len().
