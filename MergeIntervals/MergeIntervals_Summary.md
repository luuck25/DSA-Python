# Merge Intervals — Solved Problems Summary

## Quick Reference Table

| # | Problem | What It Asks | Sort By | Time | Space | Data Structure |
|---|---------|--------------|---------|------|-------|----------------|
| 1 | Merge Intervals | Merge all overlapping intervals into one | START time | O(n log n) | O(n) | List |
| 2 | Insert Interval | Insert a new interval into a sorted list & merge if needed | No sorting needed | O(n) | O(n) | List |
| 3 | Non-Overlapping Intervals | Min intervals to REMOVE so none overlap | END time | O(n log n) | O(1) | Counter |
| 4 | Meeting Rooms | Can a person attend ALL meetings? (any overlap?) | END time | O(n log n) | O(1) | Counter |
| 5 | Min Meeting Rooms | Min conference rooms needed for all meetings | START time | O(n log n) | O(n) | Min-Heap |

---

## 1. Merge Intervals (`mergeInvl.py`)

**Problem:** Given a list of intervals, merge all overlapping ones.  
**Example:** `[[1,3], [2,6], [8,10]]` → `[[1,6], [8,10]]`

**Approach:**
1. **Sort by START time** — so overlapping intervals are guaranteed to be next to each other. If we sorted by end time, `[1,10]` and `[2,3]` could end up apart and we'd miss the merge.
2. Walk through each interval:
   - No overlap with last merged → add it
   - Overlaps → extend the last merged interval's end with `max()`

**Time:** O(n log n) — sorting dominates  
**Space:** O(n) — for the merged result list

---

## 2. Insert Interval (`insertInterval.py`)

**Problem:** Given a **sorted** list of non-overlapping intervals, insert a new interval and merge if needed.  
**Example:** `[[1,2], [3,5], [6,7]], newInterval = [4,8]` → `[[1,2], [3,8]]`

**Approach:**
1. **No sorting needed** — the input is already sorted.
2. Single pass through intervals. For each one, only 3 things can happen:
   - New interval comes **AFTER** current → no overlap, add current to result
   - New interval comes **BEFORE** current → no overlap, add newInterval, swap
   - They **OVERLAP** → merge using `min()` of starts and `max()` of ends
3. Append the remaining newInterval at the end (always valid)

**Time:** O(n) — single pass, no sorting  
**Space:** O(n) — for the result list

---

## 3. Non-Overlapping Intervals (`NonOverlapping.py`)

**Problem:** Find the **minimum** number of intervals to **remove** so no two overlap.  
**Example:** `[[1,2], [2,3], [3,4], [1,3]]` → Remove 1 interval (`[1,3]`)

**Approach:**
1. **Sort by END time (not start!)** — this is a **greedy** strategy. By keeping intervals that finish earliest, we leave the most room for future intervals, guaranteeing minimum removals.
   - *Why not start time?* Consider `[1,100], [2,3], [4,5]`. Sorting by start keeps `[1,100]` and removes 2. Sorting by end keeps `[2,3]` and `[4,5]`, removing only 1. ✅
2. Track `prev_end` of the last kept interval
3. For each interval:
   - Overlaps → count it as removed (don't update `prev_end`)
   - No overlap → keep it (update `prev_end`)

**Time:** O(n log n) — sorting  
**Space:** O(1) — just a counter and a variable

---

## 4. Meeting Rooms (`MeetingRooms.py`)

**Problem:** Can a person attend **all** meetings? (i.e., do any overlap?)  
**Example:** `[(0,30), (5,10), (15,20)]` → `False`

**Approach:**
1. **Sort by END time** — same greedy idea as Non-Overlapping. Process meetings that finish earliest first to detect conflicts early.
2. Track `prev_end` of the last meeting
3. For each meeting:
   - Starts before `prev_end` → OVERLAP → return `False` immediately
   - No overlap → update `prev_end`
4. If loop finishes → return `True`

**Time:** O(n log n) — sorting  
**Space:** O(1) — only a few variables

---

## 5. Minimum Meeting Rooms (`MinMeetingRooms.py`)

**Problem:** Find the **minimum** number of conference rooms needed for all meetings.  
**Example:** `[(0,30), (5,10), (15,20)]` → `2 rooms`

**Approach:**
1. **Sort by START time** — we process meetings in chronological order and ask "is any room free right now?"
   - *Why not end time?* We need to know which meeting starts next to decide if an existing room can be reused. The min-heap handles the "which room ends earliest" part.
2. Use a **min-heap** to track end times of rooms in use. The heap top = the room that frees up earliest.
3. For each meeting:
   - Heap top ≤ meeting start → a room is free → **reuse** it (pop + push)
   - Otherwise → **allocate** a new room (just push)
4. Final heap size = number of rooms needed

**Time:** O(n log n) — sorting + heap operations  
**Space:** O(n) — heap can hold up to n end times

---

## 🧠 When to Sort by START vs END Time?

| Sort By | When to Use | Why |
|---------|-------------|-----|
| **START time** | Merging intervals, processing in order | Ensures overlapping intervals sit next to each other so you can merge/process them sequentially |
| **END time** | Greedy problems (min removals, can attend all?) | Keeping the earliest-ending interval leaves maximum room for future intervals — guarantees optimal result |
| **No sort** | Input is already sorted (e.g., Insert Interval) | Just process in one pass |

**Rule of thumb:**  
- Need to **merge or allocate resources** → sort by **START**  
- Need to **minimize conflicts/removals** → sort by **END** (greedy)

---

## 🔍 Deep Dive: Why Non-Overlapping Intervals CANNOT Use START Time Sorting

### The Goal

We want to **keep as many intervals as possible** (= remove the fewest).

### START Time Sorting Fails — Example 1

```
Intervals: [1,100], [2,3], [4,5], [6,7]
```

**Sorted by START time:**

```
[1,100]  [2,3]  [4,5]  [6,7]

Step 1: Keep [1,100]           → prev_end = 100
Step 2: [2,3]  → 2 < 100      → OVERLAP → remove ❌
Step 3: [4,5]  → 4 < 100      → OVERLAP → remove ❌
Step 4: [6,7]  → 6 < 100      → OVERLAP → remove ❌

Kept: 1 interval, Removed: 3 😢
```

We picked `[1,100]` first because it **starts** earliest. But it's a **greedy bully** — it stretches so far that it kills every other interval!

**Sorted by END time:**

```
[2,3]  [4,5]  [6,7]  [1,100]

Step 1: Keep [2,3]             → prev_end = 3
Step 2: [4,5]  → 4 > 3        → No overlap → keep ✅  → prev_end = 5
Step 3: [6,7]  → 6 > 5        → No overlap → keep ✅  → prev_end = 7
Step 4: [1,100] → 1 < 7       → OVERLAP → remove ❌

Kept: 3 intervals, Removed: 1 😄
```

### START Time Sorting Fails — Example 2

```
Intervals: [1,4], [2,3], [3,5]
```

**By START time:**
```
[1,4] → keep → prev_end = 4
[2,3] → 2 < 4 → remove ❌
[3,5] → 3 < 4 → remove ❌
Removed: 2 😢
```

**By END time:**
```
[2,3] → keep → prev_end = 3
[1,4] → 1 < 3 → remove ❌
[3,5] → 3 >= 3 → keep ✅
Removed: 1 😄
```

`[2,3]` ends at **3**, freeing up space for `[3,5]`.  
`[1,4]` ends at **4**, which would have blocked `[3,5]`.

### The Meeting Room Analogy 🏢

| Sort by START | Sort by END |
|---|---|
| Picks the meeting that **starts first** | Picks the meeting that **finishes first** |
| Could pick a 10-hour meeting at 9 AM | Picks the 30-min meeting that ends at 9:30 AM |
| Blocks the room **all day** | Frees the room **quickly** for others |
| ❌ Greedy but wasteful | ✅ Greedy and optimal |

### One-Line Summary

> **Sorting by END time picks the "shortest reach" interval first, leaving maximum space for the remaining intervals. START time sorting blindly picks whatever begins earliest — even if it stretches forever and blocks everything else.**
