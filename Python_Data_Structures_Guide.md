# 🐍 Python Data Structures – Complete Guide

A comprehensive reference for List, Tuple, Set, Dictionary, Stack, Queue, and Deque.

---

# 📌 1️⃣ List

Lists are ordered, mutable collections that can store elements of any type.

---

## 🔹 Creating List

```python
a = [1, 2, 3]
empty_list = []
```

---

## 🔹 Using `list()` Constructor

```python
list_from_tuple = list((1, 2, 3))
list_from_string = list("hello")
list_from_range = list(range(5))
```

---

## 🔹 From Another List (Copying)

```python
lst_copy1 = a.copy()
lst_copy2 = a[:]
lst_copy3 = list(a)
```

---

## 🔹 From Set

```python
list_from_set = list({1, 2, 3})
```

---

## 🔹 From Dictionary

```python
sample_dict = {"a": 1, "b": 2}

list_keys = list(sample_dict.keys())
list_values = list(sample_dict.values())
list_items = list(sample_dict.items())
```

---

## 🔹 Accessing Elements

```python
list_a = [1, 2, 3]

print(list_a[0])     # First element
print(list_a[-1])    # Last element
```

---

## 🔹 Traversing List

```python
# Using Direct Loop
for num in list_a:
    print(num)

# Using Index
for i in range(len(list_a)):
    print(list_a[i])
```

---

## 🔹 Slicing

```python
print(list_a[0:2])   # Elements from index 0 to 1
print(list_a[:2])    # From start to index 1
print(list_a[1:])    # From index 1 to end
```

---

## ➕ Adding Elements

```python
list_a.append(4)        # Add at end
list_a.insert(1, 5)     # Insert at specific index
list_a.extend([6, 7])   # Add multiple elements
```

---

## ➖ Removing Elements

```python
list_a.remove(4)        # Remove by value (first occurrence)
list_a.pop()            # Remove last element
list_a.pop(1)           # Remove element at index
del list_a[0]           # Delete by index
del list_a[1:3]         # Delete slice
list_a.clear()          # Remove all elements
```

---

## 🔹 Searching in List

```python
list_a.index(5)     # Get index of value
list_a.count(5)     # Count occurrences
5 in list_a         # Check existence
```

---

## 🔹 Sorting & Reversing

```python
lst = [3, 1, 2]

lst.sort()                    # Sort ascending (in-place)
lst.sort(reverse=True)        # Sort descending
new_lst = sorted(lst)         # Return new sorted list
lst.reverse()                 # Reverse list
```

---

## 🔹 Other Useful Operations

```python
len(lst)
max(lst)
min(lst)
sum(lst)
```

---

## 📊 List Time Complexity

| Operation | Time Complexity |
|-----------|------------------|
| Access by index | O(1) |
| Append | O(1) amortized |
| Insert at beginning | O(n) |
| Remove/Search | O(n) |
| Sort | O(n log n) |

---

## ✅ List Properties

- Ordered
- Mutable
- Allows duplicates
- Dynamic size
- Indexed
- Supports slicing

---

# 📌 2️⃣ Tuple

Tuples are ordered and immutable collections.

---

## 🔹 Creating Tuple

```python
t = (1, 2, 3)
single = (5,)        # Note: comma required for single element
empty = ()
```

---

## 🔹 Using `tuple()` Constructor

```python
t = tuple([1, 2, 3])
```

---

## 🔹 From Set

```python
t = tuple({1, 2, 3})
```

---

## 🔹 From String

```python
t = tuple("hello")
t = tuple(range(5))
```

---

## 🔹 From Dictionary

```python
d = {"a": 1, "b": 2}

tuple(d)               # Keys
tuple(d.values())      # Values
tuple(d.items())       # Key-value pairs
```

---

## 🔹 Accessing Elements

```python
t[0]       # First element
t[-1]      # Last element
t[0:2]     # Slicing
```

---

## 🔹 Traversing Tuple

```python
for item in t:
    print(item)

for i in range(len(t)):
    print(t[i])
```

---

## 🔹 Sorting Tuple

Tuples cannot be sorted directly (because immutable). Use `sorted()`:

```python
t = (3, 1, 2)
sorted_t = tuple(sorted(t))
```

---

## 🔹 Reverse Tuple

```python
t = (1, 2, 3)
reversed_t = tuple(reversed(t))
```

---

## 🔹 Searching in Tuple

```python
t.index(20)     # Get index
t.count(20)     # Count occurrences
```

---

## 🔹 Other Useful Operations

```python
len(t)
max(t)
min(t)
sum(t)
```

---

## 🔹 Convert Tuple to Other Data Structures

```python
list(t)
set(t)
dict(tuple_of_pairs)
```

---

## 🔹 Tuple Unpacking

```python
a, b, c = t
```

---

## ✅ Tuple Properties

- Ordered
- Immutable
- Allows duplicates
- Faster than list (slightly)
- Can be dictionary keys (if elements immutable)

---

# 📌 3️⃣ Set

Sets store unique elements (no duplicates).

---

## 🔹 Creating Set

```python
s = {1, 2, 3}
empty_set = set()     # {} creates dict, not set
```

---

## ➕ Adding Elements

```python
s.add(4)
s.update([5, 6])      # Add multiple
```

---

## ➖ Removing Elements

```python
s.remove(2)      # Error if not found
s.discard(10)    # No error if not found
s.pop()          # Remove random element
s.clear()        # Remove all elements
```

---

## 🔹 Accessing Elements in Set

```python
s = {10, 20, 30}
# s[0] ❌ Error - Sets don't support indexing
```

---

## 🔹 Traversing Set

```python
for item in s:
    print(item)
```

---

## 🔹 Check Membership

```python
10 in s          # Very fast → O(1)
```

---

## 🔹 Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)                  # {1, 2, 3, 4, 5}
a.intersection(b)           # {3}
a.difference(b)             # {1, 2}
a.symmetric_difference(b)   # {1, 2, 4, 5}
```

---

## ✅ Set Properties

- Unordered
- Mutable
- No duplicates
- Very fast membership check O(1)

---

# 📌 4️⃣ Dictionary

Dictionary stores key-value pairs.

---

## 🔹 Creating Dictionary

```python
d = {"a": 1, "b": 2}
empty = {}
d = dict(a=1, b=2)
```

---

## 🔹 From List of Tuples

```python
d = dict([("a", 1), ("b", 2)])
```

---

## 🔹 From Tuple of Tuples

```python
d = dict((("a", 1), ("b", 2)))
```

---

## 🔹 Accessing Elements

```python
d["a"]
d.get("a")        # Safe access
d.get("x", 0)     # Default value
```

---

## 🔹 Traversing Dictionary

```python
# Iterate Keys
for key in d:
    print(key)

# Iterate Values
for value in d.values():
    print(value)

# Iterate Key-Value
for key, value in d.items():
    print(key, value)
```

---

## ➕ Adding / Updating

```python
d["c"] = 3
d.update({"d": 4})
```

---

## ➖ Removing Elements

```python
d.pop("a")
d.popitem()       # Removes last item
del d["b"]
d.clear()
```

---

## 🔹 Convert to List

```python
list(d.keys())
list(d.values())
list(d.items())
```

---

## ✅ Dictionary Properties

- Ordered (Python 3.7+)
- Mutable
- Keys must be immutable & unique
- O(1) lookup

---

# 📌 5️⃣ Stack (LIFO)

Stack follows Last In First Out. Implemented using list.

---

## 🔹 Creating Stack

```python
stack = []
```

---

## 🔹 Push

```python
stack.append(10)
```

---

## 🔹 Pop

```python
stack.pop()
```

---

## 🔹 Peek

```python
stack[-1]
```

---

## 🔹 Check Empty

```python
if not stack:
    print("Empty")
```

---

## 📊 Stack Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Push      | O(1)            |
| Pop       | O(1)            |

---

## 💡 Stack Use Cases

- Undo/Redo
- Expression evaluation
- Parenthesis checking

---

# 📌 6️⃣ Queue (FIFO)

Queue follows First In First Out. Using `collections.deque` (recommended).

---

## 🔹 Creating Queue

```python
from collections import deque

queue = deque()
queue = deque([1, 2, 3])      # From List
queue = deque((1, 2, 3))      # From Tuple
queue = deque({1, 2, 3})      # From Set (order not guaranteed)
```

---

## 🔹 Enqueue

```python
queue.append(10)
```

---

## 🔹 Dequeue

```python
queue.popleft()
```

---

## 🔹 Peek (Front Element)

```python
queue[0]
```

---

## 🔹 Check Empty

```python
if not queue:
    print("Queue empty")
```

---

## 🔹 Traversing Queue

```python
for item in queue:
    print(item)
```

---

## 📊 Queue Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |

---

# 📌 7️⃣ Deque (Double Ended Queue)

Deque allows insertion/removal from both ends.

---

## 🔹 Creating Deque

```python
from collections import deque

dq = deque([1, 2, 3])
```

---

## 🔹 Operations

```python
dq.append(4)         # Add to right
dq.appendleft(0)     # Add to left

dq.pop()             # Remove from right
dq.popleft()         # Remove from left

dq.rotate(1)         # Rotate right
dq.rotate(-1)        # Rotate left
```

---

## ✅ Deque Properties

- Fast front & rear operations
- Better than list for queue behavior

---

# 📊 Comprehensive Cheat Sheet

## 🔷 Properties Comparison

| Structure | Ordered | Mutable | Duplicates | Indexed | Hashable |
|-----------|---------|---------|------------|---------|----------|
| List      | ✅ Yes  | ✅ Yes  | ✅ Yes     | ✅ Yes  | ❌ No    |
| Tuple     | ✅ Yes  | ❌ No   | ✅ Yes     | ✅ Yes  | ✅ Yes*  |
| Set       | ❌ No   | ✅ Yes  | ❌ No      | ❌ No   | ❌ No    |
| Dict      | ✅ Yes  | ✅ Yes  | Keys ❌    | By Key  | ❌ No    |
| Stack     | ✅ Yes  | ✅ Yes  | ✅ Yes     | Top Only| ❌ No    |
| Queue     | ✅ Yes  | ✅ Yes  | ✅ Yes     | ❌ No   | ❌ No    |
| Deque     | ✅ Yes  | ✅ Yes  | ✅ Yes     | ✅ Yes  | ❌ No    |

*Tuple is hashable only if all elements are hashable

---

## 🔷 Time Complexity Comparison

| Operation | List | Tuple | Set | Dict | Deque |
|-----------|------|-------|-----|------|-------|
| Access by index | O(1) | O(1) | ❌ | ❌ | O(n) |
| Access by key | ❌ | ❌ | ❌ | O(1) | ❌ |
| Search | O(n) | O(n) | O(1) | O(1) | O(n) |
| Insert at end | O(1) | ❌ | O(1) | O(1) | O(1) |
| Insert at start | O(n) | ❌ | O(1) | O(1) | O(1) |
| Delete | O(n) | ❌ | O(1) | O(1) | O(n)* |
| Sort | O(n log n) | O(n log n)** | ❌ | ❌ | O(n log n)** |

*O(1) for ends, **Returns new sorted sequence

---

## 🔷 Creation Syntax Quick Reference

| Structure | Empty | With Values | From Other |
|-----------|-------|-------------|------------|
| List | `[]` or `list()` | `[1, 2, 3]` | `list(iterable)` |
| Tuple | `()` or `tuple()` | `(1, 2, 3)` | `tuple(iterable)` |
| Set | `set()` | `{1, 2, 3}` | `set(iterable)` |
| Dict | `{}` or `dict()` | `{"a": 1}` | `dict(pairs)` |
| Deque | `deque()` | `deque([1,2,3])` | `deque(iterable)` |

---

## 🔷 Common Operations Quick Reference

| Operation | List | Tuple | Set | Dict |
|-----------|------|-------|-----|------|
| Add | `append()`, `insert()` | ❌ | `add()` | `d[key] = val` |
| Add Multiple | `extend()` | ❌ | `update()` | `update()` |
| Remove by value | `remove()` | ❌ | `remove()`, `discard()` | ❌ |
| Remove by index/key | `pop(i)`, `del` | ❌ | `pop()` | `pop(key)`, `del` |
| Remove last | `pop()` | ❌ | ❌ | `popitem()` |
| Clear all | `clear()` | ❌ | `clear()` | `clear()` |
| Get length | `len()` | `len()` | `len()` | `len()` |
| Check membership | `in` | `in` | `in` | `in` (keys) |
| Count | `count()` | `count()` | ❌ | ❌ |
| Find index | `index()` | `index()` | ❌ | ❌ |
| Sort in-place | `sort()` | ❌ | ❌ | ❌ |
| Get sorted copy | `sorted()` | `sorted()` | `sorted()` | `sorted()` |
| Reverse in-place | `reverse()` | ❌ | ❌ | ❌ |
| Get reversed | `reversed()` | `reversed()` | ❌ | `reversed()` |
| Copy | `copy()`, `[:]` | ❌ | `copy()` | `copy()` |

---

## 🔷 Stack & Queue Operations

| Operation | Stack (List) | Queue (Deque) | Deque |
|-----------|--------------|---------------|-------|
| Add | `append()` | `append()` | `append()`, `appendleft()` |
| Remove | `pop()` | `popleft()` | `pop()`, `popleft()` |
| Peek | `[-1]` | `[0]` | `[-1]`, `[0]` |
| Rotate | ❌ | ❌ | `rotate(n)` |

---

## 🔷 Conversion Between Types

| From \ To | List | Tuple | Set | Dict |
|-----------|------|-------|-----|------|
| List | - | `tuple(lst)` | `set(lst)` | `dict(pairs)` |
| Tuple | `list(tup)` | - | `set(tup)` | `dict(pairs)` |
| Set | `list(s)` | `tuple(s)` | - | ❌ |
| Dict | `list(d.items())` | `tuple(d.items())` | `set(d.keys())` | - |

---

## 🔷 When to Use What?

| Use Case | Best Choice | Why |
|----------|-------------|-----|
| Ordered collection, frequent modifications | **List** | Mutable, indexed |
| Fixed data, dictionary keys | **Tuple** | Immutable, hashable |
| Unique elements, fast lookup | **Set** | O(1) membership |
| Key-value mapping | **Dict** | O(1) key access |
| LIFO operations | **Stack (List)** | Simple, efficient |
| FIFO operations | **Queue (Deque)** | O(1) both ends |
| Both-end operations | **Deque** | O(1) append/pop both ends |
| Coordinates, RGB values | **Tuple** | Fixed size, immutable |
| Counting occurrences | **Dict** | Key-value pairs |
| Removing duplicates | **Set** | Auto-removes duplicates |
| Configuration data | **Dict** | Named access |
| Function return multiple values | **Tuple** | Unpacking support |

---

## 🔷 Memory & Performance Tips

| Tip | Structure |
|-----|-----------|
| Tuples use less memory than lists | Prefer tuple for fixed data |
| Set membership check is O(1) | Use set for frequent `in` checks |
| Dict lookup is O(1) | Use dict over list of tuples |
| Deque is faster than list for queue | Use deque for FIFO |
| List comprehension is faster than loop | Use `[x for x in ...]` |
| Generator saves memory | Use `(x for x in ...)` for large data |

---

# 🎯 Final Notes

- Use **List** for ordered, mutable collections
- Use **Tuple** for fixed, immutable data
- Use **Set** for uniqueness & fast membership
- Use **Dict** for key-value mapping
- Use **Stack** for LIFO problems
- Use **Queue** for FIFO problems
- Use **Deque** for fast both-end operations
