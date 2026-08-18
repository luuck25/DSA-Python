"""
=============================================================================
  EXCEPTION HANDLING IN PYTHON — Complete Guide
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. BASIC try / except
# ═══════════════════════════════════════════════════════════════════════════

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")          # this runs


# ═══════════════════════════════════════════════════════════════════════════
# 2. MULTIPLE except blocks
# ═══════════════════════════════════════════════════════════════════════════

try:
    nums = [1, 2, 3]
    print(nums[10])
except IndexError:
    print("Index out of range")
except TypeError:
    print("Type error")
except Exception as e:                     # catch-all (last resort)
    print(f"Something went wrong: {e}")


# ═══════════════════════════════════════════════════════════════════════════
# 3. MULTIPLE exceptions in one line
# ═══════════════════════════════════════════════════════════════════════════

try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"Conversion failed: {e}")


# ═══════════════════════════════════════════════════════════════════════════
# 4. else — runs ONLY if NO exception occurred
# ═══════════════════════════════════════════════════════════════════════════

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success: {result}")            # runs because no error


# ═══════════════════════════════════════════════════════════════════════════
# 5. finally — ALWAYS runs (cleanup)
# ═══════════════════════════════════════════════════════════════════════════

try:
    f = open("test.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs")              # cleanup: close file, release lock, etc.
    # f.close()  — if f was opened


# ═══════════════════════════════════════════════════════════════════════════
# 6. FULL STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════
#
#   try:
#       ...risky code...
#   except SomeError as e:
#       ...handle error...
#   else:
#       ...runs if NO error...
#   finally:
#       ...ALWAYS runs (cleanup)...


# ═══════════════════════════════════════════════════════════════════════════
# 7. RAISE — throw your own exceptions
# ═══════════════════════════════════════════════════════════════════════════

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)                               # "Age cannot be negative"


# ═══════════════════════════════════════════════════════════════════════════
# 8. RE-RAISE — catch, log, then re-throw
# ═══════════════════════════════════════════════════════════════════════════

def process():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Logging error...")
        raise                              # re-raise the same exception


# ═══════════════════════════════════════════════════════════════════════════
# 9. CUSTOM EXCEPTIONS
# ═══════════════════════════════════════════════════════════════════════════

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(e)                               # "Cannot withdraw 200, balance is 100"
    print(e.balance, e.amount)             # 100 200


# ═══════════════════════════════════════════════════════════════════════════
# 10. COMMON BUILT-IN EXCEPTIONS
# ═══════════════════════════════════════════════════════════════════════════
#
#   ValueError       — wrong value (int("abc"))
#   TypeError        — wrong type (len(5))
#   IndexError       — list index out of range
#   KeyError         — dict key not found
#   AttributeError   — object has no attribute
#   FileNotFoundError— file doesn't exist
#   ZeroDivisionError— divide by zero
#   StopIteration    — iterator exhausted
#   ImportError      — module not found
#   RuntimeError     — generic runtime error
#   OverflowError    — number too large
#   RecursionError   — max recursion depth exceeded


# ═══════════════════════════════════════════════════════════════════════════
# 11. EXCEPTION HIERARCHY (simplified)
# ═══════════════════════════════════════════════════════════════════════════
#
#   BaseException
#   ├── SystemExit
#   ├── KeyboardInterrupt
#   └── Exception              ← catch this for "normal" errors
#       ├── ValueError
#       ├── TypeError
#       ├── KeyError
#       ├── IndexError
#       ├── FileNotFoundError
#       ├── ZeroDivisionError
#       ├── AttributeError
#       ├── RuntimeError
#       └── ...
#
# ⚠️ Never catch BaseException — it swallows Ctrl+C and sys.exit()


# ═══════════════════════════════════════════════════════════════════════════
# 12. PRACTICAL PATTERNS
# ═══════════════════════════════════════════════════════════════════════════

# --- EAFP (Easier to Ask Forgiveness than Permission) — Pythonic ---
# Try it, handle failure. Preferred over checking first.

d = {"a": 1}
try:
    val = d["b"]
except KeyError:
    val = "default"

# vs LBYL (Look Before You Leap) — less Pythonic
val = d["b"] if "b" in d else "default"


# --- dict.get() avoids try/except for simple defaults ---
val = d.get("b", "default")               # same result, cleanest


# --- Context managers (with) — auto-cleanup, no finally needed ---
try:
    with open("data.txt") as f:
        data = f.read()
except FileNotFoundError:
    data = ""
# file auto-closed even if exception occurs inside `with`


# --- assert — debugging only (removed with python -O) ---
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b


# ═══════════════════════════════════════════════════════════════════════════
# 13. INTERVIEW TIPS
# ═══════════════════════════════════════════════════════════════════════════
#
# • Use specific exceptions, not bare `except:` (catches everything incl Ctrl+C)
# • `else` = "no error happened" — keeps try block minimal
# • `finally` = cleanup (close files, release locks) — runs even if return/break
# • EAFP > LBYL in Python (try first, handle failure)
# • Custom exceptions: inherit from Exception, add useful attributes
# • raise without args inside except → re-raises the caught exception
