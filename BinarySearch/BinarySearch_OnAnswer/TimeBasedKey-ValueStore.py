"""
Time Based Key-Value Store

Description:
Create a time-based key-value data structure that can store multiple values for the same key
at different timestamps and retrieve the value for a key at a specific timestamp.
If there's no exact timestamp match, return the value with the largest timestamp <= given timestamp.

Example:
    Input: set("foo", "bar", 1), get("foo", 1), get("foo", 3), set("foo", "bar2", 4), get("foo", 4), get("foo", 5)
    Output: [null, "bar", "bar", null, "bar2", "bar2"]

Approach:
1. Use a hashmap where each key maps to a list of (timestamp, value) pairs
2. For set(): Append (timestamp, value) to the key's list (timestamps are strictly increasing)
3. For get(): Use binary search on the timestamp list to find the largest timestamp <= target
4. Binary search: If store[key][mid][0] <= timestamp, it's a candidate; search right for better match
5. Otherwise, search left half
6. Return the value corresponding to the best timestamp found

Time Complexity:
    - set(): O(1) - Append to list
    - get(): O(log n) - Binary search on n timestamps for that key
Space Complexity: O(n) - Store all key-value-timestamp tuples
"""

class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))    
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""

        left = 0
        right = len(self.store[key]) - 1
        answer = ""

        while left <= right:

            mid  = (left+right)//2

            if self.store[key][mid][0] <= timestamp:
                answer =  self.store[key][mid][1]
                left = mid + 1
            else:
                right = mid -1
        return answer                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()  
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


"""
Pseudocode:
-----------
class TimeMap:
    function __init__():
        store = empty hashmap  // key -> list of (timestamp, value)
    
    function set(key, value, timestamp):
        if key not in store:
            store[key] = empty list
        append (timestamp, value) to store[key]
    
    function get(key, timestamp):
        if key not in store:
            return ""
        
        left = 0
        right = length(store[key]) - 1
        answer = ""
        
        while left <= right:
            mid = (left + right) / 2
            
            if store[key][mid].timestamp <= timestamp:
                answer = store[key][mid].value
                left = mid + 1  // Search for larger timestamp
            else:
                right = mid - 1
        
        return answer
"""