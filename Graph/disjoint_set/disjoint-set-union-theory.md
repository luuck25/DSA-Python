# Disjoint Set (Union-Find) — A Beginner's Guide

> Based on the DSU series by **codestorywithMIK**:
> 1. [DSU Basics (video 18)](https://www.youtube.com/watch?v=AsAdKHkITBQ)
> 2. [Union by Rank + Path Compression (video 19)](https://www.youtube.com/watch?v=iH3XVIVzl7M)
> 3. [Union by Size + Path Compression (video 39)](https://www.youtube.com/watch?v=kGv33AiGhdc)
>
> The original videos use C++. Everything below is translated to plain Python, with
> zero assumed prior knowledge.

---

## 1. What even is a "Disjoint Set"?

A **disjoint set** is just a fancy name for: *"a bunch of groups, where no item belongs
to more than one group."* "Disjoint" literally means "non-overlapping."

Think of it like friend circles at a party:

```
Group A: {Alice, Bob}
Group B: {Charlie, Dave, Eve}
Group C: {Frank}
```

Nobody is in two groups at once — that's "disjoint."

**Disjoint Set Union (DSU)**, a.k.a. **Union-Find**, is a data structure that lets you
do two things, *fast*, even as groups keep merging over time:

1. **Find** — "which group does this item belong to?"
2. **Union** — "merge these two groups into one."

---

## 2. Why not just use BFS/DFS for this?

Good question! BFS/DFS can absolutely tell you "is X connected to Y" — but it has to
re-walk the whole graph **every single time** you ask, which is `O(V + E)` per query.

That's fine for a one-time check. But in a lot of real problems, you're not asking
once — you're adding connections **one at a time** and repeatedly asking "are these
connected *now*?" (this is called **dynamic connectivity**). Examples:

- Kruskal's algorithm adds edges one by one, checking "would this edge create a cycle?"
- "Accounts Merge" style problems keep merging more and more accounts together.
- "Number of Islands II" adds land tiles one at a time and asks for the island count
  after each addition.

Re-running BFS/DFS after every single addition would be way too slow. DSU answers
both `find` and `union` in **near-constant time**, no matter how many times you call
them. That's the whole appeal.

---

## 3. The core idea: parent pointers

Every element points to a **parent**. The "representative" (a.k.a. the **root** or
**leader**) of a group is whichever element points to *itself*.

- At the very start, every element is its own group, and its own parent.
- `find(x)` → keep following parent pointers until you hit a node that is its own
  parent. That's the root — the "ID" of the group.
- Two elements are in the same group **if and only if** `find(x) == find(y)`.
- `union(x, y)` → find both roots, and if they're different, make one root point to
  the other (merging the two groups into one).

### Naive version (Video 18)

```python
# parent[i] starts out pointing to itself — everyone is their own group
parent = list(range(n))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_x] = root_y   # just bolt one root onto the other
```

### The problem with the naive version

If you keep unioning in an unlucky order, the parent pointers can form one long
chain — basically turning your data structure into a linked list:

```
union(1, 2)   ->   1 -> 2
union(2, 3)   ->   1 -> 2 -> 3
union(3, 4)   ->   1 -> 2 -> 3 -> 4
union(4, 5)   ->   1 -> 2 -> 3 -> 4 -> 5
```

Now `find(1)` has to walk all the way through `2 -> 3 -> 4 -> 5`. For `n` elements,
that's `O(n)` per `find()` in the worst case — not the "fast" we were promised.

This is exactly the problem the next two tricks solve.

---

## 4. Optimization #1: Path Compression (Video 19)

**Idea:** every time `find(x)` walks up to the root, grab every node it passed
through and point it **directly** at the root. Next time, there's no chain to walk —
just one hop.

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # flatten on the way back up
    return parent[x]

    or

           def find(x):

            if x == par[x]:
                return x
            par[x] = find(par[x])    
            return par[x]
```

### Visual

Before `find(5)` (chain from the earlier example):

```
1 -> 2 -> 3 -> 4 -> 5
```

After `find(1)` with path compression:

```
1 -> 5
2 -> 5
3 -> 5
4 -> 5
```

Every node now points *straight* at the root. Future `find()` calls on any of these
are instant (one hop).

---

## 5. Optimization #2a: Union by Rank (Video 19)

Path compression fixes `find()` after the fact. **Union by Rank** prevents the chain
from forming in the first place, by being smart about *which* root gets attached to
which during `union()`.

**Rank** = a rough estimate of "how tall is the tree rooted here." The rule:

> When merging two groups, always attach the **shorter** tree under the root of the
> **taller** tree. If they're equally tall, pick either one, and the new root's rank
> goes up by 1.

This keeps the overall tree shallow — you never accidentally build a long chain.

```python
parent = list(range(n))
rank = [0] * n   # everyone starts as a tree of height 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # path compression
    return parent[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x == root_y:
        return  # already in the same group, nothing to do

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
```

### Full class version

```python
class DisjointSetByRank:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # already connected

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True
```

---

## 6. Optimization #2b: Union by Size (Video 39)

**Union by Size** is a sibling idea to Union by Rank — same goal (keep the tree
flat), different measurement. Instead of tracking "height," track **how many
elements** are in each group.

> When merging two groups, attach the **smaller** group under the root of the
> **larger** group. Fewer elements end up one hop deeper this way.

```python
class DisjointSetBySize:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n   # everyone starts as a group of size 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # already connected

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def group_size(self, x):
        """Bonus: how many elements are in x's group right now?"""
        return self.size[self.find(x)]
```

### Rank vs. Size — which one should I use?

| | Union by Rank | Union by Size |
|---|---|---|
| Tracks | estimated tree height | number of elements in the group |
| Merge rule | attach shorter tree under taller | attach smaller group under bigger |
| On a tie | bump rank by 1 | just add the sizes together |
| Speed (with path compression) | ~O(α(n)) per call — practically O(1) | ~O(α(n)) per call — practically O(1) |
| Extra freebie | none | `group_size(x)` — "how big is this group?" for free |

**They perform the same.** Pick Union by Size if your problem ever asks something
like *"what's the largest connected group?"* — you get that answer for free. Otherwise
it's a coin flip; both are standard and both show up constantly in interviews.

---

## 7. Worked example — tracing it by hand

Let's union some elements `0..6` using **union by size + path compression**, and
watch the `parent` / `size` arrays change.

```
Start:  parent = [0,1,2,3,4,5,6]   size = [1,1,1,1,1,1,1]

union(0, 1):
  find(0)=0, find(1)=1 — same size, attach 1 under 0
  parent = [0,0,2,3,4,5,6]   size = [2,1,1,1,1,1,1]

union(2, 3):
  find(2)=2, find(3)=3 — same size, attach 3 under 2
  parent = [0,0,2,2,4,5,6]   size = [2,1,2,1,1,1,1]

union(0, 2):
  find(0)=0 (size 2), find(2)=2 (size 2) — tie, attach 2's group under 0
  parent = [0,0,0,2,4,5,6]   size = [4,1,2,1,1,1,1]
  (note: 3's parent is still "2" here — it'll get path-compressed to 0
   the next time anyone calls find(3))

find(3):
  3 -> 2 -> 0.  Path compression rewires 3 straight to 0.
  parent = [0,0,0,0,4,5,6]

union(4, 5):
  parent = [0,0,0,0,4,4,6]   size = [4,1,2,1,2,1,1]

union(0, 4):
  find(0)=0 (size 4), find(4)=4 (size 2) — attach 4's group under 0
  parent = [0,0,0,0,0,4,6]   size = [6,1,2,1,2,1,1]
```

Everything from `0..5` now collapses to root `0` in one hop (after a `find` call or
two triggers the remaining compressions) — flat tree, fast lookups.

---

## 8. Where DSU shows up in real problems

Once you recognize the pattern "items keep merging into groups, and I keep needing
to ask who's connected to whom," reach for DSU:

- **Kruskal's Minimum Spanning Tree** — add edges in increasing weight order, but
  skip an edge if `find(u) == find(v)` (it would create a cycle).
- **Detect cycle in an undirected graph** — if `union(u, v)` finds `u` and `v`
  already in the same group, you just found a cycle.
- **Number of Provinces / Connected Components** — count how many distinct roots
  remain after processing all edges.
- **Accounts Merge** — union accounts that share an email, then group by root.
- **Number of Islands II** — add land tiles one at a time, union with any adjacent
  land, and answer "how many islands right now?" after each addition.
- **Redundant Connection** — find the one edge that, when added, creates a cycle.

---

## 9. TL;DR cheat sheet

- **Disjoint Set / Union-Find** = a fast way to track "who's in the same group as
  whom" while groups keep merging.
- Two operations: `find(x)` (which group?) and `union(x, y)` (merge groups).
- **Naive** version: simple, but can degrade to `O(n)` per operation on bad input.
- **Path Compression**: flattens the tree every time you call `find()`.
- **Union by Rank** *or* **Union by Size**: keeps the tree from getting tall in the
  first place, during `union()`. Pick either — same performance.
- **Both optimizations together** → `O(α(n))` per operation, where `α` is the
  inverse Ackermann function — grows so slowly it's basically a constant (≤ 4, ever,
  for any input size you'll encounter in practice).
- Use **Union by Size** specifically if you want "how big is this group?" for free.
