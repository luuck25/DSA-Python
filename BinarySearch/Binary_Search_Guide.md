# Binary Search Guide

> **Core idea:** Repeatedly divide the search space in half to find a target or satisfy a condition. Works on **sorted** data or **monotonic** answer spaces. Always O(log n) time.

---

# ⚡ Binary Search Templates — Which One to Use?

> **The most confusing part of binary search:** When to use `left <= right` vs `left < right`? When `right = mid` vs `right = mid - 1`? What to return?

## Template 1: Finding Exact Target (Most Common)

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:  # ← Use <=
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid  # ← Return immediately when found
        elif nums[mid] < target:
            left = mid + 1  # ← Exclude mid
        else:
            right = mid - 1  # ← Exclude mid
    
    return -1  # Target not found
```

**When to use:**
- ✅ Finding an **exact value** in the array
- ✅ Standard "search for target" problems
- ✅ When you can **return immediately** upon finding the answer

**Why `left <= right`?**
- We need to check the case when `left == right` (one element left)
- Loop exits when `left > right` (search space exhausted)

**Why `left = mid + 1` and `right = mid - 1`?**
- We **exclude mid** because we already checked it
- Prevents infinite loops

**What to return?**
- Return `-1` or `left` (insertion position for "search insert position" problems)

---

## Template 2: Finding Boundary (First/Minimum Occurrence)

```python
def find_first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:  # ← Use < (not <=)
        mid = (left + right) // 2
        
        if nums[mid] < target:
            left = mid + 1  # ← Exclude mid
        else:
            right = mid  # ← Include mid (potential answer)
    
    return left  # ← Return left (or check if nums[left] == target)
```

**When to use:**
- ✅ Finding **first occurrence** (leftmost)
- ✅ Finding **minimum** in rotated array
- ✅ Finding **lower bound** (smallest element ≥ target)
- ✅ "Binary search on answer" problems (minimize)

**Why `left < right`?**
- Loop exits when `left == right` (converged to answer)
- We **don't exclude** the mid, so we need `<` to avoid infinite loop

**Why `right = mid` (not `mid - 1`)?**
- Mid could be the **answer** (first occurrence, minimum, etc.)
- We want to keep it in the search space

**What to return?**
- Return `left` (which equals `right` when loop exits)
- Left is the first/minimum position

**⚠️ Warning:** Never use `left = mid` with `left < right` — causes infinite loop when `left` and `right` are adjacent!

---

## Template 3: Finding Boundary (Last/Maximum Occurrence)

```python
def find_last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:  # ← Use <
        mid = (left + right + 1) // 2  # ← Round UP to avoid infinite loop
        
        if nums[mid] > target:
            right = mid - 1  # ← Exclude mid
        else:
            left = mid  # ← Include mid (potential answer)
    
    return left  # ← Return left (or check if nums[left] == target)
```

**When to use:**
- ✅ Finding **last occurrence** (rightmost)
- ✅ Finding **maximum** that satisfies condition
- ✅ Finding **upper bound** (largest element ≤ target)

**Why `mid = (left + right + 1) // 2`?**
- When `left = mid`, we must round **UP** to avoid infinite loop
- Example: `left=3, right=4` → normal mid=3 → `left=mid=3` → infinite loop
- With +1: `left=3, right=4` → mid=4 → either `left=4` or `right=3` → terminates

**Why `left = mid` (not `mid + 1`)?**
- Mid could be the **answer** (last occurrence, maximum, etc.)
- We want to keep it in the search space

**What to return?**
- Return `left` (which equals `right` when loop exits)

---

## 📊 Template Comparison Table

| Template | Loop Condition | Left Update | Right Update | Mid Calculation | Use Case | Return |
|----------|---------------|-------------|--------------|-----------------|----------|--------|
| **Template 1** | `left <= right` | `mid + 1` | `mid - 1` | `(left + right) // 2` | Find exact target | `mid` when found, else `-1` or `left` |
| **Template 2** | `left < right` | `mid + 1` | `mid` | `(left + right) // 2` | Find first/minimum | `left` |
| **Template 3** | `left < right` | `mid` | `mid - 1` | `(left + right + 1) // 2` | Find last/maximum | `left` |

---

## 🔍 How to Choose the Right Template?

### Decision Flow:

```
Do you need to return immediately when target is found?
├─ YES → Use Template 1 (left <= right, exclude mid from both sides)
│         Examples: Standard binary search, search insert position
│
└─ NO → Need to find boundary/optimize
    │
    ├─ Finding FIRST/MINIMUM? → Use Template 2 (left < right, right = mid)
    │    Examples: First occurrence, find minimum in rotated array,
    │              minimize maximum (binary search on answer)
    │
    └─ Finding LAST/MAXIMUM? → Use Template 3 (left < right, left = mid, mid+1)
         Examples: Last occurrence, maximize minimum

```

---

## 💡 Quick Rules to Remember

1. **`left <= right`** → Can return immediately → Use `mid + 1` and `mid - 1`
2. **`left < right`** → Cannot return immediately → One side uses `mid` (includes it)
3. **`left = mid`** → MUST use `mid = (left + right + 1) // 2` to avoid infinite loop
4. **`right = mid`** → Can use normal `mid = (left + right) // 2`
5. **Return `left`** in most cases (equals `right` when `left < right` exits)

---

## 🐛 Common Infinite Loop Cases

| Scenario | Problem | Fix |
|----------|---------|-----|
| `while left < right`, `left = mid`, normal mid calc | When `left=3, right=4`, mid=3, stuck! | Use `mid = (left+right+1)//2` |
| `while left <= right`, `left = mid` or `right = mid` | Never narrows gap properly | Use `left = mid+1` and `right = mid-1` |
| Both `left = mid` and `right = mid` | Can't narrow search space | At least one must exclude mid (+1 or -1) |

---

## 📝 Example: Why Different Templates?

**Problem:** Find first and last occurrence of 8 in `[5,7,7,8,8,8,10]`

**Finding FIRST (Template 2):**
```python
# Use left < right, right = mid
while left < right:
    mid = (left + right) // 2
    if nums[mid] >= target:  # Found or too big
        right = mid  # Keep mid (might be first)
    else:
        left = mid + 1
return left  # First occurrence
```

**Finding LAST (Template 3):**
```python
# Use left < right, left = mid, round up
while left < right:
    mid = (left + right + 1) // 2  # Round up!
    if nums[mid] <= target:  # Found or too small
        left = mid  # Keep mid (might be last)
    else:
        right = mid - 1
return left  # Last occurrence
```

---

# Binary Search — Standard Array Search Pattern

> **Core idea:** Search for a target in a sorted array by comparing with the middle element and eliminating half the search space each iteration.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Binary Search** | [#704](https://leetcode.com/problems/binary-search/) | O(log n) | O(1) | Standard template: `mid = (left + right) // 2`. If `nums[mid] == target` → return. If `nums[mid] < target` → search right half. Else search left half. | **Use `mid = left + (right - left) // 2`** to avoid overflow in languages with fixed-size integers. |
| 2 | **Search Insert Position** | [#35](https://leetcode.com/problems/search-insert-position/) | O(log n) | O(1) | Same as binary search, but when loop exits, `left` is the insertion position. | Return `left` at the end — it points to where target should be inserted. |
| 3 | **First Bad Version** | [#278](https://leetcode.com/problems/first-bad-version/) | O(log n) | O(1) | Binary search on versions [1..n]. If `isBadVersion(mid)` → first bad is at mid or left. Else first bad is right. | Minimize API calls by using binary search. When `isBadVersion(mid)` is True, do `right = mid - 1` (not `right = mid`). |
| 4 | **Search a 2D Matrix** | [#74](https://leetcode.com/problems/search-a-2d-matrix/) | O(log(m×n)) | O(1) | Treat 2D matrix as flattened 1D array. `row = mid // n`, `col = mid % n`. Standard binary search. | **Index conversion:** 1D → 2D coordinates. Total elements = `m × n`. |
| 5 | **Sqrt(x)** | [#69](https://leetcode.com/problems/sqrtx/) | O(log n) | O(1) | Binary search on [0..x]. Check if `mid * mid <= x`. Track largest valid `mid`. | Check `mid * mid` instead of `mid` to avoid comparing with `x / mid` (division issues). |

---

## When to Use Standard Binary Search

- Array or sequence is **sorted**
- Looking for an **exact value** or **insertion position**
- Can convert problem to 1D search space (like 2D matrix → 1D)
- Need **O(log n)** lookup instead of O(n) linear scan

---

## Binary Search Template

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found, or return left for insertion position
```

---
---

# Binary Search — Find First/Last Occurrence Pattern

> **Core idea:** Modified binary search to find the **leftmost** (first) or **rightmost** (last) occurrence of a target in a sorted array with duplicates.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Find First and Last Position** | [#34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | O(log n) | O(1) | Two binary searches: ① Find first: when `nums[mid] == target`, record and search left (`right = mid - 1`). ② Find last: when `nums[mid] == target`, record and search right (`left = mid + 1`). | **Key difference from standard:** Don't return immediately when found — keep searching to find boundary. |
| 2 | **Search for a Range** | Same as #34 | O(log n) | O(1) | Same approach — find leftmost, then find rightmost. | Use a result variable to track the found index before narrowing search. |

---

## When to Use First/Last Occurrence Pattern

- Array has **duplicates** and you need boundaries
- Need to find the **range** of a target value
- Count occurrences: `last - first + 1`

---

## First/Last Occurrence Template

```python
def find_first(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_last(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            result = mid
            left = mid + 1   # Keep searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

---
---

# Binary Search — Rotated Array Pattern

> **Core idea:** Handle sorted arrays that have been rotated at some pivot. Determine which half is properly sorted, then decide which half to search.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Search in Rotated Sorted Array** | [#33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | O(log n) | O(1) | At each mid: ① Determine which half is sorted (`nums[mid] >= nums[left]` = left sorted). ② Check if target is in sorted half's range. ③ If yes, search that half. Else search other half. | **Key insight:** At least one half is always properly sorted. Compare `nums[mid]` with `nums[left]` to identify the sorted half. |
| 2 | **Search in Rotated Sorted Array II** | [#81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | O(log n) avg, O(n) worst | O(1) | Same as #33 but handles **duplicates**. If `nums[left] == nums[mid] == nums[right]`, can't determine sorted half → shrink both ends (`left++`, `right--`). | **Worst case O(n)** when all elements are duplicates. Must handle the ambiguous case specially. |
| 3 | **Find Minimum in Rotated Sorted Array** | [#153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | O(log n) | O(1) | Compare `nums[mid]` with `nums[right]`. If `nums[mid] > nums[right]` → minimum is in right half. Else minimum is at mid or left. | **Compare with right, not left.** Minimum is at the rotation pivot. |
| 4 | **Find Minimum in Rotated Sorted Array II** | [#154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | O(log n) avg, O(n) worst | O(1) | Same as #153 but if `nums[mid] == nums[right]` → can't determine which side → `right--`. | Duplicates make it ambiguous, must shrink search space carefully. |
| 5 | **Peak Index in Mountain Array** | [#852](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | O(log n) | O(1) | Mountain = increases then decreases. If `arr[mid] < arr[mid+1]` → peak is right. Else peak is at mid or left. | **Guaranteed one peak.** Compare `mid` with `mid+1` to determine direction. |

---

## When to Use Rotated Array Binary Search

- Sorted array that was **rotated** at some unknown pivot
- Need to find **minimum/maximum** after rotation
- **Mountain array** pattern (increases then decreases)
- At least one half is always properly sorted

---

## Rotated Array Template

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[mid] >= nums[left]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in sorted left half
            else:
                left = mid + 1   # Target in rotated right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in sorted right half
            else:
                right = mid - 1  # Target in rotated left half
    
    return -1
```

---
---

# Binary Search — Binary Search on Answer Pattern

> **Core idea:** The search space is **not the input array**, but the **range of possible answers**. Binary search on the answer, and for each candidate, check if it satisfies the condition in O(n) or better.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Koko Eating Bananas** | [#875](https://leetcode.com/problems/koko-eating-bananas/) | O(n log m) | O(1) | Binary search on eating speed [1..max(piles)]. For each speed `k`, calculate hours needed = `sum(ceil(pile/k))`. If hours ≤ h → try slower. Else try faster. | **Search space is the answer (speed), not the array.** For each mid, verify in O(n) by calculating total hours. |
| 2 | **Capacity To Ship Packages Within D Days** | [#1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | O(n log S) | O(1) | Binary search on capacity [max(weights)..sum(weights)]. For each capacity, simulate loading: count days needed. If days ≤ D → try smaller capacity. Else larger. | **Minimum capacity must be ≥ max(weights)** (can't split packages). Maximum is sum(weights) (ship all at once). |
| 3 | **Split Array Largest Sum** | [#410](https://leetcode.com/problems/split-array-largest-sum/) | O(n log S) | O(1) | Binary search on max subarray sum [max(nums)..sum(nums)]. For each limit, count subarrays needed. If count ≤ k → try smaller limit. Else larger. | **Similar to package shipping.** Each subarray = partition. |
| 4 | **Kth Missing Positive Number** | [#1539](https://leetcode.com/problems/kth-missing-positive-number/) | O(log n) | O(1) | Binary search on array indices. At index `i`, missing count = `arr[i] - (i + 1)`. Find largest index where missing < k. Answer = `left + k`. | **Not searching for a value in array, but using array to calculate missing count.** Formula: `arr[i] - (i+1)` gives missing numbers before index i. |
| 5 | **Minimize Maximum** | Various | O(n log range) | O(1) | General pattern: binary search on the answer range. For each candidate answer, verify if it's achievable in O(n). Minimize the maximum or maximize the minimum. | **"Minimize the maximum" or "maximize the minimum"** are strong hints for binary search on answer. |

---

## When to Use Binary Search on Answer

- Problem asks to **"minimize the maximum"** or **"maximize the minimum"**
- Answer has a **monotonic** property: if X works, all values > X also work (or vice versa)
- Can **verify** a candidate answer in O(n) or better
- Search space is a **range of numbers** (not positions in array)

---

## Binary Search on Answer Template

```python
def binary_search_on_answer(input_data, constraint):
    # Define the search space [left, right]
    left = minimum_possible_answer
    right = maximum_possible_answer
    
    def is_valid(candidate):
        """Check if candidate answer satisfies the constraint."""
        # Verify in O(n) or better
        return True/False
    
    while left < right:
        mid = (left + right) // 2
        
        if is_valid(mid):
            right = mid  # Try to minimize (or left = mid + 1 to maximize)
        else:
            left = mid + 1  # Need larger value
    
    return left  # Optimal answer
```

---
---

# Binary Search — Special Conditions Pattern

> **Core idea:** Binary search with unique twist — special array properties, pair checking, or non-standard conditions.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Single Element in Sorted Array** | [#540](https://leetcode.com/problems/single-element-in-a-sorted-array/) | O(log n) | O(1) | Array has pairs except one single. **Pattern:** before single, pairs start at even indices. After single, pairs start at odd. Ensure `mid` is even. If `nums[mid] == nums[mid+1]` → single is right. Else left or at mid. | **Force mid to even index:** `if mid % 2 == 1: mid -= 1`. This maintains the pair pattern check. |
| 2 | **Find Peak Element** | [#162](https://leetcode.com/problems/find-peak-element/) | O(log n) | O(1) | Peak is element > neighbors. If `nums[mid] < nums[mid+1]` → peak is right (ascending). Else peak is at mid or left (descending). | **Any peak works** (multiple peaks possible). Always compare `mid` with `mid+1`. |
| 3 | **Median of Two Sorted Arrays** | [#4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | O(log(min(m,n))) | O(1) | Binary search on smaller array to partition both. `partition1 + partition2 = (m+n+1)/2`. Check if `left1 ≤ right2 AND left2 ≤ right1`. If valid → found median. | **One of the hardest binary search problems.** Must binary search on the **smaller array**. Partition logic is complex. |
| 4 | **Time-Based Key-Value Store** | [#981](https://leetcode.com/problems/time-based-key-value-store/) | O(log n) get | O(1) get | Store values with timestamps in list per key. `get()` does binary search to find largest timestamp ≤ target. | **Timestamps are strictly increasing** (guaranteed). Search for floor value. |
| 5 | **Search a 2D Matrix II** | [#240](https://leetcode.com/problems/search-a-2d-matrix-ii/) | O(m + n) | O(1) | NOT binary search. Start at top-right: if `target < current` → move left. If `target > current` → move down. | **Different from #74.** Rows sorted, columns sorted, but no relationship between row end and next row start. Staircase search, not binary. |

---

## When to Use Special Conditions Binary Search

- Array has **unique patterns** (pairs, peaks, partitions)
- Need to find **floor/ceiling** values (largest ≤ target, smallest ≥ target)
- Problem with **monotonic property** but non-standard comparison
- Requires creative application of binary search principles

---
---

# Common Binary Search Pitfalls

## 1. **Infinite Loop** 
- **Cause:** Using `while left < right` with `left = mid` or `right = mid`
- **Fix:** Use `left = mid + 1` and `right = mid - 1`, OR use `while left < right` with `mid = (left + right + 1) // 2` for `left = mid`

## 2. **Integer Overflow** (in Java/C++)
- **Cause:** `mid = (left + right) / 2` overflows when left + right > MAX_INT
- **Fix:** `mid = left + (right - left) / 2`

## 3. **Off-by-One Errors**
- **Cause:** Confusing whether to include/exclude mid, when to use ≤ vs <
- **Fix:** Be consistent: `while left <= right` with `left = mid + 1` and `right = mid - 1`

## 4. **Wrong Comparison in Rotated Arrays**
- **Cause:** Comparing `nums[mid]` with `nums[right]` when should compare with `nums[left]` (or vice versa)
- **Fix:** For finding minimum, compare with `right`. For search, compare with `left` to identify sorted half.

## 5. **Not Handling Edge Cases**
- **Cause:** Empty array, single element, all duplicates, target out of range
- **Fix:** Add checks before binary search: `if not nums: return -1`

---

# Binary Search Decision Tree

```
Is the problem asking to find something in a sorted space?
├─ YES: Binary Search is likely
│   ├─ Standard sorted array? → Standard Binary Search
│   ├─ Array rotated? → Rotated Array Pattern
│   ├─ Find first/last occurrence? → First/Last Pattern
│   ├─ "Minimize maximum" or "maximize minimum"? → Binary Search on Answer
│   └─ Special property (pairs, peaks)? → Special Conditions Pattern
└─ NO: Consider other approaches (two pointers, hash map, etc.)
```

---

# Time Complexity Cheat Sheet

| Pattern | Time | When | Example |
|---------|------|------|---------|
| Standard Binary Search | O(log n) | Search in sorted array | Binary Search |
| First/Last Occurrence | O(log n) | Find boundaries in sorted array with duplicates | Find First and Last Position |
| Rotated Array | O(log n) | Search/find in rotated sorted array | Search in Rotated Sorted Array |
| Binary Search on Answer | O(n log m) | Where m = answer range, n = verification cost | Koko Eating Bananas |
| 2D Matrix (flatten) | O(log(m×n)) | Sorted 2D matrix, row-first order | Search a 2D Matrix |

---

# Key Takeaways

1. **Binary Search = Divide and Conquer on Sorted/Monotonic Space**
2. **Three components:** Define search space, check condition, narrow space
3. **Always O(log n)** (except verification in "binary search on answer")
4. **Monotonic property is key:** if X works, then X+1 works (or vice versa)
5. **Not just for arrays:** Can search on answer ranges, rotated structures, implicit sequences
6. **Watch for rotated arrays:** Determine which half is sorted first
7. **"Minimize maximum" or "maximize minimum"** → Strong hint for binary search on answer

---

**Pro Tip:** When stuck on a binary search problem, ask yourself:
1. What is my search space? (array indices? answer range?)
2. What condition splits the space in half?
3. How do I know which half to keep?
4. What are the edge cases? (empty, single element, target not in range)
