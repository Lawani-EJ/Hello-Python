# FUNCTION binary_search(arr : ARRAY_OF INTEGER, X : INTEGER) : INTEGER
# VAR
#     left, right, mid : INTEGER;
# BEGIN
#     left := 0;
#     right := arr.length - 1;
    
#     WHILE (left <= right) DO
#         mid := left + (right - left) / 2;
        
#         IF (arr[mid] = X) THEN
#             RETURN mid;
#         END_IF
        
#         IF (arr[mid] < X) THEN
#             left := mid + 1;
#         ELSE
#             right := mid - 1;
#         END_IF
#     END_WHILE
    
#     RETURN -1;  // If X is not found
# END


def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        
        if midpoint_value == item:  
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    
    return None  

sequence_a = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
item_a = 12
print(binary_search(sequence_a, item_a))
