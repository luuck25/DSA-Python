"""
=============================================================================
  TRICKY MAP / DICT USAGE PATTERNS — HackerRank Style
=============================================================================
"""

from collections import defaultdict, Counter, OrderedDict
from re import split

# ═══════════════════════════════════════════════════════════════════════════
# PROBLEM: E-Commerce Product Grouping
# ═══════════════════════════════════════════════════════════════════════════
# Group products by category (alphabetical), show names sorted by price desc,
# and compute average price per category.
#
# Input:  ["101|Laptop|Electronics|999.99", "102|Mouse|Electronics|29.99", ...]
# Output: ["Electronics: Laptop, Mouse (avg: 514.99)", ...]


# ---------- Approach 1: defaultdict(list) — append tuples ----------
# Key trick: defaultdict auto-creates an empty list on first access.
#            Each value is a list of (name, price) tuples.

def analyze_products_v1(products):
    mp = defaultdict(list)                         # category → [(name, price), ...]

    for product in products:
        _, item, category, price = product.split('|')
        mp[category].append((item, float(price)))  # just append tuple — clean & simple

    result = []
    for category in sorted(mp):                    # sorted keys → alphabetical categories
        items = mp[category]
        sorted_items = sorted(items, key=lambda x: -x[1])           # price desc
        avg_price = sum(price for _, price in items) / len(items)    # average
        items_list = ', '.join(item for item, _ in sorted_items)     # names string
        result.append(f"{category}: {items_list} (avg: {avg_price:.2f})")

    return result


# ---------- Approach 2: plain dict — tuple value (total, count, list) ----------
# Key trick: each dict value is a TUPLE (total_price, count, items_list).
#            Must rebuild the tuple on every update (tuples are immutable).
#            More manual but avoids defaultdict import.

def analyze_products_v2(products):
    mp = {}                                        # category → (total_price, count, [(name, price)])

    for product in products:
        _, item_name, category, price = product.split('|')
        price = float(price)

        if category in mp:
            tot_price, count, items = mp[category]
            items = items + [(item_name, price)]   # create NEW list (don't mutate)
            mp[category] = (tot_price + price, count + 1, items)  # rebuild tuple
        else:
            mp[category] = (price, 1, [(item_name, price)])       # first entry

    result = []
    for k in sorted(mp.keys()):
        tot_price, count, items = mp[k]
        items_sorted = sorted(items, key=lambda x: -x[1])
        names = [name for name, _ in items_sorted]
        avg = tot_price / count
        result.append(f"{k}: {', '.join(names)} (avg: {avg:.2f})")

    return result


# ═══════════════════════════════════════════════════════════════════════════
#  MORE TRICKY MAP PATTERNS — Common in HackerRank / Interviews
# ═══════════════════════════════════════════════════════════════════════════


# ---------- Pattern 1: dict.setdefault — one-liner grouping ----------
# Like defaultdict but works on a plain dict.
# setdefault(key, []) → returns existing list OR creates & inserts [] first.

def group_words_by_length(words):
    mp = {}
    for w in words:
        mp.setdefault(len(w), []).append(w)        # no KeyError, no `if` check
    return mp
# {3: ['cat', 'dog'], 5: ['hello', 'world']}


# ---------- Pattern 2: dict comprehension with zip ----------
# Build a map from two parallel lists in one line.

keys = ["a", "b", "c"]
vals = [1, 2, 3]
mp = {k: v for k, v in zip(keys, vals)}           # {'a': 1, 'b': 2, 'c': 3}
# Also: dict(zip(keys, vals)) — even shorter


# ---------- Pattern 3: Counter arithmetic ----------
# Counter supports +, -, &, | between counters.

def common_chars(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    common = c1 & c2                               # min of each count (intersection)
    return list(common.elements())                  # ['a', 'b'] etc.
# Counter("aabbc") & Counter("abbcd") → Counter({'b': 2, 'a': 1})


# ---------- Pattern 4: defaultdict(int) — auto 0 counter ----------
# Avoids .get(key, 0) + 1 everywhere.

def char_frequency(s):
    freq = defaultdict(int)
    for ch in s:
        freq[ch] += 1                              # no KeyError — starts at 0
    return dict(freq)



# ---------- Pattern 5: defaultdict(set) — unique grouping ----------
# Like defaultdict(list) but auto-deduplicates.

def group_unique_tags(items):
    # items = [("post1", "python"), ("post1", "python"), ("post1", "java")]
    mp = defaultdict(set)
    for post, tag in items:
        mp[post].add(tag)                          # duplicates ignored
    return mp
# {"post1": {"python", "java"}}


# ---------- Pattern 6: dict as switch / dispatch ----------
# Replace long if-elif chains with a function map.

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

ops = {"+": add, "-": sub, "*": mul}
result = ops["+"](3, 4)                            # 7 — no if/elif needed


# ---------- Pattern 7: Inverting a dict (value → key) ----------
# Useful when you need reverse lookups.

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}     # {1: 'a', 2: 'b', 3: 'c'}
# ⚠️ Only works if values are unique — duplicates overwrite


# ---------- Pattern 8: Nested defaultdict ----------
# Auto-create nested dicts without checking existence.

def build_adjacency_with_weights(edges):
    # edges = [("A","B",5), ("A","C",3)]
    graph = defaultdict(lambda: defaultdict(int))
    for u, v, w in edges:
        graph[u][v] = w                            # graph["A"]["B"] = 5 — no KeyError
        graph[v][u] = w
    return graph


# ---------- Pattern 9: map() + split for parsing ----------
# HackerRank loves this — parse "1 2 3" into [1, 2, 3] in one line.

line = "10 20 30"
nums = list(map(int, line.split()))                # [10, 20, 30]

# Parse multiple lines into list of tuples:
# data = ["Alice 90", "Bob 85"]
# records = [(name, int(score)) for name, score in (line.split() for line in data)]


# ---------- Pattern 10: sorted() with dict — multiple sort keys ----------
# Sort dict items by value desc, then key asc (tie-breaker).

scores = {"Alice": 90, "Bob": 95, "Charlie": 90}
ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
# [('Bob', 95), ('Alice', 90), ('Charlie', 90)]
# -x[1] → descending score, x[0] → alphabetical name for ties


# ---------- Pattern 11: Accumulate into dict with tuple values ----------
# Track multiple stats per key without separate dicts.
# Same idea as Approach 2 above — one dict, compound value.

def stats_per_category(records):
    # records = [("Electronics", 100), ("Electronics", 200), ("Books", 50)]
    mp = {}
    for cat, price in records:
        if cat in mp:
            total, count, mn, mx = mp[cat]
            mp[cat] = (total + price, count + 1, min(mn, price), max(mx, price))
        else:
            mp[cat] = (price, 1, price, price)     # (total, count, min, max)
    return mp
# {"Electronics": (300, 2, 100, 200), "Books": (50, 1, 50, 50)}
