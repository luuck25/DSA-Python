
# Selection Sort:
# - Finds the minimum element in the unsorted portion and swaps it to the front.
# - Each pass selects the next smallest and places it in its final position.
# - Time: O(n²) — always (worst, avg, best)
# - Space: O(1) — in-place, NOT stable
# - Simple but inefficient; fewer swaps than bubble sort.

def selectionSort(arr):

    

    for i in range (len(arr)):
        min_index = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[min_index],arr[i] = arr[i],arr[min_index]


    return arr   

print(selectionSort([7,8,3,15,17]))       