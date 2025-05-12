import numpy as np
import pandas as pd

dict1 = {
    "names": ["gurmeet","sandesh","shivam","vishal"],
    #"Marks":[50,45,60,85],
    "Cities":["karachi","karachi","Ghotki","Karachi"]
}

df = pd.DataFrame(dict1)
#print(df)

#df.to_csv("names.csv", index = False)

df.index = ["one","two","three","four"] #it change the defult indx to custom

#print(df.head(2)) #it will return first 2 record

#print(df.tail(2)) #it will retun last 2 record

#print(df.describe()) # it will return statuces values like avg of numric value colum , and numbric values is not present than it will return count of record in colums unqi values in each colum etc

series = pd.Series(np.random.rand(15))
print(series)
datafram = pd.DataFrame(np.random.randint(5,50,size=(5,7)))
print(datafram)

#Series = one column
#DataFrame = multiple columns (table)

print(datafram.T) #Transfose function row into colum and viseversa
print(datafram.sort_index(axis=1,ascending=False)) #it will do sort indx axis 1 = colum and assending = false = desending
print(type(datafram)) #tell us it it will datafram or series

datafram[0][0] = "Gurmeet" # change the value of 0 indx 0 colum = "Gurmeet"
print(datafram.dtypes) #tell us datatype of every colum 
print(datafram[0]) # it will print whole colum 1 mean series
print(type(datafram[0]))
#mean multiple series = dataFram