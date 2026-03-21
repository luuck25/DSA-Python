# Python Interview Problems

A collection of common coding interview problems with solutions in Python.

---

## 🎯 Two Pointers Technique

### Key Highlights:
- **Prerequisite**: Array must be **SORTED** (ascending order) for the technique to work
- **Approach**: Use two pointers (start & end) moving towards each other
- **When to use**: Finding pairs/triplets, removing duplicates, comparing elements from both ends

### How It Works:
```
[1, 2, 3, 4, 5, 6, 7]
 ^                 ^
start             end

- If sum too small → move start RIGHT (increase sum)
- If sum too large → move end LEFT (decrease sum)
```

---

## 📁 Problems Solved

### TwoPointers/

| Problem | Description | Time | Space | Key Insight |
|---------|-------------|------|-------|-------------|
| [targetSum_Sorted.py](TwoPointers/targetSum_Sorted.py) | Find a pair in a sorted array whose sum equals the target. | O(n) | O(1) | Pointers at both ends, adjust based on sum |
| [NonDuplicatNumber.py](TwoPointers/NonDuplicatNumber.py) | Remove duplicates from a sorted array in-place. | O(n) | O(1) | Slow pointer for unique, fast pointer scans |
| [tripletSumZero.py](TwoPointers/tripletSumZero.py) | Find all unique triplets that sum to zero (3Sum). | O(n²) | O(n) | Fix one element, two-pointer for remaining |

