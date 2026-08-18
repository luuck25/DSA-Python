
# Merge Sort:
# - Divide and conquer: recursively split array in half, sort each half, then merge.
# - Merging two sorted halves takes O(n) time.
# - Time: O(n log n) — always (worst, avg, best)
# - Space: O(n) — requires extra space for merged subarrays
# - Stable sort. Preferred when stability matters or for linked lists.

def mergesort(arr):

    if len(arr) == 1:
        return arr
    mid = len(arr) // 2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left,right)

def merge(left,right):


    i = j = 0

    result = []

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1


        result.extend(left[i:])
        result.extend(right[j:])

        return result      

print(mergesort([7,8,3,15,17]))