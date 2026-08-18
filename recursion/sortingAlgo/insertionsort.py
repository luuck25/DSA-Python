

# Insertion Sort:
# - Builds the sorted array one element at a time.
# - Picks each element and inserts it into its correct position among the already-sorted left portion.
# - Shifts larger elements to the right to make space.
# - Time: O(n²) worst/avg, O(n) best (already sorted)
# - Space: O(1) — in-place, stable sort
# - Great for small or nearly sorted arrays.

def insertionSort(arr):

    for i in range(1,len(arr)):

        key = arr[i]
        j = i - 1
    
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr 
print(insertionSort([7,8,3,15,17]))
       

