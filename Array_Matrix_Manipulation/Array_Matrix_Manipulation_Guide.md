# Array & Matrix Manipulation — Plus One Pattern

> **Core idea:** Simulate arithmetic on arrays digit by digit, processing right to left. Handle carry propagation manually.

<img width="640" height="425" alt="image" src="https://github.com/user-attachments/assets/7e12938b-795b-4f43-bcb0-b98d7e3189b3" />


---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Plus One** | [#66](https://leetcode.com/problems/plus-one/) | O(n) | O(1) | Walk from last digit backward. If < 9 → increment & return. If 9 → set to 0, carry propagates. | All 9s case (e.g. `[9,9,9]`) → loop finishes without returning → `return [1] + digits`. |
| 2 | **Add to Array-Form** | [#989](https://leetcode.com/problems/add-to-array-form-of-integer/) | O(max(n, log k)) | O(1) | Walk right to left, absorb digit into `k`. `k % 10` = current digit, `k // 10` = carry. After loop, prepend remaining `k` digits. | `k` itself acts as the carry — no separate carry variable needed. |
| 3 | **Multiply Strings** | [#43](https://leetcode.com/problems/multiply-strings/) | O(n1 × n2) | O(n1 + n2) | Grade-school multiplication. Product of `num1[i] × num2[j]` lands at `res[i+j+1]` (ones) and `res[i+j]` (tens). | `res[pos2] += total // 10` — must use `+=` not `=` because multiple products carry into the same position. |

---

## When to Use Plus One / Digit Arithmetic

- Number represented as an **array of digits** (can't convert to int — too large)
- Need to **add, multiply, or increment** digit by digit
- Key: process **right to left**, manage carry manually

---
---

# Array & Matrix Manipulation — In-Place Rotation Pattern

> **Core idea:** Rotate or transform arrays/matrices in-place using reversal tricks or layer-by-layer swaps. No extra space.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Rotate Array** | [#189](https://leetcode.com/problems/rotate-array/) | O(n) | O(1) | 3 reverses: reverse whole → reverse first k → reverse rest. `k = k % n` first. | Same trick as Reverse Words. `k % n` handles k > array length. |
| 2 | **Rotate Image (Matrix 90°)** | [#48](https://leetcode.com/problems/rotate-image/) | O(n²) | O(1) | Layer by layer, outside → inside. 4-way cycle swap per position. `range(right - left)` swaps per layer. | Save ↖ to temp, then chain: ↖←↙←↘←↗←temp. Each slot is safe to overwrite because its value already moved. `n-1` swaps per layer (corners shared). |
| 3 | **Transpose Matrix** | [#867](https://leetcode.com/problems/transpose-matrix/) | O(m × n) | O(m × n) / O(1)* | General: new `col × row` matrix, `res[j][i] = matrix[i][j]`. Square in-place: swap upper triangle only (`j = i+1`). | *In-place only works for **square** matrices. `j` starts at `i+1` to avoid double swap. Don't use `[[0]*row]*col` — all rows share same reference. |

---

## When to Use In-Place Rotation

- Problem says **"rotate in-place"** or **"do not allocate extra matrix"**
- **Array rotation** → 3-reverse trick
- **Matrix rotation** → layer-by-layer 4-way swap or transpose + reverse
- **Transpose** → swap `[i][j]` with `[j][i]`

---
---

# Array & Matrix Manipulation — Merge Sorted Array Pattern

> **Core idea:** Merge two sorted structures by comparing from the **back** (or front) using pointers, filling the result without extra space.

---
<img width="777" height="438" alt="image" src="https://github.com/user-attachments/assets/96d4b5bb-2e93-4592-9b85-f1cff6fbc843" />

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Merge Sorted Array** | [#88](https://leetcode.com/problems/merge-sorted-array/) | O(m + n) | O(1) | Fill from the **back**. Compare `nums1[i]` vs `nums2[j]`, place bigger at `nex_ele`, move that pointer left. Loop until `j < 0`. | Loop condition is `while j >= 0` only — if `nums2` is fully placed, remaining `nums1` elements are already in position. |

---

## When to Use Merge Sorted Array

- Two **already sorted** arrays need to be combined
- One array has **extra space** at the end (buffer)
- Fill from the **back** to avoid overwriting unprocessed elements

---
---

# Array & Matrix Manipulation — Set Zero / State Encoding Pattern

<img width="787" height="450" alt="image" src="https://github.com/user-attachments/assets/f415a52c-c084-4503-be4c-1620232ad973" />


> **Core idea:** Mark cells that need to change using in-place encoding (flags, temp states) so you can update simultaneously without extra space.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Set Matrix Zeroes** | [#73](https://leetcode.com/problems/set-matrix-zeroes/) | O(m × n) | O(1) | Use first row/col as markers. Save flags for whether first row/col originally had 0s. Scan rest → mark → zero out → handle first row/col last. | Must check `col == n-1` **before** `row == 0` at corners. Process first row/col **last** or markers get corrupted. |
| 2 | **Game of Life** | [#289](https://leetcode.com/problems/game-of-life/) | O(m × n) | O(1) | Encode old+new state in same cell: 0=dead→dead, 1=alive→alive, 2=alive→dead, 3=dead→alive. `% 2` decodes at the end. | When counting live neighbors, check `board[nr][nc] in (1, 2)` — both mean "was alive". Not just `== 1`. |
| 3 | **Diagonal Traverse** | [#498](https://leetcode.com/problems/diagonal-traverse/) | O(m × n) | O(1)* | Toggle between ↗ and ↙. At boundaries flip direction: going up → check right wall then top; going down → check bottom then left wall. | At **top-right corner** both `col==n-1` and `row==0` are true. Must check `col==n-1` **first** → correct move is down, not right. Same at bottom-left. |

---

## When to Use Set Zero / State Encoding

- Need to **update all cells simultaneously** but can only modify in-place
- Use **temp states** (2, 3, -1) to encode "was X, now Y" → decode with `% 2` or similar
- Use **first row/col as markers** when you need O(1) space for flag storage

---
---

# Array & Matrix Manipulation — Hashing: Frequency Map Pattern

> **Core idea:** Count occurrences with a hashmap/Counter, then use frequencies to make decisions (sort, group, filter, schedule).

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Two Sum** | [#1](https://leetcode.com/problems/two-sum/) | O(n) | O(n) | Single-pass hashmap `{value: index}`. Check if `target - num` exists; if yes return both indices. | — |
| 2 | **Valid Anagram** | [#242](https://leetcode.com/problems/valid-anagram/) | O(n) | O(1)* | Frequency map of s, then walk t decrementing. Any negative or missing → False. *26-letter alphabet is constant. | — |
| 3 | **Group Anagrams** | [#49](https://leetcode.com/problems/group-anagrams/) | O(n × k) | O(n × k) | 26-element char-count tuple as hashmap key. Same key = anagram group. | Use `tuple(count)` as dict key — lists aren't hashable. |
| 4 | **Top K Frequent Elements** | [#347](https://leetcode.com/problems/top-k-frequent-elements/) | O(n) | O(n) | Count frequencies → bucket sort (index = frequency) → walk buckets right to left collecting k elements. | — |
| 5 | **Sort Characters By Frequency** | [#451](https://leetcode.com/problems/sort-characters-by-frequency/) | O(n) | O(n) | Count frequencies → bucket sort chars by count → walk from highest down. | — |
| 6 | **Task Scheduler** | [#621](https://leetcode.com/problems/task-scheduler/) | O(n × m) | O(m) | Max-heap + cooldown deque. Each tick pop most frequent, push to queue with ready time. Fast-forward if heap empty. | When heap is empty but queue has tasks → `time = q[0][1]` to skip idle time. |
| 7 | **First Non-Repeating Char** | [#387](https://leetcode.com/problems/first-unique-character-in-a-string/) | O(n) | O(1)* | Two passes: build freq map, then find first char with count == 1. | — |
| 8 | **Longest Palindrome** | [#409](https://leetcode.com/problems/longest-palindrome/) | O(n) | O(1)* | Count frequencies. Even counts → use all. Odd → use count−1. If any odd existed → add 1 for center. | — |
| 9 | **Largest Unique Number** | [#1133](https://leetcode.com/problems/largest-unique-number/) | O(n) | O(n) | Frequency map, then find max number with count == 1. Return −1 if none. | — |
| 10 | **Subarray Sum Equals K** | [#560](https://leetcode.com/problems/subarray-sum-equals-k/) | O(n) | O(n) | Prefix sum + hashmap `{prefix_sum: count}` init `{0: 1}`. At each index check if `prefix - k` exists. | Must init map with `{0: 1}` — handles subarrays starting from index 0. |

---

## When to Use Hashing: Frequency Map

- Need to **count occurrences** then act on counts (top-k, grouping, filtering)
- **Bucket sort** when you need O(n) instead of O(n log n) sorting by frequency
- **Prefix sum + hashmap** for subarray sum problems

---
---

# Array & Matrix Manipulation — Hashing: Seen Check Pattern

> **Core idea:** Use a set or dict to track what you've **seen before** — for duplicate detection, cycle detection, or existence checks.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Contains Duplicate II** | [#219](https://leetcode.com/problems/contains-duplicate-ii/) | O(n) | O(n) | HashMap `{value: last_index}`. Check if seen before and distance ≤ k. Always update to latest index. | Store `freq[num] = i` (latest index), NOT accumulate. |
| 2 | **Happy Number** | [#202](https://leetcode.com/problems/happy-number/) | O(log n) | O(log n) | HashSet cycle detection. Replace n with sum of digit squares. If seen → cycle → False. If 1 → True. | Can also use Floyd's fast/slow pointer (O(1) space). |
| 3 | **Intersection of Two Arrays** | [#349](https://leetcode.com/problems/intersection-of-two-arrays/) / [#350](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | O(n + m) | O(n) | #349: Set intersection (unique). #350: Counter intersection (preserves duplicates, decrement on match). | — |
| 4 | **Longest Consecutive Sequence** | [#128](https://leetcode.com/problems/longest-consecutive-sequence/) | O(n) | O(n) | Dump into set. Only start counting from streak beginnings (`num - 1 not in set`), count forward. | Each element touched at most twice → O(n), not O(n²). |

---

## When to Use Hashing: Seen Check

- **"Have I seen this before?"** → set/dict lookup
- **Cycle detection** without pointers (happy number, sequence loops)
- **Duplicate/existence** within a window or globally
- **Streak/consecutive** problems — set for O(1) existence check

---
---

# Array & Matrix Manipulation — Prefix Sum / Subarray / Range Query Pattern

> **Core idea:** Use prefix products, sliding windows, or binary search on the answer to handle subarray/range queries efficiently.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Product of Array Except Self** | [#238](https://leetcode.com/problems/product-of-array-except-self/) | O(n) | O(1) | Two-pass: prefix products left→right into result, then multiply by suffix products right→left. No division. | Result array is required output — only `prefix` and `postfix` vars are extra. |
| 2 | **Minimum Size Subarray Sum** | [#209](https://leetcode.com/problems/minimum-size-subarray-sum/) | O(n) | O(1) | Sliding window — expand right adding to sum, shrink left while sum ≥ target, track min window length. | Use `float('inf')` init and check at end — if unchanged, return 0 (no valid subarray). |
| 3 | **Max Consecutive Ones III** | [#1004](https://leetcode.com/problems/max-consecutive-ones-iii/) | O(n) | O(1) | Sliding window — count flipped zeros. If flipped > k → shrink left until ≤ k. Track max window. | Shrink only un-flips when `nums[left] == 0`. |
| 4 | **Product of the Last K Numbers** | [#1352](https://leetcode.com/problems/product-of-the-last-k-numbers/) | O(1) per call | O(n) | Prefix-product list. `add(0)` → reset to `[1]`. `getProduct(k)` → `prefix[-1] / prefix[-k-1]`. If k ≥ len → window crosses a 0 → return 0. | Reset on zero — any window including it has product 0. |
| 5 | **Frequency of the Most Frequent Element** | [#1838](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) | O(n log n) | O(1) | Sort → sliding window. Cost = `(window_size × target) − actual_sum`. If cost > k → shrink left. | Sort first so window targets `nums[right]`. Cost formula: ideal_sum − curr_sum. |
| 6 | **Split Array Largest Sum** | [#410](https://leetcode.com/problems/split-array-largest-sum/) | O(n · log(sum−max)) | O(1) | Binary search on the answer. For candidate mid, greedily count subarrays needed. If count > k → mid too small. | `low = max(nums)`, `high = sum(nums)`. Greedy packs until sum exceeds mid → new subarray. |
| 7 | **Longest Mountain in Array** | [#845](https://leetcode.com/problems/longest-mountain-in-array/) | O(n) | O(1) | Scan for peaks (`arr[i-1] < arr[i] > arr[i+1]`), expand left (uphill) and right (downhill). Track longest. | Skip `i` to `right` after each mountain — no new peak starts inside. |

---

## When to Use Prefix Sum / Subarray / Range Query

- **Product/sum of all elements except current** → prefix + suffix pass
- **Minimum/maximum subarray** meeting a condition → sliding window
- **Prefix-product stream** → running product list with zero-reset
- **"Minimize the maximum"** or **"maximize the minimum"** → binary search on the answer
- **Expansion from a center** (mountain, palindrome) → scan for peaks, expand both sides

---
---

# Array & Matrix Manipulation — Cyclic Sort Pattern

> **Core idea:** For arrays with values in a known range [0, n] or [1, n], place each value at its "correct" index by swapping. After sorting, mismatches reveal missing/duplicate numbers.

---

## Problems

| # | Problem | LeetCode | Time | Space | Approach | ⚠️ Special Attention |
|---|---------|----------|------|-------|----------|----------------------|
| 1 | **Missing Number** | [#268](https://leetcode.com/problems/missing-number/) | O(n) | O(1) | Values [0, n] in size-n array. Place `nums[i]` at index `nums[i]`. Skip if value == n (no slot). Scan for mismatch → return index. If all match → n is missing. | Need `nums[i] < n` guard — value n has no valid index. |
| 2 | **Find All Numbers Disappeared in an Array** | [#448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | O(n) | O(1) | Values [1, n]. Place value v at index v−1. Scan: `nums[i] ≠ i+1` → i+1 is missing. Collect all. | No bounds check needed — every value in [1, n] has a valid slot. |
| 3 | **Find All Duplicates in an Array** | [#442](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | O(n) | O(1) | Same sort as #448. Scan: `nums[i] ≠ i+1` → `nums[i]` is the duplicate. Collect all. | Same as Disappeared — just return `nums[i]` (the extra value) instead of `i+1` (the missing value). |
| 4 | **First Missing Positive** | [#41](https://leetcode.com/problems/first-missing-positive/) | O(n) | O(1) | Values can be anything. Place v at index v−1 only if `1 ≤ v ≤ n`. Scan for first mismatch → return i+1. If all match → n+1. | Need `1 ≤ nums[i] ≤ n` guard — skip negatives, zeros, and out-of-range values. |

---

## When to Use Cyclic Sort

- Array values are in a **known contiguous range** [0, n] or [1, n]
- Need to find **missing, duplicate, or first-missing-positive** in O(n) time, O(1) space
- Key: **swap `nums[i]` to its correct index**, don't increment `i` until current slot is right
- Guard condition depends on range: `nums[i] < n` for [0, n], none for [1, n], `1 ≤ nums[i] ≤ n` for mixed
