import pandas as pd
Test_list = [['jack',34,'Paris'],['Thomas',30,'Roma'],['Alexender',16,'New York']]
df =  pd.DataFrame(Test_list,columns=['name','age','city'])
print(df)

dictionary = {'name':['Jack','Thomas','Alexender'],'age':[34,30,16],'city':['Paris','Roma','New York']}
df = pd.DataFrame(dictionary)
print(df)

import numpy as np
import pandas as pd

my_numpyarr = np.random.randn(3,4)
df=pd.DataFrame(my_numpyarr, columns=list("abcd"))
print(df)

import pandas as pd
df = pd.read_csv("vgsales.csv")

# Exporting a DataFrame into a csv 
import pandas as pd
dict1 = {
    "Name":["John","Jack","Angelica","Andrew","Isaac","Tyroone"],
    "Last Name":["Scott","McBride","NewMan","Hines","Justice","Buck"],
    "Age":["23","20","21","22","23","24"],
    "Role":["AI","AI","WEB1","Manager","DataScience","Developer"],
    "Home Address":["LA","California","New York","Florida","La","Washignton"]
}
data = pd.DataFrame(dict1)
data.to_csv('Data.csv')
new_data = pd.read_csv('Data.csv')
new_data.head(5)

# Getting info for the dataframe 
print(df.info())
print(df.head())
print(df.tail())
print(df.describe())


print(new_data[['Age','Home Address']])
print(new_data[0:4])

print(new_data)
new_data = new_data.set_index('Name')
print(new_data)

# loc method 
print(new_data.loc[["John","Jack"]])
print(new_data.iloc[:, 1:3])

# Drop methood 
new_data = new_data.drop(['Last Name', 'Home Address'], axis=1)
print(new_data)