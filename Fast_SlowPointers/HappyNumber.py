"""
Problem: Happy Number (LeetCode #202)
--------------------------------------
A happy number is defined by the following process:
1. Start with any positive integer
2. Replace the number by the sum of squares of its digits
3. Repeat until the number equals 1 (happy!) or loops endlessly (not happy)

Example:
    Input:  19
    Process: 19 -> 1² + 9² = 82
             82 -> 8² + 2² = 68
             68 -> 6² + 8² = 100
             100 -> 1² + 0² + 0² = 1
    Output: True (19 is a happy number)
    
    Input:  2
    Process: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (CYCLE!)
    Output: False (2 is not a happy number)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if a number is a happy number using Floyd's Cycle Detection.
        
        Algorithm (Fast and Slow Pointers):
        ------------------------------------
        This problem is essentially detecting a cycle in a sequence!
        
        The sequence of sum-of-squares either:
        1. Reaches 1 (happy number) - like reaching end of list
        2. Enters a cycle (not happy) - like a linked list cycle
        
        We use fast and slow pointers on this implicit "linked list":
        - Each number points to its sum of digit squares
        - Slow computes sum once per step
        - Fast computes sum twice per step
        
        Visual Example (n = 19, Happy):
        -------------------------------
        slow: 19 -> 82 -> 68 -> 100 -> 1
        fast: 19 -> 68 -> 1
        
        Fast reaches 1 -> HAPPY!
        
        Visual Example (n = 2, Not Happy):
        ----------------------------------
        Sequence: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (cycle!)
                       ^                                              |
                       +-------------------<--------------------------+
        
        slow: 2 -> 4 -> 16 -> 37 -> 58 -> 89 ...
        fast: 2 -> 16 -> 58 -> 145 -> 20 -> 16 ...
        
        Eventually slow == fast (in cycle) -> NOT HAPPY!
        
        Why This Works:
        ---------------
        - If happy: sequence reaches 1, stays at 1 (1² = 1)
        - If not happy: sequence must eventually cycle (finite possible values)
        - Fast pointer either reaches 1 first, or catches slow in cycle
        
        Args:
            n: A positive integer to check
            
        Returns:
            True if n is a happy number, False otherwise
            
        Time Complexity: O(log n)
            - Each number has at most log₁₀(n) digits
            - Sum of squares reduces large numbers quickly
            - Cycle detection is bounded by limited possible values
            
        Space Complexity: O(1)
            - Only two pointer variables (slow, fast)
            - No set or extra storage needed
        """
        def get_sum_of_squares(num: int) -> int:
            """Calculate sum of squares of digits."""
            total_sum = 0
            while num > 0:
                digit = num % 10           # Extract last digit
                total_sum += digit * digit  # Add square of digit
                num //= 10                  # Remove last digit
            return total_sum

        # Initialize slow and fast pointers
        slow = n
        fast = n
        
        # Floyd's cycle detection on the sequence
        while True:
            slow = get_sum_of_squares(slow)                        # Move 1 step
            fast = get_sum_of_squares(get_sum_of_squares(fast))    # Move 2 steps
            
            # Fast reached 1 -> Happy number!
            if fast == 1:
                return True
            
            # Slow caught up to fast -> Cycle detected, not happy
            if slow == fast:
                return False  