"""
=============================================================================
  *args, **kwargs & UNPACKING — Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. *args — VARIABLE POSITIONAL ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Collects extra positional arguments into a TUPLE.

def add(*args):
    print(type(args))       # <class 'tuple'>
    return sum(args)

# add(1, 2, 3)       → 6
# add(10, 20)        → 30
# add()              → 0 (empty tuple)

# "args" is just a convention — any name works:
def multiply(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 2. **kwargs — VARIABLE KEYWORD ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Collects extra keyword arguments into a DICT.

def build_profile(**kwargs):
    print(type(kwargs))     # <class 'dict'>
    return kwargs

# build_profile(name="Alice", age=30, city="NYC")
# → {"name": "Alice", "age": 30, "city": "NYC"}


# ═══════════════════════════════════════════════════════════════════════════
# 3. COMBINING THEM — THE ORDER MATTERS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Order: regular → *args → keyword-only → **kwargs
#
#   def func(a, b, *args, key_only, **kwargs):

def example(name, *args, separator=" ", **kwargs):
    print(f"name: {name}")
    print(f"args: {args}")
    print(f"separator: {separator}")
    print(f"kwargs: {kwargs}")

# example("Alice", 1, 2, 3, separator="-", age=30, city="NYC")
# name: Alice
# args: (1, 2, 3)
# separator: -
# kwargs: {'age': 30, 'city': 'NYC'}


# ═══════════════════════════════════════════════════════════════════════════
# 4. UNPACKING — SPREADING INTO FUNCTION CALLS
# ═══════════════════════════════════════════════════════════════════════════

def greet(first, last, greeting="Hello"):
    return f"{greeting}, {first} {last}!"

# Unpack a list/tuple with *
names = ["John", "Doe"]
# greet(*names)                    → "Hello, John Doe!"

# Unpack a dict with **
info = {"first": "Jane", "last": "Smith", "greeting": "Hi"}
# greet(**info)                    → "Hi, Jane Smith!"

# Java has nothing like this — you'd pass arrays/maps explicitly.


# ═══════════════════════════════════════════════════════════════════════════
# 5. UNPACKING IN ASSIGNMENTS
# ═══════════════════════════════════════════════════════════════════════════

# Basic unpacking
a, b, c = [1, 2, 3]              # a=1, b=2, c=3

# Star unpacking (catch-all)
first, *rest = [1, 2, 3, 4, 5]   # first=1, rest=[2,3,4,5]
*start, last = [1, 2, 3, 4, 5]   # start=[1,2,3,4], last=5
first, *mid, last = [1, 2, 3, 4] # first=1, mid=[2,3], last=4

# Swap without temp variable
x, y = 10, 20
x, y = y, x                      # x=20, y=10

# Ignore values with _
_, second, _ = (1, 2, 3)         # only need second


# ═══════════════════════════════════════════════════════════════════════════
# 6. UNPACKING IN DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════

# Merge lists
a_list = [1, 2, 3]
b_list = [4, 5, 6]
merged = [*a_list, *b_list]          # [1, 2, 3, 4, 5, 6]

# Merge dicts (Python 3.9+ also has |)
defaults = {"color": "blue", "size": 10}
custom = {"size": 20, "weight": 5}
final = {**defaults, **custom}       # {"color": "blue", "size": 20, "weight": 5}
# Later dict wins on conflicts

# Python 3.9+ dict merge:
# final = defaults | custom          # same result


# ═══════════════════════════════════════════════════════════════════════════
# 7. KEYWORD-ONLY ARGUMENTS (after *)
# ═══════════════════════════════════════════════════════════════════════════

def connect(host, port, *, timeout=30, retries=3):
    # timeout and retries MUST be passed as keywords
    pass

# connect("localhost", 8080, timeout=10)     ✓
# connect("localhost", 8080, 10)             ✗ TypeError!

# Bare * forces everything after it to be keyword-only.
# Useful for API clarity — prevents positional mistakes.


# ═══════════════════════════════════════════════════════════════════════════
# 8. POSITIONAL-ONLY ARGUMENTS (before /) — Python 3.8+
# ═══════════════════════════════════════════════════════════════════════════

def divide(a, b, /):
    return a / b

# divide(10, 2)          ✓
# divide(a=10, b=2)      ✗ TypeError! Cannot use as keyword.

# Full syntax:
def full(pos_only, /, normal, *, kw_only):
    pass
# pos_only: positional only
# normal: either way
# kw_only: keyword only


# ═══════════════════════════════════════════════════════════════════════════
# 9. REAL-WORLD PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

# --- Decorator that passes through all args ---
def log_calls(func):
    def wrapper(*args, **kwargs):       # accept anything
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)    # forward everything
    return wrapper

@log_calls
def add_two(a, b):
    return a + b

# --- Factory with defaults ---
def create_user(name, **defaults):
    user = {"name": name, "role": "viewer", "active": True}
    user.update(defaults)               # override defaults
    return user

# create_user("Alice", role="admin")  → {"name": "Alice", "role": "admin", "active": True}


# ═══════════════════════════════════════════════════════════════════════════
# 10. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What's *args?
#   A: Collects variable positional arguments into a tuple.
#
#   Q: What's **kwargs?
#   A: Collects variable keyword arguments into a dict.
#
#   Q: What's the parameter order?
#   A: (positional, *args, keyword-only, **kwargs)
#
#   Q: Difference between * in def vs call?
#   A: In def: collects. In call: unpacks/spreads.
#
#   Q: Can you unpack a dict into another dict?
#   A: Yes: {**dict1, **dict2} — later keys win.
#
#   Q: What does / mean in parameters?
#   A: Everything before / is positional-only (Python 3.8+).
