import numpy as np
import pandas as pd

dict1 = {
    "names": ["gurmeet","sandesh","shivam","vishal"],
    "Marks":[50,45,60,85],
    "Cities":["karachi","karachi","Ghotki","Karachi"]
}

df = pd.DataFrame(dict1)
print(df)

df.to_csv("names.csv", index = False)