"""
=============================================================================
  CLOSURES & SCOPE (LEGB) — Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. LEGB RULE — VARIABLE LOOKUP ORDER
# ═══════════════════════════════════════════════════════════════════════════
#
#   When Python sees a variable name, it searches in this order:
#
#   L — Local:      inside the current function
#   E — Enclosing:  inside enclosing (outer) functions
#   G — Global:     module-level (top of file)
#   B — Built-in:   Python built-ins (len, print, range...)
#
#   First match wins. If not found anywhere → NameError.

x = "global"                          # G — Global

def outer():
    x = "enclosing"                   # E — Enclosing

    def inner():
        x = "local"                   # L — Local
        print(x)                      # → "local" (L wins)

    inner()

# outer()  → "local"

# If we remove x="local" from inner():  → "enclosing" (E)
# If we also remove x="enclosing":      → "global" (G)
# If we also remove x="global":         → NameError


# ═══════════════════════════════════════════════════════════════════════════
# 2. global KEYWORD — MODIFY MODULE-LEVEL VARIABLE
# ═══════════════════════════════════════════════════════════════════════════

counter = 0

def increment():
    global counter         # without this, counter would be treated as local
    counter += 1

# increment()
# increment()
# counter  → 2

# Without `global`:
# def increment():
#     counter += 1         → UnboundLocalError!
#     # Python sees assignment → assumes local → but local doesn't exist yet


# ═══════════════════════════════════════════════════════════════════════════
# 3. nonlocal KEYWORD — MODIFY ENCLOSING VARIABLE
# ═══════════════════════════════════════════════════════════════════════════

def make_counter():
    count = 0

    def increment():
        nonlocal count     # modify the enclosing variable
        count += 1
        return count

    return increment

# counter = make_counter()
# counter()  → 1
# counter()  → 2
# counter()  → 3

# Without `nonlocal`:
# count += 1  → UnboundLocalError (same as global issue)

# Java equivalent: effectively final variables in lambdas (can't modify!)
# Python is more flexible — nonlocal allows modification.


# ═══════════════════════════════════════════════════════════════════════════
# 4. CLOSURES — FUNCTION + ITS ENCLOSING SCOPE
# ═══════════════════════════════════════════════════════════════════════════
#
#   A closure is a function that "remembers" variables from its enclosing scope,
#   even after the outer function has returned.

def multiplier(factor):
    def multiply(x):
        return x * factor      # factor is "closed over"
    return multiply

double = multiplier(2)         # factor=2 is captured
triple = multiplier(3)         # factor=3 is captured

# double(5)  → 10
# triple(5)  → 15

# The inner function carries a reference to `factor` — it's not copied.
# double.__closure__[0].cell_contents  → 2


# ═══════════════════════════════════════════════════════════════════════════
# 5. CLOSURE TRAP — LATE BINDING IN LOOPS
# ═══════════════════════════════════════════════════════════════════════════

# WRONG — all functions share the same `i`:
functions = []
for i in range(5):
    functions.append(lambda: i)

# [f() for f in functions]  → [4, 4, 4, 4, 4]  ⚠️ NOT [0,1,2,3,4]!
# Why: lambda captures REFERENCE to i, not the VALUE. After loop, i=4.

# FIX 1: default argument (captures value at creation time)
functions_fixed = []
for i in range(5):
    functions_fixed.append(lambda i=i: i)     # i=i binds current value
# [f() for f in functions_fixed]  → [0, 1, 2, 3, 4] ✓

# FIX 2: factory function
def make_func(n):
    return lambda: n

functions_fixed2 = [make_func(i) for i in range(5)]
# [f() for f in functions_fixed2]  → [0, 1, 2, 3, 4] ✓


# ═══════════════════════════════════════════════════════════════════════════
# 6. CLOSURES AS LIGHTWEIGHT OBJECTS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Closures can replace simple classes that just hold state:

# Class approach:
class Averager:
    def __init__(self):
        self.numbers = []

    def __call__(self, new_value):
        self.numbers.append(new_value)
        return sum(self.numbers) / len(self.numbers)

# Closure approach (lighter):
def make_averager():
    numbers = []

    def averager(new_value):
        numbers.append(new_value)       # mutating list — no nonlocal needed!
        return sum(numbers) / len(numbers)

    return averager

# avg = make_averager()
# avg(10)  → 10.0
# avg(20)  → 15.0
# avg(30)  → 20.0

# Note: appending to a list doesn't reassign the variable → no nonlocal needed.
# But: count += 1 DOES reassign → needs nonlocal.


# ═══════════════════════════════════════════════════════════════════════════
# 7. SCOPE IN COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════════

# List comprehension has its OWN scope (Python 3+):
x = 10
result = [x for x in range(5)]
# x is still 10! (comprehension variable doesn't leak)

# Python 2: x would be 4 (leaked into enclosing scope)

# But walrus operator (:=) DOES leak:
# [y := x for x in range(5)]
# y is now 4 (walrus assigns to enclosing scope)


# ═══════════════════════════════════════════════════════════════════════════
# 8. COMMON GOTCHAS
# ═══════════════════════════════════════════════════════════════════════════

# --- GOTCHA 1: Assignment creates local variable ---
x = 100
def test():
    # print(x)        → UnboundLocalError!
    x = 200           # this makes x LOCAL for entire function
    print(x)

# Python decides scope at COMPILE time (when parsing the function).
# If any assignment to x exists in function body → x is local everywhere in it.

# --- GOTCHA 2: Mutable objects don't need global/nonlocal ---
data = [1, 2, 3]
def modify():
    data.append(4)    # works! We're not reassigning `data`, just mutating it.
# modify()
# data → [1, 2, 3, 4]

# But this fails:
# def replace():
#     data = [5, 6]   # creates NEW local `data`, doesn't touch global


# ═══════════════════════════════════════════════════════════════════════════
# 9. DECORATORS ARE CLOSURES!
# ═══════════════════════════════════════════════════════════════════════════

import functools

def timer(func):                       # outer — takes func
    @functools.wraps(func)
    def wrapper(*args, **kwargs):      # inner — closes over func
        import time
        start = time.time()
        result = func(*args, **kwargs) # func is "remembered" via closure
        print(f"{time.time() - start:.4f}s")
        return result
    return wrapper

# Every decorator is a closure:
# - outer function receives the decorated function
# - inner function (wrapper) captures it via closure
# - returned wrapper replaces the original function


# ═══════════════════════════════════════════════════════════════════════════
# 10. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What is LEGB?
#   A: Variable lookup order: Local → Enclosing → Global → Built-in.
#
#   Q: What is a closure?
#   A: A function that captures variables from its enclosing scope.
#
#   Q: global vs nonlocal?
#   A: global = module-level variable. nonlocal = enclosing function variable.
#
#   Q: Why do I get UnboundLocalError?
#   A: You assigned to a variable somewhere in the function, making it local.
#      Python decides scope at parse time, not runtime.
#
#   Q: The loop-lambda trap?
#   A: Lambdas in loops share the SAME loop variable (late binding).
#      Fix: default argument lambda i=i: i.
#
#   Q: Do you need nonlocal to append to a list?
#   A: No. Mutation (append) doesn't reassign. Only reassignment (=) needs it.
