# Two Pointers — Converging Pattern

> **Core idea:** Start pointers at both ends of a **sorted** (or indexable) structure, move them inward based on a condition until they meet.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Two Sum II** | [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | O(n) | O(1) | Sort guaranteed. Two pointers — sum too big? move `end` left. Too small? move `start` right. | Array is **1-indexed** in LeetCode — return `[left+1, right+1]`. |
| 2 | **3Sum** | [#15](https://leetcode.com/problems/3sum/) | O(n²) | O(1) | Sort + fix `i`, two-pointer on the rest to find pairs summing to `-nums[i]`. | **Skip duplicates at 3 places:** ① `if i > 0 and nums[i] == nums[i-1]: continue` ② after a match, `while start < end and nums[start] == nums[start+1]: start += 1` ③ `while start < end and nums[end] == nums[end-1]: end -= 1`. Miss any one → duplicate triplets. |
| 3 | **3Sum Closest** | [#16](https://leetcode.com/problems/3sum-closest/) | O(n²) | O(1) | Same as 3Sum but track closest sum via `abs(total - target) < abs(closestSum - target)`. | Init `closestSum = float('inf')`. If exact match found, **return immediately** — can't beat distance 0. |
| 4 | **Container With Most Water** | [#11](https://leetcode.com/problems/container-with-most-water/) | O(n) | O(1) | Area = `min(h[left], h[right]) × (right - left)`. Always move the **shorter** side inward. | Moving the **taller** side can never help — the bottleneck is the short side, and width is shrinking. |
| 5 | **Valid Palindrome** | [#125](https://leetcode.com/problems/valid-palindrome/) | O(n) | O(1) | Two pointers from ends, skip non-alphanumeric with `continue`, compare `.lower()`. | Use `continue` after skipping — without it you'd fall through and compare a junk char. |
| 6 | **Squares of a Sorted Array** | [#977](https://leetcode.com/problems/squares-of-a-sorted-array/) | O(n) | O(1)* | Largest squares are at the **edges** (big negatives left, big positives right). Compare `|start|` vs `|end|`, fill result from the back. | Fill result array **right to left** (index `n-1` → `0`). If you fill left to right you'd need to reverse. *Result array is required output, not extra space. |

---

## When to Use Converging Two Pointers

- Array is **sorted** (or problem benefits from sorting first)
- Looking for **pairs/triplets** that satisfy a sum condition
- Need to **compare elements from both ends** (palindrome, container)
- Want **O(1) space** instead of hash map
