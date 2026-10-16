"""Car Fleet — Plain English Walkthrough
=========================================
Problem:
    Cars travel toward the same target along a one-lane road. Given each car's
    starting position and speed, return how many fleets arrive at the target.
    A faster car catches the car or fleet ahead and then travels at its speed;
    cars cannot pass one another.

    Input:  target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
    Output: 3

    Explanation:
        Car at position 10 takes 1 hour to reach the target.
        Car at position 8 also takes 1 hour, so it joins the fleet ahead.
        Car at position 5 takes 7 hours and forms a new fleet.
        Car at position 3 takes 3 hours, catches the fleet from position 5,
        and joins it.
        Car at position 0 takes 12 hours and forms another fleet.

Approach:
Calculate how long each car would take to reach the target, then sort cars
from closest to the target to farthest. Scan in that order and keep arrival
times for fleets ahead. A car whose arrival time is less than or equal to the
fleet ahead catches it and joins that fleet. A car with a later arrival time
cannot catch up, so it starts a new fleet.

Pseudocode:
1. Pair each car's position with its time to reach the target.
2. Sort the pairs by position, descending.
3. Scan from front to back, keeping a stack of fleet arrival times.
4. Add a time if the stack is empty or the time is greater than the last
   fleet's time; otherwise, the car joins the fleet ahead.
5. Return the number of times in the stack.

Time complexity: O(n log n), due to sorting the n cars.
Space complexity: O(n), for the car pairs and fleet-time stack.
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=[]

        for pos,speed in zip(position,speed):

            time = (target - pos) / speed

            cars.append((pos,time))

        cars.sort(reverse=True)

        st = []

        for _,time in cars:

            if not st or time > st[-1]:
                st.append(time)
        return len(st)        


        