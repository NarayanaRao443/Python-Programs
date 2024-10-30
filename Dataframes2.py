# creating an empty dataframe
'''import pandas as pd 
df = pd.DataFrame()  
print(df)
'''


#Creating a dataframe using List: 
'''import pandas as pd
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)
print(df)
'''

#Creating DataFrame from dict of ndarray/lists: 
'''import pandas as pd 
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 
        'Age':[20, 21, 19, 18]
        }
df = pd.DataFrame(data)
print(df)
'''

'''
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)

#retrieve the first element
print(ser[:5])
'''

'''
import pandas as pd 
df = pd.read_csv('data.csv')
ser = pd.Series(df['Calories'])
data = ser.head(10)
print(data)
print()
print(df.head(10))
print(df[2:7])
print(df.loc[5:13])
print(df.iloc[5:13])
'''

'''
import pandas as pd 
df = pd.read_csv('nba.csv')
#print(df.head(10))
n=14
series = df['Name']
top =series.head(n=n)
#print(top)
top2=series.tail(n=n)
#print(top2)
print(df.describe())
'''
'''
import pandas as pd 
df = pd.read_csv('nba.csv')
#print(df.describe())

print(df.to_string())
#df.dropna(inplace=True)  # removing null values to avoid errors
#desc = df['Name'].describe()
#print(desc)

#df.fillna(9999,inplace=True) # filling all null values with 9999
#print(df.to_string())

df['College'].fillna(10000,inplace=True)  # replace the NaN values in College column with 10000
#print(df.to_string())  
print(df)
'''


'''import pandas as pd
df = pd.read_csv('data.csv')
x=df['Calories'].mean()
df['Calories'].fillna(x,inplace=True) # replacing the null values(NaN) with 375.790244
print(df.to_string()) '''


'''
import pandas as pd
df = pd.read_csv('data.csv')
x=df['Calories'].median()
df['Calories'].fillna(x,inplace=True) # replacing the null values(NaN) with 318.6 
print(df.to_string())

'''


'''
import pandas as pd
df = pd.read_csv('data.csv')
x=df['Calories'].mode()[0]
df['Calories'].fillna(x,inplace=True) # replacing the null values(NaN) with 300.0
print(df.to_string()) 
'''

'''
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
#df.plot() # prints one type of graph
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')  #prints scatter plot
plt.show()'''


import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
#df.plot()
#plt.show()

#df.plot(kind='scatter',x='Duration',y='Maxpulse')
df.plot(kind='hist',x='Duration')
plt.show()
print(df)