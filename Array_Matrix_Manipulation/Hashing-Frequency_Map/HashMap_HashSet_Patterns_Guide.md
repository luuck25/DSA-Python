# HashMap & HashSet — Deep Dive: Patterns & Problem Types

---

## 🧠 Core Difference

| | **HashSet** | **HashMap** |
|---|---|---|
| Stores | Only **keys** | **Key → Value** pairs |
| Use when | You care about **existence/uniqueness** | You care about **frequency / mapping / association** |
| Python | `set()` | `dict()` or `defaultdict()` |
| Operations | `add`, `remove`, `in` — all O(1) | `get`, `set`, `in` — all O(1) |

---

## 📌 PATTERN 1: Frequency Counting (HashMap)

**Recognize when:** "most frequent", "least frequent", "top K", "count occurrences", "frequency"

**How it works:** Count how many times each element appears.

```python
# Template
freq = {}
for item in arr:
    freq[item] = freq.get(item, 0) + 1
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Top K Frequent Elements | freq map → heap or bucket sort |
| First Non-Repeating Character | freq map → first with count == 1 |
| Largest Unique Number | freq map → max of keys with count == 1 |
| Longest Palindrome from String | count even pairs + at most 1 odd |
| Valid Anagram | compare two freq maps |
| Group Anagrams | sorted string as key → list of anagrams |

**🔍 Recognition cues:** "how many times", "most/least common", "frequency", "count"

---

## 📌 PATTERN 2: Duplicate Detection (HashSet)

**Recognize when:** "contains duplicate", "unique", "seen before", "first repeating"

**How it works:** Track what you've already seen.

```python
# Template
seen = set()
for item in arr:
    if item in seen:
        return True  # duplicate!
    seen.add(item)
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Contains Duplicate | set size vs array size |
| Contains Duplicate II | sliding window + set |
| Happy Number | detect cycle via seen set |
| Longest Consecutive Sequence | set lookup for chain start |
| Intersection of Two Arrays | set intersection |

**🔍 Recognition cues:** "duplicate", "unique", "already exists", "repeating"

---

## 📌 PATTERN 3: Two Sum / Complement Lookup (HashMap)

**Recognize when:** "two numbers that sum to target", "find pair", "complement"

**How it works:** Store `{value: index}`. For each element, check if its complement exists.

```python
# Template
lookup = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in lookup:
        return [lookup[complement], i]
    lookup[num] = i
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Two Sum | complement = target - num |
| Two Sum II (sorted) | can also use two pointers |
| 4Sum II | split into two groups, map sums |
| Subarray Sum Equals K | prefix sum as key |
| Count Pairs with Difference K | check num+k and num-k in map |

**🔍 Recognition cues:** "pair", "two numbers", "sum to", "difference equals"

---

## 📌 PATTERN 4: Prefix Sum + HashMap

**Recognize when:** "subarray sum equals K", "count subarrays with sum", "divisible by K"

**How it works:** Store `{prefix_sum: count}`. If `prefix_sum - target` exists in map → a valid subarray exists.

```python
# Template
prefix_sum = 0
count = 0
seen = {0: 1}  # empty subarray has sum 0

for num in arr:
    prefix_sum += num
    if prefix_sum - k in seen:
        count += seen[prefix_sum - k]
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Subarray Sum Equals K | prefix_sum - k in map |
| Continuous Subarray Sum (mod K) | prefix_sum % k in map |
| Subarray Sums Divisible by K | same mod approach |
| Binary Subarrays With Sum | prefix sum on binary array |
| Count Nice Subarrays | transform to binary + prefix sum |

**🔍 Recognition cues:** "subarray sum", "contiguous", "divisible", "count subarrays"

---

## 📌 PATTERN 5: Grouping / Categorization (HashMap)

**Recognize when:** "group by", "categorize", "same property together"

**How it works:** Use a shared property as the key, group items into lists.

```python
# Template
from collections import defaultdict
groups = defaultdict(list)

for item in items:
    key = get_property(item)  # e.g., sorted(word), len(word)
    groups[key].append(item)
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Group Anagrams | key = sorted(word) or char count tuple |
| Group Shifted Strings | key = tuple of char differences |
| Isomorphic Strings | map char → char, both directions |
| Word Pattern | map pattern_char → word, both directions |

**🔍 Recognition cues:** "group", "same category", "pattern matching", "isomorphic"

---

## 📌 PATTERN 6: Sliding Window + HashSet/Map

**Recognize when:** "longest substring", "window with distinct", "at most K distinct"

**How it works:** Expand window, track chars in set/map, shrink when constraint breaks.

```python
# Template (HashSet — no repeating)
seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    max_len = max(max_len, right - left + 1)
```

```python
# Template (HashMap — at most K distinct)
char_count = {}
left = 0

for right in range(len(s)):
    char_count[s[right]] = char_count.get(s[right], 0) + 1
    while len(char_count) > k:
        char_count[s[left]] -= 1
        if char_count[s[left]] == 0:
            del char_count[s[left]]
        left += 1
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Longest Substring Without Repeating Chars | set + sliding window |
| Longest Substring with K Distinct Chars | map size ≤ k |
| Minimum Window Substring | map for target freq, shrink when valid |
| Permutation in String | fixed window + freq map match |

**🔍 Recognition cues:** "substring", "window", "distinct", "at most K"

---

## 📌 PATTERN 7: Cycle Detection (HashSet)

**Recognize when:** "detect loop", "infinite loop", "repeating state"

```python
# Template
seen = set()
while state not in seen:
    seen.add(state)
    state = transform(state)
# state is the repeated element
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Happy Number | seen set of sums (or Floyd's) |
| Linked List Cycle | seen set of nodes (or fast/slow) |
| Find Duplicate Number | index as implicit hash |

**🔍 Recognition cues:** "cycle", "loop", "infinite", "repeating state"

---

## 📌 PATTERN 8: Index Mapping (HashMap)

**Recognize when:** "find position", "last occurrence", "first occurrence index"

```python
# Template
index_map = {}
for i, val in enumerate(arr):
    index_map[val] = i  # stores last index of each value
```

**Problems:**

| Problem | Key Idea |
|---|---|
| Two Sum | value → index for complement lookup |
| Contains Duplicate II | value → last index, check distance |
| First Unique Character | value → first index, filter by freq |
| Intersection with indices | track positions |

---

## 🎯 Quick Decision Flowchart

```
Need to track something?
│
├── Just existence? ──────────────► HashSet
│   "Have I seen this before?"
│
├── Need count/frequency? ────────► HashMap {item: count}
│   "How many times?"
│
├── Need value association? ──────► HashMap {key: value}
│   "What maps to what?"
│
├── Need index? ──────────────────► HashMap {value: index}
│   "Where was this?"
│
└── Need grouping? ───────────────► HashMap {property: [items]}
    "Which go together?"
```

---

## ⚠️ Common Pitfalls

| Pitfall | Fix |
|---|---|
| Forgetting `{0: 1}` in prefix sum | Always init with base case |
| Using mutable types as dict keys | Use `tuple()` instead of `list` |
| Not handling empty input | Check `if not arr` first |
| Off-by-one in sliding window | Carefully define window boundaries |
| Checking `if map[key]` instead of `if key in map` | Use `in` for existence, `[]` for value |

---

These 8 patterns cover **~90%** of all HashMap/HashSet problems you'll encounter in interviews. The key skill is recognizing which pattern fits from the problem's keywords and constraints.
