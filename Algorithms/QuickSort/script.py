# #PSEUDO CODE
# QuickSort(A as array, low as int, high as int)
# if (low<high)
# pivot_location = Partition(A, low, high)
# QuickSort(A, low, pivot_location)
# QuickSort(A,pivot_location + 1, high)

# Partition(A as array, low as int, high as int)
# pivot = A[low]
# leftwall = low

# for i = low + 1 to high
#     if(A[i] < pivot) then
#     swap (A[i],A[leftwall])
#     leftwall = leftwall + 1
# swap (pivot,A[leftwall])
# return(leftwall)

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

arr = [22, 11, 88, 66, 55, 77, 33, 44]
quicksort(arr, 0, len(arr) - 1)
print(arr)