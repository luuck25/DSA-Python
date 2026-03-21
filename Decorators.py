
## without Args

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()


# Before function runs
# Hello!
# After function runs

"""

How It Works

When you write:
@my_decorator
def greet():

Python internally does this:

greet = my_decorator(greet)

So the original function is replaced by the wrapper function.
"""

# with args

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is running")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(5, 3))

"""
What Are *args and **kwargs?

They allow a function to accept any number of arguments.

✅ *args

Collects positional arguments

Stored as a tuple

✅ **kwargs

Collects keyword arguments

Stored as a dictionary

Example

def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(2, 5, x=10, y=20)


How Arguments Enter wrapper

def wrapper(*args, **kwargs):

Python collects:

2 → positional
5 → positional


So:

args = (2, 5)
kwargs = {}

### Step 4️⃣: Inside wrapper

return func(*args, **kwargs)

return func(2, 5)

The * operator unpacks the tuple.

So:

(2, 5) → 2, 5

Visual Flow

add(2, 5)
   ↓
wrapper(2, 5)
   ↓
args = (2, 5)
kwargs = {}
   ↓
func(*args)
   ↓
func(2, 5)
   ↓
add(2, 5)
   ↓
return 7


Why 2 returns Are needed


First Return
return func(*args, **kwargs)

This is inside wrapper.

What it does:

It:

Calls the original function

Passes the arguments

Returns its result

return func(*args, **kwargs)

return func(2, 5) becomes return 2 + 5

what if we remove - Then the result of add(2,5) would be:

None

Second Return

return wrapper

This one is MUCH more important.

This is what actually makes decorators work.

add = my_decorator(add) -> return wrapper

so add = wrapper


If we remove:

return wrapper

add = my_decorator(add) will become add = None

Big Picture Understanding :

Decorator → Takes function → Wraps it → Returns new function

If we don't return wrapper, we never give back the new wrapped function.


Visual Flow


Original add function
        ↓
my_decorator(add)
        ↓
Creates wrapper
        ↓
return wrapper
        ↓
add now points to wrapper



Super Simple Analogy

Imagine this:

You give your phone to someone to install a protective case.

You expect:

Same phone

Extra protection

If they don’t give it back (no return wrapper),
you no longer have a phone 😄

"""




"""

IMP - What Does @wraps(func) Do?

from functools import wraps

@wraps(func) is used to preserve the metadata of the original function when using decorators.

metadata like:

__name__

__doc__

__annotations__

__module__

"""