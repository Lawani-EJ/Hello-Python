# MERGE SORT PSEUDOCODE 
# mergeSort(array a)
# if(n == 1)
# return a

# arrayOne = a[0]...a[n/2]
# arrayTwo = a[n/2 + 1]....a[n]

# arrayOne = mergeSort(arrayOne)
# arrayTwo = mergeSort(arrayTwo)

# return merge (arrayOne,arrayTwo)

# merge (array a, array b)
# array c

# while(a and b have elements)
#     if(a[0] > b[0])
#     add b[0] to the end of c
#     remove b[0] from b
#     else
#     add a[0] to the end of c
#     remove a[0] from a

# At this point either a or b is empty
# while (a has elements)
#     add a[0] to the end of c 
#     remove a[0] from a

#     while (b has elements)
#         add b[0] to the end of c
#         remove b[0] from b

#         return c

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        #recursive call on each half
        mergeSort(left)
        mergeSort(right)

        #Two iterators for transvering the two halves
        i = 0
        j = 0

        #Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left has been used 
                myList[k] = left[i]
                # Move the iterator forward 
                i += 1
            else:
                myList[k] = right[j]
                j += 1
                # Move to the next slot 
            k += 1

                # for all the remaining values 
        while i < len(left):
                    myList[k] = left[i]
                    i += 1
                    k += 1

        while j < len(right):
                    myList[k] = right[j]
                    j += 1
                    k += 1

myList  = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)