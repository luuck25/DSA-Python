"""
=============================================================================
  DECORATORS — Advanced & Complete Guide for Interviews
=============================================================================
"""


# ═══════════════════════════════════════════════════════════════════════════
# 1. WHAT IS A DECORATOR?
# ═══════════════════════════════════════════════════════════════════════════
#
#   A decorator is a function that takes a function and returns a new function.
#   @decorator is syntactic sugar for: func = decorator(func)

def simple_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

# say_hello()  →  Before / Hello! / After
# Equivalent to: say_hello = simple_decorator(say_hello)


# ═══════════════════════════════════════════════════════════════════════════
# 2. DECORATOR WITH ARGUMENTS PASS-THROUGH
# ═══════════════════════════════════════════════════════════════════════════

import functools

def log_call(func):
    @functools.wraps(func)             # preserves original func name/docstring
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    """Add two numbers."""
    return a + b

# add(3, 4)  →  "Calling add with (3, 4), {}" / "Returned: 7" / returns 7
# add.__name__  → "add" (thanks to @functools.wraps)


# ═══════════════════════════════════════════════════════════════════════════
# 3. WHY @functools.wraps MATTERS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Without @wraps:
#     add.__name__  → "wrapper"   (lost original name!)
#     add.__doc__   → None        (lost docstring!)
#
#   With @wraps:
#     add.__name__  → "add"       (preserved)
#     add.__doc__   → "Add two numbers."  (preserved)
#
#   ALWAYS use @functools.wraps(func) in your decorators.


# ═══════════════════════════════════════════════════════════════════════════
# 4. DECORATOR THAT TAKES ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════
#
#   Need an extra layer of nesting: decorator_factory → decorator → wrapper

def repeat(n):
    """Decorator factory — returns a decorator."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)                            # repeat(3) returns the actual decorator
def greet(name):
    print(f"Hello {name}")

# greet("Alice")  → prints "Hello Alice" 3 times


# ═══════════════════════════════════════════════════════════════════════════
# 5. COMMON BUILT-IN DECORATORS
# ═══════════════════════════════════════════════════════════════════════════

class MyClass:
    class_var = "shared"

    def instance_method(self):        # regular — needs instance
        return self

    @classmethod
    def factory(cls):                 # gets class, not instance
        return cls()

    @staticmethod
    def utility():                    # no self or cls
        return "just a function in a namespace"

    @property
    def name(self):                   # attribute-style access
        return self._name

# Other important decorators:
# @functools.lru_cache    → memoization
# @functools.wraps        → preserve function metadata
# @abc.abstractmethod     → force subclass to implement
# @dataclasses.dataclass  → auto-generate __init__, __repr__, etc.


# ═══════════════════════════════════════════════════════════════════════════
# 6. PRACTICAL DECORATOR EXAMPLES
# ═══════════════════════════════════════════════════════════════════════════

#--logging--

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper



# --- Timer ---



import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Time:", time.time() - start)
        return result
    return wrapper


import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

# --- Retry on exception ---


def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except:
                print("Retrying...")
    return wrapper


def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_api_call():
    pass  # might fail

# --- Cache/Memoize ---
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# --- Validate types ---
def validate_types(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            for arg, expected in zip(args, types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected}, got {type(arg)}")
            return func(*args)
        return wrapper
    return decorator

@validate_types(int, int)
def multiply(a, b):
    return a * b


# ═══════════════════════════════════════════════════════════════════════════
# 7. STACKING DECORATORS
# ═══════════════════════════════════════════════════════════════════════════

@timer
@log_call
def compute(x):
    return x ** 2

# Equivalent to: compute = timer(log_call(compute))
# Order: timer wraps log_call wraps compute
# Execution: timer's wrapper → log_call's wrapper → compute


# ═══════════════════════════════════════════════════════════════════════════
# 8. CLASS-BASED DECORATORS
# ═══════════════════════════════════════════════════════════════════════════

class CountCalls:
    """Counts how many times a function is called."""
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

# say_hi()   → "say_hi called 1 times" / "Hi!"
# say_hi()   → "say_hi called 2 times" / "Hi!"
# say_hi.count  → 2


# ═══════════════════════════════════════════════════════════════════════════
# 9. DECORATING CLASSES
# ═══════════════════════════════════════════════════════════════════════════

def singleton(cls):
    """Only one instance ever created."""
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Creating DB connection")

# db1 = Database()   → "Creating DB connection"
# db2 = Database()   → (nothing — returns same instance)
# db1 is db2         → True


# ═══════════════════════════════════════════════════════════════════════════
# 10. INTERVIEW QUICK-FIRE
# ═══════════════════════════════════════════════════════════════════════════
#
#   Q: What is a decorator?
#   A: A function that wraps another function to add behavior.
#      @deco is sugar for func = deco(func).
#
#   Q: How to preserve the original function's metadata?
#   A: Use @functools.wraps(func) in the wrapper.
#
#   Q: How to make a decorator that takes arguments?
#   A: Triple nesting: factory(args) → decorator(func) → wrapper(*args).
#
#   Q: What order do stacked decorators execute?
#   A: Bottom-up for wrapping, top-down for execution.
#      @A @B def f → f = A(B(f)), A's wrapper runs first.
#
#   Q: Can a class be a decorator?
#   A: Yes — implement __init__(self, func) and __call__(self, *args).
#
#   Q: Name practical uses.
#   A: Logging, timing, caching, retry, auth, rate limiting, validation.
