# CSA & CSB-TEST – April 8, 2025
# QUESTION 1
# Name: LAWANI ELYON JOHN
# Matric No: 20/3446

# Step 1: Create the OrigNum list
# This is the original list of numbers
OrigNum = [21, 52, 67, 95, 20, 14, 63, 36, 28, 71, 18, 29]

# Q1(a): Function to swap the digits
# Example: 95 becomes 59, 21 becomes 12
def SwapPos(orig_list):
    RR = []  # This list will store the new swapped numbers
    for num in orig_list:
        # Convert the number to a string, reverse it, and change back to number
        swapped = int(str(num)[::-1])
        RR.append(swapped)
    return RR

RR = SwapPos(OrigNum)
print("Swapped List (RR):", RR)


# Q1(b): Create a new list using list comprehension
# Rule: if the index is odd, multiply it by 2
#       if the index is even, divide it by 2
LiCom = [index * 2 if index % 2 != 0 else index / 2 for index in range(len(RR))]
print("List Comprehension (LiCom):", LiCom)


# Q1(c): Function to get the largest and average value from the LiCom list
def LargeFun(list_input):
    largest = max(list_input)  # Finds the biggest number
    average = sum(list_input) / len(list_input)  # Calculates the average
    return largest, average

# Call the function and store the results
largest_value, average_value = LargeFun(LiCom)

# Print results
print("Largest number in LiCom:", largest_value)
print("Average of numbers in LiCom:", average_value)
