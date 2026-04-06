# Two Pointers — Converging Pattern

> **Core idea:** Start pointers at both ends of a **sorted** (or indexable) structure, move them inward based on a condition until they meet.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Two Sum II** | [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | O(n) | O(1) | Sort guaranteed. Two pointers — sum too big? move `end` left. Too small? move `start` right. | — |
| 2 | **3Sum** | [#15](https://leetcode.com/problems/3sum/) | O(n²) | O(1) | Sort + fix `i`, two-pointer on the rest to find pairs summing to `-nums[i]`. | **Skip duplicates at 3 places:** ① `if i > 0 and nums[i] == nums[i-1]: continue` ② after a match, `while start < end and nums[start] == nums[start+1]: start += 1` ③ `while start < end and nums[end] == nums[end-1]: end -= 1`. Miss any one → duplicate triplets. |
| 3 | **3Sum Closest** | [#16](https://leetcode.com/problems/3sum-closest/) | O(n²) | O(1) | Same as 3Sum but track closest sum via `abs(total - target) < abs(closestSum - target)`. | — |
| 4 | **Container With Most Water** | [#11](https://leetcode.com/problems/container-with-most-water/) | O(n) | O(1) | Area = `min(h[left], h[right]) × (right - left)`. Always move the **shorter** side inward. | — |
| 5 | **Valid Palindrome** | [#125](https://leetcode.com/problems/valid-palindrome/) | O(n) | O(1) | Two pointers from ends, skip non-alphanumeric with `continue`, compare `.lower()`. | — |
| 6 | **Squares of a Sorted Array** | [#977](https://leetcode.com/problems/squares-of-a-sorted-array/) | O(n) | O(1)* | Largest squares are at the **edges** (big negatives left, big positives right). Compare `|start|` vs `|end|`, fill result from the back. *Result not counted as extra space. | — |

---

## When to Use Converging Two Pointers

- Array is **sorted** (or problem benefits from sorting first)
- Looking for **pairs/triplets** that satisfy a sum condition
- Need to **compare elements from both ends** (palindrome, container)
- Want **O(1) space** instead of hash map

---
---

# Two Pointers — String Reversal Pattern

> **Core idea:** Two pointers at both ends, swap and move inward. Variation: skip certain characters, or reverse in chunks (whole string → per word).

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Reverse String** | [#344](https://leetcode.com/problems/reverse-string/) | O(n) | O(1) | Two pointers from ends, swap and move inward. In-place. | — |
| 2 | **Reverse Vowels of a String** | [#345](https://leetcode.com/problems/reverse-vowels-of-a-string/) | O(n) | O(n) | Two pointers from ends, each skips non-vowels. When both land on vowels → swap. | — |
| 3 | **Reverse Words in a String** | [#151](https://leetcode.com/problems/reverse-words-in-a-string/) | O(n) | O(n) | Clean spaces via `split+join`, convert to list. Reverse entire string, then reverse each word back. | **`s.split()` strips ALL extra spaces** → `" ".join(...)` adds exactly 1 space → `list(...)` makes it mutable (strings are immutable, can't swap). Two-pass reverse: whole-string reverse flips word order but scrambles letters, per-word reverse fixes letters. |

---

## When to Use String Reversal Two Pointers

- Need to reverse **in-place** (no extra string allocation)
- Reverse **selectively** — only vowels, only words, skip certain chars
- Trick: **reverse twice** (whole + parts) to reorder segments

---
---

# Two Pointers — In-place Array Modification Pattern

> **Core idea:** Use a slow/write pointer to build the result in-place while a fast/scan pointer reads through the array. No extra array needed.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Remove Element** | [#27](https://leetcode.com/problems/remove-element/) | O(n) | O(1) | If `nums[i] == val` → overwrite with last element, shrink `n`. Else move `i`. | Don't advance `i` after overwrite — the swapped-in value is unchecked. |
| 2 | **Remove Duplicates** | [#26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | O(n) | O(1) | `next_unique` write pointer starts at 1. If `nums[i] != nums[i-1]` → write it. | — |
| 3 | **Remove Duplicates (allow 2)** | [#80](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | O(n) | O(1) | Same idea but start at 2. Compare `nums[i]` with `nums[next_unique - 2]`. | — |
| 4 | **Move Zeroes** | [#283](https://leetcode.com/problems/move-zeroes/) | O(n) | O(1) | `start` = write pointer. If non-zero → swap with `start`, advance. Zeroes end up at back. | — |
| 5 | **Dutch National Flag** | [#75](https://leetcode.com/problems/sort-colors/) | O(n) | O(1) | 3 pointers: `start` (0s boundary), `mid` (scanner), `end` (2s boundary). Swap based on `mid` value. | When `mid == 2` and you swap with `end` → **don't advance mid** — the swapped-in value is unchecked. |

---

## When to Use In-place Array Modification

- Problem says **"modify in-place"** or **"return new length"**
- Need to **partition** elements (remove, move, sort by category)
- Write pointer builds the clean result while scan pointer reads ahead

---
---

# Two Pointers — Fast & Slow Pointers Pattern

> **Core idea:** Two pointers move at **different speeds** — slow (1 step) and fast (2 steps). Used for cycle detection, finding midpoints, or matching at different rates.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Linked List Cycle** | [#141](https://leetcode.com/problems/linked-list-cycle/) | O(n) | O(1) | Slow (1 step), fast (2 steps). If they meet → cycle. If fast hits None → no cycle. | — |
| 2 | **Start of Linked List Cycle** | [#142](https://leetcode.com/problems/linked-list-cycle-ii/) | O(n) | O(1) | Phase 1: detect cycle (slow/fast meet). Phase 2: reset slow to head, both move 1 step → meet at cycle start. | Floyd's algo Phase 2: **reset slow to head, NOT fast**. Both move 1 step now. |
| 3 | **Middle of Linked List** | [#876](https://leetcode.com/problems/middle-of-linked-list/) | O(n) | O(1) | Slow (1 step), fast (2 steps). When fast reaches end, slow is at middle. | Even-length: returns **second** middle because `while fast and fast.next` lets slow take one extra step. |
| 4 | **Happy Number** | [#202](https://leetcode.com/problems/happy-number/) | O(log n) | O(1) | Treat digit-square-sum sequence as a linked list. Slow = 1 call, fast = 2 calls. Cycle = not happy, reaches 1 = happy. | — |
| 5 | **Find the Duplicate Number** | [#287](https://leetcode.com/problems/find-the-duplicate-number/) | O(n) | O(1) | Array as linked list: `index → nums[index]`. Duplicate = cycle. Floyd's Phase 1 + Phase 2 → duplicate value. | Start both at `nums[0]` not `0`. Array values are the "next pointers". |
| 6 | **Is Subsequence** | [#392](https://leetcode.com/problems/is-subsequence/) | O(n) | O(1) | Slow scans `s`, fast scans `t`. Match → advance both. No match → advance fast only. If slow reaches end → True. | — |

---

## When to Use Fast & Slow Pointers

- **Cycle detection** in linked lists or sequences (Floyd's algorithm)
- Finding the **middle** of a linked list in one pass
- Any problem where a sequence can **loop** (happy number, duplicate in array)
- Two sequences scanned at **different rates** (subsequence)
