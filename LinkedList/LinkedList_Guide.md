# Linked List — Patterns & Problem Guide

> **Core idea:** Linked lists use pointer manipulation instead of index-based access. Most problems rely on a small set of recurring patterns.

---

## Key Concepts

### Dummy Node (Sentinel)
Use when the **head might change** or you need a uniform "previous node."

```
dummy -> [1] -> [2] -> [3]
  ^
 always stays here — return dummy.next at the end
```

**Use dummy when:**
- Head might be removed (remove elements, remove duplicates)
- Merging/building a new list from scratch
- Partial reversal starting at position 1
- Partitioning a list

**Skip dummy when:**
- Head never changes (detect cycle, find middle, reverse entire list)

### ⚠️ Gotcha: Dummy doesn't move — its `.next` gets updated

A common confusion: "If the head is removed, how does dummy know the new head?"

**Dummy never moves.** But `dummy.next` gets **reassigned** by the algorithm.

```
Start:
    dummy -> [1] -> [2] -> [3]       dummy.next = node(1) = head
    prev = dummy                     (prev and dummy point to SAME object)

Now suppose we remove node(1) (the head):
    prev.next = node(1).next         i.e., prev.next = node(2)

    But prev IS dummy (same object in memory)!
    So prev.next = node(2) is the SAME as dummy.next = node(2).
    You updated dummy.next without ever touching dummy directly.

Result:
    dummy -> [2] -> [3]              dummy.next = node(2) = NEW head
      ^
     prev (still here, never moved)

    node(1) still exists in memory but nothing points to it anymore.
    Neither dummy nor prev moved — we just changed what their .next points to.
    And since they're the same object, changing prev.next IS changing dummy.next.
```

**This is the key insight:** when `prev` hasn't moved from `dummy`, they're the
same node. So `prev.next = something` automatically updates `dummy.next`.
That's why `return dummy.next` gives the correct new head even though you
never wrote `dummy.next = ...` explicitly — you wrote `prev.next = ...` which
did the same thing.

**Where it gets confusing — reversal (Reverse Linked List II, left=1):**
```
Before reversal:
    dummy -> [1] -> [2] -> [3] -> [4]
              ^
         dummy.next still points to node(1)

After reversing nodes 1-3:
    Reversed: [3] -> [2] -> [1]     prev = node(3)
    Remaining: [4]                   curr = node(4)
    But dummy.next is STILL node(1)! (old head, now the TAIL of reversed)

Reconnection fixes it:
    dummy.next.next = curr    →  node(1).next = node(4)   (tail -> rest)
    dummy.next = prev         →  dummy.next = node(3)     (dummy -> new head)

Final:
    dummy -> [3] -> [2] -> [1] -> [4]
```

**Key takeaway:** dummy sits still. The algorithm updates `dummy.next`
(either directly or through `prev_left.next` when `prev_left == dummy`).
That's why `return dummy.next` always gives the correct new head.

### Why `curr = head` instead of using `head` directly?
- If you traverse with `head`, you lose the reference to the start.
- `curr` walks the list; `head` (or `dummy.next`) stays as your bookmark.

### Pointer Wiring Order Matters
Always **save the next node before breaking a link**, or you'll lose the rest of the list:
```python
nxt = curr.next       # save first!
curr.next = prev      # now safe to break the link
```

---

## Pattern 1: Reversal (3-Pointer Technique)

> Reverse pointers one by one using `prev`, `curr`, `nxt`.

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Reverse Linked List** | [#206](https://leetcode.com/problems/reverse-linked-list/) | O(n) | O(1) | 3 pointers: save `nxt = curr.next`, reverse `curr.next = prev`, advance both. When `curr` is None, `prev` is new head. | No dummy needed — just return `prev`. |
| 2 | **Reverse Linked List II** | [#92](https://leetcode.com/problems/reverse-linked-list-ii/) | O(n) | O(1) | Walk to node before `left` (`prev_left`). Reverse `right - left + 1` nodes. Reconnect: `prev_left.next.next = curr`, `prev_left.next = prev`. | **Dummy needed** — if `left=1`, head changes. `range(right - left + 1)` includes both endpoints. |

### When to Use Reversal
- Reverse entire or partial list
- Reverse in k-groups
- Palindrome check (reverse second half)

---

## Pattern 2: Merge / Build with Dummy

> Use a dummy node as starting anchor. `curr` pointer builds the result list.

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Merge Two Sorted Lists** | [#21](https://leetcode.com/problems/merge-two-sorted-lists/) | O(n+m) | O(1) | Dummy + curr. Compare heads, pick smaller, advance. `curr.next = list1 if list1 else list2` appends remainder. | Remaining portion is already sorted and ≥ last merged node — just link directly. |

### When to Use Merge/Build
- Merging sorted lists
- Building a result list from two or more sources
- Any problem where you construct a new list node by node

---

## Pattern 3: Two-Pointer Gap (Fast & Slow)

> Create a fixed gap between two pointers, or move at different speeds.

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Remove Nth From End** | [#19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | O(n) | O(1) | Advance `fast` by n, then move both until `fast.next` is None. `slow` lands before the target. | **Two valid styles:** `range(n)` + `while fast.next` OR `range(n+1)` + `while fast`. Same result. **Dummy needed** — removing head when n = list length. |
| 2 | **Middle of Linked List** | [#876](https://leetcode.com/problems/middle-of-linked-list/) | O(n) | O(1) | Slow (1 step), fast (2 steps). When fast reaches end, slow is at middle. | Even-length: returns second middle (`while fast and fast.next`). |
| 3 | **Linked List Cycle** | [#141](https://leetcode.com/problems/linked-list-cycle/) | O(n) | O(1) | Slow (1 step), fast (2 steps). If they meet → cycle. | — |
| 4 | **Linked List Cycle II** | [#142](https://leetcode.com/problems/linked-list-cycle-ii/) | O(n) | O(1) | Phase 1: detect cycle. Phase 2: reset slow to head, both move 1 step → meet at cycle start. | Floyd's algo: reset **slow** to head, NOT fast. |

### When to Use Two-Pointer Gap
- Find nth from end in one pass
- Find middle of list
- Cycle detection (Floyd's algorithm)
- Check if list is a palindrome (find middle → reverse second half → compare)

---

## Pattern 4: Skip / Remove Nodes

> Traverse with `curr` (or `prev` + `curr`), skip nodes that match a condition.

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Remove Duplicates (Sorted)** | [#83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | O(n) | O(1) | Look forward: if `curr.val == curr.next.val` → skip (`curr.next = curr.next.next`), else advance. | **No dummy needed** — head never changes (keep first occurrence). Don't advance `curr` after skip — new next might also be duplicate. |
| 2 | **Remove Duplicates II (Sorted)** | [#82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | O(n) | O(1) | `prev` + `curr`. When duplicate found, save `dup_value`, skip ALL nodes with that value, then `prev.next = curr`. | **Dummy needed** — head itself might be a duplicate. `prev` only advances on confirmed unique nodes. |

### When to Use Skip/Remove
- Remove nodes by value or condition
- Remove duplicates (keep one or keep none)
- Filter nodes in-place

---

## Pattern 5: Hashmap + Linked List

> Use a hashmap to store node mappings for O(1) lookup during construction.

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Copy List with Random Pointer** | [#138](https://leetcode.com/problems/copy-list-with-random-pointer/) | O(n) | O(n) | Pass 1: create copy nodes, store `old → new` in hashmap. Pass 2: wire `next` and `random` using hashmap lookup. | `old_to_new = {None: None}` trick handles null pointers without extra if-checks. Use `curr` to traverse — don't lose `head` (needed for Pass 2). |

### When to Use Hashmap + Linked List
- Deep copy with extra pointers (random, arbitrary)
- LRU Cache (hashmap + doubly linked list)
- Finding intersections or detecting patterns across nodes

---

## Quick Reference: Which Pattern to Use?

| If the problem says... | Use this pattern |
|------------------------|-----------------|
| Reverse (all or part) | Reversal (3-pointer) |
| Merge sorted lists | Merge with dummy |
| Nth from end / middle / cycle | Two-pointer gap (fast & slow) |
| Remove / skip / filter nodes | Skip/Remove with prev + curr |
| Deep copy / clone | Hashmap + linked list |
| Head might change | Dummy node |
| Build a new list | Dummy node |

---

## Common Mistakes

1. **Forgetting to save `nxt` before reversing** → lose the rest of the list
2. **Using `head` to traverse** → lose reference to the start
3. **Shadowing parameter names** (`left = dummy` when `left` is an int param) → TypeError
4. **Off-by-one in reversal range** → `range(right - left + 1)` for inclusive range
5. **Moving `prev` on duplicates** → `prev` should only advance on confirmed unique nodes
6. **Skipping dummy when head can change** → returning stale head
