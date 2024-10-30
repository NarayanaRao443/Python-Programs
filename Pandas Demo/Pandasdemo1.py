'''import pandas as pd 
df = pd.read_csv('datacsv/survey_results_public.csv')
sdf = pd.read_csv('datacsv/survey_results_schema.csv')
print(sdf)
#print(df)
#print(df.to_string())
#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.info())
#df2=pd.set_option('display.max_columns',84)
#df2=pd.set_option('display.max_rows',83)
#print(df2)
'''
'''
people = {
    "first":["Corey","John","James"],
    "last":["schafer","Doe","Anderson"],
    "email":["corey@gmail.com","john@gmail.com","james@gmail.com"]

}

print(people['first'])
import pandas as pd 
df=pd.DataFrame(people)
#print(df)
print(type(df))
#print(df['email'])
#print(type(df['email']))
#print(df.email)
#print(df.count())
#print(df[['first','email']])

#print(df.columns)
#print(df.iloc[0])
#print(df.iloc[[0,1],2])
#print(df.loc[[0,1],'email'])
'''

'''import pandas as pd 
df = pd.read_csv('datacsv/survey_results_public.csv')
#print(df['MainBranch']) # returns the paritcular column data
#print(df['MainBranch'].value_counts()) # prints the count of data in each row
#print(df.loc[[0,1,2],'MainBranch']) # prints first 3 row values of MainBranch
print(df.columns)
#print(df.loc[0:2,'MainBranch'])
print(df.loc[0:2,'MainBranch':'EdLevel']) # prints from 0 to 2 rows and MainBranch to EdLevel columns
'''
'''
people = {
    "first":["Corey","John","James"],
    "last":["schafer","Doe","Anderson"],
    "email":["corey@gmail.com","john@gmail.com","james@gmail.com"]

}
import pandas as pd
df=pd.DataFrame(people)
print(df)
#print(df['email'])
#print(df.set_index('email'))

print(df.set_index('email',inplace=True)) # here email will comes to the first column
print(df.index)
print(df.loc['corey@gmail.com','last'])
#print(df.iloc[1])
print(df.reset_index(inplace=True))  # here email will move back to the original position
print(df)
'''

#import pandas as pd 
#df = pd.read_csv('datacsv/survey_results_public.csv',index_col='ResponseId')

#print(df.head())
#print(df.loc[2])
#print(df.loc['Age'])
#print(df.sort_index(ascending=False))  # prints in descending order

#sdf = pd.read_csv('datacsv/survey_results_schema.csv',index_col='qname')
#print(sdf)
#print(sdf.columns)
#print(sdf.value_counts())
#print(sdf.loc['OpSys']) # here both index_col name and sdf.loc=['']values are from same column
#print(sdf.sort_index())
#print(sdf.sort_index(ascending=False)) # prints in descending order


'''
people = {
    "first":["Corey","John","James"],
    "last":["schafer","Doe","Doe"],
    "email":["corey@gmail.com","john@gmail.com","james@gmail.com"]

}
#----filtering-----

d=pd.DataFrame(people)
#f=d['last']=='Doe'
#print(d[f])   # d[f] and d.loc[f] gives same results
#print(d.loc[f])
 
#print(d.loc[f,'email'])  #gives only email
f = (d['last']=='Doe') & (d['first']=='John') # returns one value only 
g = (d['last']=='Doe') | (d['first']=='John') #returns two values because of or condition
print(d[f])
print(d[g])'''


'''import pandas as pd 
df = pd.read_csv('datacsv/survey_results_public.csv')
fil = (df['ConvertedCompYearly']>70000)
#print(df[fil].head())  # return the frist 5 rows of data which is salary > 70000

#fil2 = (df.loc[fil,['Country','LanguageHaveWorkedWith','ConvertedCompYearly']])
#print(fil2.head(10))

#countries = ['India','United States of America','United Kingdom','Canada','Finland']
#fil3 = df['Country'].isin(countries)
#print(df[fil3].head(10))
#print(df.loc[fil3,'Country'])
#print(df['LanguageHaveWorkedWith'])
#print(df.columns)

fil4 = df['LanguageHaveWorkedWith'].str.contains('Python',na=False)
print(df.loc[fil4, 'LanguageHaveWorkedWith'].head(10))

sdf = pd.read_csv('datacsv/survey_results_schema.csv')
#fil = (sdf['qname']=='Age')

#print(fil.head(10))
#print(fil.head(20))
'''

 #    =================        ----Updating rows and columns-----       ==================

'''people = {
    "first":["Corey","John","James"],
    "last":["schafer","Doe","Doe"],
    "email":["corey@gmail.com","john@gmail.com","james@gmail.com"]

}'''
#import pandas as pd
#df = pd.DataFrame(people)
#print(df.columns)
#print(df)

# update column names
#df.columns = ['first_name','last_name','email']
#print(df.columns)
#print(df)

# columns in uppercase()
#df.columns = [x.upper() for x in df.columns]
#print(df)
#print(df.columns)

# replace the column spaces or underscores
#df.columns = df.columns.str.replace('_',' ')
#print(df.columns)

# columns in lowercase()
#df.columns = [x.lower() for x in df.columns]
#print(df.columns)

# ---rename the columns
#df.rename(columns={'first_name':'first','last_name':'last'},inplace=True)
#print(df.columns)

#print(df)
#print(df.loc[2])

# updating the values
#df3= df.loc[2,['last','email']]= ['Smith','jameSmith@gmail.com']
#print(df3)
#print(df)
#print()

#fil = (df['first']=='John')
#print(df[fil]['last'])

#df4=df.loc[fil,'last']='Angel'
#print(df4)
#print(df)

'''print()
# length of the each email in dataframe
print(df['email'].apply(len))
print(df.apply(len))
# updating the email to uppercase by using functions

def update_email(email):
    return email.upper()
print(df['email'].apply(update_email))


df['email'] = df['email'].apply(update_email)
print(df)
print()

# by lambda functions
df['email'] =df['email'].apply(lambda x:x.lower())
print(df)
'''

#prints alphabetical order in whole dataframe
#print(df.apply(pd.Series.max))
#print(df.apply(pd.Series.min))

# applymap() 
#print(df.applymap(len)) # prints length of the each value
#print(df['first'].map({'Corey':'Chris','John':'Mary'}))
#print(df["first"].replace({'Corey':'Chris','John':'Mary'}))


'''import pandas as pd 
df = pd.read_csv('datacsv/survey_results_public.csv')
print(df.columns)
df5 = df.rename(columns={'RemoteWork':'Workfromhome'}, inplace=True) # it will changes the remotework to workfromhome permanently
#print(df5.columns)

print(df.columns)
#print(df['Workfromhome'].head(10))
print(df['TBranch'])
print(df['TBranch'].map({'Yes':True, 'No':False}))  # here all Yes and values replaces with True and False
'''

#------------Add or remove columns -------------

'''people = {
    "first":["Corey","John","James"],
    "last":["schafer","Doe","Doe"],
    "email":["corey@gmail.com","john@gmail.com","james@gmail.com"]

}
import pandas as pd
df=pd.DataFrame(people)
#print(df)
print()
'''
#print(df['first'] + ' '+df['last'])
#print()
'''
df['full_name'] = df['first'] + ' '+df['last']
#print(df)
print()

#print(df.drop(columns=['first','last'],inplace=True))
#print(df)

#print()
#print(df['full_name'].str.split(' '))
#print(df['full_name'].str.split(' ',expand=True))
#print()

#df[['first','last']] = df['full_name'].str.split(' ',expand=True)
#print(df)
print()

#print(df._append({'first':'Tony'},ignore_index=True)) # added new row 
print()

people = {
        'first':['michael','steve'],
        'last':['clark','smith'],
        'email':['michael@gmail.com','clark@gmail.com']
}
df2 = pd.DataFrame(people)
print(df2)
print()
df3 = df._append(df2,ignore_index=True, sort=True)
print(df3)
print()
print(df3.drop(index=4))   # index 4 data will be deleted
print()
print(df3.drop(index=df3[df3['last']=='Doe'].index))  
print()
 
fil = df3['last']=='Doe'
print(df3.drop(index=df3[fil].index))
# the above both statments gives same ouput from line number 274 to 278
'''




#----------------sorting----------------------

'''people = {
    "first":["John","Corey","James",'Adam'],
    "last":["Doe","schafer","Doe",'Janes'],
    "email":["john@gmail.com","corey@gmail.com","james@gmail.com","adam@gmail.com"]

}

import pandas as pd 
df = pd.DataFrame(people)
#print(df)
print()
#print(df.sort_values(by='last'))
print()
#print(df.sort_values(by='last',ascending=False))
print()
#print(df.sort_values(by=['last','first'])) # sorting both first and last values by passing the list[]
print()
print(df.sort_values(by=['last','first'],ascending=[False,True]))
print()
print(df.sort_index())
print()
print(df['last'].sort_values())
'''

'''import pandas as pd
df = pd.read_csv('datacsv/survey_results_public.csv')
#print(df.columns)
#print(df.sort_values(by='Country').head())
#print(df.sort_values(by=['Country','ConvertedCompYearly'],ascending=[True,False]).head(10))
#print(df[['Country', 'ConvertedCompYearly']].head(10))
print()
print(df['ConvertedCompYearly'].nlargest(10))
print(df.nlargest(10,'ConvertedCompYearly'))
print(df.nsmallest(10,'ConvertedCompYearly'))
'''

#------------mean,median and aggregating-------------

'''import pandas as pd 
df = pd.read_csv('datacsv/survey_results_public.csv')
#print(df['ConvertedCompYearly'].head(10))
#print(df['ConvertedCompYearly'].median())
#print(df.median())
#print(df.describe())

#print(df['ConvertedCompYearly'].count())
print()
#print(df['SOAccount'])

#print(df['SOAccount'].value_counts())  # returns the how may yes/no values are present in column
#print(df['SOAccount'].value_counts(normalize=True))
#print(df['Country'].value_counts())  # prints each country how many times it presents

# groupby the values

country_grp = df.groupby(['Country'])
#print(country_grp.get_group('India'))

#fil = df['Country']=='India'
#print(df.loc[fil]['Currency'].value_counts())
print()
#print(df['Currency'].value_counts().head(20))
#print(country_grp['ConvertedCompYearly'].median())
#print(country_grp['ConvertedCompYearly'].median().loc['Germany']) # returns data with median of Germany

#print(country_grp['ConvertedCompYearly'].agg(['median','mean']))
#print(country_grp['ConvertedCompYearly'].agg(['median','mean']).loc['Canada'])

#print(df.columns)
fil = df['Country']=='India'
#print(df.loc[fil]['LanguageHaveWorkedWith'].str.contains('Python').sum())
#print(country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum()))  # using apply method with lambda function

# how many country users using the python
country_uses_python = country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
#print(country_uses_python)

country_respond = df['Country'].value_counts()
print(country_respond) 

python_df = pd.concat([country_respond,country_uses_python], axis='columns')
print(python_df)

print(python_df.rename(columns={'count':'NumRespondents', 'LanguageHaveWorkedWith':'NumKnowsPython'}))
print()

#python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents']) * 100
#print(python_df)

#print(python_df.sort_values(by='PctKnowsPython',ascending=False,inplace=True))
python_df.loc['Japan']
'''

#--------cleaning data-----------
import pandas as pd 
import numpy as np 
people = {
    'first':[ 'Corey','Jane','John','Chris',np.nan, None,'NA'],
    'last':['Schafer','Doe','Doe','Schafer',np.nan, np.nan, 'Missing'],
    'email':['Corey@gmail.com','JaneDoe@gmail.com','JohnDoe@gmail.com',None,np.nan,'Anonymous@gmail.com',None],
    'age':['33','55','63','36',None,None,'Missing']
}


'''df = pd.DataFrame(people)
#print(df)
print()
#print(df.dropna())

#print(df.dropna(axis='index',how='any'))  # if any na is presents in data, the won't be displayed
print()
#print(df.dropna(axis='index',how='all')) # if all the columns have NA or None then the total row will be deleted
print()
#print(df.dropna(axis='columns',how='any')) 
print()
#print(df.dropna(axis='index',how='all', subset=['last','email']))

df.replace('NA',np.nan, inplace=True)
print(df)
print()
df.replace('Missing',np.nan, inplace=True)
print(df)
print()
print(df.isna())  # returns True where NaN and False where data is given
print()
print(df.fillna('Missing')) # replaces all the NA values with Missings
print()
print(df.fillna(0))
print()
print(df.dtypes)
print()
#print(df['age'].mean())  # returns error because str to int never concated
print(type(np.nan)) # returns float data type

#df['age']=df['age'].astype(int) #error
df['age']= df['age'].astype(float) #  age data converted from into to float values
print(df)
#print(df['age'].median()) # 45.5
print(df['age'].mean()) #46.75
'''


'''df = pd.read_csv('datacsv/survey_results_public.csv')
#print(df['YearsCode'].mean()) # returns errors

#df['YearsCode'] = df['YearsCode'].astype(float)
print(df['YearsCode'].unique()) # returns unique values only

print(df['YearsCode'].replace('Less than 1 year',0, inplace=True))
print(df['YearsCode'].replace('More than 50 years',51,inplace=True))

df['YearsCode'] = df['YearsCode'].astype(float)
print(df['YearsCode'].mean())
print(df['YearsCode'].median())
print(df['YearsCode'].sum())
'''


# --------- Reading/Writing/ JSON/ SQL-------------

import pandas as pd 
df = pd.read_csv('datacsv/survey_results_public.csv',index_col='ResponseId')
#print(df)

fil = (df['Country']=='India')
India_df = df.loc[fil]
#print(India_df.head())

# here all india country data will be stored in new document
India_df.to_csv('datacsv/modified.csv')
#print(India_df)

# here file will be saved with the name of .csv strucutre
India_df.to_csv('datacsv/modified.tsv', sep='@')
#print(India_df)

#pip install xlwt openpyxl xlrd
# creating the excel file
India_df.to_excel('datacsv/modified.xlsx')
#print(India_df)

#reading the file
test = pd.read_excel('datacsv/modified.xlsx',index_col='ResponseId')
#print(test.head())

# creating the JSON file 
#India_df.to_json('datacsv/modified.json')
India_df.to_json('datacsv/modified2.json',orient='records',lines=True)  # create the json file line by line
#print(India_df)

test = pd.read_json('datacsv/modified2.json',orient='records',lines=True)
#print(test.head())

# installing the SQL
# pip install SQLAlchemy
# pip install psycopg2-binary

'''from sqlalchemy import create_engine
import psycopg2
# connection to the database, here dbname: is sample_db
engine = create_engine('postgresql://dbuser@localhost:5432/sample_db') 
# creating the table with csv values
# converted the data from csv to sql table
#India_df.to_sql('sample_table',engine)
India_df.to_sql('sample_table',engine, if_exists='replace')
sql_df = pd.read_sql('sample_table',engine,index_col='ResponseId')
print(sql_df)

sql_df = pd.read_sql_query('SELECT * FROM sample_table', engine , index_col='ResponseId')
print(sql_df.head())
'''

# url methods
posts_df = pd.read_json('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/snippets/posts.json')
print(posts_df.head(20))