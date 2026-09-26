from typing import List

"""
PROBLEM: Asteroid Collision
Given an array of asteroids, each represented by its size and direction:
- positive = moving right
- negative = moving left

When two asteroids meet, they collide:
- If one explodes, it is removed.
- If both explode, both are removed.
- If one survives, it continues in the same direction.

Return the final list of asteroids after all collisions.

APPROACH:
Use a stack to simulate collisions.
1. Iterate through each asteroid.
2. Track whether the current asteroid survives (alive = True).
3. While the stack is not empty AND the top is moving right AND current is moving left:
   - If top < |current| (current magnitude greater): top explodes, pop it, continue.
   - If top == |current| (equal magnitudes): both explode, pop and mark current dead.
   - If top > |current| (top magnitude greater): current explodes, mark dead, break.
4. If current asteroid survived all collisions, push it onto stack.
5. Return the stack (remaining asteroids).

PSEUDOCODE:
1. stack = empty
2. for each asteroid in asteroids:
   - alive = True
   - while stack not empty AND stack[-1] > 0 AND asteroid < 0:
       if stack[-1] < -asteroid:
           stack.pop()
           continue
       else if stack[-1] == -asteroid:
           stack.pop()
           alive = False
           break
       else:
           alive = False
           break
   - if alive:
       stack.append(asteroid)
3. return stack

TIME COMPLEXITY: O(n)
- Each asteroid is pushed and popped from the stack at most once.
- Total operations across all asteroids is O(n).

SPACE COMPLEXITY: O(n)
- In the worst case, all asteroids survive and are stored in the stack.
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack stores surviving asteroids in order
        st = []

        for asteroid in asteroids:
            # Track whether current asteroid survives all collisions
            alive = True

            # Collision loop: right-moving asteroid (positive) collides with left-moving (negative)
            while st and st[-1] > 0 and asteroid < 0:
                if st[-1] < -asteroid:
                    # Top asteroid has smaller magnitude, so it explodes and is removed
                    # Current asteroid continues to check next collision
                    st.pop()
                    continue

                elif st[-1] == -asteroid:
                    # Equal magnitudes: both asteroids explode
                    st.pop()
                    alive = False
                    break

                else:
                    # Top asteroid has larger magnitude: current asteroid explodes
                    alive = False
                    break

            # If current asteroid survived all collisions, add it to stack
            if alive:
                st.append(asteroid)

        return st
