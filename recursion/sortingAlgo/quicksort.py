
# Quick Sort:
# - Divide and conquer: pick a pivot, partition array so elements < pivot go left, > pivot go right.
# - Recursively sort left and right partitions.
# - Time: O(n log n) avg, O(n²) worst (bad pivot choices)
# - Space: O(log n) avg (recursion stack), O(n) worst
# - In-place, NOT stable. Fastest in practice for most inputs.

def quick_sort(arr, low,high):

    if low >=high:
        return
    
    pivot = arr[low]
    left = low + 1
    right = high

    while left <= right:

        while left<=right and arr[left] <= pivot:
            left += 1

        while left<=right and arr[right] >= pivot:
            right += 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]

        quick_sort(arr,low, right -1)
        quick_sort(arr,right+1,high)               


    
