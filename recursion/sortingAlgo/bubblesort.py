

# Bubble Sort:
# - Repeatedly swaps adjacent elements if they are in the wrong order.
# - Each pass "bubbles" the largest unsorted element to its correct position at the end.
# - After pass i, the last i elements are already sorted.
# - Time: O(n²) worst/avg, O(n) best (with early termination optimization)
# - Space: O(1) — in-place, stable sort

def  bubble_sort(arr):

    for i in range(len(arr)):

        for j in range(0, len(arr) -i -1):

            if arr [j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort([7,8,3,15,17]))

# If you do O(n) work repeatedly O(n) times, the total is O(n²).