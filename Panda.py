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

datafram2 = datafram #it is not copy we are just changeing the name , only view
datafram2[0][0] = 17 #it will change the changeing into datafram same we are just make two pointer 
print(datafram) 

datafram3 = datafram.copy() # this will make copy of datafram the pointer refrence variable name is datafram 3

datafram3[0][0] = "dsa"
print(datafram) #it will not change in datafram, datafram3 is seprate table copy of datafram at memory it have their own memory
print(datafram3)

#if we cahnge something like right datafram3[0][0] = "dsa" than interpreter gives warning b/c it is confused what we have to give or change into in the view or in orginal 

#that why we use loc function for changeing

datafram.loc[0,1] = "hello"
print(datafram)

datafram.columns = list("ABCDEFG") # it will cahnge the row indx into alphbat
print(datafram.head(2))

datafram = datafram.drop(0, axis=0) #if we write inplace after axis it will drop in orginally we donot need to write datafram = ;
print(datafram.head(2))

print(datafram.iloc[[1,2],[1,2]]) #iloc function work on indx wise if the colum name is alpbhat wise or any other or row name are changed sitll it will work on it will count number wise

#if we drop any row or colum the sequnce series is change to set it we use 
datafram.reset_index(drop = True, inplace = True)
print(datafram.head(5))