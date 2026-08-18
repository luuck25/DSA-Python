"""
=============================================================================
  PYTHON vs JAVA — Complete Comparison for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# HOW THEY RUN CODE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Java:   Source.java → javac → Source.class (bytecode) → JVM executes
#   Python: app.py → python → app.cpython-313.pyc (cached) → PVM executes
#
#   Java:   compile step is EXPLICIT and SEPARATE (you ship .class files)
#   Python: compile step is HIDDEN and AUTOMATIC (you ship .py source)


# ═══════════════════════════════════════════════════════════════════════════
# SIDE-BY-SIDE COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Aspect            | Java                              | Python                            |
#   |-------------------|-----------------------------------|-----------------------------------|
#   | Compilation       | Explicit (javac)                  | Implicit (automatic on run)       |
#   | Bytecode file     | .class                            | .pyc (in __pycache__/)            |
#   | VM                | JVM                               | CPython interpreter (PVM)         |
#   | Typing            | Static (int x = 5;)              | Dynamic (x = 5)                   |
#   | Type checked      | At compile time                   | At runtime                        |
#   | Entry point       | public static void main(...)      | if __name__ == "__main__":        |
#   | File = Class?     | Yes (one public class per file)   | No (file = module, anything)      |
#   | Imports           | import java.util.List;            | import os / from os import path   |
#   | Packaging         | .jar (zip of .class files)        | .whl / .tar.gz (pip packages)     |
#   | Build tool        | Maven / Gradle                    | pip / poetry                      |
#   | Run               | java MyClass                      | python app.py                     |
#   | REPL              | jshell (Java 9+)                  | python (built-in)                 |
#   | Memory            | GC (JVM GC)                       | GC (reference counting + GC)      |
#   | Speed             | Faster (JIT compilation)          | Slower (interpreted, no JIT)      |
#   | Semicolons        | Required ;                        | Not needed                        |
#   | Blocks            | { } braces                        | Indentation                       |
#   | Null              | null                              | None                              |
#   | OOP               | Everything in a class             | Procedural, functional, or OOP    |


# ═══════════════════════════════════════════════════════════════════════════
# THE __pycache__ FOLDER
# ═══════════════════════════════════════════════════════════════════════════
#
#   When you run python app.py, Python:
#   1. Compiles app.py → bytecode
#   2. Caches it in __pycache__/app.cpython-313.pyc
#   3. Next run: if source unchanged → skips compilation, uses cache
#
#   project/
#   ├── app.py
#   ├── utils.py
#   └── __pycache__/
#       ├── app.cpython-313.pyc
#       └── utils.cpython-313.pyc
#
#   You can safely delete __pycache__/ — it regenerates. Add to .gitignore.


# ═══════════════════════════════════════════════════════════════════════════
# JAVA NEEDS A CLASS, PYTHON DOESN'T
# ═══════════════════════════════════════════════════════════════════════════
#
#   Java:
#       public class Hello {
#           public static void main(String[] args) {
#               System.out.println("Hello");
#           }
#       }
#
#   Python:
#       print("Hello")


# ═══════════════════════════════════════════════════════════════════════════
# COMPILE-TIME SAFETY
# ═══════════════════════════════════════════════════════════════════════════
#
#   Python has NO compile-time type checking by default.
#
#   | Scenario                 | Java                    | Python                     |
#   |--------------------------|-------------------------|----------------------------|
#   | int x = "hello";         | Compiler error          | x = "hello" — no error     |
#   | Wrong type to function   | Caught at compile time  | Crashes at RUNTIME         |
#   | Misspelled variable      | Compiler error          | Fails when line executes   |
#
#   Optional static checking tools:
#       Type hints:  def add(a: int) -> int:   (Python IGNORES at runtime)
#       mypy:        static checker — run before execution
#       Pylance:     real-time checking in VS Code
#       pyright:     another static checker (Pylance uses it)


# ═══════════════════════════════════════════════════════════════════════════
# PLATFORM INDEPENDENCE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Both are platform-independent for pure code:
#       Java:   ships BYTECODE → needs JVM on target
#       Python: ships SOURCE → needs Python interpreter on target
#
#   Where Python breaks portability:
#       • C extensions (numpy compiled modules) — OS-specific binaries
#       • OS-specific calls (os.fork() = Linux only)
#       • Path separators — use pathlib or os.path.join() to stay portable


# ═══════════════════════════════════════════════════════════════════════════
# 1. MEMORY MANAGEMENT & MUTABILITY
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Concept            | Java                              | Python                          |
#   |--------------------|-----------------------------------|---------------------------------|
#   | Primitives         | int, char on stack (value types)  | No primitives — everything obj  |
#   | Pass by?           | Value (prim) / Ref copy (objects) | Pass by object reference        |
#   | Strings mutable?   | No (immutable)                    | No (immutable)                  |

# GOTCHA: Mutable default argument
def add_item_bad(item, lst=[]):    # ⚠️ same list reused across calls!
    lst.append(item)
    return lst

# add_item_bad(1)   # [1]
# add_item_bad(2)   # [1, 2] — NOT [2]! The list persists.

# Fix:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# ═══════════════════════════════════════════════════════════════════════════
# 2. == vs is
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Operator | Java                              | Python                          |
#   |----------|-----------------------------------|---------------------------------|
#   | ==       | Value (prim) / Reference (objects) | Always VALUE (__eq__)           |
#   | is       | N/A                               | IDENTITY (same object in memory)|

a = [1, 2, 3]
b = [1, 2, 3]
# a == b    → True  (same content)
# a is b    → False (different objects)

# Integer caching trap:
# x = 256; y = 256  → x is y = True  (Python caches -5 to 256)
# x = 257; y = 257  → x is y = False (outside cache range)


# ═══════════════════════════════════════════════════════════════════════════
# 3. MULTIPLE INHERITANCE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Java:   Single inheritance only (+ interfaces)
#   Python: Multiple inheritance allowed, diamond problem solved via MRO

class A:
    def greet(self): return "A"

class B(A):
    def greet(self): return "B"

class C(A):
    def greet(self): return "C"

class D(B, C):     # multiple inheritance
    pass

# D().greet()      → "B" — MRO: D → B → C → A
# print(D.__mro__) → shows resolution order


# ═══════════════════════════════════════════════════════════════════════════
# 4. ACCESS MODIFIERS (ENCAPSULATION)
# ═══════════════════════════════════════════════════════════════════════════
#
#   Java:   private, protected, public (ENFORCED by compiler)
#   Python: Convention only — NOTHING is truly private

class Account:
    def __init__(self):
        self.public = 1        # anyone can access
        self._protected = 2    # "please don't touch" (convention)
        self.__private = 3     # name-mangled → _Account__private

# a = Account()
# a.__private            → AttributeError!
# a._Account__private    → 3 — still accessible if you try hard

# Interview answer: Python has no real encapsulation — __ is just
# name-mangling, not security.


# ═══════════════════════════════════════════════════════════════════════════
# 5. GIL (GLOBAL INTERPRETER LOCK)
# ═══════════════════════════════════════════════════════════════════════════
#
#   Java:   True multi-threading — threads run in parallel
#   Python: GIL allows only ONE thread to execute bytecode at a time
#
#   CPU-bound → threads DON'T help (GIL blocks parallelism)
#   I/O-bound → threads DO help (GIL released during I/O waits)
#
#   For CPU parallelism → use multiprocessing (separate processes)
#
#   import multiprocessing
#
#   Interview trap: "Is Python multi-threaded?"
#   → Yes, but CPU-bound threads don't run in parallel due to GIL.
#     Use multiprocessing for true parallelism.


# ═══════════════════════════════════════════════════════════════════════════
# 6. ITERATORS & GENERATORS (Python-specific)
# ═══════════════════════════════════════════════════════════════════════════
#
#   Java has Iterator interface. Python has generators — much simpler:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a           # pauses here, resumes on next()
        a, b = b, a + b

# fib = fibonacci()
# next(fib)   → 0
# next(fib)   → 1
# next(fib)   → 1
# Infinite sequence with O(1) memory!

# Interview point: Generators are memory-efficient for large/infinite sequences.
# Java equivalent requires explicit Iterator class with state.


# ═══════════════════════════════════════════════════════════════════════════
# 7. DUCK TYPING vs INTERFACES
# ═══════════════════════════════════════════════════════════════════════════
#
#   Java:   Must implement interface explicitly
#   Python: "If it walks like a duck..." — only methods matter, not types

def get_length(obj):
    return len(obj)       # works on list, str, dict, tuple — anything with __len__

# get_length([1, 2, 3])   → 3
# get_length("hello")     → 5
# get_length({"a": 1})    → 1
# No interface declaration needed


# ═══════════════════════════════════════════════════════════════════════════
# 8. EVERYTHING IS AN OBJECT
# ═══════════════════════════════════════════════════════════════════════════

# Functions are objects:
def greet(): return "hi"
funcs = [greet, len, print]       # store in a list
# funcs[0]()                      → "hi"

# Classes are objects:
classes = [int, str, list]
# classes[2]([1, 2, 3])           → creates a list

# Java: functions aren't first-class (need lambda/functional interfaces since Java 8)


# ═══════════════════════════════════════════════════════════════════════════
# 9. SHALLOW vs DEEP COPY
# ═══════════════════════════════════════════════════════════════════════════

import copy

a_list = [[1, 2], [3, 4]]
b_list = a_list.copy()              # shallow — inner lists are SHARED
# b_list[0].append(99)
# a_list → [[1, 2, 99], [3, 4]]    — a is affected!

c_list = copy.deepcopy(a_list)      # deep — completely independent
# c_list[0].append(100)
# a_list → unchanged


# ═══════════════════════════════════════════════════════════════════════════
# 10. QUICK-FIRE INTERVIEW ANSWERS
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Question                                    | Answer                                                        |
#   |---------------------------------------------|---------------------------------------------------------------|
#   | Compiled or interpreted?                    | Both — compiled to bytecode, then interpreted by PVM          |
#   | Strongly typed?                             | Yes (can't do "3" + 3) — but DYNAMICALLY typed               |
#   | List vs tuple?                              | List = mutable, tuple = immutable (& hashable → dict key)     |
#   | How is dict implemented?                    | Hash table (O(1) avg lookup)                                  |
#   | What's a decorator?                         | Function that wraps another (sugar for func = decorator(func))|
#   | *args and **kwargs?                         | *args = tuple of positional, **kwargs = dict of keyword args  |
#   | List vs Generator?                          | List stores all in memory; generator yields one at a time     |
#   | What's GIL?                                 | Only one thread runs Python bytecode at a time (CPython)      |
#   | How to achieve parallelism?                 | multiprocessing (processes) or asyncio (I/O-bound)            |
#   | Is Python pass-by-value or reference?       | Pass by object reference (like Java's object passing)         |
#   | What makes something hashable?              | Immutable + has __hash__ (int, str, tuple — NOT list, dict)   |
#   | What's the difference between is and ==?    | is = identity (same object), == = equality (same value)       |
