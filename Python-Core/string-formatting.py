"""
=============================================================================
  STRING FORMATTING IN PYTHON — All Methods
=============================================================================
"""

name = "Alice"
age = 30
price = 3.14159


# ═══════════════════════════════════════════════════════════════════════════
# 1. f-string (Python 3.6+) — PREFERRED
# ═══════════════════════════════════════════════════════════════════════════
# Inline expressions inside {}, evaluated at runtime.

print(f"Hello {name}, age {age}")          # Hello Alice, age 30
print(f"{age * 2}")                         # 60 — expressions allowed
print(f"{price:.2f}")                       # 3.14 — 2 decimal places
print(f"{age:05d}")                         # 00030 — zero-padded 5 digits
print(f"{'hi':>10}")                        # "        hi" — right-align 10 chars
print(f"{'hi':<10}")                        # "hi        " — left-align
print(f"{'hi':^10}")                        # "    hi    " — center-align


# ═══════════════════════════════════════════════════════════════════════════
# 2. .format() method
# ═══════════════════════════════════════════════════════════════════════════
# Placeholders {} filled by .format() arguments.

print("Hello {}, age {}".format(name, age))           # positional
print("Hello {0}, age {1}".format(name, age))         # indexed
print("Hello {n}, age {a}".format(n=name, a=age))     # named
print("{:.2f}".format(price))                          # 3.14
print("{:,}".format(1000000))                          # 1,000,000 — comma separator


# ═══════════════════════════════════════════════════════════════════════════
# 3. % operator (old style — like C's printf)
# ═══════════════════════════════════════════════════════════════════════════
# %s = string, %d = int, %f = float

print("Hello %s, age %d" % (name, age))    # Hello Alice, age 30
print("Price: %.2f" % price)                # Price: 3.14
print("%05d" % 42)                          # 00042 — zero-padded
print("%-10s|" % "hi")                      # "hi        |" — left-align


# ═══════════════════════════════════════════════════════════════════════════
# 4. str.join() — for combining lists/iterables
# ═══════════════════════════════════════════════════════════════════════════
# separator.join(iterable_of_strings)

print(", ".join(["a", "b", "c"]))                   # a, b, c
print(", ".join(str(x) for x in [1, 2, 3]))         # 1, 2, 3
print(" -> ".join(["start", "middle", "end"]))      # start -> middle -> end

# ⚠️ join only works on strings — use str(x) or map(str, list) for non-strings
print(", ".join(map(str, [10, 20, 30])))            # 10, 20, 30


# ═══════════════════════════════════════════════════════════════════════════
# 5. String concatenation (+) — avoid for multiple parts
# ═══════════════════════════════════════════════════════════════════════════

print("Hello " + name + ", age " + str(age))   # must manually str() non-strings
# Slow for many pieces — creates new string each time


# ═══════════════════════════════════════════════════════════════════════════
# 6. Template strings (from string module) — rare, safe for user input
# ═══════════════════════════════════════════════════════════════════════════

from string import Template
t = Template("Hello $name, age $age")
print(t.substitute(name="Alice", age=30))      # Hello Alice, age 30
# Won't execute arbitrary code — safe for untrusted templates


# ═══════════════════════════════════════════════════════════════════════════
# COMMON FORMAT SPECS (work in f-strings and .format())
# ═══════════════════════════════════════════════════════════════════════════
#
#   {value:spec}
#
#   .2f     → 2 decimal float          3.14159 → "3.14"
#   .0f     → no decimals              3.14    → "3"
#   ,       → thousands separator      1000000 → "1,000,000"
#   05d     → zero-pad to 5 digits     42      → "00042"
#   >10     → right-align in 10 chars  "hi"    → "        hi"
#   <10     → left-align in 10 chars   "hi"    → "hi        "
#   ^10     → center in 10 chars       "hi"    → "    hi    "
#   +       → always show sign         42      → "+42"
#   b       → binary                   10      → "1010"
#   x       → hex                      255     → "ff"
#   e       → scientific notation      1500    → "1.500000e+03"
#   %       → percentage               0.85    → "85.000000%"
#   .1%     → percentage 1 decimal     0.85    → "85.0%"

print(f"{255:x}")          # ff
print(f"{10:b}")           # 1010
print(f"{0.85:.1%}")       # 85.0%
print(f"{1000000:,}")      # 1,000,000
print(f"{42:+d}")          # +42
print(f"{-42:+d}")         # -42


# ═══════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE TABLE
# ═══════════════════════════════════════════════════════════════════════════
#
# | Method     | Speed   | Readability | Use when                          |
# |------------|---------|-------------|-----------------------------------|
# | f-string   | Fastest | Best        | Always (default choice)           |
# | .format()  | Medium  | Good        | Dynamic format strings            |
# | %          | Medium  | OK          | Legacy code                       |
# | join       | Fast    | Good        | Combining lists of strings        |
# | +          | Slow    | Poor        | Avoid for multiple parts          |
# | Template   | Slow    | OK          | Untrusted user input (safe)       |
#
# TL;DR: Use f-strings for everything unless you have a reason not to.
