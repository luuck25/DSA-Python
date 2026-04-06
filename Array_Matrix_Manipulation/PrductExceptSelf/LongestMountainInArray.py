class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        longest = 0

        i = 1
        n= len(arr)

        while i < n -1:

            if arr[i-1] < arr[i] > arr[i+1]:

                left = i

                while left >0 and arr[left] > arr[left-1]:
                    left -= 1
                right = i  
                while right < n -1 and arr[right] > arr[right+1]:
                    right += 1

                longest = max(longest, right -left +1)
                i = right
            else:
                i += 1                            
        return longest