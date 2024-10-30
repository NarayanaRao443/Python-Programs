'''import pandas as pd 
data = {
    "Name":["Raj","Kumar","Lokesh"],
    "age":[30,20,28]
}
df = pd.DataFrame(data)
print(df)
print()
print(df.loc[0])
print(df.loc[[0,1]])
print()
ef = pd.DataFrame(data,index = ['p1','p2','p4'])
print(ef)
print(ef.loc['p2'])'''

# create empty dataframe
'''import pandas as pd
k = pd.DataFrame()
print(k)'''

# Read CSV files
'''

import pandas as pd 
df = pd.read_csv('data.csv')
#print(df) # returns first 5 and last 5 rows

x = pd.read_csv('data.csv')
#print(x.to_string())  #use to_string() to print the entire DataFrame.

#print(pd.options.display.max_rows) #60
#print(pd.options.display.max_columns) #0

y = pd.options.display.max_rows=999
#print(y)

z=pd.read_csv('data.csv')
print(z.loc[[0,10]]) #prints 0th row and 10th row only
'''

# Read JSON files
'''
import pandas as pd 
df = pd.read_json('data.js')
print(df) # first 5 rows and last 5 rows 
print()
print(df.to_string())   #use to_string() to print the entire DataFrame.
'''

'''
JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:

'''


'''
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)
'''


# Analyzing the data -> viewing the data

# The head() method returns the headers and a specified number of rows, starting from the top.
# if the number of rows is not specified, the head() method will return the top 5 rows.

import pandas as pd 
df = pd.read_csv('data.csv')
#print(df.head())

#print("upto 30 rows")
#print(df.head(30))

#The tail() method returns the headers and a specified number of rows, starting from the bottom.
#Print the last 5 rows of the DataFrame:
#print(df.tail())

#The DataFrames object has a method called info(), that gives you more information about the data set.
#Print information about the data:
#print(df.info())

