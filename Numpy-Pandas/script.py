import numpy as np
new_array=np.array([1,2,3])
print("Array with rank 1: \n",new_array)
new_2D_array=np.array([[1,2,3],[4,5,6]])
print("Array with rank 2: \n",new_2D_array)
new_array=np.array((1,2,3))
print("Array with rank 3 that is created using a passed tuple: \n",new_array)


import numpy as np
liste = [1,2,3]
Converted_List = np.array([1,2,3])
print(type(Converted_List))
print(Converted_List * 3)

import numpy as np
my_arr = np.arange(8)
my_arr = np.arange(1,8)
my_arr = np.arange(1,8,2)
print(my_arr)
print(type(my_arr))


import numpy as np
arr2D = np.array([[1,2],[3,4]])
print(arr2D)
print(arr2D * 4)
print(arr2D / 2)
print(arr2D + 5)
print(arr2D.shape)
print(arr2D.T)

arr3_2D = np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr3_2D)
print(arr3_2D.T)

print(np.eye(10))
print(np.zeros(7))
print(np.ones(16).reshape(4,4))

main = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(main)
print(main[0,1])
print(main[0:2])
print(main[1:3, 0:2])

# genreating random values
import numpy as np
ran = np.random.randint(2,56)
print(ran)


# Class Checkpoint
import numpy as np

num_of_students = int(input("Enter the number of students: "))
num_of_subjects = int(input("Enter the number of subjects: "))

marks = np.zeros((num_of_students, num_of_subjects), dtype=float)

for i in range(num_of_students):
    print(f"\nEnter marks for student {i + 1}: ")
    for j in range(num_of_subjects):
        marks[i, j] = float(input(f"Subject {j + 1}: "))

total = np.sum(marks, axis=1)
percentages = (total / (num_of_subjects * 100)) * 100

grades = []
for percentage in percentages: 
    if percentage >= 90:
        grades.append("A+")
    elif percentage >= 80:
        grades.append("A")
    elif percentage >= 70:
        grades.append("B+")
    elif percentage >= 60:
        grades.append("B")
    elif percentage >= 50:
        grades.append("C")
    else:
        grades.append("F")

print("\nStudent\t Total Marks\t Percentage\t Grade")
print("-" * 50)

for i in range(num_of_students):
    print(f"Student {i + 1}\t {total[i]:.2f}\t \t {percentages[i]:.2f}%\t \t {grades[i]}")

    # Class exercise
    # create an array of 10 zeros

# Printing 10 zeros    
import numpy as np
print(np.zeros(10))

# printing 10 ones
print(np.ones(10))
new = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(new)


ran2 = np.array([[1,0.,0.,0.,1.,0.,0.,0.,1.]])
print(ran2.reshape(3,3))
ran3 = np.random.randint(0,1)
print(ran3)

# Pandas
df = pd.DataFrame({"Subjects":["Math","Engl","CS"],"Scores":[20,30,40],"Grades":["A","B","C"]})
print(df)

import pandas as pd
table = pd.read_csv("vgsales.csv")
print(table)
print(table[["Rank","Name"]])
print(table.head())
print(table.info())
print(table.columns)
print(table.describe())


table["NorthAmerica and Europe sales"] = (table["NA_Sales"] + table["JP_Sales"])
print(table)
table["Other_Sales"]  = table["Other_Sales"] * 4
print(table)

print(table.head(2))

import os
os.getcwd()