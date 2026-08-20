"""
Koko Eating Bananas

Description:
Koko loves eating bananas. There are n piles of bananas, and Koko can decide her eating speed k
(bananas per hour). Each hour, she chooses a pile and eats k bananas from it.
If the pile has less than k bananas, she eats all and won't eat more bananas during that hour.
Find the minimum integer k such that she can eat all bananas within h hours.

Example:
    Input: piles = [3,6,7,11], h = 8
    Output: 4
    Explanation: At speed 4, Koko can finish in 1+2+2+3 = 8 hours

Approach:
1. Binary search on the answer (eating speed k)
2. Search range: left = 1 (minimum speed), right = max(piles) (maximum needed speed)
3. For each mid speed, calculate total hours needed:
   - For each pile: hours += ceil(pile / mid) = (pile + mid - 1) // mid
4. If total hours <= h, this speed works; try slower (right = mid)
5. If total hours > h, need faster speed (left = mid + 1)
6. Return left as the minimum valid speed

Time Complexity: O(n * log m) - Binary search on speed range (log m) × calculate hours for n piles
    where m = max(piles)
Space Complexity: O(1) - Only using constant extra space
"""

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)  # O(n)

        while left < right:
            hours = 0

            mid = (left + right)//2

            for pile in piles: # n work log M times -> n log m
                hours += (pile + mid - 1 )// mid

            if hours <= h :
                right = mid
            else:
                left = mid +1
        return left


"""
Pseudocode:
-----------
function minEatingSpeed(piles, h):
    left = 1
    right = max(piles)  // Maximum possible speed
    
    while left < right:
        mid = (left + right) / 2
        hours = 0
        
        // Calculate hours needed at speed mid
        for each pile in piles:
            hours += ceiling(pile / mid)
        
        if hours <= h:
            right = mid  // Try slower speed
        else:
            left = mid + 1  // Need faster speed
    
    return left  // Minimum valid speed
"""