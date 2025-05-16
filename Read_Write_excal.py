import pandas as pd
sheet = pd.read_excel('C:/Users/Gurmeet KUMAR/Downloads/Marks sent to students 1B.xlsx', sheet_name='Table 1') 
#it will read the file from execl and give us output
print(sheet.head(4).to_string(index = False)) #we can use sheet only for print but it donot have functionaty like i want to print without indx or only sheet can do auto trancat but .to_string cannot

excel_file = pd.ExcelFile('C:/Users/Gurmeet KUMAR/Downloads/Marks sent to students 1B.xlsx')
sheet_list = excel_file.sheet_names
print(sheet_list)