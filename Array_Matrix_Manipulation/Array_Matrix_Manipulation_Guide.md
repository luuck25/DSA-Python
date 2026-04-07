# Array & Matrix Manipulation — Plus One Pattern

> **Core idea:** Simulate arithmetic on arrays digit by digit, processing right to left. Handle carry propagation manually.

<img width="854" height="741" alt="image" src="https://github.com/user-attachments/assets/931909bd-eedf-4a66-b19f-7ffa0cfd6151" />

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
