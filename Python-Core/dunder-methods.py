"""
=============================================================================
  DUNDER (DOUBLE UNDERSCORE) METHODS & SPECIAL ATTRIBUTES IN PYTHON
=============================================================================
  "dunder" = double underscore = __name__
  Python uses these as hooks — you define them, Python calls them automatically.
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. __name__ — Module Identity
# ═══════════════════════════════════════════════════════════════════════════
# Python sets this automatically for every file/module.
#
#   Run directly:  python app.py    → __name__ = "__main__"
#   Imported:      import app       → __name__ = "app"
#
# Use it to guard test/demo code:

def add(a, b):
    return a + b

if __name__ == "__main__":
    # Only runs when this file is executed directly, NOT when imported
    print(add(2, 3))


# ═══════════════════════════════════════════════════════════════════════════
# 2. __init__ — Constructor (Object Initialization)
# ═══════════════════════════════════════════════════════════════════════════
# Called automatically when you create an object.

class Dog:
    def __init__(self, name, age):       # Python calls this on Dog("Rex", 3)
        self.name = name                 # set instance attributes
        self.age = age

d = Dog("Rex", 3)                        # __init__ runs here
print(d.name)                            # "Rex"


# ═══════════════════════════════════════════════════════════════════════════
# 3. __str__ vs __repr__ — String Representations
# ═══════════════════════════════════════════════════════════════════════════
#
#   __str__  → for end users (print, str())     — "human friendly"
#   __repr__ → for developers (REPL, debugging) — "unambiguous, ideally eval-able"

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):                   # print(p) or str(p)
        return f"({self.x}, {self.y})"

    def __repr__(self):                  # repr(p) or in REPL
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(p)                                 # calls __str__ → "(3, 4)"
print(repr(p))                           # calls __repr__ → "Point(3, 4)"
# If __str__ is missing, Python falls back to __repr__


# ═══════════════════════════════════════════════════════════════════════════
# 4. __len__, __getitem__, __contains__ — Make Objects Behave Like Collections
# ═══════════════════════════════════════════════════════════════════════════

class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):                   # len(playlist)
        return len(self.songs)

    def __getitem__(self, index):        # playlist[0]
        return self.songs[index]

    def __contains__(self, song):        # "song" in playlist
        return song in self.songs

pl = Playlist()
pl.add("Song A")
pl.add("Song B")
print(len(pl))                           # 2  — calls __len__
print(pl[0])                             # "Song A" — calls __getitem__
print("Song A" in pl)                    # True — calls __contains__


# ═══════════════════════════════════════════════════════════════════════════
# 5. __eq__, __lt__, __le__ — Comparison Operators
# ═══════════════════════════════════════════════════════════════════════════

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):             # s1 == s2
        return self.grade == other.grade

    def __lt__(self, other):             # s1 < s2 (also enables sorted())
        return self.grade < other.grade

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)
print(s1 == s2)                          # False
print(s2 < s1)                           # True (85 < 90)
print(sorted([s1, s2], key=lambda s: s.grade))  # works because __lt__ defined


# ═══════════════════════════════════════════════════════════════════════════
# 6. __add__, __mul__ — Arithmetic Operators
# ═══════════════════════════════════════════════════════════════════════════

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):            # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):           # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

v = Vector(1, 2) + Vector(3, 4)         # __add__ → Vector(4, 6)
print(v)                                 # (4, 6)
print(Vector(2, 3) * 5)                  # (10, 15)


# ═══════════════════════════════════════════════════════════════════════════
# 7. __call__ — Make Object Callable Like a Function
# ═══════════════════════════════════════════════════════════════════════════

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):               # obj(x) — treat object as function
        return x * self.factor

double = Multiplier(2)
print(double(5))                         # 10 — calls __call__(5)
print(double(100))                       # 200


# ═══════════════════════════════════════════════════════════════════════════
# 8. __iter__ and __next__ — Make Object Iterable
# ═══════════════════════════════════════════════════════════════════════════

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):                  # for x in obj
        return self

    def __next__(self):                  # next(obj)
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in Countdown(3):                 # 3, 2, 1
    print(num)


# ═══════════════════════════════════════════════════════════════════════════
# 9. __enter__ and __exit__ — Context Manager (with statement)
# ═══════════════════════════════════════════════════════════════════════════

class Timer:
    import time

    def __enter__(self):                 # called at `with Timer() as t:`
        self.start = self.time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # called when `with` block ends
        elapsed = self.time.time() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False                     # don't suppress exceptions

# Usage:
# with Timer():
#     do_something_slow()
# → prints "Elapsed: 0.1234s"


# ═══════════════════════════════════════════════════════════════════════════
# 10. __slots__ — Memory Optimization
# ═══════════════════════════════════════════════════════════════════════════
# Prevents creation of __dict__ per instance → saves memory for many objects.

class PointSlots:
    __slots__ = ['x', 'y']               # only x, y allowed — no dynamic attrs

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = PointSlots(1, 2)
# p.z = 3  → AttributeError! (can't add new attributes)


# ═══════════════════════════════════════════════════════════════════════════
# 11. __dict__ — Object's Attribute Dictionary
# ═══════════════════════════════════════════════════════════════════════════

class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

c = Car("Toyota", 2020)
print(c.__dict__)                        # {'make': 'Toyota', 'year': 2020}
# Useful for serialization, debugging, or dynamic access


# ═══════════════════════════════════════════════════════════════════════════
# 12. __class__ and type() — Object's Type
# ═══════════════════════════════════════════════════════════════════════════

print(c.__class__)                       # <class '__main__.Car'>
print(type(c))                           # same thing
print(type(c).__name__)                  # "Car"


# ═══════════════════════════════════════════════════════════════════════════
# 13. __doc__ — Docstring Access
# ═══════════════════════════════════════════════════════════════════════════

def greet(name):
    """Say hello to someone."""
    return f"Hello {name}"

print(greet.__doc__)                     # "Say hello to someone."


# ═══════════════════════════════════════════════════════════════════════════
# COMPLETE DUNDER CHEAT SHEET
# ═══════════════════════════════════════════════════════════════════════════
#
# | Dunder              | Triggered by              | Purpose                    |
# |---------------------|---------------------------|----------------------------|
# | __init__(self)      | MyClass()                 | Constructor                |
# | __str__(self)       | print(obj), str(obj)      | Human-readable string      |
# | __repr__(self)      | repr(obj), REPL           | Developer string           |
# | __len__(self)       | len(obj)                  | Length                     |
# | __getitem__(self,k) | obj[k]                    | Index/key access           |
# | __setitem__(self,k) | obj[k] = v                | Index/key assignment       |
# | __contains__(self)  | x in obj                  | Membership test            |
# | __eq__(self,other)  | obj == other              | Equality                   |
# | __lt__(self,other)  | obj < other               | Less than (enables sort)   |
# | __add__(self,other) | obj + other               | Addition                   |
# | __mul__(self,other) | obj * other               | Multiplication             |
# | __call__(self)      | obj()                     | Callable object            |
# | __iter__(self)      | for x in obj              | Iterator protocol          |
# | __next__(self)      | next(obj)                 | Next item in iteration     |
# | __enter__/__exit__  | with obj:                 | Context manager            |
# | __hash__(self)      | hash(obj), dict key       | Hashability                |
# | __bool__(self)      | if obj:                   | Truthiness                 |
# | __del__(self)       | del obj / garbage collect | Destructor (rarely used)   |
#
# SPECIAL ATTRIBUTES (not methods):
# | __name__            | module/function name      |
# | __dict__            | object's attribute dict   |
# | __class__           | object's class            |
# | __doc__             | docstring                 |
# | __slots__           | restrict allowed attrs    |
# | __file__            | module's file path        |
