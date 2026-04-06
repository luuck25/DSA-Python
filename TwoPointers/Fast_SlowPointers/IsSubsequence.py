class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = fast = 0

        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        
        
        return slow == len(s)        
        

        """
        
        slow move conditionally if match is there

        fast moves if no match
        
        so speed of fast is more than slow 
        
        
        """
