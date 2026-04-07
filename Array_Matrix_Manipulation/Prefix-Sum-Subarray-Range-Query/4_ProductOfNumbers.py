"""
Product of Numbers (LeetCode #1352)
====================================
Problem:
    Design a class that supports two operations:
      add(num)        — append num to the stream
      getProduct(k)   — return the product of the last k numbers

    Input:  add(3,0,2,5,4)  →  getProduct(2) = 20, getProduct(3) = 40,
            getProduct(4) = 0  (because 0 is in the window)

Logic:
    Keep a prefix-product list starting with [1].
    • add: if num is 0 → reset list to [1] (any window that includes this
      0 will have product 0).  Otherwise append last * num.
    • getProduct(k): if k ≥ len(prefix) the window crosses a 0 → return 0.
      Otherwise  prefix[-1] / prefix[-k-1]  gives the product of last k.

Time:  O(1) per add / getProduct
Space: O(n) — prefix list grows with non-zero adds
"""


class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]              # prefix-product list, starts with 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]          # reset — 0 kills all previous products
        else:
            self.prefix.append(self.prefix[-1] * num)  # running product

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix) - 1:   # window includes a 0 (list was reset)
            return 0
        else:
            return self.prefix[-1] // self.prefix[-k - 1]  # product of last k


# ---- Clean version (no comments) ----
class ProductOfNumbers_clean:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix) - 1:
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]