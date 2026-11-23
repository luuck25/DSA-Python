"""Cheapest Flights Within K Stops (LeetCode 787).

Approach - Min-heap ordered by total price:
1. Build a directed adjacency list from the flights.
2. Push (cost, city, stops) into a min-heap, starting with the source at cost
    0 and stops set to 0.
3. Pop the cheapest route prefix. If its city is the destination, return its
	cost. Otherwise, add each outgoing flight if the route can still use one.
4. In this version, `stops` counts flights taken (edges). K intermediate
    stops permits at most K + 1 flights, so do not expand when `stops == k + 1`.
5. Return -1 if no allowed route reaches the destination.

This version follows the provided approach and does not prune repeated
(city, flights_used) states. Its worst-case work can be exponential in the
flight limit when many different route prefixes are possible. A best-cost
table indexed by city and flights used can reduce repeated exploration.
Returning the first destination removed from the heap is valid because
flight prices are nonnegative (they are positive in this problem).

Pseudocode:
-----------
function findCheapestPrice(n, flights, src, dst, k):
    build directed adjacency list
    min_heap = [(0, src, 0)]  # cost, city, stops (flights taken)

    while heap is not empty:
        cost, city, stops = remove cheapest entry
        if city is dst:
            return cost
        if stops > k :
            continue

        for each outgoing flight (neighbor, price):
            add (cost + price, neighbor, stops + 1) to heap

    return -1

Time -

Like dijstra p log (pop) + p log p (push)

Let P be the number of route-prefix entries generated and processed, and E
the number of flights. Time: O(E + P log P). 


Space: O(E + P). P can be
exponential in K in the worst case because duplicate route states are not
pruned. Building the adjacency list takes O(E) space.
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, price in flights:
            adj[u].append((v, price))   #  o(v)

        # Tuple stores (cost, city, stops); stops here counts flights taken.
        min_heap = [(0, src, 0)]   

        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)  # log(v)

            if city == dst:
                return cost

            if stops > k :
                continue

            for neighbour, price in adj[city]:
                new_cost = cost + price
                new_stops = stops + 1
                heapq.heappush(min_heap, (new_cost, neighbour, new_stops))    # elogv

        return -1
