"""
=============================================================================
  DATACLASSES — Complete Guide for Interviews
=============================================================================
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List


# ═══════════════════════════════════════════════════════════════════════════
# 1. THE PROBLEM — BOILERPLATE IN REGULAR CLASSES
# ═══════════════════════════════════════════════════════════════════════════

# Without dataclass — lots of repetitive code:
class PointOld:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointOld(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# With dataclass — all auto-generated:
@dataclass
class Point:
    x: float
    y: float

# Point auto-generates: __init__, __repr__, __eq__
# p = Point(1.0, 2.0)
# repr(p)              → "Point(x=1.0, y=2.0)"
# Point(1, 2) == Point(1, 2)  → True


# ═══════════════════════════════════════════════════════════════════════════
# 2. FEATURES — WHAT @dataclass GENERATES
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Generated        | Default | Flag to control         |
#   |------------------|---------|-------------------------|
#   | __init__         | Yes     | init=False to disable   |
#   | __repr__         | Yes     | repr=False to disable   |
#   | __eq__           | Yes     | eq=False to disable     |
#   | __hash__         | No*     | frozen=True enables it  |
#   | __lt__,__gt__... | No      | order=True enables it   |
#
#   * __hash__ is set to None if eq=True and frozen=False (mutable + eq = unhashable)


# ═══════════════════════════════════════════════════════════════════════════
# 3. DEFAULT VALUES & field()
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Student:
    name: str
    age: int = 18                           # simple default
    grades: List[int] = field(default_factory=list)  # mutable default!

# WHY field(default_factory=list)?
# Same reason as the "mutable default argument" trap:
# grades: List[int] = []   → SHARED across all instances! ⚠️
# field(default_factory=list) → creates NEW list for each instance ✓

# Other field() options:
# field(repr=False)          → exclude from __repr__
# field(compare=False)       → exclude from __eq__
# field(init=False)          → exclude from __init__ (set in __post_init__)


# ═══════════════════════════════════════════════════════════════════════════
# 4. __post_init__ — COMPUTED FIELDS
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)    # not in constructor

    def __post_init__(self):
        """Called after __init__. Use for validation or computed fields."""
        self.area = self.width * self.height

# r = Rectangle(3, 4)
# r.area  → 12.0


# ═══════════════════════════════════════════════════════════════════════════
# 5. FROZEN — IMMUTABLE DATACLASS
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class FrozenPoint:
    x: float
    y: float

# p = FrozenPoint(1, 2)
# p.x = 3   → FrozenError! Cannot modify.
# hash(p)   → works! (frozen = hashable → can use as dict key / set member)

# Java equivalent: record Point(double x, double y) {} (Java 16+)


# ═══════════════════════════════════════════════════════════════════════════
# 6. ORDER — COMPARISON OPERATORS
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

# Compares field by field (like tuple comparison):
# Version(2, 0, 0) > Version(1, 9, 9)  → True
# sorted([Version(1,2,0), Version(1,1,9)])  → [Version(1,1,9), Version(1,2,0)]

# Custom sort key with sort_index:
@dataclass(order=True)
class Employee:
    sort_index: int = field(init=False, repr=False)
    name: str
    salary: float

    def __post_init__(self):
        self.sort_index = self.salary    # sort by salary


# ═══════════════════════════════════════════════════════════════════════════
# 7. CONVERSION UTILITIES
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Config:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False

c = Config(host="prod.server.com", port=443)

# To dict:
d = asdict(c)       # {'host': 'prod.server.com', 'port': 443, 'debug': False}

# To tuple:
t = astuple(c)      # ('prod.server.com', 443, False)

# From dict:
# config = Config(**some_dict)


# ═══════════════════════════════════════════════════════════════════════════
# 8. INHERITANCE
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Animal:
    name: str
    age: int

@dataclass
class Dog(Animal):
    breed: str = "Unknown"

# d = Dog(name="Rex", age=5, breed="Labrador")
# Fields from parent come first in __init__


# ═══════════════════════════════════════════════════════════════════════════
# 9. DATACLASS vs NAMEDTUPLE vs DICT
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Feature          | dataclass       | NamedTuple      | dict            |
#   |------------------|-----------------|-----------------|-----------------|
#   | Mutable          | Yes (default)   | No              | Yes             |
#   | Type hints       | Yes             | Yes             | No              |
#   | Methods          | Yes             | Limited         | No              |
#   | Memory           | Normal          | Less (tuple)    | More (hash)     |
#   | Access           | obj.field       | obj.field / [i] | obj["key"]      |
#   | Hashable         | If frozen       | Always          | No              |
#   | Default values   | Yes             | Yes             | N/A             |
#
#   Use dataclass when: you need a class with data + possibly methods
#   Use NamedTuple when: you need immutable, lightweight, tuple-like
#   Use dict when: keys are dynamic or unknown at design time


# ═══════════════════════════════════════════════════════════════════════════
# 10. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What does @dataclass do?
#   A: Auto-generates __init__, __repr__, __eq__ from type-annotated fields.
#
#   Q: How to make it immutable?
#   A: @dataclass(frozen=True) — raises error on assignment.
#
#   Q: How to handle mutable defaults (like lists)?
#   A: field(default_factory=list) — creates new list per instance.
#
#   Q: What's __post_init__?
#   A: Called after __init__. Use for validation or computed fields.
#
#   Q: Java equivalent?
#   A: Java 16 records: record Point(int x, int y) {}
#
#   Q: When NOT to use dataclass?
#   A: When you need complex __init__ logic, or very performance-sensitive
#      code (consider __slots__ or NamedTuple instead).
