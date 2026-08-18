"""
=============================================================================
  TYPE HINTS & ANNOTATIONS — Complete Guide for Interviews
=============================================================================
"""

from typing import (
    List, Dict, Set, Tuple, Optional, Union,
    Any, Callable, Iterator, Generator,
    TypeVar, Generic, Protocol, Final, Literal
)


# ═══════════════════════════════════════════════════════════════════════════
# 1. BASICS — WHAT ARE TYPE HINTS?
# ═══════════════════════════════════════════════════════════════════════════
#
#   Type hints are OPTIONAL annotations. Python IGNORES them at runtime.
#   They help: IDEs (autocomplete), static checkers (mypy/pyright), humans.
#
#   Java: types are ENFORCED. Python: types are DOCUMENTATION.

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Variables:
age: int = 25
price: float = 9.99
is_active: bool = True
names: list = ["Alice", "Bob"]


# ═══════════════════════════════════════════════════════════════════════════
# 2. COLLECTION TYPES
# ═══════════════════════════════════════════════════════════════════════════

# Python 3.9+: use built-in types directly
scores: list[int] = [95, 87, 92]
user_ages: dict[str, int] = {"Alice": 30, "Bob": 25}
unique_ids: set[int] = {1, 2, 3}
point: tuple[float, float] = (1.0, 2.0)         # fixed length
data: tuple[int, ...] = (1, 2, 3, 4)            # variable length

# Python 3.8 and below: use typing module
scores_old: List[int] = [95, 87, 92]
user_ages_old: Dict[str, int] = {"Alice": 30}

# Nested:
matrix: list[list[int]] = [[1, 2], [3, 4]]
registry: dict[str, list[str]] = {"admin": ["Alice", "Bob"]}


# ═══════════════════════════════════════════════════════════════════════════
# 3. Optional AND Union
# ═══════════════════════════════════════════════════════════════════════════

# Optional[X] = X | None (value might be None)
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None                     # explicitly might return None

# Union[X, Y] = X | Y (multiple possible types)
def process(value: Union[int, str]) -> str:
    return str(value)

# Python 3.10+: use | syntax (cleaner)
def find_user_new(user_id: int) -> str | None:
    return None

def process_new(value: int | str) -> str:
    return str(value)


# ═══════════════════════════════════════════════════════════════════════════
# 4. FUNCTION TYPES — Callable
# ═══════════════════════════════════════════════════════════════════════════

# Callable[[arg_types], return_type]
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# apply(lambda x, y: x + y, 3, 4)  → 7

# Function that takes no args:
callback: Callable[[], None] = lambda: print("done")

# Any callable (don't care about signature):
handler: Callable[..., Any] = print


# ═══════════════════════════════════════════════════════════════════════════
# 5. TypeVar — GENERICS
# ═══════════════════════════════════════════════════════════════════════════

T = TypeVar('T')

def first(items: list[T]) -> T:
    """Returns first item — type-safe for any list type."""
    return items[0]

# first([1, 2, 3])       → int (inferred)
# first(["a", "b"])      → str (inferred)

# Bounded TypeVar:
Num = TypeVar('Num', int, float)       # only int or float

def double(x: Num) -> Num:
    return x * 2


# ═══════════════════════════════════════════════════════════════════════════
# 6. Generic CLASSES
# ═══════════════════════════════════════════════════════════════════════════

T2 = TypeVar('T2')

class Stack(Generic[T2]):
    def __init__(self) -> None:
        self._items: list[T2] = []

    def push(self, item: T2) -> None:
        self._items.append(item)

    def pop(self) -> T2:
        return self._items.pop()

# s: Stack[int] = Stack()
# s.push(1)        ✓
# s.push("str")    ✗ (type checker catches this)

# Java: class Stack<T> { ... }
# Python: class Stack(Generic[T]): ...


# ═══════════════════════════════════════════════════════════════════════════
# 7. SPECIAL TYPES
# ═══════════════════════════════════════════════════════════════════════════

# Any — opt out of type checking
def anything(x: Any) -> Any:
    return x

# Final — cannot be reassigned
MAX_SIZE: Final = 100
# MAX_SIZE = 200  → type checker error

# Literal — specific values only
def set_mode(mode: Literal["read", "write", "append"]) -> None:
    pass
# set_mode("read")    ✓
# set_mode("delete")  ✗

# None as return type
def log(msg: str) -> None:
    print(msg)

# Self (Python 3.11+) — for chaining
from typing import Self
class Builder:
    def set_name(self, name: str) -> Self:
        self.name = name
        return self


# ═══════════════════════════════════════════════════════════════════════════
# 8. TYPE ALIASES
# ═══════════════════════════════════════════════════════════════════════════

# Simple alias:
Vector = list[float]
Matrix = list[list[float]]

def scale(v: Vector, factor: float) -> Vector:
    return [x * factor for x in v]

# Python 3.12+ explicit syntax:
# type Vector = list[float]
# type Matrix = list[list[float]]

# Complex alias:
JSON = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None


# ═══════════════════════════════════════════════════════════════════════════
# 9. TYPE CHECKING TOOLS
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Tool        | Type        | Usage                               |
#   |-------------|-------------|-------------------------------------|
#   | mypy        | CLI checker | mypy script.py                      |
#   | pyright     | CLI checker | pyright script.py                   |
#   | Pylance     | VS Code ext | Real-time checking in editor        |
#
#   # Run mypy:
#   pip install mypy
#   mypy my_module.py --strict
#
#   # Common flags:
#   --strict              → enable all checks
#   --ignore-missing-imports
#   --disallow-untyped-defs


# ═══════════════════════════════════════════════════════════════════════════
# 10. RUNTIME BEHAVIOR — TYPES ARE IGNORED!
# ═══════════════════════════════════════════════════════════════════════════

def add(a: int, b: int) -> int:
    return a + b

# This RUNS without error (Python ignores hints):
# add("hello", " world")  → "hello world"

# To enforce at runtime, use:
# 1. isinstance() checks manually
# 2. pydantic library (auto-validates)
# 3. @beartype decorator

# Access annotations at runtime:
# add.__annotations__  → {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


# ═══════════════════════════════════════════════════════════════════════════
# 11. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: Does Python enforce type hints?
#   A: No. They're ignored at runtime. Only static checkers use them.
#
#   Q: Optional[int] means what?
#   A: int | None — the value can be an int OR None.
#
#   Q: How to type a function parameter?
#   A: Callable[[arg_types], return_type]
#
#   Q: TypeVar is for what?
#   A: Generics — like Java's <T>. Lets you write type-safe generic functions.
#
#   Q: list[int] vs List[int]?
#   A: Same thing. list[int] works Python 3.9+. List[int] for older versions.
#
#   Q: How to check types before running?
#   A: mypy, pyright, or Pylance in VS Code.
