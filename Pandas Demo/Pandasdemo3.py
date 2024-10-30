import pandas as pd 
#path = 'C:\Users\Narayana Rao\Desktop\PythonCodingQuestions\PandasDemo\datacsv\surveyResultsPublic.csv'
df = pd.read_csv('datacsv/surveyResultsPublic.csv') 
#df = pd.read_csv('datacsv/surveyResultsPublic.csv',header=None) # if we put header then it shows the columns count 
#print(df.head())
#print(df.columns)
#print(df.head(10))
#print(df.tail(10))

# replacing the header values but need same number of columns in both csv and header variable
#headers = ['A','B','C','D','E','F','G','H','I','J']
#df.columns=headers
#print(df.columns)

#print(df.head())
#print(df.dtypes)

print(df.info())
#print(df.describe())
#print(df.describe(include='all'))

#df.to_csv('newsurvey.csv')

#print(df)
