"""
=============================================================================
  OOP IN PYTHON — Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. CLASS BASICS — self, __init__, INSTANCE vs CLASS
# ═══════════════════════════════════════════════════════════════════════════

class Dog:
    species = "Canis familiaris"      # CLASS variable (shared by all)

    def __init__(self, name, age):    # constructor
        self.name = name              # INSTANCE variable (unique per object)
        self.age = age

    def bark(self):                   # instance method
        return f"{self.name} says Woof!"

# self = reference to the current instance (like 'this' in Java)
# BUT: self is EXPLICIT in Python (must be first param)
#
# Java:  public Dog(String name) { this.name = name; }
# Python: def __init__(self, name): self.name = name


# ═══════════════════════════════════════════════════════════════════════════
# 2. @classmethod vs @staticmethod vs INSTANCE METHOD
# ═══════════════════════════════════════════════════════════════════════════

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    # INSTANCE METHOD — has access to self (instance)
    def describe(self):
        return f"Pizza with {self.ingredients}"

    # CLASS METHOD — has access to cls (the class itself)
    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomato", "basil"])   # factory method

    # STATIC METHOD — no access to self or cls (just a regular function in class namespace)
    @staticmethod
    def is_valid_topping(topping):
        return topping != "pineapple"

# Usage:
# p = Pizza.margherita()           → factory creates instance
# p.describe()                     → "Pizza with ['mozzarella', 'tomato', 'basil']"
# Pizza.is_valid_topping("ham")    → True

# Summary:
#   | Type           | First arg | Can modify instance? | Can modify class? |
#   |----------------|-----------|---------------------|-------------------|
#   | Instance       | self      | Yes                 | Yes (via class)   |
#   | @classmethod   | cls       | No                  | Yes               |
#   | @staticmethod  | (none)    | No                  | No                |


# ═══════════════════════════════════════════════════════════════════════════
# 3. INHERITANCE
# ═══════════════════════════════════════════════════════════════════════════

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Cat(Animal):                    # Cat inherits from Animal
    def speak(self):
        return f"{self.name} says Meow!"

class Dog2(Animal):
    def __init__(self, name, breed):
        super().__init__(name)        # call parent constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

# Java: class Dog extends Animal { super(name); }
# Python: class Dog(Animal): super().__init__(name)


# ═══════════════════════════════════════════════════════════════════════════
# 4. super() AND MRO (Method Resolution Order)
# ═══════════════════════════════════════════════════════════════════════════

class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B → " + super().greet()

class C(A):
    def greet(self):
        return "C → " + super().greet()

class D(B, C):    # multiple inheritance
    def greet(self):
        return "D → " + super().greet()

# D().greet() → "D → B → C → A"
# MRO: D → B → C → A (C3 linearization)
# print(D.__mro__)

# Key: super() follows MRO, NOT just the direct parent.
# This is how Python solves the diamond problem.


# ═══════════════════════════════════════════════════════════════════════════
# 5. @property — GETTERS/SETTERS THE PYTHON WAY
# ═══════════════════════════════════════════════════════════════════════════

class Circle:
    def __init__(self, radius):
        self._radius = radius        # "private" by convention

    @property
    def radius(self):                # getter
        return self._radius

    @radius.setter
    def radius(self, value):         # setter
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):                  # computed property (read-only)
        import math
        return math.pi * self._radius ** 2

# c = Circle(5)
# c.radius          → 5        (calls getter)
# c.radius = 10     → sets     (calls setter)
# c.radius = -1     → ValueError
# c.area            → 314.15... (computed, no setter = read-only)

# Java: getRadius(), setRadius() — explicit methods
# Python: @property — looks like attribute access but runs code


# ═══════════════════════════════════════════════════════════════════════════
# 6. ABSTRACT CLASSES (ABC)
# ═══════════════════════════════════════════════════════════════════════════

from abc import ABC, abstractmethod

class Shape(ABC):                     # cannot instantiate
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):               # concrete method — inherited as-is
        return f"Area: {self.area()}"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):                   # MUST implement
        return self.w * self.h

    def perimeter(self):              # MUST implement
        return 2 * (self.w + self.h)

# Shape()         → TypeError: Can't instantiate abstract class
# Rectangle(3,4)  → works

# Java: abstract class Shape { abstract double area(); }
# Python: class Shape(ABC): @abstractmethod def area(self)


# ═══════════════════════════════════════════════════════════════════════════
# 7. PROTOCOL — STRUCTURAL TYPING (Python 3.8+)
# ═══════════════════════════════════════════════════════════════════════════

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...       # just the signature

class Circle2:
    def draw(self) -> None:           # matches Protocol — no explicit inheritance!
        print("Drawing circle")

def render(obj: Drawable):
    obj.draw()

# render(Circle2())  → works! Circle2 matches the Protocol structurally.
# This is duck typing + type safety. Best of both worlds.


# ═══════════════════════════════════════════════════════════════════════════
# 8. COMPOSITION OVER INHERITANCE
# ═══════════════════════════════════════════════════════════════════════════

# Instead of deep inheritance hierarchies, prefer composition:

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()        # HAS-A relationship

    def start(self):
        return self.engine.start()

# Better than: class Car(Vehicle(Machine(Base))): ...
# Rule: "Favor composition over inheritance" — same in Java & Python.


# ═══════════════════════════════════════════════════════════════════════════
# 9. MAGIC/DUNDER METHODS FOR OOP
# ═══════════════════════════════════════════════════════════════════════════

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):               # developer string
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):         # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):          # v1 == v2
        return self.x == other.x and self.y == other.y

    def __hash__(self):               # needed if __eq__ is defined
        return hash((self.x, self.y))

    def __len__(self):                # len(v)
        return int((self.x**2 + self.y**2)**0.5)

# v1 = Vector(1, 2) + Vector(3, 4)  → Vector(4, 6)


# ═══════════════════════════════════════════════════════════════════════════
# 10. __slots__ — MEMORY OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════

class PointWithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Each instance has a __dict__ → extra memory

class PointWithSlots:
    __slots__ = ('x', 'y')           # no __dict__ → less memory
    def __init__(self, x, y):
        self.x = x
        self.y = y

# PointWithSlots uses ~40% less memory per instance
# Trade-off: can't add arbitrary attributes later
# p = PointWithSlots(1, 2)
# p.z = 3  → AttributeError!


# ═══════════════════════════════════════════════════════════════════════════
# 11. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What is self?
#   A: Reference to the current instance. Like 'this' in Java but explicit.
#
#   Q: @classmethod vs @staticmethod?
#   A: classmethod gets cls (can create instances, access class state).
#      staticmethod gets nothing (just a namespaced function).
#
#   Q: How does Python handle multiple inheritance?
#   A: MRO (C3 linearization). super() follows MRO, not just parent.
#
#   Q: How to make an abstract class?
#   A: Inherit from ABC, use @abstractmethod. Can't instantiate.
#
#   Q: What's @property?
#   A: Makes a method behave like an attribute. Python's getter/setter.
#
#   Q: What are __slots__?
#   A: Declares fixed attributes, skips __dict__. Saves memory.
#
#   Q: isinstance vs type?
#   A: isinstance checks inheritance chain. type() checks exact class.
#      isinstance(True, int) → True (bool subclasses int)
#      type(True) == int → False
