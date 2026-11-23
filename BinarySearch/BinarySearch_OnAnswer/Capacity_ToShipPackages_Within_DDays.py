"""
Capacity To Ship Packages Within D Days

Description:
Given package weights in their required order, ship all packages within `days`
days. The ship has the same capacity each day, and packages must be loaded in
the given order. Return the minimum possible capacity.

Approach:
1. Binary search on the ship capacity.
2. The minimum capacity is max(weights), since every package must fit. The
    maximum capacity is sum(weights), which can ship all packages in one day.
3. For each candidate capacity `mid`, greedily load packages in order. When
    the next package would exceed `mid`, start a new day for that package.
4. If the packages need at most `days` days, `mid` is sufficient. Keep it as a
    candidate and try a smaller capacity by setting `right = mid`.
5. Otherwise, the capacity is too small; search larger capacities by setting
    `left = mid + 1`.
6. When `left == right`, that is the minimum capacity that works.

Time Complexity: O(n * log S), where n is the number of packages and S is the
     sum of their weights. Each candidate capacity is checked in O(n) time, and
     binary search checks O(log S) capacities.
Space Complexity: O(1), using only a fixed number of variables.
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            required_days = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > mid:
                    required_days += 1
                    current_load = 0

                current_load += weight

            if required_days <= days:
                right = mid
            else:
                left = mid + 1

        return left


"""
Pseudocode:
-----------
function shipWithinDays(weights, days):
    left = maximum weight
    right = sum of all weights

    while left < right:
        capacity = floor((left + right) / 2)
        required_days = 1
        current_load = 0

        for each weight in weights, in order:
            if current_load + weight > capacity:
                required_days += 1
                current_load = 0
            current_load += weight

        if required_days <= days:
            right = capacity  // Capacity works; try a smaller one
        else:
            left = capacity + 1  // Capacity is too small

    return left  // Minimum capacity that works
"""
