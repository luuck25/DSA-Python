"""
Sort Characters By Frequency

Description:
Given a string `s`, reorder its characters so that characters with higher
frequency appear first. Any order is valid for characters with equal frequency.

Approach:
1. Count each character with `Counter`.
2. Build a list of (negative frequency, character) pairs. Negative frequencies
    make Python's min-heap pop the highest-frequency character first.
3. Heapify the list in O(m), where m is the number of distinct characters.
4. Pop each character and repeat it by its frequency, appending the resulting
    string to `result`.
5. Join `result` to create the reordered string.

Let:
- `n = len(s)`
- `m` = number of distinct characters, where m <= n

Time Complexity:
1. `Counter(s)` takes O(n).
2. Building the heap list takes O(m), and `heapq.heapify` takes O(m).
3. Popping all m characters takes O(m log m).
4. Expanding the characters creates n total characters: O(n).
5. Joining the result takes O(n).
Overall: O(n + m log m), commonly written as O(n log n) since m <= n.
If the input is restricted to uppercase letters, lowercase letters, and
digits, then m <= 62, so the running time is O(n) for that fixed alphabet.

Space Complexity:
- `Counter`: O(m).
- Heap: O(m).
- `result` stores n output characters: O(n).
- The joined string also stores n characters: O(n).
Overall auxiliary and output space is O(n + m) = O(n). Excluding the returned
string does not change the bound, because `result` itself stores O(n) output.
"""

import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        mp = Counter(s)

        heap = []

        for k,v in mp.items():

            heap.append((-v,k))

        heapq.heapify(heap)

        result = []

        while heap:

            frq,val = heapq.heappop(heap)
            

            result.append(-frq * val)

        return ''.join(result)


"""
Pseudocode:
-----------
function frequencySort(s):
    frequencies = count each character in s
    heap = empty list

    for each (character, frequency) in frequencies:
        append (-frequency, character) to heap

    heapify(heap)
    result = empty list

    while heap is not empty:
        (negative_frequency, character) = pop heap
        append character repeated -negative_frequency times to result

    return join result into one string
"""


        






