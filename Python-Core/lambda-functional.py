"""
=============================================================================
  LAMBDA & FUNCTIONAL PROGRAMMING — Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. LAMBDA — ANONYMOUS FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Syntax: lambda parameters: expression
#   - Single expression only (no statements, no assignments)
#   - Returns result of the expression automatically

square = lambda x: x ** 2          # same as def square(x): return x**2
add = lambda a, b: a + b           # same as def add(a, b): return a + b

(lambda a, b: a + b)(a,b)

add(3,4)

# square(5)  → 25
# add(3, 4)  → 7

# When to use lambda:
#   ✓ Short, throwaway functions (sorting keys, map/filter)
#   ✗ Complex logic (use regular def instead)


# ═══════════════════════════════════════════════════════════════════════════
# 2. sorted() with key — MOST COMMON LAMBDA USE
# ═══════════════════════════════════════════════════════════════════════════

sorted([1,2,3])

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# Sort by grade (second element)
by_grade = sorted(students, key=lambda s: s[1])
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort by name length
by_name_len = sorted(students, key=lambda s: len(s[0]))

# Sort descending
by_grade_desc = sorted(students, key=lambda s: s[1], reverse=True)

# Sort dicts
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
by_age = sorted(people, key=lambda p: p["age"])

# Multiple sort keys: sort by age, then name
data = [("Alice", 30), ("Bob", 25), ("Charlie", 30)]
multi_sort = sorted(data, key=lambda x: (x[1], x[0]))
# [('Bob', 25), ('Alice', 30), ('Charlie', 30)]



# ═══════════════════════════════════════════════════════════════════════════
# 3. map() — TRANSFORM EACH ELEMENT
# ═══════════════════════════════════════════════════════════════════════════
#
#   map(function, iterable) → applies function to each element
#   Returns a MAP OBJECT (lazy iterator — not a list!)

nums = [1, 2, 3, 4, 5]

map(int,["1","2"])

# Double each number
doubled = list(map(lambda x: x * 2, nums))        # [2, 4, 6, 8, 10]

# Convert strings to ints
strs = ["1", "2", "3"]
ints = list(map(int, strs))                        # [1, 2, 3]

# Multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))        # [11, 22, 33]

# PYTHONIC ALTERNATIVE — list comprehension (preferred):
doubled_lc = [x * 2 for x in nums]                # same result, more readable


# ═══════════════════════════════════════════════════════════════════════════
# 4. filter() — KEEP ELEMENTS THAT PASS A TEST
# ═══════════════════════════════════════════════════════════════════════════
#
#   filter(function, iterable) → keeps elements where function returns True

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6, 8, 10]

# Keep non-empty strings
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, words))              # ["hello", "world", "python"]
# filter(None, ...) removes falsy values (0, "", None, [], {})

# PYTHONIC ALTERNATIVE — list comprehension (preferred):
evens_lc = [x for x in nums if x % 2 == 0]        # same result


# ═══════════════════════════════════════════════════════════════════════════
# 5. reduce() — ACCUMULATE TO A SINGLE VALUE
# ═══════════════════════════════════════════════════════════════════════════

from functools import reduce

nums = [1, 2, 3, 4, 5]

# Sum (1+2+3+4+5)
total = reduce(lambda acc, x: acc + x, nums)       # 15

# Product (1*2*3*4*5)
product = reduce(lambda acc, x: acc * x, nums)     # 120

# Find max
maximum = reduce(lambda a, b: a if a > b else b, nums)  # 5

# With initial value
total_100 = reduce(lambda acc, x: acc + x, nums, 100)   # 115

# How reduce works step by step:
#   reduce(f, [1,2,3,4]) →
#   f(f(f(1, 2), 3), 4)
#   step1: acc=1, x=2 → 3
#   step2: acc=3, x=3 → 6
#   step3: acc=6, x=4 → 10

# PYTHONIC ALTERNATIVE: use sum(), math.prod(), max() for common cases.


# ═══════════════════════════════════════════════════════════════════════════
# 6. map + filter + reduce CHAINED
# ═══════════════════════════════════════════════════════════════════════════

# Sum of squares of even numbers from 1-10
nums = range(1, 11)

# Functional style:
result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, nums))
)
# → 4 + 16 + 36 + 64 + 100 = 220

# PYTHONIC style (much cleaner):
result_py = sum(x**2 for x in nums if x % 2 == 0)  # 220


# ═══════════════════════════════════════════════════════════════════════════
# 7. OTHER FUNCTIONAL TOOLS
# ═══════════════════════════════════════════════════════════════════════════

# --- any() and all() ---
nums = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in nums)          # True
any_odd = any(x % 2 != 0 for x in nums)           # False

# --- zip() --- pair up iterables
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
paired = list(zip(names, scores))
# [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Create dict from two lists:
name_score = dict(zip(names, scores))
# {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# --- enumerate() --- index + value
for i, name in enumerate(names, start=1):
    pass  # i=1,name="Alice" → i=2,name="Bob" → ...


# ═══════════════════════════════════════════════════════════════════════════
# 8. OPERATOR MODULE — REPLACE SIMPLE LAMBDAS
# ═══════════════════════════════════════════════════════════════════════════

import operator

# Instead of lambda a, b: a + b
total = reduce(operator.add, [1, 2, 3, 4])         # 10

# Instead of lambda x: x[1]
from operator import itemgetter
sorted_by_grade = sorted(students, key=itemgetter(1))

# Instead of lambda obj: obj.name
from operator import attrgetter
# sorted(people_objs, key=attrgetter('age'))

# Common operators:
# operator.add, sub, mul, truediv, mod
# operator.lt, le, eq, ne, ge, gt
# operator.itemgetter(0), itemgetter('key')
# operator.attrgetter('attr')


# ═══════════════════════════════════════════════════════════════════════════
# 9. functools — FUNCTIONAL UTILITIES
# ═══════════════════════════════════════════════════════════════════════════

from functools import partial, lru_cache

# --- partial: fix some arguments ---
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)     # fix exp=2
cube = partial(power, exp=3)       # fix exp=3
# square(5) → 25
# cube(3)   → 27

# --- lru_cache: memoization ---
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# fib(100) → instant (without cache would be exponential)


# ═══════════════════════════════════════════════════════════════════════════
# 10. WHEN TO USE WHAT — INTERVIEW GUIDE
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Task                          | Functional            | Pythonic (preferred)        |
#   |-------------------------------|-----------------------|-----------------------------|
#   | Transform elements            | map(f, lst)           | [f(x) for x in lst]        |
#   | Filter elements               | filter(f, lst)        | [x for x in lst if f(x)]   |
#   | Accumulate to one value       | reduce(f, lst)        | sum() / math.prod() / loop |
#   | Sort by key                   | sorted(lst, key=f)    | sorted(lst, key=f) — same  |
#   | Check condition               | any/all               | any/all — same              |
#
#   Rule of thumb:
#   - Use list comprehensions over map/filter (more Pythonic)
#   - Use lambda only for short, obvious one-liners
#   - Use sorted(key=...) freely — it's idiomatic
#   - Avoid complex reduce — use a simple loop instead
