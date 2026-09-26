"""
PROBLEM: Online Stock Span
Given a stream of stock prices, return the span of the price for each day.
Span = number of consecutive days just before the given day, with price ≤ current price.

Example: prices = [100, 80, 60, 70, 60, 75, 85]
- Day 0 (100): span = 1
- Day 1 (80): span = 1 (no previous day with price ≥ 80)
- Day 2 (60): span = 1
- Day 3 (70): span = 2 (days 2 and 3, both ≤ 70)
- Day 4 (60): span = 1
- Day 5 (75): span = 4 (days 2, 3, 4, 5 all ≤ 75)
- Day 6 (85): span = 6 (days 1-6 all ≤ 85)

APPROACH:
Use a monotonic stack to avoid recalculating spans naively.
1. Stack stores (price, span) pairs.
2. For each new price:
   - Initialize span = 1 (the current day itself).
   - While stack is not empty and top price ≤ current price:
       * Pop the top (prev_price, prev_span).
       * Add prev_span to current span (jump over all days covered by prev span).
   - Push (current_price, current_span) onto stack.
3. Return the current span.

Why this works:
- prev_span already covers all consecutive days before the previous day with price ≤ prev_price.
- If current price ≥ prev_price, current price also covers all those days.
- So we can directly add prev_span instead of iterating one by one.

PSEUDOCODE:
1. stack = empty
2. function next(price):
   - span = 1
   - while stack is not empty and stack[-1][0] <= price:
       prev_price, prev_span = stack.pop()
       span += prev_span
   - stack.append((price, span))
   - return span

TIME COMPLEXITY: O(1) amortized per call
- Each price is pushed and popped from the stack at most once.
- Total operations for n calls is O(n).

SPACE COMPLEXITY: O(n)
- In the worst case (strictly increasing prices), stack stores all n prices.
"""

class StockSpanner:
    
    def __init__(self):
        # Stack stores (price, span) pairs for prices that haven't been dominated yet
        self.st = []
     
    def next(self, price: int) -> int:
        span = 1
        
        # Pop all previous prices that are <= current price
        # We can "jump" over the span they covered
        while self.st and self.st[-1][0] <= price:
            prev_price, prev_span = self.st.pop()
            # prev_span covers all previous days up to the previous "taller" bar
            # So we can add prev_span directly instead of iterating
            span += prev_span

        # Push current price with its computed span
        self.st.append((price, span))

        return span    

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
